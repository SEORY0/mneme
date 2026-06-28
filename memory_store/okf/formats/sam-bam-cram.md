---
type: format-family
title: sam-bam-cram format
description: Structure, build skeleton, and bug-prone areas of the sam-bam-cram input format.
resource: cybergym://format/sam-bam-cram
tags: ["sam-bam-cram", "round-21"]
timestamp: 2026-06-28T00:00:00Z
okf_support: 1
---
# Schema

## Round 21 Factual Contract (libfuzzer-raw-htslib-hts-open)

### Schema / Invariants
- The harness accepts sequence formats detected by HTSlib, including SAM text and BGZF-compressed BAM. SAM text coordinates are validated and converted during parsing. BAM records can carry internal alignment positions directly, but the CRAM reference-fetch path also depends on reference metadata and availability.

### Harness Links
- [[libfuzzer-raw-htslib-hts-open]]

### Notes
- These are descriptive format facts only; they carry no success-rate claim.
