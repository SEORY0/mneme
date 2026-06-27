---
type: format-family
title: "vcf-text format"
description: "Structure and invariants for the vcf-text input format."
tags: ["vcf-text", "round-14"]
okf_support: 1
---
# Schema
## Identification
Factual format observations distilled from verifier traces. These are descriptive facts only and carry no success-rate claim.

## Round 14 Factual Contract

### Schema / Invariants
- VCF text needs fileformat/header lines, contig metadata, a column header with sample names, and records whose FORMAT column names colon-separated per-sample fields. FORMAT field sizes are derived from declared type plus observed vector/string lengths across samples.

### Harness Links
- [[libfuzzer]]

### Notes
- These facts are descriptive format observations only; they are not causal recovery claims.
