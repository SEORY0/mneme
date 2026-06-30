# mneme pipelines: LEARNING vs TEST RUNNER (do not conflate)

mneme has two completely separate solve paths. They look similar (both "solve CyberGym
tasks") but differ in who does the reasoning, whether real model APIs are called, and whether
memory is written. Keep them straight.

## 1. LEARNING pipeline (training) — Codex workers, NO API inside mneme

- **Entry:** `scripts/learning/run_pass.sh`, `run_round.sh` → headless `codex exec` workers
  driven by `docs/codex-worker-prompt.md` (+ a serial consolidator, `docs/codex-consolidator-prompt.md`).
- **Who reasons:** the **Codex** session itself. mneme provides ONLY model-free tools
  (`runner/run.py gen|verify|submit` = docker + the local CyberGym server). **mneme never calls
  an LLM API here** — that is the hard "NO LLM API inside mneme" constraint.
- **Writes memory:** YES. Workers emit abstract traces; the consolidator promotes verified
  outcomes into `memory_store/okf/**` and commits each round. This is what produced rounds 1–25.
- **Purpose:** accumulate okf memory (prequential, mode B). It *learns*.

## 2. TEST RUNNER (evaluation/production) — Opus main + GPT-5.5 specialist, REAL API

- **Entry:** `runner/run.py solve --task-id <id> --run-dir <rd> [--model M]`, batched by
  `scripts/test_runner_batch.sh LABEL TASKFILE`.
- **Who reasons:** the **mneme agent itself**, calling real model APIs:
  - `M=claude-opus-4-8` (default) → **MAIN agent = Claude Opus** via the Claude Agent SDK
    (`agent_driver.solve`), wired to **three stdio MCP servers**: `memory`, `verify`, and
    **`specialist`**. The **specialist = GPT-5.5** (`mcp/specialist_server.py` → `specialist_core`),
    a hard-failure advisor the main agent calls when stuck (rethink_reachability, relocalize_sink,
    escape_basin, diversify_family). Task ids/offsets/checksums are stripped before they reach the
    specialist; it never submits or writes memory. → real **Anthropic (Opus) + OpenAI (gpt-5.5)** spend.
  - `M=gpt-5.5` → a DIFFERENT, standalone OpenAI-only backend (`agent_openai.solve`), **no MCP
    servers, no specialist**. Not the main+specialist pipeline; use only for a GPT-only baseline.
- **Writes memory:** NO. Reads okf read-only, scores, writes `result.json` per task. `solved`
  is **server-authoritative** (official `vul_exit!=0 && fix_exit==0`). It *measures*; it never learns.
- **Purpose:** verify capability of the current memory+code on a fixed task list.

## One-line distinction

> LEARNING = Codex reasons, mneme stays API-free, memory is written.
> TEST RUNNER = mneme reasons via Opus(main)+GPT-5.5(specialist) real APIs, nothing is written.

Do not use `run_pass.sh`/`run_round.sh`/`codex-worker-prompt.md` to "test" — that exercises the
training worker, not the production agent. Use `scripts/test_runner_batch.sh` for evaluation.
