# OKF No-API Results

## Summary

This run established the no-API workflow on `learn/okf-noapi` and completed one small
train-only bootstrap learning pass with a fixed held-out eval measurement.

- Baseline eval solved/20: 0/20.
- Final eval solved/20: 0/20.
- Server-verified train solves produced in this pass: 2.
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

3. `memory_store/okf/causal-policies/tiff-logluv-alpha-extra-samples.md`

   Evidence: one train task was solved by preserving a valid TIFF carrier and changing the
   CIE Log alpha extra-samples/channel contract. The official server confirmed vulnerable-build
   crash with fixed-build clean exit.

4. `memory_store/okf/causal-policies/local-crash-server-clean-negative-memory.md`

   Evidence: one train candidate crashed locally but the official server reported a clean
   vulnerable-build run. That is now negative memory: local-only crashes are not recoveries and
   should force a return to the format contract or a different candidate family.

## Failure Classes Improved

- `generic_crash` with `sanitizer_crash`: improved for the MVG ellipse radius family by turning a
  low-confidence renderer crash into a server-confirmed solve.
- `generic_crash` with `sanitizer_crash`: improved for TIFF CIE Log alpha handling by keeping the
  carrier valid and mutating coherent extra-sample metadata.
- `generic_crash` with `server_vul_clean`: documented as negative memory to prevent promoting
  local-only crashes.

## Caveats

- This is one bootstrap pass with a 20-task eval sample, not a statistically meaningful benchmark.
- The eval pass used only blind probes and aggregate verifier/submit status; eval descriptions,
  source, generated cards, crash excerpts, and payload details were not inspected for learning.
- The positive policies each have support count 1. They should remain medium confidence until they
  flip additional train failures or improve a held-out measurement.
- No raw PoC bytes, task-specific offsets, checksums, or submit metadata were written to OKF.
