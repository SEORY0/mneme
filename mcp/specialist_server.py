"""specialist_server.py — MCP stdio server for the GPT-5.5 specialist advisor.

Exposes five tools (one per specialist kind):
  specialist.rethink_reachability
  specialist.relocalize_sink
  specialist.escape_basin
  specialist.diversify_family
  specialist.review_consolidation

Each tool calls specialist_core.advise() with the matching kind after
redacting the diagnosis for scope hygiene.

Config (env vars):
  OPENAI_API_KEY             – required for live calls (not needed at import time)
  MEMONAEMO_SPECIALIST_MODEL – override / offline fallback model id

Design rules:
  - Model is resolved once at startup via resolve_model(); if the client is
    unavailable (no key / offline) the env fallback is used — construction
    never raises.
  - The specialist NEVER writes memory or submits.
"""
from __future__ import annotations

import json
import os

import anyio
from mcp.server import Server
from mcp.server.stdio import stdio_server
import mcp.types as types

from mneme import specialist_core

# ---------------------------------------------------------------------------
# Client + model — resolved at startup, gracefully offline
# ---------------------------------------------------------------------------

def _build_client():
    """Construct the OpenAI client.  Returns None if the SDK is not installed
    or no key is available (server will refuse tool calls at runtime)."""
    api_key = os.environ.get("OPENAI_API_KEY", "")
    try:
        from openai import OpenAI  # type: ignore
        return OpenAI(api_key=api_key or "offline-placeholder")
    except Exception:
        return None


_client = _build_client()

# Resolve model once at startup; guard against offline / no client
_model: str
try:
    if _client is not None:
        _model = specialist_core.resolve_model(_client)
    else:
        _model = os.environ.get("MEMONAEMO_SPECIALIST_MODEL", "gpt-5.5")
except Exception:
    _model = os.environ.get("MEMONAEMO_SPECIALIST_MODEL", "gpt-5.5")

# ---------------------------------------------------------------------------
# MCP server
# ---------------------------------------------------------------------------

server = Server("specialist")

_TOOL_KINDS = [
    ("specialist.rethink_reachability", "rethink_reachability",
     "Hard-failure specialist: redesign the reachability path to the target sink."),
    ("specialist.relocalize_sink", "relocalize_sink",
     "Hard-failure specialist: relocalize the crash/sink target."),
    ("specialist.escape_basin", "escape_basin",
     "Hard-failure specialist: escape a local basin of attraction."),
    ("specialist.diversify_family", "diversify_family",
     "Hard-failure specialist: diversify the corpus/seed family."),
    ("specialist.review_consolidation", "review_consolidation",
     "Hard-failure specialist: review and consolidate offline knowledge."),
]

_INPUT_SCHEMA = {
    "type": "object",
    "properties": {
        "diagnosis": {
            "type": "object",
            "description": (
                "Failure diagnosis dict. Will be redacted (task ids / offsets / "
                "checksums stripped) before reaching the specialist."
            ),
        },
        "repair_policy": {
            "type": ["object", "null"],
            "description": "Compact repair policy record, or null.",
        },
    },
    "required": ["diagnosis"],
}


@server.list_tools()
async def list_tools() -> list[types.Tool]:
    return [
        types.Tool(name=name, description=desc, inputSchema=_INPUT_SCHEMA)
        for name, _kind, desc in _TOOL_KINDS
    ]


@server.call_tool()
async def call_tool(name: str, arguments: dict) -> list[types.TextContent]:
    kind_map = {n: k for n, k, _ in _TOOL_KINDS}
    if name not in kind_map:
        raise ValueError(f"Unknown tool: {name}")
    if _client is None:
        raise RuntimeError("OpenAI client unavailable — check OPENAI_API_KEY")

    result = specialist_core.advise(
        kind=kind_map[name],
        diagnosis=arguments.get("diagnosis", {}),
        repair_policy=arguments.get("repair_policy"),
        client=_client,
        model=_model,
    )
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
