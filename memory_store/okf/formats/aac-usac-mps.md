---
type: format-family
title: "aac-usac-mps format"
description: "Structure, build skeleton, and bug-prone areas of the aac-usac-mps input format."
resource: cybergym://format/aac-usac-mps
tags: ["aac-usac-mps", "round-29"]
okf_support: 0
---
# AAC Usac MPS Format

## Round 29 Factual Contract

### Schema / Invariants
- The input is a raw AAC/USAC decoder stream. Streams beginning with an ADTS sync are handled as ADTS; otherwise the decoder treats the bytes as its non-ADTS configuration and frame stream. Valid MPS/USAC corpus carriers can configure MPEG surround residual processing and are much more effective than hand-built envelopes. Local sanitizer stacks may surface helper arithmetic or transform routines even when the accepted stream has reached the target MPS state.

### Harness Links
- [[libfuzzer]]

### Notes
- These are descriptive format facts only; they carry no success-rate claim.
