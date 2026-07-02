---
type: harness-contract
title: "Honggfuzz Style File Fuzzer Harness"
description: "Round 7 input contract facts for honggfuzz-style-file-fuzzer."
tags: ["honggfuzz-style-file-fuzzer", "harness-contract", "round-7"]
okf_support: 1
train_only: true
---
# Honggfuzz Style File Fuzzer Harness

## Round 7 Input Contract
- The harness rejects short inputs. It reads selector and option bytes from the front of the file,
optionally consumes fixed-size null-terminated time fields and decoder parameters, and then calls
the parser on the remaining bytes.

## Round {ROUND} Format Links
- [[fluent-bit-parser-fuzzer-control-plus-record]]

## Round {ROUND} Notes
- These are descriptive harness-carving facts only; they are not causal recovery claims.

## Round 38 Factual Contract

### Input Contract
- The harness rejects short files, then consumes fields front-to-back. Its fixed-width string helper includes the current selector byte as the first byte of the string before advancing. After parser options, the remaining bytes are passed to flb_parser_do. There is no FuzzedDataProvider back-consumption and no leading mode byte beyond the explicit parser selector.

### Format Links
- [[fluent-bit-parser-fuzzer-control-plus-record]]

### Notes
- These are descriptive format and harness observations only; they carry no success-rate claim.
