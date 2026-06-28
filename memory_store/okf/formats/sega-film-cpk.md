---
type: format-family
title: "Sega Film Cpk format"
description: "Structure and invariants for the sega-film-cpk input format."
tags: ["sega-film-cpk", "round-20"]
okf_support: 1
---
# Schema
## Identification
Factual format observations distilled from verifier traces. These are descriptive facts only and carry no success-rate claim.

## Round 20 Factual Contract

### Schema / Invariants
- Sega FILM/CPK files use a top-level movie header with descriptive and sample-table chunks. The sample table records media samples with timing, size, and flags; audio and video records are distinguished by marker and timestamp conventions, and video records carry keyframe state while audio records may not.

### Harness Links
- [[libfuzzer]]

### Notes
- These facts are descriptive format observations only; they are not causal recovery claims.
