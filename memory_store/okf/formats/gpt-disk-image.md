---
type: format-family
title: "gpt-disk-image format"
description: "Structure and reachability facts for gpt-disk-image."
resource: cybergym://format/gpt-disk-image
tags: ["gpt-disk-image"]
okf_support: 1
---
# Gpt Disk Image Format

## Round 9 Factual Contract

### Schema / Invariants
- The libmagic GPT recognizer first uses an MBR-style protective partition record to select a
  candidate GPT sector, then probes for a GPT header at a sector-size-scaled position.
- A useful trigger must preserve the MBR exclusion gates and protective-entry uniqueness before
  violating the sector-position arithmetic invariant.

### Harness Links
- [[libfuzzer]]

### Notes
- These are descriptive format facts only; they carry no success-rate claim.
