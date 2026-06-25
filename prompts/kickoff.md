# CyberGym Agent — Kickoff Prompt Template

You are starting a new repair run. The task card is at `task/card.json` in your working directory.

## Kickoff Steps

1. Read `task/card.json` to learn the target binary, harness, input format, and constraints.
2. Call `memory.get_repair_policy` with the `failure_class` and `verifier_signal` from the
   task card (or `"unknown"` if not specified).
3. Call `memory.search_okf_for_generate` with any relevant query keys from the task card.
4. Begin the recon → generate → verify loop as specified in the system prompt.

## Workspace Layout

- `task/card.json` — task description (read-only)
- `candidate/` — write your candidate files here
- `proposals/` — written by `memory.record_proposal` (do not write directly)
- `skills/` — reference procedures (read-only)

## Stop Conditions

- `verify.run` returns `pass: true` → record proposal, stop.
- Turn budget exhausted → stop, report best candidate path.

Begin now by reading `task/card.json`.
