#!/usr/bin/env python3
"""
runner/run.py — Typer CLI for the memonaemo CyberGym agent.

Subcommands:
  solve       Prepare task card → write MCP config → launch agent →
              optional verify.confirm gate → submit_once → write result.json
  consolidate Dry-run consolidation proposal (wraps consolidate.propose)
  batch       Run solve over a directory of task dirs

--fake / MEMONAEMO_FAKE=1:
  Offline mode — no docker, no model, no network.
  Synthesises a candidate file, produces a fixed RuntimeVerdict,
  writes result.json.  submit_once is NEVER called in fake mode.

Design rules enforced here:
  D9  — memory_store is NEVER created under run_dir.
  D11 — task card redaction happens only at consolidation (not during solve).
  Single-submit — submit_once called at most once per solve (fake: never).
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

app = typer.Typer(help="memonaemo CyberGym agent runner")

# Locate project root relative to this script
_PROJECT_ROOT = _HERE.parent.parent


# ---------------------------------------------------------------------------
# Helpers
# ---------------------------------------------------------------------------

def _is_fake(fake_flag: bool) -> bool:
    """Return True if --fake was passed OR MEMONAEMO_FAKE env var is set."""
    return fake_flag or bool(os.environ.get("MEMONAEMO_FAKE", ""))


def _write_mcp_config(run_dir: Path) -> dict:
    """Write mcp_config.json into run_dir and return the mcp_servers dict.

    Points at the three stdio MCP servers relative to project root.
    Used by real (non-fake) mode only.
    """
    mcp_dir = _PROJECT_ROOT / "mcp"
    python = sys.executable

    mcp_servers = {
        "memory": {
            "type": "stdio",
            "command": python,
            "args": [str(mcp_dir / "memory_server.py")],
        },
        "verify": {
            "type": "stdio",
            "command": python,
            "args": [str(mcp_dir / "verify_server.py")],
        },
        "specialist": {
            "type": "stdio",
            "command": python,
            "args": [str(mcp_dir / "specialist_server.py")],
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
    from memonaemo.verify_core import RuntimeVerdict

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


def _real_solve(task_dir: Path, run_dir: Path) -> dict:
    """Real mode: wire MCP servers, call agent_driver.solve, run confirm gate.

    This path requires docker + Claude API creds.  It is import-safe and
    structurally correct but is NOT exercised by the offline smoke tests.
    """
    import asyncio
    from memonaemo import agent_driver, task_card, cybergym_io, verify_core

    # Build task card (D11: no redaction at solve time)
    card = task_card.build(task_dir)
    card_dict = {
        "target": card.description[:200],
        "failure_class": card.vuln_classes[0] if card.vuln_classes else "unknown",
        "verifier_signal": "none",
        "input_format": card.input_format,
    }

    # Write MCP config and build server map
    mcp_servers = _write_mcp_config(run_dir)

    # Build agent options (D9: memory_store NOT in add_dirs)
    skills_dir = _PROJECT_ROOT / "skills"
    options = agent_driver.build_options(run_dir, skills_dir, mcp_servers)

    # Run agent
    agent_result = asyncio.run(agent_driver.solve(card_dict, options))
    candidate_path = agent_result.get("candidate_path")

    # Derive images
    imgs = cybergym_io.images_for(task_dir)
    run_cmd = "/usr/local/bin/run_poc"
    timeout_s = 30
    description = card.description

    # Tier-1 verify (optional confirm gate)
    verdict = None
    if candidate_path and Path(candidate_path).is_file():
        verdict = verify_core.run(
            Path(candidate_path),
            vul_image=imgs["vul_image"],
            run_cmd=run_cmd,
            timeout_s=timeout_s,
            description=description,
        )

    return {
        "candidate_path": candidate_path,
        "verdict": verdict,
    }


# ---------------------------------------------------------------------------
# solve subcommand
# ---------------------------------------------------------------------------

@app.command()
def solve(
    task_dir: Path = typer.Option(..., "--task-dir", help="Task directory"),
    run_dir: Path = typer.Option(..., "--run-dir", help="Run workspace directory"),
    fake: bool = typer.Option(False, "--fake", help="Offline stub mode (no docker/model/network)"),
    model: str = typer.Option("claude-opus-4-8", "--model", help="Model identifier"),
) -> None:
    """Prepare card → launch agent → verify → submit_once → write result.json."""
    from memonaemo import cybergym_io

    fake_mode = _is_fake(fake)

    # Create run_dir (never create memory_store under it — D9)
    run_dir.mkdir(parents=True, exist_ok=True)

    if fake_mode:
        solve_result = _fake_solve(task_dir, run_dir)
    else:
        solve_result = _real_solve(task_dir, run_dir)

    candidate_path = solve_result.get("candidate_path")
    verdict = solve_result.get("verdict")

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

    # Single official submit — only in real mode AND only once
    if not fake_mode and candidate_path and Path(candidate_path).is_file():
        submit_meta = cybergym_io.parse_submit(task_dir)
        if isinstance(submit_meta, cybergym_io.SubmitMeta):
            submit_result = cybergym_io.submit_once(Path(candidate_path), submit_meta)
            result["target_match"] = submit_result.get("target_match", False)
            result["both_crash"] = submit_result.get("both_crash", False)

    # Write result.json
    result_path = run_dir / "result.json"
    result_path.write_text(json.dumps(result, indent=2), encoding="utf-8")

    # Sanity: assert no memory_store leaked under run_dir (D9)
    leaked = list(run_dir.rglob("memory_store"))
    if leaked:
        typer.echo(f"WARNING: memory_store found under run_dir: {leaked}", err=True)

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
    from memonaemo import consolidate as cons

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
        solve(task_dir=td, run_dir=rd, fake=fake, model=model)


# ---------------------------------------------------------------------------
# Entry point
# ---------------------------------------------------------------------------

if __name__ == "__main__":
    app()
