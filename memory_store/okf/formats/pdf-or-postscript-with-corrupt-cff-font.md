---
type: format-family
title: "pdf-or-postscript-with-corrupt-cff-font format"
description: "Descriptive format contract facts for pdf-or-postscript-with-corrupt-cff-font."
tags: ["pdf-or-postscript-with-corrupt-cff-font", "round-18"]
okf_support: 1
train_only: true
---
# PDF Or Postscript With Corrupt CFF Font Format

## Round 18 Factual Contract

### Schema / Invariants
- The target is an embedded CFF/Type 1C font buffer. The failing conversion path expands certain compact numeric encodings into a longer textual representation and must reserve space for the expanded form plus string termination. A minimal page without a malformed embedded font will not reach this parser.

### Harness Links
- [[libfuzzer-ghostscript-ps2write-device]]

### Notes
- These are descriptive format and harness observations only; they carry no success-rate claim.
