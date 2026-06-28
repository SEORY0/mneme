---
type: harness-contract
title: "Libfuzzer Fuzzeddataprovider Like Splitter harness"
description: "Input contract facts for libfuzzer FuzzedDataProvider-like splitter."
tags: ["libfuzzer-fuzzeddataprovider-like-splitter", "round-11"]
okf_support: 1
train_only: true
---
# Libfuzzer Fuzzeddataprovider Like Splitter Harness

## Round 11 Input Contract
- The first byte selects the word length. The following bytes become the word, and the remaining bytes are split into affix and dictionary halves before the harness constructs Hunspell and calls spell/suggest on the word.

## Format Links
- [[hunspell-aff-dic-word-triple]]

## Notes
- These are descriptive harness-carving facts only; they are not causal recovery claims.
