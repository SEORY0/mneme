---
type: format-family
title: "Sam Bam Cram Sequence Data format"
description: "Round 8 descriptive format facts for sam/bam/cram sequence data."
resource: cybergym://format/sam-bam-cram-sequence-data
tags: ["sam-bam-cram-sequence-data", "round-8"]
okf_support: 1
---
# Sam Bam Cram Sequence Data Format

## Round 8 Factual Contract

### Schema / Invariants
- Text SAM aux fields must include tag, type, and value syntax or they are rejected early. Binary BAM can carry read records with qname, cigar, sequence, qualities, and trailing aux bytes; aux iteration starts after those variable-length fields.

### Harness Links
- [[libfuzzer]]

### Notes
- These are descriptive format facts only; they carry no success-rate claim.

