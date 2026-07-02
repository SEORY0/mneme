---
type: format-family
title: "Bam format"
description: "Descriptive contract facts for bam."
resource: "cybergym://format/bam"
tags: ["bam", "round-17"]
okf_support: 2
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

## Round 31 Factual Contract

### Schema / Invariants
- BAM inputs are BGZF/gzip-compressed streams whose decompressed payload begins with a BAM header, reference dictionary, and alignment records. Each alignment has a fixed core followed by variable qname, CIGAR, sequence, quality, and aux data. Aux tags use a two-character tag plus a type byte; B-array aux values carry a subtype and an element count before the array bytes. HTSlib may add internal qname padding and rounds record allocations, so a boundary-triggering malformed aux tail must account for the internal record allocation size, not just the logical file length.

### Harness Links
- [[libfuzzer-raw-htslib-hts-open]]

### Notes
- These are descriptive format facts only; they carry no success-rate claim.
