---
type: format-family
title: "Hunspell Aff Dic Word format"
description: "Descriptive contract facts for hunspell-aff-dic-word."
resource: "cybergym://format/hunspell-aff-dic-word"
tags: ["hunspell-aff-dic-word", "round-17"]
okf_support: 2
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

## Round 18 Factual Contract

### Schema / Invariants
- The first logical file is an `.aff` file with directives such as character set, flag mode, compound/affix options, and affix rules. The second is a `.dic` file beginning with a word count followed by word entries with optional slash-separated flag vectors. In numeric flag mode, flag vectors are comma-separated decimal numbers.

### Harness Links
- [[libfuzzer-front-carved-hunspell-affdic]]

### Notes
- These are descriptive format and harness observations only; they carry no success-rate claim.
