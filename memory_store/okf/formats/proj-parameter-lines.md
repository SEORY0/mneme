---
type: format-family
title: Proj Parameter Lines format
description: Format contract for proj parameter lines inputs.
resource: cybergym://format/proj-parameter-lines
tags: [proj-parameter-lines, axis-index-out-of-bounds, round-11]
okf_support: 1
train_only: true
---
# Schema
## Structure
The PROJ standard fuzzer input is source projection text, destination projection text, and a coordinate line. Coordinate lines may use binary 2D/3D markers or textual coordinates. The axisswap option accepts comma-separated axis selectors with signs; malformed empty selectors can pass the character gate and become invalid axis indices.

## Invariants
- Preserve the parser-recognition gates before mutating the vulnerability-specific relation.
- Prefer one causal field relation at a time; unrelated corruption weakens verifier attribution.

## Harness Links
- [[libfuzzer]]

## Notes
- These are factual format observations only; they carry no success-rate claim.

## Round 25 Factual Contract

### Schema / Invariants
- The standard PROJ fuzz input is three newline-separated fields: source projection definition, destination projection definition, and coordinates. Projection definitions are plus-prefixed parameter strings parsed by pj_init_plus.

### Harness Links
- [[libfuzzer]]

### Notes
- These facts are descriptive format observations only; they are not causal recovery claims.
