---
type: format-family
title: "Heif"
description: "Round 12 factual format contract for heif."
resource: cybergym://format/heif
tags: ["heif", "format-contract", "round-12"]
okf_support: 0
train_only: true
---
# Heif

## Round 12 Factual Contract

### Schema / Invariants
- The target format is an ISO BMFF HEIF file. Region annotations are stored as region items and assigned to images through item references. Referenced mask regions require region data plus a mask item reference, and the vulnerable relation is whether that referenced item is a valid image.

### Harness Links
- [[libfuzzer]]

### Notes
- These are descriptive format facts only; they carry no success-rate claim.

## Round 22 Factual Contract

### Schema / Invariants
- HEIF inputs are ISO-BMFF-style box files. The bundled corpus contains ordinary HEIC files with color and alpha variants; those are useful for reaching the file parser but do not directly provide the raw plane layout expected by the separate color-conversion fuzzer.

### Harness Links
- [[libfuzzer]]

### Notes
- These are descriptive format facts only; they carry no success-rate claim.
