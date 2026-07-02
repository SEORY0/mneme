---
type: format-family
title: "php format"
description: "Structure, build skeleton, and bug-prone areas of the php input format."
resource: cybergym://format/php
tags: ["php", "round-29"]
okf_support: 0
---
# PHP Format

## Round 29 Factual Contract

### Schema / Invariants
- The input is not a container format: the libFuzzer buffer is compiled and executed as PHP source, with a size cap in the execution fuzzer. PHP opening tags are accepted, and normal try/catch syntax can keep ordinary arithmetic errors from aborting before sanitizer handling. Literal strings may be interned, while strings created at runtime are heap allocated.

### Harness Links
- [[libfuzzer]]

### Notes
- These are descriptive format facts only; they carry no success-rate claim.
