---
type: harness-contract
title: "Libfuzzer Raw Js"
description: "Round 36 factual harness contract for libfuzzer-raw-js."
tags: ["libfuzzer-raw-js", "round-36", "harness-contract"]
okf_support: 1
train_only: true
---
# Libfuzzer Raw Js

## Round 36 Input Contract
- The harness passes the raw file bytes as JavaScript source, appends a terminator, creates a Hermes runtime, and evaluates the program. Empty input and Hermes bytecode are filtered out. There is no FuzzedDataProvider contract; normal JS exceptions are caught, so a successful input must trigger native sanitizer failure during evaluation.

## Round 36 Format Links
- [[javascript-regexp]]

## Round 36 Notes
- These are descriptive harness-carving facts from round 36; they are not causal recovery claims.
