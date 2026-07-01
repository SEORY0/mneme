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

## Round 28 Factual Contract

### Schema / Invariants
- VCF text input starts with metadata lines and a tab-separated column header, followed by tab-separated records. ALT alleles are comma-separated in text, but the parser stores alleles in an internal BCF shared block while the record allele count is narrower than the shared payload. On writeback, the internal BCF representation is unpacked and INFO keys are resolved through the header dictionary.

### Harness Links
- [[libfuzzer]]

### Notes
- These are descriptive format facts only; they carry no success-rate claim.

## Round 35 Factual Contract

### Schema / Invariants
- Text VCF parsing requires metadata lines, a tab-separated #CHROM header with sample names, and records with fixed columns followed by a colon-separated FORMAT column and one sample column per declared sample. FORMAT field sizes are inferred from declared header type and observed sample values; string FORMAT fields use the maximum observed text length, and omitted trailing fields in later samples are still represented in the per-sample FORMAT storage.

### Harness Links
- [[libfuzzer]]

### Notes
- These facts are descriptive observations from round 35; they carry no success-rate claim.
