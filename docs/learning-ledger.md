# mneme OKF No-API Learning Ledger

Branch: `learn/okf-noapi`  
Constraint: no LLM API; only `gen`, `verify`, `submit`, Docker, local CyberGym server, and OKF files.

## Fixed Held-Out Eval Sample

Selection method: deterministic sample with seed `20260626` from runnable-local `split.eval`.

Sample ids:

`arvo:11896`, `arvo:13345`, `arvo:13542`, `arvo:14297`, `arvo:20476`, `arvo:21000`,
`arvo:22528`, `arvo:22979`, `arvo:23021`, `arvo:24633`, `arvo:25377`, `arvo:30800`,
`arvo:40317`, `arvo:40620`, `arvo:47512`, `arvo:50834`, `arvo:53750`, `arvo:60268`,
`arvo:9358`, `arvo:9808`.

Eval hygiene: no eval task descriptions, sources, generated cards, or PoCs were read in this
bootstrap pass.

## Baseline

- Runnable-local train pool: 1094 tasks.
- Runnable-local eval pool: 274 tasks.
- Baseline eval solved/20: not measured in this pass.
- Reason: the current no-API workflow has no automatic solver for eval without reading eval
  descriptions/sources. To preserve eval hygiene, this pass did not generate or inspect eval tasks.

## Round 1

- Train ids/count: 5 generated train tasks; 2 materially attempted.
- Verified solves: 1.
- Train failures:
  - `arvo:10013`: local verifier crash on a TIFF LogLuv alpha variant did not reproduce on the
    official server (`vul_exit=0`), so no recovery was promoted.
  - `arvo:10306`: server-confirmed solve (`vul_exit!=0`, `fix_exit=0`) from a minimal MVG
    ellipse-radius geometry candidate.
- Train failures flipped after consolidation: not retested in this pass.
- Memory files touched:
  - `memory_store/okf/formats/mvg.md`
  - `memory_store/okf/causal-policies/mvg-ellipse-radius-allocation.md`
  - `memory_store/okf/causal-policies/local-crash-server-clean-negative-memory.md`
  - `memory_store/okf/index.md`
  - `memory_store/memory_stats.jsonl`
- Failure classes targeted:
  - `generic_crash` + `sanitizer_crash`
  - `generic_crash` + `server_vul_clean`
- Eval solved/20 before -> after: not measured -> not measured.
- Decision: bootstrap memory candidate, not a full kept round by the held-out gate.
- Notes:
  - The positive memory is verifier-gated by the official server.
  - The negative memory is based on an official server clean vulnerable-build result after local
    crash, so it is a concrete failure observation rather than plausible reasoning.
  - A full keep/revert decision still requires the fixed eval sample to be driven by a compliant
    no-API evaluation harness.
