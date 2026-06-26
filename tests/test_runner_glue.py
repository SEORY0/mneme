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
# T3: Confirm gate logic tests (pure, no Docker)
# ---------------------------------------------------------------------------

def test_confirm_gate_target_match_submits():
    """Gate: confirm available + target_match → should submit."""
    import run as runner_mod
    from mneme.verify_core import RuntimeVerdict, ConfirmVerdict

    verdict = RuntimeVerdict(
        failure_class="generic_crash", crash_type="heap-buffer-overflow",
        sink_fn="parse_header", sink_loc="parser.c:128", parser_reached=True,
        target_likelihood="high", output_excerpt="..."
    )
    confirm = ConfirmVerdict(available=True, both_crash=False, post_patch_crash=False, target_match=True)

    # We need a fake candidate file
    import tempfile, os
    with tempfile.NamedTemporaryFile(delete=False) as f:
        f.write(b"poc")
        candidate_path = f.name
    try:
        should_submit, reason = runner_mod._apply_confirm_gate(candidate_path, verdict, confirm)
        assert should_submit is True
        assert reason == "confirm_target_match"
    finally:
        os.unlink(candidate_path)


def test_confirm_gate_both_crash_does_not_submit():
    """Gate: confirm available + both_crash → do NOT submit."""
    import run as runner_mod
    from mneme.verify_core import RuntimeVerdict, ConfirmVerdict
    import tempfile, os

    verdict = RuntimeVerdict(
        failure_class="generic_crash", crash_type="heap-buffer-overflow",
        sink_fn="parse_header", sink_loc="parser.c:128", parser_reached=True,
        target_likelihood="high", output_excerpt="..."
    )
    confirm = ConfirmVerdict(available=True, both_crash=True, post_patch_crash=True, target_match=False)

    with tempfile.NamedTemporaryFile(delete=False) as f:
        f.write(b"poc")
        candidate_path = f.name
    try:
        should_submit, reason = runner_mod._apply_confirm_gate(candidate_path, verdict, confirm)
        assert should_submit is False
        assert reason == "both_crash_too_generic"
    finally:
        os.unlink(candidate_path)


def test_confirm_gate_unavailable_high_likelihood_submits():
    """Gate: confirm unavailable + target_likelihood=high → submit (high-confidence fallback)."""
    import run as runner_mod
    from mneme.verify_core import RuntimeVerdict, ConfirmVerdict
    import tempfile, os

    verdict = RuntimeVerdict(
        failure_class="generic_crash", crash_type="heap-buffer-overflow",
        sink_fn="parse_header", sink_loc="parser.c:128", parser_reached=True,
        target_likelihood="high", output_excerpt="..."
    )
    confirm = ConfirmVerdict(available=False)

    with tempfile.NamedTemporaryFile(delete=False) as f:
        f.write(b"poc")
        candidate_path = f.name
    try:
        should_submit, reason = runner_mod._apply_confirm_gate(candidate_path, verdict, confirm)
        assert should_submit is True
        assert reason == "high_confidence_fallback"
    finally:
        os.unlink(candidate_path)


def test_confirm_gate_unavailable_low_likelihood_does_not_submit():
    """Gate: confirm unavailable + target_likelihood!=high → do NOT submit."""
    import run as runner_mod
    from mneme.verify_core import RuntimeVerdict, ConfirmVerdict
    import tempfile, os

    verdict = RuntimeVerdict(
        failure_class="no_crash", crash_type=None,
        sink_fn=None, sink_loc=None, parser_reached=None,
        target_likelihood="low", output_excerpt=""
    )
    confirm = ConfirmVerdict(available=False)

    with tempfile.NamedTemporaryFile(delete=False) as f:
        f.write(b"poc")
        candidate_path = f.name
    try:
        should_submit, reason = runner_mod._apply_confirm_gate(candidate_path, verdict, confirm)
        assert should_submit is False
        assert "low" in reason
    finally:
        os.unlink(candidate_path)


def test_confirm_gate_no_target_match_does_not_submit():
    """Gate: confirm available + target_match=False (no match) → do NOT submit."""
    import run as runner_mod
    from mneme.verify_core import RuntimeVerdict, ConfirmVerdict
    import tempfile, os

    verdict = RuntimeVerdict(
        failure_class="generic_crash", crash_type="heap-buffer-overflow",
        sink_fn="parse_header", sink_loc="parser.c:128", parser_reached=True,
        target_likelihood="medium", output_excerpt="..."
    )
    confirm = ConfirmVerdict(available=True, both_crash=False, post_patch_crash=False, target_match=False)

    with tempfile.NamedTemporaryFile(delete=False) as f:
        f.write(b"poc")
        candidate_path = f.name
    try:
        should_submit, reason = runner_mod._apply_confirm_gate(candidate_path, verdict, confirm)
        assert should_submit is False
        assert reason == "confirm_no_target_match"
    finally:
        os.unlink(candidate_path)


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
