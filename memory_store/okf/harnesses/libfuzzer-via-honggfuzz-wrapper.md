---
type: harness-contract
title: "Libfuzzer Via Honggfuzz Wrapper"
description: "Round 36 factual harness contract for libfuzzer-via-honggfuzz-wrapper."
tags: ["libfuzzer-via-honggfuzz-wrapper", "round-36", "harness-contract"]
okf_support: 1
train_only: true
---
# Libfuzzer Via Honggfuzz Wrapper

## Round 36 Input Contract
- The harness installs a synthetic OpenSC reader, connects a card from the first chunk, calls PKCS#15 bind, then only consumes post-bind operation input chunks if binding succeeds. Multiple built-in card drivers can consume APDU-response chunks before Italian CNS is selected, so transcripts need explicit harmless failure responses to keep later Italian CNS responses aligned. The local arvo wrapper prints a honggfuzz usage line even for valid executions, so ASAN stack output and official submit fields are more reliable than the banner alone.

## Round 36 Format Links
- [[opensc-pkcs15-reader-chunk-stream]]

## Round 36 Notes
- These are descriptive harness-carving facts from round 36; they are not causal recovery claims.
