---
type: harness-contract
title: "Honggfuzz Fuzzshark harness"
description: "Round 23 input contract facts for honggfuzz-fuzzshark."
tags: ["honggfuzz-fuzzshark", "round-23"]
okf_support: 1
train_only: true
---
# Honggfuzz Fuzzshark Harness

## Round 23 Input Contract
- The generated fuzzshark binary reports a configured UDP dissector under the IP protocol table. It accepts raw single-input bytes through a honggfuzz-style wrapper, but the observed configuration disables several other dissectors and does not directly hand raw bytes to packet-gsm_rlp.

## Round 23 Format Links
- [[wireshark-fuzzshark-udp-payload]]

## Round 23 Notes
- These are descriptive harness-carving facts only; they carry no success-rate claim.
