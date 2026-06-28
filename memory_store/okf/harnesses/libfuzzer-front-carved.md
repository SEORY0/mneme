---
type: harness-contract
title: "Libfuzzer Front Carved harness"
description: "Input contract facts for Libfuzzer Front Carved."
tags: ["libfuzzer-front-carved", "round-21"]
okf_support: 1
---
# Libfuzzer Front Carved Harness

## Round 21 Input Contract (hunspell-aff-dic-word-triple)

- The first byte is a word length. That many following bytes become the query word. The remaining bytes are split evenly into affix and dictionary files; Hunspell is constructed, spell is called, and suggest is called when spell fails.

## Round 21 Format Links (hunspell-aff-dic-word-triple)
- [[hunspell-aff-dic-word-triple]]

## Round 21 Notes (hunspell-aff-dic-word-triple)
- These are descriptive harness-carving facts only; they are not causal recovery claims.
