---
type: format-family
title: "Ogg Opus format"
description: "Structure and invariants for the ogg-opus input format."
tags: ["ogg-opus", "round-20"]
okf_support: 1
---
# Schema
## Identification
Factual format observations distilled from verifier traces. These are descriptive facts only and carry no success-rate claim.

## Round 20 Factual Contract

### Schema / Invariants
- Ogg streams are made of pages with a capture header, version, page type flags, granule position, stream serial, sequence number, checksum, segment count, lacing values, and page body. Opus-in-Ogg begins with an Opus identification packet and usually a tags packet before audio packets.

### Harness Links
- [[libfuzzer]]

### Notes
- These facts are descriptive format observations only; they are not causal recovery claims.
