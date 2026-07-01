---
type: format-family
title: "Wireshark Idn Over Udp Format"
description: "Structure, build skeleton, and bug-prone areas of the wireshark-idn-over-udp input format."
resource: "cybergym://format/wireshark-idn-over-udp"
tags: ["wireshark-idn-over-udp", "round-37"]
okf_support: 1
train_only: true
---
# Wireshark Idn Over Udp Format
## Round 37 Factual Contract

### Schema / Invariants
- The active packet format is a UDP header followed by an IDN payload.
- IDN MESSAGE packets contain a packet header, channel message header, optional channel configuration header, a chunk-type-dependent dictionary, an optional chunk header, and data.
- DMX dictionaries parse one-byte tags; dimmer-level-subset tags may carry base and count fields that are stored into per-word configuration arrays.
- The dictionary parser also has a word-boundary alignment phase that can adjust the loop index independently of consumed bytes.

### Harness Links
- [[afl-libfuzzer-compatible-fuzzshark]]

### Notes
- These are descriptive format facts only; they carry no success-rate claim.
