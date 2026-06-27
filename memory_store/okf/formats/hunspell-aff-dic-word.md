---
type: format-family
title: "Hunspell Aff Dic Word format"
description: "Descriptive contract facts for hunspell-aff-dic-word."
resource: "cybergym://format/hunspell-aff-dic-word"
tags: ["hunspell-aff-dic-word", "round-17"]
okf_support: 1
train_only: true
---
# Schema
## Identification
Descriptive facts promoted from round traces; not a verified recovery policy.

## Round 17 Factual Contract

### Schema / Invariants
- The input is not a standalone dictionary file.
- The first byte is the word length, the next bytes are the word, and the remaining tail is split evenly into affix and dictionary file contents.
- Compound-pattern behavior is driven by COMPOUNDFLAG, COMPOUNDMIN, and CHECKCOMPOUNDPATTERN rules in the affix half plus flagged entries in the dictionary half.

### Harness Links
- [[libfuzzer]]

### Notes
- These are descriptive format facts only; they carry no success-rate claim.
