# mneme

**CyberGym Level-1 PoC agent** — verification-gated, scope-isolated causal memory.

The differentiator vs Crystalline is not a bigger harness or a bigger OKF; it is
**keyed markdown + MCP-enforced scoped memory + verifier-gated consolidation**.

---

## Architecture

Full design spec: [`docs/superpowers/specs/2026-06-25-mneme-design.md`](docs/superpowers/specs/2026-06-25-mneme-design.md)

```
mneme/
  runner/
    run.py              CLI: solve / consolidate / batch
  mcp/
    memory_server.py    memory.* tools (5 tools)
    verify_server.py    verify.* tools (2 tools)
    specialist_server.py  specialist.* tools (5 tools — GPT-5.5 advisor)
  memory_store/         NOT agent-readable (D9) — served only via memory.* MCP tools
    okf/                curated OKF: index, vuln-classes, formats, strategies, causal-policies
    memory_stats.jsonl  success/frequency/recency sidecar
  skills/               curated tool-use guides — directly agent-readable
  prompts/
    system.md           memory-first system prompt; tool-scope protocol
  data/
    okf_split.json      train/eval split
  scripts/
    audit_leak.py       OKF leak audit
  src/mneme/        Python library (runner / MCP / glue only — no policy logic)
    task_card.py        task dir -> compact redacted task card
    cybergym_io.py      task generation, submit.sh parsing, docker verify shell-out
    agent_driver.py     launch Claude Agent SDK session + collect result
    consolidate.py      offline verifier-gated causal-distill (train-only, dry-run)
  tests/
```

---

## Three MCP Servers

### 1. `memory` (`mcp/memory_server.py`)

Tool name = scope boundary (decision D3). Five tools:

| Tool | Scope | Returns |
|------|-------|---------|
| `memory.search_okf_for_generate` | GENERATE | Ranked compact OKF records: `{name, policy, procedure, negative_memory, evidence_level}` |
| `memory.get_repair_policy` | GENERATE | Best-matching causal repair policy (compact) keyed by `failure_class × verifier_signal`. Never returns the full OKF body. |
| `memory.get_discriminator_evidence` | DISCRIMINATE | `{verifier_summary, candidate_metadata}` only. Structurally cannot reach OKF or generate reasoning (no `store_dir` param). Defined for v1; not called by the main loop (D10). |
| `memory.record_proposal` | housekeeping | Writes a dry-run proposal JSON under `RUN_DIR/proposals/`. Never writes to `memory_store/okf/`. |
| `memory.scope_check` | housekeeping | Reports visibility for a given `(memory_class, tool)` pair. |

### 2. `verify` (`mcp/verify_server.py`)

Two tools — signal split is strict (see below):

| Tool | Tier | Returns |
|------|------|---------|
| `verify.run` | Tier 1 (vul image only) | `RuntimeVerdict`: `failure_class`, `crash_type`, `sink_fn`, `sink_loc`, `parser_reached`, `target_likelihood`, `output_excerpt` |
| `verify.confirm_if_available` | Tier 2 (vul + fix images) | `ConfirmVerdict`: `available`, `both_crash`, `post_patch_crash`, `target_match` — or `available=False` when fix image is absent |

### 3. `specialist` (`mcp/specialist_server.py`)

GPT-5.5 hard-failure advisor. Five tools, one per failure kind:

| Tool | When invoked |
|------|--------------|
| `specialist.rethink_reachability` | after `no_crash` — redesign parser reachability |
| `specialist.relocalize_sink` | after `wrong_sink` — re-review localization |
| `specialist.escape_basin` | after `generic_crash` / `both_crash` — basin-escape strategy |
| `specialist.diversify_family` | propose alternative candidate families |
| `specialist.review_consolidation` | offline adversarial review of consolidation proposals |

The specialist receives only a redacted diagnosis + compact repair policy (same scope hygiene as the agent). It returns a strategy/plan; the main loop executes it. The specialist never writes memory or submits.

---

## D9 Filesystem Boundary (load-bearing)

OKF and causal-policy markdown live under `memory_store/` and are served **only**
through `memory.*` MCP tools. The agent's filesystem tools (Read/Grep/Glob) are
confined to the run workspace and `skills/`.

**If the agent could read `memory_store/okf/**` directly, every scope boundary
above would be bypassable.** The runner enforces this restriction when configuring
allowed tools / working directory in the Agent SDK session.

**The runner FAILS HARD** if a `memory_store` path appears under a run directory:

```python
leaked = list(run_dir.rglob("memory_store"))
if leaked:
    typer.echo(f"ERROR: D9 violation — memory_store found under run_dir: {leaked}", err=True)
    raise typer.Exit(1)
```

This is verified by tests in `tests/test_run_smoke.py` and `tests/test_memory_scope.py`.

---

## How to Run

### `solve` — run the agent on a single task

```bash
# Offline stub (no docker, model, or network):
PYTHONPATH=src python runner/run.py solve \
  --task-dir /path/to/cybergym/task_123 \
  --run-dir  /tmp/runs/task_123 \
  --fake

# Real mode (requires Docker + ANTHROPIC_API_KEY):
PYTHONPATH=src python runner/run.py solve \
  --task-dir /path/to/cybergym/task_123 \
  --run-dir  /tmp/runs/task_123 \
  --model    claude-opus-4-8
```

### `consolidate` — dry-run consolidation proposal

```bash
PYTHONPATH=src python runner/run.py consolidate \
  --result-file /tmp/runs/task_123/result.json \
  --split-file  data/okf_split.json \
  --out-dir     /tmp/proposals/
```

### `ab-eval` — A/B harness (memory on vs off)

```python
from mneme import ab_eval
import json

split = json.loads(open("data/okf_split.json").read())
tasks = split["train"][:10]

# Memory ON arm (dry-run — no solve performed):
report = ab_eval.run(tasks, split, memory_on=True, dry_run=True)
print(report.metrics)

# Memory OFF arm:
report_off = ab_eval.run(tasks, split, memory_on=False, dry_run=True)
```

`ab_eval.run` refuses any task not in `split["train"]` — refused ids appear in
`report.refused_eval`. In dry-run mode (default) no agent, docker, or network
calls are made; all metrics are zero-valued placeholders. Live mode
(`dry_run=False`) requires Docker + model credentials and is not part of the
offline test suite.

---

## Verify Signal Split

**Hard rule:** runtime diagnosis != confirmed match.

`verify.run` (vul image only) emits:
- `failure_class` in `{no_crash, bad_format, wrong_sink, generic_crash}`
- `target_likelihood` in `{low, medium, high}` — explicitly **not** a confirmed match
- `crash_type`, `sink_fn`, `sink_loc`, `parser_reached`, `output_excerpt`

`verify.confirm_if_available` (vul + fix images) is the **only** source of:
- `both_crash` (crashes fix image too — too generic)
- `post_patch_crash`
- confirmed `target_match`

When the fix image is missing or unbuildable, `confirm_if_available` returns
`{"available": false}` and `submit.sh` remains the only official confirmation path.

This split is asserted by tests in `tests/test_verify_core.py`.

---

## OKF Leak Audit

Before any commit that touches `memory_store/okf/` or the import pipeline, run:

```bash
PYTHONPATH=src python scripts/audit_leak.py
```

`audit_leak.py` scans every file in `memory_store/okf/` for patterns that indicate
task-id leakage, exact offsets, submit metadata, server URLs, and checksums —
the same forbidden fields that `task_card.redact_for_promotion` strips at
consolidation time. The script exits non-zero if any leaks are found.

---

## Live Integration Disclaimer

**The current offline test suite (39 tests) does NOT exercise:**
- Real Docker container launches
- The Claude Agent SDK against a live model
- Real `submit.sh` calls or official CyberGym scoring

Live Docker / submit / model integration is only claimed once a real command is
run and its output is captured as evidence. The offline suite asserts structural
correctness (scope isolation, signal split, redaction, refusal logic) but cannot
substitute for an end-to-end run with credentials and a live CyberGym instance.

To validate live integration:

1. Run `runner/run.py solve` against one train task with real Docker + `ANTHROPIC_API_KEY`.
2. Confirm exactly one `submit.sh` call appears in the run log.
3. Grep the agent transcript for OKF body text that exists only in
   `memory_store/okf/` — it must arrive **only** via `memory.*` tool results,
   never as a direct file read.
