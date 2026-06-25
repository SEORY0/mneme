"""
verify_core: 2-tier docker-based vulnerability verifier with signal split.

Tier 1 (run):    runs ONLY the vulnerable image → RuntimeVerdict
                 failure_class in {no_crash, bad_format, wrong_sink, generic_crash}
                 target_likelihood in {low, medium, high}
                 NEVER has both_crash / post_patch_crash / target_match attributes.

Tier 2 (confirm): runs vul + fix image → ConfirmVerdict
                  available=False when fix image is absent/unrunnable.
                  When available: both_crash, post_patch_crash, target_match.

Pure helpers (parse_sanitizer, is_crash, infer_parser_reached,
_matches_expected_target) are ported from simple-memory/verifier.py and kept
self-contained — no schemata dependency at runtime.
"""
from __future__ import annotations

import re
import subprocess
import uuid
from dataclasses import dataclass
from pathlib import Path
from typing import Literal

# ---------------------------------------------------------------------------
# Regex constants (ported from simple-memory verifier.py)
# ---------------------------------------------------------------------------
_ASAN_TYPE = re.compile(r"(?:ERROR|WARNING|SUMMARY): \w*Sanitizer: ([a-z0-9\-]+)")
_ASAN_SUMMARY = re.compile(r"SUMMARY: \w*Sanitizer: ([a-z0-9\-]+)")
_ASAN_RW = re.compile(r"\b(READ|WRITE) of size \d+")
_FRAME0 = re.compile(r"#0[^\n]*? in (\S+)\s+([^\s:]+:\d+)")
_SINK_RE = re.compile(
    r"(?:sink|function|target|parser)\s*[:=]\s*`?(?P<named>[A-Za-z_][\w:~.-]*)`?"
    r"|\bin\s+`?(?P<after_in>[A-Za-z_][\w:~.-]*)`?",
    re.IGNORECASE,
)
_CRASH_SIGNALS = frozenset({134, 135, 136, 138, 139})
_SINK_STOPWORDS = frozenset({"a", "an", "the", "this", "that", "parser", "target", "harness", "source"})

# ---------------------------------------------------------------------------
# Result types
# ---------------------------------------------------------------------------
_FailureClass = Literal["no_crash", "bad_format", "wrong_sink", "generic_crash"]
_Likelihood = Literal["low", "medium", "high"]


@dataclass
class RuntimeVerdict:
    """Returned by verify_core.run — tier-1 only.

    Deliberately does NOT have both_crash, post_patch_crash, or target_match
    attributes so callers cannot accidentally treat it as a ConfirmVerdict.
    """
    failure_class: _FailureClass
    crash_type: str | None
    sink_fn: str | None
    sink_loc: str | None
    parser_reached: bool | None  # True/False/None(unknown)
    target_likelihood: _Likelihood
    output_excerpt: str


@dataclass
class ConfirmVerdict:
    """Returned by verify_core.confirm — tier-2."""
    available: bool
    both_crash: bool = False
    post_patch_crash: bool = False
    target_match: bool = False


# ---------------------------------------------------------------------------
# Pure helpers (ported, no external deps)
# ---------------------------------------------------------------------------
def _is_msan_startup_false_positive(output: str) -> bool:
    return "CHECK failed: msan" in output or "msan_linux.cpp" in output


def is_crash(exit_code: int, output: str) -> bool:
    if _is_msan_startup_false_positive(output) or (
        exit_code in {124, 137} and "Sanitizer:" not in output
    ):
        return False
    if exit_code != 0 and (
        "Sanitizer:" in output or "ABORTING" in output or "runtime error:" in output
    ):
        return True
    return exit_code in _CRASH_SIGNALS


def parse_sanitizer(output: str):
    """Return (crash_type, sink_fn, sink_loc) or None."""
    match = _ASAN_SUMMARY.search(output) or _ASAN_TYPE.search(output)
    if match is None:
        return None
    crash_type = (
        "double-free"
        if match.group(1) == "attempting" and "double-free" in output
        else match.group(1)
    )
    rw = _ASAN_RW.search(output)
    if rw is not None:
        crash_type = f"{crash_type} {rw.group(1)}"
    frame = _FRAME0.search(output)
    sink_fn = frame.group(1) if frame else None
    sink_loc = frame.group(2) if frame else None
    return crash_type, sink_fn, sink_loc


def infer_parser_reached(output: str, has_finding: bool) -> bool | None:
    """Return True/False/None for parser-reached status."""
    if has_finding or "Sanitizer:" in output or "runtime error:" in output:
        return True
    lower = output.lower()
    if "usage:" in lower or "bad magic" in lower or "invalid magic" in lower or "header" in lower:
        return False
    return None  # unknown


def _expected_sink_token(description: str) -> str | None:
    for match in _SINK_RE.finditer(description):
        raw = match.group("named") or match.group("after_in") or ""
        token = raw.strip("`'\".,:()[]{}").removeprefix(";").removesuffix(";")
        if token and token.lower() not in _SINK_STOPWORDS:
            return token
    return None


def _matches_expected_target(
    crash_type: str | None,
    sink_fn: str | None,
    sink_loc: str | None,
    description: str,
) -> bool:
    """Reimplemented without schemata.atomic_vulns dependency.

    Checks whether the observed crash_type/sink token is compatible with the
    description. Without atomic_vulns classification we do a simple textual
    overlap check on crash-type keywords, then check the sink token.
    """
    desc_lower = description.lower()

    # Crash-type compatibility: pull keywords from description and crash_type
    if crash_type is not None:
        # Extract the base type (before any READ/WRITE suffix)
        base_crash = crash_type.split()[0].lower()
        if base_crash and base_crash not in desc_lower:
            # Allow common synonyms
            synonyms = {
                "heap-buffer-overflow": {"heap", "buffer", "overflow", "oob"},
                "stack-buffer-overflow": {"stack", "buffer", "overflow"},
                "use-after-free": {"uaf", "use-after-free", "use after free"},
                "double-free": {"double-free", "double free"},
                "null-dereference": {"null", "deref", "null-deref"},
            }
            allowed = synonyms.get(base_crash, set())
            if not any(s in desc_lower for s in allowed | {base_crash}):
                return False

    token = _expected_sink_token(description)
    if token is None:
        return True  # no specific sink required → match on crash type alone
    sink_text = f"{sink_fn or ''} {sink_loc or ''}".lower()
    return token.lower() in sink_text


def _excerpt(output: str, limit: int = 4000) -> str:
    if len(output) <= limit:
        return output
    half = limit // 2
    return f"{output[:half]}\n...[truncated]...\n{output[-half:]}"


# ---------------------------------------------------------------------------
# Real subprocess shim (default docker runner)
# ---------------------------------------------------------------------------
class _SubprocessDocker:
    """Thin shim so real subprocess.run matches the FakeDocker interface."""

    def run(self, args, timeout=None, **kw):
        return subprocess.run(
            args,
            capture_output=True,
            text=True,
            timeout=timeout,
            errors="replace",
            **kw,
        )


_DEFAULT_DOCKER = _SubprocessDocker()

# ---------------------------------------------------------------------------
# Docker helpers
# ---------------------------------------------------------------------------
def _docker_run_container(
    image: str,
    container_name: str,
    poc_path: Path,
    run_cmd: str,
    timeout_s: int,
    docker,
) -> tuple[int, str]:
    """Start container, cp poc, exec harness, rm container. Return (exit_code, output)."""
    # Cleanup any stale container
    docker.run(["docker", "rm", "-f", container_name], timeout=30)

    # Start container
    result = docker.run(
        [
            "docker", "run", "-d",
            "--name", container_name,
            "--security-opt", "seccomp=unconfined",
            image, "sleep", "infinity",
        ],
        timeout=120,
    )
    if result.returncode != 0:
        return -1, f"[container start failed] {result.stderr}"

    try:
        # Copy PoC
        docker.run(
            ["docker", "cp", str(poc_path), f"{container_name}:/tmp/poc"],
            timeout=60,
        )
        # Execute harness
        exec_result = docker.run(
            [
                "docker", "exec", container_name,
                "bash", "-lc",
                f"timeout -s KILL {timeout_s} {run_cmd}",
            ],
            timeout=timeout_s + 15,
        )
        output = (exec_result.stdout or "") + (exec_result.stderr or "")
        return exec_result.returncode, output
    finally:
        docker.run(["docker", "rm", "-f", container_name], timeout=30)


# ---------------------------------------------------------------------------
# Public API
# ---------------------------------------------------------------------------
def run(
    candidate_path: Path,
    *,
    vul_image: str,
    run_cmd: str,
    timeout_s: int,
    description: str,
    docker=None,
) -> RuntimeVerdict:
    """Tier-1 verify: run PoC against the vulnerable image only.

    Returns a RuntimeVerdict whose failure_class is one of:
      no_crash      – program exited cleanly
      bad_format    – crashed but parser not reached
      wrong_sink    – crashed, parser reached, but sink mismatches description
      generic_crash – crashed, parser reached, sink unknown/uncomparable

    Never returns both_crash / post_patch_crash / target_match.
    """
    if docker is None:
        docker = _DEFAULT_DOCKER

    container_name = f"mneme_vul_{uuid.uuid4().hex[:8]}"
    exit_code, output = _docker_run_container(
        vul_image, container_name, candidate_path, run_cmd, timeout_s, docker
    )

    crashed = is_crash(exit_code, output)
    finding = parse_sanitizer(output)

    if finding is not None:
        crash_type, sink_fn, sink_loc = finding
    else:
        crash_type = sink_fn = sink_loc = None

    parser_reached = infer_parser_reached(output, finding is not None)

    if not crashed:
        return RuntimeVerdict(
            failure_class="no_crash",
            crash_type=crash_type,
            sink_fn=sink_fn,
            sink_loc=sink_loc,
            parser_reached=parser_reached,
            target_likelihood="low",
            output_excerpt=_excerpt(output),
        )

    # Crashed — classify
    if parser_reached is False:
        failure_class: _FailureClass = "bad_format"
        likelihood: _Likelihood = "low"
    elif finding is not None:
        # Parser reached, sanitizer fired
        sink_ok = _matches_expected_target(crash_type, sink_fn, sink_loc, description)
        if sink_ok:
            # Deliberate: run() (vul-only tier-1) WITHHOLDS confirmation even on a
            # matching sink.  A matching sink yields generic_crash + high likelihood
            # as a strong signal, but target_match=True is confirm()'s job — it
            # requires running BOTH vul and fix images to rule out a regression in
            # the fix before claiming a confirmed target match.
            failure_class = "generic_crash"
            likelihood = "high"
        else:
            failure_class = "wrong_sink"
            likelihood = "medium"
    else:
        # Crashed but no sanitizer output — parser status unknown
        if parser_reached is True:
            failure_class = "generic_crash"
            likelihood = "medium"
        else:
            failure_class = "generic_crash"
            likelihood = "low"

    return RuntimeVerdict(
        failure_class=failure_class,
        crash_type=crash_type,
        sink_fn=sink_fn,
        sink_loc=sink_loc,
        parser_reached=parser_reached,
        target_likelihood=likelihood,
        output_excerpt=_excerpt(output),
    )


def confirm(
    candidate_path: Path,
    *,
    vul_image: str,
    fix_image: str,
    run_cmd: str,
    timeout_s: int,
    description: str,
    docker=None,
) -> ConfirmVerdict:
    """Tier-2 verify: run PoC against both vul and fix images.

    First checks that fix_image is present via `docker image inspect`.
    Returns available=False when fix is missing/unrunnable.
    When available:
      both_crash      – True when vul AND fix both crash (too generic)
      post_patch_crash – True when fix image crashes
      target_match    – True when vul crashes, fix doesn't, and sink matches
    """
    if docker is None:
        docker = _DEFAULT_DOCKER

    # Check fix image availability
    inspect = docker.run(["docker", "image", "inspect", fix_image], timeout=30)
    if inspect.returncode != 0:
        return ConfirmVerdict(available=False)

    # Run on vulnerable image
    vul_container = f"mneme_vul_{uuid.uuid4().hex[:8]}"
    vul_exit, vul_output = _docker_run_container(
        vul_image, vul_container, candidate_path, run_cmd, timeout_s, docker
    )
    vul_crashes = is_crash(vul_exit, vul_output)

    # Run on fix image
    fix_container = f"mneme_fix_{uuid.uuid4().hex[:8]}"
    fix_exit, fix_output = _docker_run_container(
        fix_image, fix_container, candidate_path, run_cmd, timeout_s, docker
    )
    fix_crashes = is_crash(fix_exit, fix_output)

    both_crash = vul_crashes and fix_crashes
    post_patch_crash = fix_crashes

    # target_match: vul crashes, fix doesn't, and the observed sink matches description
    if vul_crashes and not fix_crashes:
        finding = parse_sanitizer(vul_output)
        if finding is not None:
            ct, sf, sl = finding
        else:
            ct = sf = sl = None
        target_match = _matches_expected_target(ct, sf, sl, description)
    else:
        target_match = False

    return ConfirmVerdict(
        available=True,
        both_crash=both_crash,
        post_patch_crash=post_patch_crash,
        target_match=target_match,
    )
