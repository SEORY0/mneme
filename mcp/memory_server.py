"""
memory_server: MCP stdio server exposing the five memory tools with tool-name
scope boundaries (D3).

Config is read from environment variables set by the runner:
  MEMORY_STORE_DIR  – absolute path to the memory_store/ directory
  STATS_PATH        – absolute path to the stats .jsonl file
  RUN_DIR           – absolute path to the current run directory (for proposals)

Design rules enforced here:
  D3  – SCOPE = TOOL NAME (one tool per permission boundary)
  D9  – this process is the ONLY reader of memory_store/; it is launched with
        NO filesystem tools, so agents cannot bypass the scope boundaries by
        reading OKF files directly.

Tools:
  memory.search_okf_for_generate   – GENERATE scope; ranked compact records
  memory.get_repair_policy         – GENERATE scope; best compact record or null
  memory.get_discriminator_evidence – DISCRIMINATE scope; verifier_summary +
                                      candidate_metadata ONLY
  memory.record_proposal           – writes under RUN_DIR/proposals/; NEVER
                                     writes to memory_store/okf/
  memory.scope_check               – visibility query against the VISIBILITY map
"""
from __future__ import annotations

import json
import os
from pathlib import Path

import anyio
from mcp.server import Server
from mcp.server.stdio import stdio_server
import mcp.types as types

from memonaemo import memory_api, stats as stats_mod

# ---------------------------------------------------------------------------
# Config helpers
# ---------------------------------------------------------------------------

def _store_dir() -> Path:
    v = os.environ.get("MEMORY_STORE_DIR", "")
    if not v:
        raise RuntimeError("MEMORY_STORE_DIR environment variable not set")
    return Path(v)


def _stats() -> stats_mod.Stats:
    path = os.environ.get("STATS_PATH", "")
    if not path:
        return stats_mod.Stats()
    return stats_mod.Stats.load(Path(path))


def _run_dir() -> Path:
    v = os.environ.get("RUN_DIR", "")
    if not v:
        raise RuntimeError("RUN_DIR environment variable not set")
    return Path(v)


# ---------------------------------------------------------------------------
# MCP server
# ---------------------------------------------------------------------------

server = Server("memory")


@server.list_tools()
async def list_tools() -> list[types.Tool]:
    return [
        types.Tool(
            name="memory.search_okf_for_generate",
            description=(
                "GENERATE scope. Search the OKF causal-policy store for compact "
                "records that match the supplied query keys. Returns a list of "
                "compact records: {name, policy, procedure, negative_memory, "
                "evidence_level}."
            ),
            inputSchema={
                "type": "object",
                "properties": {
                    "query_keys": {
                        "type": "object",
                        "description": (
                            "Dict of query keys, e.g. "
                            "{\"failure_class\": \"bad_format\", "
                            "\"verifier_signal\": \"parser_not_reached\"}."
                        ),
                    }
                },
                "required": ["query_keys"],
            },
        ),
        types.Tool(
            name="memory.get_repair_policy",
            description=(
                "GENERATE scope. Return the best-matching causal repair policy as "
                "a compact record ({name, policy, procedure, negative_memory, "
                "evidence_level}) or null. NEVER returns the full OKF body."
            ),
            inputSchema={
                "type": "object",
                "properties": {
                    "failure_class": {
                        "type": "string",
                        "description": "e.g. bad_format, generic_crash, wrong_sink, no_crash",
                    },
                    "verifier_signal": {
                        "type": "string",
                        "description": "e.g. parser_not_reached, exit_0, wrong_address",
                    },
                    "input_format": {"type": "string"},
                    "harness_convention": {"type": "string"},
                    "vuln_class": {"type": "string"},
                },
                "required": ["failure_class", "verifier_signal"],
            },
        ),
        types.Tool(
            name="memory.get_discriminator_evidence",
            description=(
                "DISCRIMINATE scope. Returns {verifier_summary, candidate_metadata} "
                "ONLY. Has NO access to OKF, causal policies, or generate reasoning — "
                "the isolation is structural (no store_dir parameter exists on the "
                "underlying function). Defined for v1; not called by the main loop "
                "(D10)."
            ),
            inputSchema={
                "type": "object",
                "properties": {
                    "candidate_id": {
                        "type": "string",
                        "description": "Opaque candidate identifier.",
                    },
                    "candidate_meta": {
                        "type": "object",
                        "description": "Metadata dict about the candidate.",
                    },
                    "verifier_summary": {
                        "type": "object",
                        "description": "Verifier output summary dict.",
                    },
                },
                "required": ["candidate_id"],
            },
        ),
        types.Tool(
            name="memory.record_proposal",
            description=(
                "Write a dry-run proposal JSON under RUN_DIR/proposals/. "
                "NEVER writes to memory_store/okf/ or any OKF path."
            ),
            inputSchema={
                "type": "object",
                "properties": {
                    "payload": {
                        "type": "object",
                        "description": "Proposal data to persist.",
                    }
                },
                "required": ["payload"],
            },
        ),
        types.Tool(
            name="memory.scope_check",
            description=(
                "Query whether a given tool is permitted to see a given memory class. "
                "Returns {visible: bool, memory_class, tool}."
            ),
            inputSchema={
                "type": "object",
                "properties": {
                    "memory_class": {
                        "type": "string",
                        "description": (
                            "One of: causal_policy, okf_example, procedure, "
                            "negative_memory, verifier_summary, candidate_metadata, "
                            "proposal."
                        ),
                    },
                    "tool": {
                        "type": "string",
                        "description": "Full tool name, e.g. memory.get_repair_policy.",
                    },
                },
                "required": ["memory_class", "tool"],
            },
        ),
    ]


@server.call_tool()
async def call_tool(name: str, arguments: dict) -> list[types.TextContent]:
    if name == "memory.search_okf_for_generate":
        result = memory_api.search_okf_for_generate(
            store_dir=_store_dir(),
            stats=_stats(),
            query_keys=arguments["query_keys"],
        )

    elif name == "memory.get_repair_policy":
        result = memory_api.get_repair_policy(
            store_dir=_store_dir(),
            stats=_stats(),
            failure_class=arguments["failure_class"],
            verifier_signal=arguments["verifier_signal"],
            input_format=arguments.get("input_format"),
            harness_convention=arguments.get("harness_convention"),
            vuln_class=arguments.get("vuln_class"),
        )

    elif name == "memory.get_discriminator_evidence":
        # DISCRIMINATE scope — store_dir is intentionally NOT passed.
        # candidate_id is accepted for the MCP interface but the pure function
        # only uses candidate_meta + verifier_summary.
        candidate_meta = arguments.get("candidate_meta") or {"id": arguments.get("candidate_id", "")}
        verifier_summary = arguments.get("verifier_summary") or {}
        result = memory_api.get_discriminator_evidence(
            candidate_meta=candidate_meta,
            verifier_summary=verifier_summary,
        )

    elif name == "memory.record_proposal":
        result = memory_api.record_proposal(
            run_dir=_run_dir(),
            payload=arguments["payload"],
        )

    elif name == "memory.scope_check":
        result = memory_api.scope_check(
            memory_class=arguments["memory_class"],
            tool=arguments["tool"],
        )

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
