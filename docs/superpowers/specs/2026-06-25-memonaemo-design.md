# memonaemo — Design Spec (v1)

- **Status:** Draft for review
- **Date:** 2026-06-25
- **Target benchmark:** CyberGym Level 1 (PoC generation against real-world vuln tasks)
- **Goal:** Beat the #1 agent (Crystalline) not with a bigger harness or a bigger OKF, but with a
  **verification-gated, scope-isolated causal memory** layer on a thin single-agent loop.

## 1. One-line definition

memonaemo is a **single Claude agent** that solves CyberGym Level-1 tasks. Skills and OKF knowledge
are injected as **markdown**; **memory and verification are exposed as MCP tools**; Python is a thin
runner that only does *task preparation → agent launch → final submit → offline consolidation*. A
**GPT-5.5 hard-failure specialist** is available to the agent as MCP advisor tools.

The differentiator vs Crystalline is the memory substrate, not the loop:
**keyed markdown + MCP-enforced scoped memory + verifier-gated consolidation**.

## 2. Decisions locked during brainstorming

| # | Decision | Choice |
|---|----------|--------|
| D1 | Agent runtime | **Python Claude Agent SDK** + MCP servers. `claude -p` headless = smoke/fallback only. |
| D2 | Loop ownership | **Agent-owned loop**; `verify.*` and `memory.*` are MCP tools the agent calls itself. |
| D3 | Scope enforcement | **Tool name = scope boundary** (no `scope` argument). |
| D4 | Verify substrate | **2-tier**: `verify.run` (vul-image, runtime diagnosis) → `verify.confirm_if_available` (vul+fix when runnable, else high-confidence gate) → final `submit.sh` once. |
| D5 | Multi-model split | Claude Opus 4.6/4.8 = main loop; **GPT-5.5 = MCP advisor tools** for hard failures. |
| D6 | Memory store | **keyed markdown** (frontmatter `match_keys`), **no vectors/embeddings in v1**. |
| D7 | Stats | success-rate/frequency/recency in **`memory_stats.jsonl` sidecar**, not by rewriting markdown. |
| D8 | Consolidation | offline, **train-only, dry-run default**; GPT-5.5 adversarial review before any promotion. |
| D9 | Filesystem isolation | **OKF / causal memory are NOT directly file-readable by the agent**; reachable only through `memory.*` MCP tools. Otherwise MCP scoping is bypassable via Read/Grep. |
| D10 | Discriminator | **No in-loop discriminator in v1** — a single agent that authored the candidate cannot be a blind judge. Verification (`verify.*`) is the judge. A separate-session discriminator is deferred. |
| D11 | Redaction altitude | Strictness applies to **long-term memory promotion only**. Run-local solve context may use repo-discovered function names / lines / sinks. |
| D12 | Knowledge import | **Curated import, not verbatim copy.** Import `tools/`, `shared/`, `knowledge/okf/`; **rewrite `stages/` for single-agent** (originals assume a staged pipeline). |

## 3. What is copied vs newly written

**Curated import from `/home/nsd/SCHE-MA` (NOT verbatim copy — D12):**
- `skills/knowledge/okf/**` → `memonaemo/memory_store/okf/**` (index, vuln-classes, formats,
  strategies, causal-policies, log). Durable, abstract, task-agnostic knowledge. **Placed outside the
  agent's accessible workspace** (D9) — served only via `memory.*`.
- `skills/tools/**`, `skills/shared/**` → `memonaemo/skills/**` (directly agent-readable).
- `skills/stages/**` → **rewritten** as single-agent prompt guidance; the originals assume a
  staged recon/analyze/generate/discriminate pipeline that conflicts with the single-agent loop.
- `skills/agents/**` → re-evaluated per file; keep only those that make sense for one agent.
- `data/okf_split.json` (train/eval split) → `memonaemo/data/okf_split.json` for eval hygiene.

All imported OKF/skills are **re-audited for task-id / offset / submit-metadata leakage** before the
first commit.

**Newly written (thin Python + MCP + prompts):** see §4 layout. No operating procedure or policy
playbook is encoded in Python — those live in OKF markdown / skills.

## 4. Repository layout

```
memonaemo/
  runner/                 # the only substantial Python — kept thin
    run.py                #   CLI: solve / batch / consolidate (dry-run default)
    task_card.py          #   cybergym task dir -> compact, redacted task card
    cybergym_io.py        #   task generation, submit.sh parsing, docker verify shell-out
    agent_driver.py       #   launch Claude Agent SDK session (MCP servers + skills), collect result
    consolidate.py        #   offline verifier-gated causal-distill (train-only, dry-run)
  mcp/
    memory_server.py      #   memory.* tools (see §7)
    verify_server.py      #   verify.* tools (see §6)
    specialist_server.py  #   GPT-5.5 advisor tools (see §8)
  memory_store/           # NOT in the agent's accessible workspace (D9) — only memory_server reads it
    okf/                  #   curated import of SCHE-MA OKF (index, vuln-classes, formats, strategies, causal-policies)
    memory_stats.jsonl    #   success/frequency/recency sidecar (D7)
  skills/                 # curated import (tools/, shared/) — agent-readable
  prompts/
    system.md             #   memory-first system prompt; tool-scope protocol
    kickoff.md
  data/
    okf_split.json
  tests/
  docs/superpowers/specs/2026-06-25-memonaemo-design.md
```

## 5. Data flow (one task)

1. `task_card.py` builds a compact card from `description.txt` + deterministic harness facts + seed
   hints. It redacts **raw task id, submit metadata, server URLs, checksums** from the card. It does
   **not** strip repo-discovered function names / lines / sinks — those are legitimate run-local
   solve context (D11). Strict redaction is enforced at promotion time (§9), not here.
2. `agent_driver.py` launches a Claude Opus session with: `system.md` (tool-scope protocol), the
   compact card, **read access restricted to the run workspace + `skills/**` only**, and the three
   MCP servers. The agent has **no filesystem access to `memory_store/`** (D9); OKF and causal memory
   arrive exclusively through `memory.*` tool results.
3. Agent works `recon → generate`, writes a candidate PoC, calls `verify.run` (vul-image).
4. On failure, `verify.run` returns a **runtime diagnosis** (`failure_class` ∈ {`no_crash`,
   `bad_format`, `wrong_sink`, `generic_crash`} + `target_likelihood`, never a confirmed match). The
   agent calls `memory.get_repair_policy` for that `failure_class × verifier_signal` and, for hard
   classes, a `specialist.*` advisor tool (§8). It retries.
5. Before spending the single submit, the agent (or runner gate) calls `verify.confirm_if_available`.
   When both vul **and** fix images are runnable locally it establishes `both_crash` /
   `post_patch_crash` / strong `target_match`; when they are not, it returns `unavailable` and the
   runner falls back to a **high-confidence gate** (runtime `target_likelihood=high` + repair-policy
   checks) before submitting.
6. The runner performs **exactly one** `submit.sh` for the official score.
7. Offline only, `consolidate.py` promotes verified train outcomes into OKF proposals (dry-run),
   reviewed adversarially by GPT-5.5 before any human-approved merge.

## 6. Verification model (2-tier, signal-split)

`verify.run(candidate_path)` — runs the **vulnerable** oss-fuzz image, parses sanitizer output, returns:
- `failure_class`: `no_crash` | `bad_format` | `wrong_sink` | `generic_crash`
- `crash_type`, `sink_fn`, `sink_loc`, `parser_reached`
- `target_likelihood`: low/medium/high — **explicitly not a confirmed target match**
- `output_excerpt` (redacted)

`verify.confirm_if_available(candidate_path)` — when both **vul + fix** images are runnable locally,
runs both; only this (or final submit) may report `both_crash` (crashes fix too → too generic),
`post_patch_crash`, or a confirmed `target_match`. Used sparingly (cost), normally once before submit.
**Local vul+fix availability is not assumed** — when the fix image is missing/unbuildable it returns
`unavailable`, and `submit.sh` remains the only official confirmation path.

**Hard rule:** runtime diagnosis ≠ confirmed match. `both_crash` / `post_patch_crash` /
`target_match` are *official/post-run signals* and must never be fabricated from a vul-only run.

`verify.run` was renamed from the originally proposed `verify.target_match` precisely because vul-only
verification cannot confirm a match.

## 7. Memory model (the differentiator)

**Tiers, separated by lifetime and access:**
1. **Private episodic trace** — run-local `task_card.json`, `prompt.md`, `attempts.jsonl`,
   `result.json`, candidates. Never injected directly into prompts; never promoted directly.
2. **OKF durable memory** — markdown under `memory_store/okf/**` (MCP-served only, D9). Tool-skill
   markdown under `skills/**` is directly agent-readable.
3. **Causal-policy markdown** — keyed by `failure_class`, `verifier_signal`, `candidate_family`,
   `input_format`, `harness_convention`, `vuln_class`.
4. **Negative memory** — first-class: failed PoC families, generic-crash basins, bad carrier formats,
   overlarge-mutation traps.

**Retrieval score is NOT semantic similarity.** Ranking weights:
`past_success_rate · same_failure_class · same_format/harness · verifier_confidence ·
recency/frequency · scope_allowed`. v1 lookup is keyed (frontmatter `match_keys`); the stats
(`past_success_rate`, frequency, recency) come from `memory_stats.jsonl` (D7), not from mutating the
markdown on every read.

**Causal-policy frontmatter (extended):** existing fields plus
`allowed_scopes`, `forbidden_fields`, `evidence_level`, `train_only`.

### MCP tool surface (tool name = scope boundary, D3)

Generate-scoped (full causal/OKF access):
- `memory.search_okf_for_generate(query_keys)` → abstract OKF examples + procedural policy.
- `memory.get_repair_policy(failure_class, verifier_signal, …)` → **compact policy record only**, never
  the full OKF body. Returns policy + procedure + negative-memory bullets + evidence shape.

Discriminate-scoped (**defined but not used by the v1 main loop — D10**):
- `memory.get_discriminator_evidence(candidate_id)` → verifier summaries + candidate metadata **only**.
  Generator OKF, causal policy, and generate reasoning are **not reachable through this tool at all**.
  This tool exists for a future **separate-session** discriminator; the v1 single-agent loop does not
  call it, because an agent that authored the candidate cannot be a blind judge of it.

Shared / housekeeping:
- `memory.record_proposal(payload)` → returns a dry-run proposal path; **does not write OKF**.
- `memory.scope_check(memory_class, tool)` → reports visibility for audit.

Because each tool is a distinct scope boundary, a discriminator request can never escalate to generate
memory through a mis-set argument or prompt drift.

### Filesystem boundary (D9 — load-bearing)

OKF and causal-policy markdown live under `memory_store/` and are served **only** through `memory.*`
tools. The agent's filesystem tools (Read/Grep/Glob) are confined to the run workspace and `skills/`.
If the agent could read `memory_store/okf/**` directly, every scope boundary above would be
bypassable, so the runner must enforce this restriction when configuring allowed tools / working dir
in the Agent SDK session. This is verified by a test (§12).

## 8. Multi-model split (Opus loop + GPT-5.5 specialist)

- **Claude Opus 4.6/4.8 = main agent loop:** repo exploration, MCP tool use, long-running sessions,
  PoC authoring/editing, incorporating verify feedback.
- **GPT-5.5 = hard-failure specialist**, exposed as MCP advisor tools in `specialist_server.py`. The
  main loop invokes the matching tool when `verify.run` returns a hard `failure_class`:
  - `specialist.rethink_reachability` — after `no_crash`: redesign parser reachability.
  - `specialist.relocalize_sink` — after `wrong_sink`: re-review localization.
  - `specialist.escape_basin` — after `generic_crash` / `both_crash`: basin-escape strategy.
  - `specialist.diversify_family` — propose alternative candidate families.
  - `specialist.review_consolidation` — offline adversarial review of consolidation proposals.
- The specialist receives **redacted diagnosis + the relevant compact repair policy only** — same
  scope hygiene as the agent. It returns a strategy/plan; Claude executes it. The specialist never
  writes memory or submits.
- `specialist_server.py` wraps an OpenAI client (key in env). This is the only new external dependency.

## 9. Consolidation (verifier-gated)

Offline, **train-only, dry-run by default**. Promotes only verifier-confirmed effects, never
"plausible reasoning". Failures are promoted as **negative memory** with equal status.

**Forbidden in any promotion:** raw PoC bytes, task-id-keyed facts, submit metadata, server URLs,
agent ids, checksums, exact offsets. This strictness is the **promotion altitude** (D11): repo-found
function names / lines / sinks are fine in run-local solve context but must be abstracted before they
enter long-term memory. `consolidate.py` refuses eval-split tasks, unsolved/unverified runs, and
missing-PoC results. GPT-5.5 `review_consolidation` runs as an adversarial gate before any human merge.

## 10. The five bets vs Crystalline (made explicit)

1. **Verification-gated promotion** — only verifier-confirmed effects enter long-term memory.
2. **Failure-causal retarget policies** keyed by `failure_class × verifier_signal`.
3. **First-class negative memory** (Crystalline-style libraries under-weight this).
4. **Access-scoped retrieval enforced at the substrate** — tool-name boundaries + filesystem
   isolation (D9), so memory scope cannot be bypassed by Read/Grep. (A blind discriminator that
   exploits this is deferred to a separate session — D10; the same boundaries already protect the
   specialist and consolidation scopes in v1.)
5. **Success-rate-weighted keyed/graph retrieval**, not text similarity.

## 11. v1 YAGNI (intentionally excluded)

Embeddings/vector search; Zettelkasten auto-linking (manual `[[links]]` allowed); **in-loop
discriminator** (separate-session discriminator deferred — D10); automatic fuzzer fallback (gates
retained, no auto-loop); multi-host docker; verbatim copy of `stages/` (rewritten — D12).

## 12. Testing & evaluation

- **Fake backend/verifier smoke** + pytest covering: tool-scope denial (`get_discriminator_evidence`
  cannot reach generate memory), **filesystem-boundary isolation** (agent session cannot Read/Grep
  `memory_store/okf/**` — D9), task-card redaction altitude (run-local sinks allowed, promotion strict
  — D11), keyed retrieval ranking, consolidation refusal rules, the runtime-vs-official signal split
  (`both_crash` never produced by `verify.run`), and the `verify.confirm_if_available` → `unavailable`
  fallback path.
- **A/B**: OKF memory on/off, train-only subset; metrics: target-match rate, median attempts,
  negative-memory hit rate, submit count (must be ≤1/task), cost/tokens.
- Live docker/submit integration is only *claimed* when a real command is run and captured as
  evidence — not asserted from code presence.

## 13. Open risks

- GPT-5.5 cross-provider latency/cost inside an Opus loop; mitigated by invoking specialist only on
  hard `failure_class`, not every attempt.
- `verify.confirm_if_available` doubles docker cost; mitigated by single pre-submit use, and it is
  not always runnable (fix image may be absent) — submit remains the fallback official signal.
- Copied OKF must be re-audited for any task-id/offset leakage before first commit.
