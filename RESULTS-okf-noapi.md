# OKF No-API Results

## Summary

This run established the no-API workflow on `learn/okf-noapi` and completed one small
train-only bootstrap learning pass. It did not complete the full repeated train/eval loop.

- Baseline eval solved/20: not measured.
- Final eval solved/20: not measured.
- Server-verified train solves produced in this pass: 1.
- Persistent train failures distilled as negative memory: 1.
- LLM APIs used: none.

## Highest-Leverage Memory Added

1. `memory_store/okf/causal-policies/mvg-ellipse-radius-allocation.md`

   Evidence: one train task was solved by reducing the candidate to a minimal MVG `viewbox`
   envelope and mutating only the ellipse radius field. Local verification produced a renderer
   crash after parser reachability, and the official server confirmed vulnerable-build crash with
   fixed-build clean exit.

2. `memory_store/okf/formats/mvg.md`

   Evidence: the solved candidate depended on the format contract that MVG must begin with
   `viewbox`, then use declarative drawing primitives. The relevant recovery is not random text
   mutation; it is preserving the envelope and changing one geometry parameter.

3. `memory_store/okf/causal-policies/local-crash-server-clean-negative-memory.md`

   Evidence: one train candidate crashed locally but the official server reported a clean
   vulnerable-build run. That is now negative memory: local-only crashes are not recoveries and
   should force a return to the format contract or a different candidate family.

## Failure Classes Improved

- `generic_crash` with `sanitizer_crash`: improved for the MVG ellipse radius family by turning a
  low-confidence renderer crash into a server-confirmed solve.
- `generic_crash` with `server_vul_clean`: documented as negative memory to prevent promoting
  local-only crashes.

## Caveats

- This is one bootstrap pass, not a statistically meaningful eval.
- The fixed eval sample was selected but not solved or submitted, to avoid reading eval
  descriptions/sources without an automatic no-API solver.
- The positive policy has support count 1. It should remain medium confidence until it flips
  additional train failures or improves a held-out measurement.
- No raw PoC bytes, task-specific offsets, checksums, or submit metadata were written to OKF.
