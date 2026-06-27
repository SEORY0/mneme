---
type: format-family
title: ecoff-or-bfd-object format
description: Structure and reachability facts for ecoff-or-bfd-object inputs.
tags: [ecoff-or-bfd-object]
okf_support: 0
---
# Ecoff Or BFD Object Format

## Round 10 Factual Contract

### Schema / Invariants
- The target relation involves ECOFF file-descriptor records, symbol records, and string-table bases used by BFD while nm filters symbols. A reachable input must be recognized as an ECOFF object and provide internally consistent enough optional/debug headers for BFD to allocate and walk those tables.

### Harness Links
- [[file-fuzzer]]

### Notes
- These are descriptive format facts only; they carry no success-rate claim.
