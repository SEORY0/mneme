---
type: format-family
title: "Samba Ndr Spoolss Fuzzer Blob format"
description: "Structure and invariants for the samba-ndr-spoolss-fuzzer-blob input format."
tags: ["samba-ndr-spoolss-fuzzer-blob", "round-20"]
okf_support: 1
---
# Schema
## Identification
Factual format observations distilled from verifier traces. These are descriptive facts only and carry no success-rate claim.

## Round 20 Factual Contract

### Schema / Invariants
- Samba generated NDR fuzz targets use a small fuzzer control prefix followed by an NDR-encoded structure for a specific RPC interface/type. NDR strings carry referent/length metadata and may be ASCII or UTF-16 depending on the generated field. Length fields alone are not enough unless they appear inside the expected spoolss structure branch.

### Harness Links
- [[libfuzzer-fuzz-ndr-spoolss-type-struct]]

### Notes
- These facts are descriptive format observations only; they are not causal recovery claims.

## Round 34 Factual Contract

### Schema / Invariants
- The blob starts with little-endian flags/type and a public-struct selector, then TYPE_STRUCT passes the remaining bytes as a raw NDR stub. Fixed charset(UTF16),to_null arrays are parsed as zero-code-unit-terminated strings, not single-byte strings.

### Harness Links
- [[libfuzzer]]

### Notes
- These facts are descriptive observations only; they carry no success-rate claim.
