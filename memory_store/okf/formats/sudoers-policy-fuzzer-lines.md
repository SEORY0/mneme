---
type: format-family
title: "Sudoers Policy Fuzzer Lines"
description: "Abstract format facts observed during verifier-causal consolidation."
tags: ["sudoers-policy-fuzzer-lines", "format_contract"]
okf_support: 0
---
# Sudoers Policy Fuzzer Lines

## Notes
- These are descriptive format facts only; they carry no success-rate claim.

## Round 38 Factual Contract

### Schema / Invariants
- The fuzzer input is newline-delimited key/value text. Lines with known plugin-argument prefixes go to plugin args, known user-information prefixes go to user_info, argv lines form the command vector, env lines form added environment, and other lines are policy settings. Blank lines and comment lines are ignored. The harness inserts a default command only when no argv lines are present.

### Harness Links
- [[libfuzzer]]

### Notes
- These are descriptive format and harness observations only; they carry no success-rate claim.
