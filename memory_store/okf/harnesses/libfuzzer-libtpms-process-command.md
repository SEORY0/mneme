---
type: harness-contract
title: "Libfuzzer Libtpms Process Command harness"
description: "Input contract facts for libfuzzer libtpms process command."
tags: ["libfuzzer-libtpms-process-command", "round-17"]
okf_support: 1
train_only: true
---
# Libfuzzer Libtpms Process Command Harness

## Round 17 Input Contract
- The harness initializes a TPM2 instance, sends a startup command internally, then passes the raw fuzzer command buffer into TPMLIB_Process.
- There is no file envelope or length-prefix outside the TPM command itself.

## Round 17 Format Links
- [[tpm2-command-buffer]]

## Round 17 Notes
- These are descriptive harness-carving facts only; they carry no success-rate claim.

## Round 17 Format Links
- [[tpm2-command-buffer]]

## Round 17 Notes
- These are descriptive harness-carving facts only; they carry no success-rate claim.
