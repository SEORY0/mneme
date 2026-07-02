---
type: format-family
title: "Dex Format"
description: "Input contract facts for dex."
tags: ["dex", "round-30"]
okf_support: 0
train_only: true
---
# Dex Format

## Round 30 Factual Contract

### Schema / Invariants
- A DEX file starts with an accepted dex magic and a little-endian header containing offsets and sizes for string IDs, type IDs, proto IDs, field IDs, method IDs, class definitions, and data. A class definition can point to class data, where ULEB128 counts are followed by encoded field and method records. Encoded method and field records store index deltas, so counts and deltas control which method_ids or field_ids entries are resolved and which string_ids name is later read.

### Harness Links
- [[libfuzzer-yara-dex-module]]

### Notes
- These facts are descriptive format observations only; they are not causal recovery claims.
