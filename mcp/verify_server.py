"""
verify_server: MCP stdio server exposing verify.run and verify.confirm_if_available.

Config is read from a JSON file at the path provided in the RUN_CONFIG env var
(written by the runner in Task 7). The config file must contain:
  {
    "vul_image":   "...",
    "fix_image":   "...",          # optional for verify.run
    "run_cmd":     "...",
    "timeout_s":   30,
    "description": "..."
  }

Tools:
  verify.run                – tier-1: runs PoC on vul image, returns RuntimeVerdict JSON
  verify.confirm_if_available – tier-2: checks fix image, runs both, returns ConfirmVerdict JSON
"""
from __future__ import annotations

import json
import os
import dataclasses
from pathlib import Path

import anyio
from mcp.server import Server
from mcp.server.stdio import stdio_server
import mcp.types as types

from mneme import verify_core

# ---------------------------------------------------------------------------
# Config loading
# ---------------------------------------------------------------------------
def _load_config() -> dict:
    """Load run config from the file pointed to by RUN_CONFIG env var."""
    config_path = os.environ.get("RUN_CONFIG", "")
    if not config_path:
        raise RuntimeError("RUN_CONFIG environment variable not set")
    return json.loads(Path(config_path).read_text())


# ---------------------------------------------------------------------------
# MCP server setup
# ---------------------------------------------------------------------------
server = Server("verify")


@server.list_tools()
async def list_tools() -> list[types.Tool]:
    return [
        types.Tool(
            name="run",
            description=(
                "Tier-1 verify: run the PoC against the vulnerable image only. "
                "Returns a RuntimeVerdict with failure_class "
                "(no_crash|bad_format|wrong_sink|generic_crash) and target_likelihood."
            ),
            inputSchema={
                "type": "object",
                "properties": {
                    "candidate_path": {
                        "type": "string",
                        "description": "Absolute path to the PoC file to test.",
                    }
                },
                "required": ["candidate_path"],
            },
        ),
        types.Tool(
            name="confirm_if_available",
            description=(
                "Tier-2 verify: check whether the fix image is available then run "
                "the PoC on both vul and fix images. Returns a ConfirmVerdict with "
                "available, both_crash, post_patch_crash, target_match."
            ),
            inputSchema={
                "type": "object",
                "properties": {
                    "candidate_path": {
                        "type": "string",
                        "description": "Absolute path to the PoC file to test.",
                    }
                },
                "required": ["candidate_path"],
            },
        ),
    ]


@server.call_tool()
async def call_tool(name: str, arguments: dict) -> list[types.TextContent]:
    cfg = _load_config()
    candidate_path = Path(arguments["candidate_path"])

    if name == "run":
        verdict = verify_core.run(
            candidate_path,
            vul_image=cfg["vul_image"],
            run_cmd=cfg["run_cmd"],
            timeout_s=int(cfg["timeout_s"]),
            description=cfg["description"],
        )
        result = dataclasses.asdict(verdict)

    elif name == "confirm_if_available":
        fix_image = cfg.get("fix_image", "")
        if not fix_image:
            result = {"available": False, "reason": "fix_image not configured"}
        else:
            verdict = verify_core.confirm(
                candidate_path,
                vul_image=cfg["vul_image"],
                fix_image=fix_image,
                run_cmd=cfg["run_cmd"],
                timeout_s=int(cfg["timeout_s"]),
                description=cfg["description"],
            )
            result = dataclasses.asdict(verdict)

    else:
        raise ValueError(f"Unknown tool: {name}")

    return [types.TextContent(type="text", text=json.dumps(result, indent=2))]


# ---------------------------------------------------------------------------
# Entry point
# ---------------------------------------------------------------------------
async def _main() -> None:
    async with stdio_server() as (read_stream, write_stream):
        await server.run(
            read_stream,
            write_stream,
            server.create_initialization_options(),
        )


if __name__ == "__main__":
    anyio.run(_main)
