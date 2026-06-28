---
type: format-family
title: "ruby-script format"
description: "Structure and invariants for the ruby-script input format."
tags: ["ruby-script", "round-14"]
okf_support: 2
---
# Schema
## Identification
Factual format observations distilled from verifier traces. These are descriptive facts only and carry no success-rate claim.

## Round 14 Factual Contract

### Schema / Invariants
- The input is Ruby source. The pack/unpack template language has single-letter directives, optional decimal counts, star counts, endian/size suffixes, and movement directives. String, hex, base64, quoted-printable, numeric, and cursor movement directives use different count semantics.
- The input is Ruby source. Large numeric strings can overflow fixnum parsing and enter the BigInt constructor; base prefixes and explicit base arguments influence the digit scanner before BigInt creation.

### Harness Links
- [[libfuzzer]]

### Notes
- These facts are descriptive format observations only; they are not causal recovery claims.
