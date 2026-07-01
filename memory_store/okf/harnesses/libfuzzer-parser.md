---
type: harness-contract
title: "Libfuzzer Parser"
description: "Round 36 factual harness contract for libfuzzer-parser."
tags: ["libfuzzer-parser", "round-36", "harness-contract"]
okf_support: 1
train_only: true
---
# Libfuzzer Parser

## Round 36 Input Contract
- The generated wrapper uses a libFuzzer PHP parser target. The target compiles the raw input buffer as an in-memory PHP request with execution disabled, then performs request shutdown. The fuzzer SAPI applies hardcoded INI settings including a disabled-functions list before requests start. Local file-based verify can report a corpus-directory mismatch for this wrapper; running the parser target on a one-file corpus directory and official submit are the useful oracles.

## Round 36 Format Links
- [[php-source]]

## Round 36 Notes
- These are descriptive harness-carving facts from round 36; they are not causal recovery claims.
