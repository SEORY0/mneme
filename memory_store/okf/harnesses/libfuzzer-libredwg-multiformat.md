---
type: harness-contract
title: "Libfuzzer Libredwg Multiformat harness"
description: "Round 23 input contract facts for libfuzzer-libredwg-multiformat."
tags: ["libfuzzer-libredwg-multiformat", "round-23"]
okf_support: 1
train_only: true
---
# Libfuzzer Libredwg Multiformat Harness

## Round 23 Input Contract
- The harness consumes raw bytes directly. It selects the parser by the first bytes and then may emit one of several output formats; merely placing a malformed Unicode escape in a syntactically shallow input is not sufficient to prove the parsed field reaches the text conversion sink.

## Round 23 Format Links
- [[libredwg-json-dxf]]

## Round 23 Notes
- These are descriptive harness-carving facts only; they carry no success-rate claim.
