---
type: harness-contract
title: "Libfuzzer Fuzzshark Epan harness"
description: "Input contract facts for libfuzzer-fuzzshark-epan."
tags: ["libfuzzer-fuzzshark-epan", "round-11"]
okf_support: 1
train_only: true
---
# Libfuzzer Fuzzshark Epan Harness

## Round 11 Input Contract
- The libFuzzer harness feeds the raw file bytes directly to the configured fuzzshark target. The target setup disables several unrelated dissectors and selects the UDP dissector by environment/configuration; there is no mode byte, archive envelope, or FuzzedDataProvider carving in the PoC itself.

## Format Links
- [[wireshark-fuzzshark-udp-payload]]

## Notes
- These are descriptive harness-carving facts only; they are not causal recovery claims.
