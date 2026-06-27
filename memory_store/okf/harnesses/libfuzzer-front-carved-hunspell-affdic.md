---
type: harness-contract
title: "libfuzzer-front-carved-hunspell-affdic harness"
description: "Descriptive harness contract facts for libfuzzer-front-carved-hunspell-affdic."
tags: ["libfuzzer-front-carved-hunspell-affdic", "round-18"]
okf_support: 1
train_only: true
---
# Libfuzzer Front Carved Hunspell Affdic Harness

## Round 18 Input Contract

### Schema / Invariants
- The first input byte is the query-word length, followed by that many word bytes. The remaining bytes are split exactly in half: the first half is written as the affix file and the second half as the dictionary file. The harness constructs Hunspell, checks the word, and calls suggestions if spelling fails.

### Format Links
- [[hunspell-aff-dic-word]]

### Notes
- These are descriptive format and harness observations only; they carry no success-rate claim.
