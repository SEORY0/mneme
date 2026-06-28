---
type: format-family
title: "Hunspell Word Or Affdic Carrier"
description: "Round 19 factual format contract for hunspell-word-or-affdic-carrier."
resource: cybergym://format/hunspell-word-or-affdic-carrier
tags: ["hunspell-word-or-affdic-carrier", "format-contract", "round-19"]
okf_support: 0
train_only: true
---

# Hunspell Word Or Affdic Carrier

## Round 19 Factual Contract

- The visible Hunspell sources include a word-only fuzzer that loads dictionaries placed beside the executable and an affix/dictionary splitter fuzzer where a front length selects the query word and the remaining bytes are split evenly into affix and dictionary files. Affix files can declare UTF-8 and suggestion-related tables; dictionaries need a count line and entries.
- Harness link: [[libfuzzer]].

### Notes
- These facts are descriptive observations only; they are not causal recovery claims.
