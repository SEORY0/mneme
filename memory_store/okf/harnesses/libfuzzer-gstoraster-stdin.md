---
type: harness-contract
title: "libfuzzer-gstoraster-stdin harness"
description: "Descriptive harness contract facts for libfuzzer-gstoraster-stdin."
tags: ["libfuzzer-gstoraster-stdin", "round-18"]
okf_support: 1
train_only: true
---
# Libfuzzer Gstoraster Stdin Harness

## Round 18 Input Contract

### Schema / Invariants
- The gstoraster fuzzer passes the raw input to Ghostscript as stdin with raster-device arguments. The document must be accepted far enough for the embedded font to be interpreted; there is no selector byte or FuzzedDataProvider carving.

### Format Links
- [[postscript-type1-font-carrier]]

### Notes
- These are descriptive format and harness observations only; they carry no success-rate claim.
