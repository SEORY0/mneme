---
type: format-family
title: "PE Dotnet format"
description: "Descriptive contract facts for pe-dotnet."
resource: "cybergym://format/pe-dotnet"
tags: ["pe-dotnet", "round-16"]
okf_support: 1
---
# Schema
## Identification
Descriptive facts promoted from round traces; not a verified recovery policy.

## Round 16 Factual Contract

### Schema / Invariants
- A .NET sample must be a valid PE container with DOS and PE headers, section mapping, a CLR data-directory entry, metadata root streams, and tables/blobs that are mutually consistent enough for the YARA dotnet module to walk custom attributes. The vulnerable field is inside metadata blob decoding, not in the outer PE header.

### Harness Links
- [[libfuzzer]]

### Notes
- These are factual format and harness observations only; they carry no success-rate claim.
