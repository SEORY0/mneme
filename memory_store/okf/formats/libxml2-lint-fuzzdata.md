---
type: format-family
title: "libxml2-lint-fuzzdata format"
description: "Structure and invariants for the libxml2-lint-fuzzdata input format."
tags: ["libxml2-lint-fuzzdata", "round-14"]
okf_support: 1
---
# Schema
## Identification
Factual format observations distilled from verifier traces. These are descriptive facts only and carry no success-rate claim.

## Round 14 Factual Contract

### Schema / Invariants
- The lint target does not consume argv text directly. It serializes switch bitmasks, parser mode bits, numeric options, escaped strings for encode/pattern/xpath, then URL/content entity pairs. Strings terminate with a backslash-newline sentinel.

### Harness Links
- [[libfuzzer]]

### Notes
- These facts are descriptive format observations only; they are not causal recovery claims.
