---
type: harness-contract
title: "libfuzzer-ghostscript-ps2write-device harness"
description: "Descriptive harness contract facts for libfuzzer-ghostscript-ps2write-device."
tags: ["libfuzzer-ghostscript-ps2write-device", "round-18"]
okf_support: 1
train_only: true
---
# Libfuzzer Ghostscript Ps2write Device Harness

## Round 18 Input Contract

### Schema / Invariants
- The observed fuzzer target feeds raw document bytes into a Ghostscript writer device. There is no separate fuzzer envelope; the bytes must form a document that loads an embedded CFF font and asks the writer to process it.

### Format Links
- [[pdf-or-postscript-with-corrupt-cff-font]]

### Notes
- These are descriptive format and harness observations only; they carry no success-rate claim.

## Round 29 Input Contract

- The wrapper runs the libFuzzer Ghostscript ps2write device target on the raw file contents as standard input. There is no mode byte, checksum, archive wrapper, or FuzzedDataProvider layout. The fuzzer invokes Ghostscript with ps2write output, quiet/batch/no-pause options, stdout redirected to stderr, and the document read from stdin.

## Round 29 Format Links
- [[ghostscript-document-with-embedded-truetype]]

## Notes
- These are descriptive harness-carving facts only; they are not causal recovery claims.
