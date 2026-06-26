#!/usr/bin/env python3
"""
runner/run.py — Typer CLI for the mneme CyberGym agent.

Subcommands:
  solve       gen_task (--task-id) or pre-generated dir (--task-dir) → task card →
              MCP config → launch agent → optional verify.confirm gate →
              single official submit (SubmitClient) → verify+query official
              target_match → write result.json
  consolidate Dry-run consolidation proposal (wraps consolidate.propose)
  batch       Run solve over a directory of task dirs

--fake / MEMONAEMO_FAKE=1:
  Offline mode — no docker, no model, no network, no gen_task, no server.
  Synthesises a candidate file, produces a fixed RuntimeVerdict,
  writes result.json.  The official submit is NEVER called in fake mode.

Design rules enforced here:
  D9  — memory_store is NEVER created under run_dir.
  D11 — task card redaction happens only at consolidation (not during solve).
  Single-submit — SubmitClient.submit called at most once per solve (fake: never).
"""
from __future__ import annotations

import json
import os
import sys
from pathlib import Path

# ---------------------------------------------------------------------------
# Ensure src/ is on sys.path when run as a script (PYTHONPATH=src also works).
# ---------------------------------------------------------------------------
_HERE = Path(__file__).resolve()
_SRC = _HERE.parents[1] / "src"
if str(_SRC) not in sys.path:
    sys.path.insert(0, str(_SRC))

import typer
from typing import Optional

app = typer.Typer(help="mneme CyberGym agent runner")

# Locate project root relative to this script
_PROJECT_ROOT = _HERE.parent.parent


def _load_env() -> None:
    """Load repo-root .env into os.environ (real-mode only). Safe no-op if absent."""
    try:
        from mneme import cybergym_config

        cybergym_config.load_dotenv()
    except Exception:
        pass


# ---------------------------------------------------------------------------
# Helpers
# ---------------------------------------------------------------------------

def _is_fake(fake_flag: bool) -> bool:
    """Return True if --fake was passed OR MEMONAEMO_FAKE env var is set."""
    return fake_flag or bool(os.environ.get("MEMONAEMO_FAKE", ""))


def _mcp_server_env(run_dir: Path, store_dir: Path, stats_path: Path) -> dict:
    """Return env vars required by all three MCP server processes.

    memory_server needs: MEMORY_STORE_DIR, STATS_PATH, RUN_DIR
    verify_server needs: RUN_CONFIG (set after _write_verify_config is called)
    specialist_server needs no new vars (OPENAI_API_KEY etc come from os.environ)

    Returns a dict to MERGE with os.environ when spawning server subprocesses.
    This function is pure and unit-testable without launching anything.
    """
    return {
        "MEMORY_STORE_DIR": str(store_dir),
        "STATS_PATH": str(stats_path),
        "RUN_DIR": str(run_dir),
    }


def _write_verify_config(
    run_dir: Path,
    vul_image: str,
    fix_image: str,
    run_cmd: str,
    timeout_s: int,
    description: str,
) -> Path:
    """Write the verify server config JSON into run_dir/verify_config.json.

    Returns the path to the written config file.
    The verify_server reads this file at the path given by RUN_CONFIG env var.
    This function is pure and unit-testable without launching anything.
    """
    config = {
        "vul_image": vul_image,
        "fix_image": fix_image,
        "run_cmd": run_cmd,
        "timeout_s": timeout_s,
        "description": description,
    }
    config_path = run_dir / "verify_config.json"
    config_path.write_text(json.dumps(config, indent=2), encoding="utf-8")
    return config_path


def _write_mcp_config(run_dir: Path, server_env: dict | None = None) -> dict:
    """Write mcp_config.json into run_dir and return the mcp_servers dict.

    Points at the three stdio MCP servers relative to project root.
    server_env: extra env vars to pass to each server subprocess.
    Used by real (non-fake) mode only.
    """
    mcp_dir = _PROJECT_ROOT / "mcp"
    python = sys.executable

    # Claude Code/MCP passes this `env` dict as the COMPLETE child environment
    # (it does not inherit the parent). A minimal 4-var env drops PATH/HOME and
    # the API keys, which crashes the server at startup ("Connection closed") so
    # its tools never register. Merge os.environ so PATH/HOME/OPENAI_API_KEY/etc.
    # reach the server processes.
    full_env = {**os.environ, **(server_env or {})}

    mcp_servers = {
        "memory": {
            "type": "stdio",
            "command": python,
            "args": [str(mcp_dir / "memory_server.py")],
            "env": full_env,
        },
        "verify": {
            "type": "stdio",
            "command": python,
            "args": [str(mcp_dir / "verify_server.py")],
            "env": full_env,
        },
        "specialist": {
            "type": "stdio",
            "command": python,
            "args": [str(mcp_dir / "specialist_server.py")],
            "env": full_env,
        },
    }

    config_path = run_dir / "mcp_config.json"
    config_path.write_text(json.dumps(mcp_servers, indent=2), encoding="utf-8")
    return mcp_servers


def _fake_solve(task_dir: Path, run_dir: Path) -> dict:
    """Offline stub: synthesise a candidate and a fixed RuntimeVerdict.

    Never calls the agent SDK, docker, or network.
    Never creates memory_store under run_dir (D9).
    """
    from mneme.verify_core import RuntimeVerdict

    # Write a synthetic candidate
    candidates_dir = run_dir / "candidates"
    candidates_dir.mkdir(parents=True, exist_ok=True)
    candidate = candidates_dir / "candidate.bin"
    candidate.write_bytes(b"\x00" * 16)  # minimal fake PoC

    # Write a stub transcript (no memory_store path anywhere)
    transcript = run_dir / "transcript.txt"
    transcript.write_text("[fake mode — no agent invoked]\n", encoding="utf-8")

    # Fixed RuntimeVerdict — offline, deterministic
    verdict = RuntimeVerdict(
        failure_class="generic_crash",
        crash_type=None,
        sink_fn=None,
        sink_loc=None,
        parser_reached=None,
        target_likelihood="medium",
        output_excerpt="[fake mode — no docker]",
    )

    return {
        "candidate_path": str(candidate),
        "verdict": verdict,
    }


def _apply_confirm_gate(
    candidate_path: "str | None",
    verdict: "RuntimeVerdict | None",
    confirm_verdict: "ConfirmVerdict | None",
) -> tuple[bool, str]:
    """Pure confirm gate logic — returns (should_submit, reason).

    Rules (spec §5/§6):
    - If no candidate or no tier-1 verdict: do not submit.
    - confirm available + target_match=True  → submit.
    - confirm available + both_crash=True    → do not submit (too generic).
    - confirm available + target_match=False → do not submit (wrong target).
    - confirm unavailable + target_likelihood=high → submit (high-confidence fallback).
    - confirm unavailable + target_likelihood!=high → do not submit.
    """
    if not candidate_path or not Path(candidate_path).is_file():
        return False, "no_candidate"
    if verdict is None:
        return False, "no_verdict"

    if confirm_verdict is not None and confirm_verdict.available:
        if confirm_verdict.target_match:
            return True, "confirm_target_match"
        elif confirm_verdict.both_crash:
            return False, "both_crash_too_generic"
        else:
            return False, "confirm_no_target_match"
    else:
        # confirm unavailable — high-confidence fallback
        if verdict.target_likelihood == "high":
            return True, "high_confidence_fallback"
        return False, f"low_confidence_{verdict.target_likelihood}"


def _extract_repo_src(task_dir: Path, run_dir: Path) -> None:
    """Extract repo-vul.tar.gz from the task dir into run_dir/task/src/.

    Gives the agent read access to the vulnerable source. Best-effort: if the
    tarball is missing (e.g. a pre-generated dir without it) this is a no-op.
    """
    import tarfile

    tarball = task_dir / "repo-vul.tar.gz"
    if not tarball.is_file():
        return
    src_dir = run_dir / "task" / "src"
    src_dir.mkdir(parents=True, exist_ok=True)
    with tarfile.open(tarball, "r:gz") as tf:
        # Python 3.12+: filter='data' to avoid path-traversal members.
        try:
            tf.extractall(src_dir, filter="data")
        except TypeError:
            tf.extractall(src_dir)


def _real_solve(task_dir: Path, run_dir: Path, task_id: str | None = None) -> dict:
    """Real mode: wire MCP servers, call agent_driver.solve, run confirm gate.

    This path requires docker + Claude API creds.  It is import-safe and
    structurally correct but is NOT exercised by the offline smoke tests.

    ``task_id`` (e.g. "arvo:10400") drives the LOCAL image-tag derivation and is
    required in real mode.
    """
    import asyncio
    from mneme import agent_driver, task_card, cybergym_io, verify_core

    if not task_id:
        raise RuntimeError(
            "real-mode solve requires a task id for image derivation; pass --task-id "
            "(or use --task-dir together with --task-id)"
        )

    # Build task card (D11: no redaction at solve time)
    card = task_card.build(task_dir)

    # I3: Write full card markdown to task/card.md in run_dir so agent can read it
    task_subdir = run_dir / "task"
    task_subdir.mkdir(parents=True, exist_ok=True)
    card_md = task_card.to_markdown(card)
    (task_subdir / "card.md").write_text(card_md, encoding="utf-8")

    # Build card dict for agent_driver.solve (kept for backward-compat)
    card_dict = {
        "target": card.description[:200],
        "failure_class": card.vuln_classes[0] if card.vuln_classes else "unknown",
        "verifier_signal": "none",
        "input_format": card.input_format,
    }

    # Derive LOCAL images from the task id (arvo -> n132/arvo, oss-fuzz -> cybergym/oss-fuzz)
    imgs = cybergym_io.images_for(task_id)
    # arvo targets run /bin/arvo; oss-fuzz targets run /usr/local/bin/run_poc.
    run_cmd = "/bin/arvo" if task_id.split(":", 1)[0] == "arvo" else "/usr/local/bin/run_poc"
    timeout_s = 30
    description = card.description

    # C1: Write verify config file; build server env dict
    store_dir = _PROJECT_ROOT / "memory_store"
    stats_path = store_dir / "memory_stats.jsonl"
    server_env = _mcp_server_env(run_dir, store_dir, stats_path)

    # C1: Write verify config and set RUN_CONFIG in server env
    verify_config_path = _write_verify_config(
        run_dir,
        vul_image=imgs["vul_image"],
        fix_image=imgs["fix_image"],
        run_cmd=run_cmd,
        timeout_s=timeout_s,
        description=description,
    )
    server_env["RUN_CONFIG"] = str(verify_config_path)

    # Write MCP config with env vars for each server
    mcp_servers = _write_mcp_config(run_dir, server_env)

    # Build agent options (D9: memory_store NOT in add_dirs)
    skills_dir = _PROJECT_ROOT / "skills"
    options = agent_driver.build_options(run_dir, skills_dir, mcp_servers)

    # Run agent
    agent_result = asyncio.run(agent_driver.solve(card_dict, options))
    candidate_path = agent_result.get("candidate_path")

    # Tier-1 verify
    verdict = None
    if candidate_path and Path(candidate_path).is_file():
        verdict = verify_core.run(
            Path(candidate_path),
            vul_image=imgs["vul_image"],
            run_cmd=run_cmd,
            timeout_s=timeout_s,
            description=description,
        )

    # C2: Tier-2 confirm gate
    confirm_verdict = None
    if candidate_path and Path(candidate_path).is_file() and verdict is not None:
        try:
            confirm_verdict = verify_core.confirm(
                Path(candidate_path),
                vul_image=imgs["vul_image"],
                fix_image=imgs["fix_image"],
                run_cmd=run_cmd,
                timeout_s=timeout_s,
                description=description,
            )
        except Exception:
            confirm_verdict = None  # Docker unavailable — fall back to high-confidence gate

    should_submit, submit_reason = _apply_confirm_gate(candidate_path, verdict, confirm_verdict)

    return {
        "candidate_path": candidate_path,
        "verdict": verdict,
        "confirm_verdict": confirm_verdict,
        "should_submit": should_submit,
        "submit_reason": submit_reason,
    }


# ---------------------------------------------------------------------------
# solve subcommand
# ---------------------------------------------------------------------------

@app.command()
def solve(
    task_dir: Optional[Path] = typer.Option(None, "--task-dir", help="Pre-generated task directory"),
    task_id: Optional[str] = typer.Option(None, "--task-id", help="CyberGym task id, e.g. arvo:10400 (real mode: gen_task into run_dir/task)"),
    run_dir: Path = typer.Option(..., "--run-dir", help="Run workspace directory"),
    fake: bool = typer.Option(False, "--fake", help="Offline stub mode (no docker/model/network)"),
    difficulty: str = typer.Option("level1", "--difficulty", help="CyberGym difficulty level"),
    model: str = typer.Option("claude-opus-4-8", "--model", help="Model identifier"),
) -> None:
    """Prepare card → launch agent → verify → single official submit → write result.json."""
    from mneme import cybergym_io

    fake_mode = _is_fake(fake)

    # Create run_dir (never create memory_store under it — D9)
    run_dir.mkdir(parents=True, exist_ok=True)

    # Resolve the task id used for LOCAL image-tag derivation.
    resolved_task_id = task_id

    # Real mode with --task-id and no pre-generated --task-dir: generate the task dir
    # via the real cybergym harness.
    task_handle = None
    if not fake_mode and task_id is not None and task_dir is None:
        _load_env()
        from mneme import cybergym_config

        config = cybergym_config.load_config()
        gen_out = run_dir / "task" / "gen"
        task_handle = cybergym_io.gen_task(task_id, gen_out, config=config, difficulty=difficulty)
        task_dir = task_handle.task_dir
        _extract_repo_src(task_dir, run_dir)
        resolved_task_id = task_id

    if task_dir is None:
        typer.echo("ERROR: one of --task-dir or --task-id is required", err=True)
        raise typer.Exit(2)

    if fake_mode:
        solve_result = _fake_solve(task_dir, run_dir)
    else:
        solve_result = _real_solve(task_dir, run_dir, task_id=resolved_task_id)

    candidate_path = solve_result.get("candidate_path")
    verdict = solve_result.get("verdict")
    confirm_verdict = solve_result.get("confirm_verdict")
    # In fake mode there is no gate result; fake mode never submits
    should_submit = solve_result.get("should_submit", False) and not fake_mode
    submit_reason = solve_result.get("submit_reason", "fake_mode" if fake_mode else "no_gate_result")

    # Build result dict — always contains failure_class (from RuntimeVerdict)
    result: dict = {}

    if verdict is not None:
        result["failure_class"] = verdict.failure_class
        result["target_likelihood"] = verdict.target_likelihood
        if verdict.crash_type is not None:
            result["crash_type"] = verdict.crash_type
        if verdict.sink_fn is not None:
            result["sink_fn"] = verdict.sink_fn
    else:
        result["failure_class"] = "no_crash"
        result["target_likelihood"] = "low"

    if candidate_path:
        result["candidate_path"] = candidate_path

    # C2: Single official submit — only when gate approves, only in real mode, only once.
    # Submit the candidate to the REAL server, then ask the private verifier to re-run
    # it on vul+fix and query the stored records for the official target_match.
    target_match = False
    if should_submit and candidate_path:
        from mneme import cybergym_config

        config = cybergym_config.load_config()

        # Resolve the submission handle: from gen_task (--task-id) or by parsing submit.sh.
        handle = task_handle
        if handle is None:
            info = cybergym_io._parse_submit_sh(task_dir / "submit.sh")
            handle = cybergym_io.TaskHandle(
                task_id=resolved_task_id or "",
                task_dir=task_dir,
                masked_id=info["task_id"],
                agent_id=info["agent_id"],
                checksum=info["checksum"],
                server_url=info["server_url"] or config.server_url,
            )

        client = cybergym_io.SubmitClient.from_handle(handle, config.cybergym_api_key)
        submit_verdict = client.submit(Path(candidate_path))
        result["submit_exit_code"] = submit_verdict.exit_code
        result["submit_poc_id"] = submit_verdict.poc_id

        # Official reproduction: re-run on vul+fix and read the recorded exit codes.
        client.verify_agent_pocs()
        official = client.official_target_match()
        target_match = bool(official["target_match"])
        result["target_match"] = target_match
        result["official_vul_exit"] = official["vul_exit"]
        result["official_fix_exit"] = official["fix_exit"]

    # M2: Write solved/verified/poc_path so consolidate.propose won't auto-refuse
    # solved/verified = True only when confirm gate confirmed a real target match
    confirmed_target = (
        confirm_verdict is not None
        and confirm_verdict.available
        and confirm_verdict.target_match
    ) or target_match
    result["solved"] = confirmed_target
    result["verified"] = confirmed_target
    result["poc_path"] = candidate_path if candidate_path else None
    result["submit_reason"] = submit_reason

    # Write result.json
    result_path = run_dir / "result.json"
    result_path.write_text(json.dumps(result, indent=2), encoding="utf-8")

    # Sanity: assert no memory_store leaked under run_dir (D9)
    leaked = list(run_dir.rglob("memory_store"))
    if leaked:
        typer.echo(f"ERROR: D9 violation — memory_store found under run_dir: {leaked}", err=True)
        raise typer.Exit(1)

    typer.echo(f"Done. result.json written to {result_path}")


# ---------------------------------------------------------------------------
# consolidate subcommand (dry-run)
# ---------------------------------------------------------------------------

@app.command()
def consolidate(
    result_file: Path = typer.Option(..., "--result-file", help="Path to result.json"),
    split_file: Optional[Path] = typer.Option(None, "--split-file", help="Path to split.json"),
    out_dir: Optional[Path] = typer.Option(None, "--out-dir", help="Output directory for proposal"),
) -> None:
    """Dry-run consolidation proposal from a solved run result."""
    from mneme import consolidate as cons

    result_json = json.loads(result_file.read_text())
    split = json.loads(split_file.read_text()) if split_file else {}

    proposal = cons.propose(result_json, split, out_dir=out_dir)
    if proposal.refused:
        typer.echo(f"Consolidation refused: {proposal.reason}")
        raise typer.Exit(1)
    else:
        typer.echo(f"Proposal written to {proposal.out_path}")
        typer.echo(f"Status: {proposal.status}")


# ---------------------------------------------------------------------------
# batch subcommand
# ---------------------------------------------------------------------------

@app.command()
def batch(
    tasks_dir: Path = typer.Option(..., "--tasks-dir", help="Directory containing task subdirs"),
    runs_dir: Path = typer.Option(..., "--runs-dir", help="Directory to write per-task run dirs"),
    fake: bool = typer.Option(False, "--fake", help="Offline stub mode"),
    model: str = typer.Option("claude-opus-4-8", "--model"),
) -> None:
    """Run solve over all subdirectories of tasks_dir."""
    task_dirs = sorted(p for p in tasks_dir.iterdir() if p.is_dir())
    if not task_dirs:
        typer.echo("No task directories found.")
        raise typer.Exit(1)

    for td in task_dirs:
        rd = runs_dir / td.name
        typer.echo(f"Solving {td.name} ...")
        # Invoke solve for each task via Typer's context
        solve(task_dir=td, task_id=None, run_dir=rd, fake=fake, difficulty="level1", model=model)


# ---------------------------------------------------------------------------
# Entry point
# ---------------------------------------------------------------------------

if __name__ == "__main__":
    app()
