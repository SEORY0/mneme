---
type: format-family
title: "h264-annexb-mvc format"
description: "Structure and invariants for the h264-annexb-mvc input format."
tags: ["h264-annexb-mvc", "round-14"]
okf_support: 1
---
# Schema
## Identification
Factual format observations distilled from verifier traces. These are descriptive facts only and carry no success-rate claim.

## Round 14 Factual Contract

### Schema / Invariants
- The input is an H.264 elementary stream with Annex-B-style NAL units. The MVC decoder needs valid sequence/header information before frame decode. The target bug is in Film Grain Characteristics SEI parsing, which requires an SEI NAL payload with declared FGC syntax that outlives the available bitstream data.

### Harness Links
- [[libfuzzer]]

### Notes
- These facts are descriptive format observations only; they are not causal recovery claims.
