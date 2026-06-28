---
type: harness-contract
title: "Libfuzzer Samba Sddl Access Check harness"
description: "Input contract facts for libfuzzer-samba-sddl-access-check."
tags: ["libfuzzer-samba-sddl-access-check", "round-11"]
okf_support: 1
train_only: true
---
# Libfuzzer Samba Sddl Access Check Harness

## Round 11 Input Contract
- The harness scans backward over trailing NUL bytes, treats the buffer start as an SDDL C string, decodes it with a fixed domain SID, and then calls Samba access-check logic using a fixed token and an access mask read from the end of the input.

## Format Links
- [[sddl-string-with-access-mask]]

## Notes
- These are descriptive harness-carving facts only; they are not causal recovery claims.
