---
type: format-family
title: "Avif Bmff"
description: "Round 12 factual format contract for avif-bmff."
resource: cybergym://format/avif-bmff
tags: ["avif-bmff", "format-contract", "round-12"]
okf_support: 0
train_only: true
---
# Avif Bmff

## Round 12 Factual Contract

### Schema / Invariants
- AVIF uses BMFF boxes with a size, type, and payload. A minimal decoded seed carried a file-type box followed by metadata and media-data boxes. Metadata boxes contain nested item/property structures with their own uniqueness checks, while the described invariant concerns top-level uniqueness and error flow.

### Harness Links
- [[libfuzzer]]

### Notes
- These are descriptive format facts only; they carry no success-rate claim.
