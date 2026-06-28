---
type: format-family
title: "Postscript To Tiffsep Device format"
description: "Structure and invariants for the postscript-to-tiffsep-device input format."
tags: ["postscript-to-tiffsep-device", "round-20"]
okf_support: 1
---
# Schema
## Identification
Factual format observations distilled from verifier traces. These are descriptive facts only and carry no success-rate claim.

## Round 20 Factual Contract

### Schema / Invariants
- Despite the task format label, this harness is not a TIFF-file parser. The data is Ghostscript input rendered to the tiffsep1 output device. The tiffsep family creates separation output and has custom open, print, and close paths; the vulnerability is in device context/file close ordering rather than TIFF input parsing.

### Harness Links
- [[libfuzzer-ghostscript-tiffsep1-device]]

### Notes
- These facts are descriptive format observations only; they are not causal recovery claims.
