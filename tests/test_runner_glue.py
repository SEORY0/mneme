"""
tests/test_runner_glue.py — Tests for the real-mode runner glue fixes.

All tests run offline (no Docker, no model, no network).
"""
import json
import sys
import types
from pathlib import Path

import pytest

# Ensure src/ is on sys.path
_HERE = Path(__file__).resolve()
_SRC = _HERE.parents[1] / "src"
_RUNNER = _HERE.parents[1] / "runner"
if str(_SRC) not in sys.path:
    sys.path.insert(0, str(_SRC))
if str(_RUNNER) not in sys.path:
    sys.path.insert(0, str(_RUNNER))


# ---------------------------------------------------------------------------
# T1: MCP server env helper returns all required vars + verify config writer
# ---------------------------------------------------------------------------

def test_mcp_server_env_contains_all_required_vars(tmp_path):
    """_mcp_server_env returns a dict with EVERY env var the server modules require."""
    import run as runner_mod

    run_dir = tmp_path / "run"
    store_dir = tmp_path / "memory_store"
    stats_path = store_dir / "memory_stats.jsonl"

    env = runner_mod._mcp_server_env(run_dir, store_dir, stats_path)

    # memory_server.py reads: MEMORY_STORE_DIR, STATS_PATH, RUN_DIR
    assert "MEMORY_STORE_DIR" in env
    assert env["MEMORY_STORE_DIR"] == str(store_dir)
    assert "STATS_PATH" in env
    assert env["STATS_PATH"] == str(stats_path)
    assert "RUN_DIR" in env
    assert env["RUN_DIR"] == str(run_dir)


def test_write_verify_config_produces_required_keys(tmp_path):
    """_write_verify_config writes JSON with all keys verify_server reads."""
    import run as runner_mod

    run_dir = tmp_path / "run"
    run_dir.mkdir()

    config_path = runner_mod._write_verify_config(
        run_dir,
        vul_image="cybergym/oss-fuzz:1234-vul",
        fix_image="cybergym/oss-fuzz:1234-fix",
        run_cmd="/usr/local/bin/run_poc",
        timeout_s=30,
        description="heap overflow in parse_header",
    )

    assert config_path.exists()
    config = json.loads(config_path.read_text())

    # verify_server reads: vul_image, fix_image, run_cmd, timeout_s, description
    assert config["vul_image"] == "cybergym/oss-fuzz:1234-vul"
    assert config["fix_image"] == "cybergym/oss-fuzz:1234-fix"
    assert config["run_cmd"] == "/usr/local/bin/run_poc"
    assert config["timeout_s"] == 30
    assert config["description"] == "heap overflow in parse_header"


# ---------------------------------------------------------------------------
# T2: Prompt / tool-surface consistency test
# ---------------------------------------------------------------------------

def _extract_tool_refs(text: str) -> set[str]:
    """Extract `mcp__<server>__<tool>` references from prompt markdown.

    Claude Code namespaces MCP tools as ``mcp__<server>__<tool>``; the prompts
    must reference that exact callable form (not a dotted ``server.tool``,
    which is an INVALID Claude Code tool name and never resolves).
    """
    import re
    return set(re.findall(r"mcp__(?:memory|verify|specialist)__[a-zA-Z_]+", text))


def _registered_mcp_names() -> set[str]:
    """Derive the real exposed tool names (``mcp__<server>__<bare>``) from the
    server modules — the bare names they actually register, namespaced by server.

    Tool names MUST be ``^[a-zA-Z0-9_-]+$`` (no dots) or Claude Code drops them.
    """
    import re
    mcp_dir = Path(__file__).resolve().parents[1] / "mcp"
    names: set[str] = set()
    # memory / verify: bare names appear as `name="..."` in their list_tools
    for server in ("memory", "verify"):
        src = (mcp_dir / f"{server}_server.py").read_text()
        for bare in re.findall(r'types\.Tool\(\s*name="([^"]+)"', src):
            assert "." not in bare, f"{server} tool name has an invalid dot: {bare!r}"
            names.add(f"mcp__{server}__{bare}")
    # specialist: bare names are the first element of each _TOOL_KINDS tuple
    import importlib.util
    spec = importlib.util.spec_from_file_location(
        "specialist_server", mcp_dir / "specialist_server.py"
    )
    specialist_mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(specialist_mod)
    for bare, _kind, _desc in specialist_mod._TOOL_KINDS:
        assert "." not in bare, f"specialist tool name has an invalid dot: {bare!r}"
        names.add(f"mcp__specialist__{bare}")
    return names


def test_prompt_tool_refs_match_registered_tools():
    """Every `mcp__server__tool` the prompts reference must be a real exposed tool,
    and the names must be dot-free (or Claude Code never registers them)."""
    prompts_dir = Path(__file__).resolve().parents[1] / "prompts"
    all_text = (prompts_dir / "system.md").read_text() + "\n" + (prompts_dir / "kickoff.md").read_text()

    refs = _extract_tool_refs(all_text)
    registered = _registered_mcp_names()

    assert registered, "no MCP tools derived from server modules"
    assert refs, "prompts reference no mcp__ tools — agent cannot discover them"

    bad_refs = refs - registered
    assert not bad_refs, (
        f"Prompt references tools not registered by any server: {bad_refs}\n"
        f"All registered: {sorted(registered)}"
    )


# ---------------------------------------------------------------------------
# T3: Submit-decision logic (server-authoritative; no local confirm). Pure, no Docker.
# The runner submits any candidate that CRASHED the vul build in tier-1 and lets the
# SERVER's official vul!=0 & fix==0 verify decide `solved`. The local vul+fix confirm
# heuristic was dropped — it false-negatived a real solve (arvo:10400 `wrong_sink`).
# ---------------------------------------------------------------------------

def _verdict(failure_class, target_likelihood, **kw):
    from mneme.verify_core import RuntimeVerdict
    return RuntimeVerdict(
        failure_class=failure_class, crash_type=kw.get("crash_type"),
        sink_fn=kw.get("sink_fn"), sink_loc=kw.get("sink_loc"),
        parser_reached=kw.get("parser_reached"),
        target_likelihood=target_likelihood, output_excerpt=kw.get("output_excerpt", ""),
    )


def _gate(verdict):
    """Run _should_submit_on_crash against a real temp candidate file."""
    import run as runner_mod
    import tempfile, os
    with tempfile.NamedTemporaryFile(delete=False) as f:
        f.write(b"poc")
        candidate_path = f.name
    try:
        return runner_mod._should_submit_on_crash(candidate_path, verdict)
    finally:
        os.unlink(candidate_path)


def test_gate_generic_crash_submits():
    should_submit, reason = _gate(_verdict("generic_crash", "high"))
    assert should_submit is True and reason == "crash_submit"


def test_gate_wrong_sink_still_submits():
    """Regression: wrong_sink crashed the vul build, so it MUST submit and let the
    server decide — the old local-confirm gate wrongly blocked this (arvo:10400)."""
    should_submit, reason = _gate(_verdict("wrong_sink", "medium", sink_fn="mng_get_long"))
    assert should_submit is True and reason == "crash_submit"


def test_gate_no_crash_does_not_submit():
    should_submit, reason = _gate(_verdict("no_crash", "low"))
    assert should_submit is False and "no_crash" in reason


def test_gate_bad_format_does_not_submit():
    should_submit, reason = _gate(_verdict("bad_format", "low"))
    assert should_submit is False and reason == "no_crash_local_bad_format"


def test_gate_no_candidate():
    import run as runner_mod
    should_submit, reason = runner_mod._should_submit_on_crash(None, _verdict("generic_crash", "high"))
    assert should_submit is False and reason == "no_candidate"


# ---------------------------------------------------------------------------
# T4: Compose test — fake-mode result.json has solved/verified/poc_path
# ---------------------------------------------------------------------------

def test_fake_solve_result_has_compose_keys(tmp_path):
    """fake-mode result.json contains solved, verified, poc_path so consolidate won't auto-refuse."""
    import subprocess, os

    task = tmp_path / "task"
    task.mkdir()
    (task / "description.txt").write_text("heap overflow in parse, tiff input")
    (task / "meta.json").write_text('{"id": "0000-fake"}')
    run_dir = tmp_path / "run"

    env = {**os.environ, "PYTHONPATH": str(_SRC), "MEMONAEMO_FAKE": "1"}
    r = subprocess.run(
        [sys.executable, str(_RUNNER / "run.py"), "solve",
         "--task-dir", str(task), "--run-dir", str(run_dir), "--fake"],
        capture_output=True, text=True, env=env, cwd=str(_HERE.parents[1]),
    )
    assert r.returncode == 0, f"solve failed:\n{r.stderr}"

    result = json.loads((run_dir / "result.json").read_text())
    assert "solved" in result, "result.json missing 'solved' key"
    assert "verified" in result, "result.json missing 'verified' key"
    assert "poc_path" in result, "result.json missing 'poc_path' key"
