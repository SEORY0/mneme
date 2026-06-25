"""
agent_driver: wires the Claude Agent SDK with D9 filesystem isolation.

Design rule D9: the agent's filesystem tools (Read/Grep/Glob/Bash) are
confined to the RUN WORKSPACE + the skills/ dir.  memory_store/ is NEVER
added to the allowed roots — OKF reaches the agent ONLY via the memory.*
MCP tools, never by direct file reads.

Key SDK fields used:
  - cwd        : set to run_dir (establishes the implicit allowed root)
  - add_dirs   : list[str | Path] — additional allowed directories; we add
                 skills_dir here and NEVER add memory_store
  - system_prompt : str — the loaded text of prompts/system.md
  - mcp_servers   : dict[name, McpSdkServerConfig] — the three MCP servers
  - model         : str — model identifier

allowed_fs_roots(opts) reads [opts.cwd] + opts.add_dirs so the test can
assert on real option state (not a hardcoded echo).
"""
from __future__ import annotations

import asyncio
from pathlib import Path
from typing import Any

import claude_agent_sdk as sdk
from claude_agent_sdk import ClaudeAgentOptions, ClaudeSDKClient

# ---------------------------------------------------------------------------
# Resolve the prompts directory relative to this module's location.
# The prompts/ dir sits at the project root, two levels above src/memonaemo/.
# ---------------------------------------------------------------------------
_PROMPTS_DIR = Path(__file__).resolve().parents[2] / "prompts"


def _load_system_prompt() -> str:
    """Load prompts/system.md text. Raises FileNotFoundError if missing."""
    path = _PROMPTS_DIR / "system.md"
    return path.read_text(encoding="utf-8")


# ---------------------------------------------------------------------------
# Public interface
# ---------------------------------------------------------------------------

def build_options(
    run_dir: Path | str,
    skills_dir: Path | str,
    mcp_servers: dict[str, Any],
    model: str = "claude-opus-4-8",
) -> ClaudeAgentOptions:
    """
    Build ClaudeAgentOptions with D9-compliant filesystem isolation.

    Filesystem roots allowed:
      - cwd = run_dir         (implicit allowed root for all FS tools)
      - add_dirs = [skills_dir]  (reference procedures, read-only by convention)

    memory_store/ is NOT in cwd or add_dirs — it is deliberately excluded.
    OKF is accessible only via the memory.* MCP tool surface.
    """
    run_dir = Path(run_dir)
    skills_dir = Path(skills_dir)

    system_prompt_text = _load_system_prompt()

    return ClaudeAgentOptions(
        cwd=run_dir,
        add_dirs=[skills_dir],
        system_prompt=system_prompt_text,
        mcp_servers=mcp_servers,
        model=model,
        permission_mode="bypassPermissions",
        setting_sources=[],  # ignore user/project/local settings for reproducibility
    )


def allowed_fs_roots(opts: ClaudeAgentOptions) -> list[Path]:
    """
    Return the resolved filesystem roots encoded in opts.

    Reads the REAL option state: [opts.cwd] + opts.add_dirs.
    The test asserts on this list, not on a hardcoded echo.
    """
    roots: list[Path] = []
    if opts.cwd is not None:
        roots.append(Path(opts.cwd))
    for d in (opts.add_dirs or []):
        roots.append(Path(d))
    return roots


def system_prompt_text(opts: ClaudeAgentOptions) -> str:
    """Return the system prompt text stored in opts."""
    sp = opts.system_prompt
    if sp is None:
        return ""
    # system_prompt is stored as a plain str in our build_options
    return str(sp)


# ---------------------------------------------------------------------------
# solve — async agent loop
# ---------------------------------------------------------------------------

async def solve(card: dict, options: ClaudeAgentOptions) -> dict:
    """
    Run the agent loop to completion via ClaudeSDKClient.

    Returns a result dict: {candidate_path, transcript_path, stop_reason, cost}.

    The unit tests do NOT invoke this against a live model; it is implemented
    correctly so it is import-safe and structurally sound.
    """
    run_dir = Path(options.cwd) if options.cwd else Path.cwd()
    transcript: list[str] = []
    stop_reason: str = "max_turns"
    cost: float = 0.0
    candidate_path: str | None = None

    # Build kickoff prompt from card fields
    kickoff_lines = [
        "Begin. Task card loaded from options.",
        f"Target: {card.get('target', 'unknown')}",
        f"Failure class: {card.get('failure_class', 'unknown')}",
        f"Verifier signal: {card.get('verifier_signal', 'unknown')}",
    ]
    prompt = "\n".join(kickoff_lines)

    async with ClaudeSDKClient(options=options) as client:
        await client.connect(prompt)
        async for message in client:
            # Collect transcript
            transcript.append(repr(message))

            # Check for result/stop messages
            if isinstance(message, sdk.ResultMessage):
                stop_reason = getattr(message, "stop_reason", "end_turn") or "end_turn"
                usage = getattr(message, "usage", None)
                if usage:
                    cost = getattr(usage, "total_cost_usd", 0.0) or 0.0
                break

    # Write transcript to run workspace
    transcript_path = run_dir / "transcript.txt"
    transcript_path.write_text("\n".join(transcript), encoding="utf-8")

    # Candidate path is conventional — the agent writes here per the kickoff prompt
    candidate_dir = run_dir / "candidate"
    if candidate_dir.exists():
        candidates = list(candidate_dir.iterdir())
        if candidates:
            candidate_path = str(candidates[0])

    return {
        "candidate_path": candidate_path,
        "transcript_path": str(transcript_path),
        "stop_reason": stop_reason,
        "cost": cost,
    }
