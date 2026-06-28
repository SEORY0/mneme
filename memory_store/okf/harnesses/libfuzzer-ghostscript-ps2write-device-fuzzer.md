---
type: harness-contract
title: "Libfuzzer Ghostscript Ps2write Device Fuzzer harness"
description: "Input contract facts for libfuzzer Ghostscript ps2write device fuzzer."
tags: ["libfuzzer-ghostscript-ps2write-device-fuzzer", "round-16"]
okf_support: 1
---
# Libfuzzer Ghostscript Ps2write Device Fuzzer Harness

## Round 16 Input Contract
- The selected wrapper runs the ps2write device fuzzer. It feeds the raw file through Ghostscript stdin using fixed device arguments, discards normal output, and performs cleanup through gsapi_exit and instance deletion.

## Round 16 Format Links
- [[postscript-pdf]]

## Round 16 Notes
- These are descriptive harness-carving facts only; they are not causal recovery claims.
