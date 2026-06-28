---
type: harness-contract
title: "Libfuzzer Libjpeg Turbo Transform harness"
description: "Round 23 input contract facts for libfuzzer-libjpeg-turbo-transform."
tags: ["libfuzzer-libjpeg-turbo-transform", "round-23"]
okf_support: 1
train_only: true
---
# Libfuzzer Libjpeg Turbo Transform Harness

## Round 23 Input Contract
- The source fuzzer consumes a single JPEG byte stream, but the local `/bin/arvo` wrapper for this task rejected ordinary file inputs with a directory requirement before reaching the libFuzzer callback. Passing an actual directory path through the runner still produced the same wrapper error.

## Round 23 Format Links
- [[jpeg]]

## Round 23 Notes
- These are descriptive harness-carving facts only; they carry no success-rate claim.
