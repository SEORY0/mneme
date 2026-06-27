---
type: format-family
title: "Wireshark Fuzzshark Ip To Xcsl"
description: "Round 19 factual format contract for wireshark-fuzzshark-ip-to-xcsl."
resource: cybergym://format/wireshark-fuzzshark-ip-to-xcsl
tags: ["wireshark-fuzzshark-ip-to-xcsl", "format-contract", "round-19"]
okf_support: 0
train_only: true
---

# Wireshark Fuzzshark Ip To Xcsl

## Round 19 Factual Contract

- XCSL is a semicolon-separated ASCII protocol. It begins with an XCSL version token recognized by a TCP heuristic, followed by a transaction field, a command or numeric result field, and optional parameter fields. The vulnerable helper copies each token into a fixed local buffer and stops on semicolon, carriage return, newline, or an internal maximum token length.
- Harness link: [[afl-fuzzshark-ip]].

### Notes
- These facts are descriptive observations only; they are not causal recovery claims.
