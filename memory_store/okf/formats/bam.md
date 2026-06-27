---
type: format-family
title: "Bam format"
description: "Descriptive contract facts for bam."
resource: "cybergym://format/bam"
tags: ["bam", "round-17"]
okf_support: 1
train_only: true
---
# Schema
## Identification
Descriptive facts promoted from round traces; not a verified recovery policy.

## Round 17 Factual Contract

### Schema / Invariants
- BAM stores a compressed header followed by records with a fixed-size core and variable data.
- The low byte of the packed bin/mapq/name field is the raw read-name length.
- If that length is not aligned, the reader adds extra NUL bytes internally; a multiple-of-four unterminated name avoids that implicit padding.
- CIGAR, sequence, quality, and auxiliary data follow the name in the same record allocation.

### Harness Links
- [[libfuzzer]]

### Notes
- These are descriptive format facts only; they carry no success-rate claim.
