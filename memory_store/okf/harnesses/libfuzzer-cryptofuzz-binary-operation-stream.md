---
type: harness-contract
title: "Libfuzzer Cryptofuzz Binary Operation Stream harness"
description: "Input contract facts for libfuzzer-cryptofuzz-binary-operation-stream."
tags: ["libfuzzer-cryptofuzz-binary-operation-stream", "round-31"]
okf_support: 1
train_only: true
---
# Libfuzzer Cryptofuzz Binary Operation Stream Harness

## Round 31 Input Contract

### Input Contract
- The harness passes the raw file bytes to a libFuzzer-style Cryptofuzz entrypoint; there is no file magic and no back-consumed FuzzedDataProvider layout. Datasource records are consumed front-to-back as little-endian length-prefixed fields. The executable prints honggfuzz usage text in single-input mode, but the relevant parser contract is the Cryptofuzz binary datasource feeding the forced wolfCrypt module.

### Format Links
- [[cryptofuzz-binary-operation-stream]]

### Notes
- These are descriptive harness-carving facts only; they carry no success-rate claim.
## Round 37 Input Contract

### Input Contract
- The libFuzzer wrapper passes the raw file bytes directly to Cryptofuzz.
- The active binary is configured for wolfCrypt-focused operation families and permits BignumCalc.
- For BignumCalc, the parent datasource supplies the modifier stream and module selector, while the nested payload supplies the calculation and four operands.
- The wolfCrypt module consumes modifier booleans for decimal versus hexadecimal parsing, optional clamping, optional base-conversion round trips, and operand rewiring.

### Format Links
- [[cryptofuzz-binary-operation-stream]]

### Notes
- These are descriptive harness-carving facts only; they are not causal recovery claims.
