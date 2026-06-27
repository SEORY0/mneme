---
type: harness-contract
title: "libfuzzer-ghostscript harness"
description: "Descriptive harness contract facts for libfuzzer-ghostscript."
tags: ["libfuzzer-ghostscript", "round-18"]
okf_support: 1
train_only: true
---
# Libfuzzer Ghostscript Harness

## Round 18 Input Contract

### Schema / Invariants
- The Ghostscript fuzzer takes raw PDF bytes from the input file. The extracted raster fuzzer has a quick PDF-header gate before invoking Ghostscript, while the verifier output showed a pdfwrite-oriented target; in both cases there is no mode selector or FuzzedDataProvider carving.

### Format Links
- [[pdf]]

### Notes
- These are descriptive format and harness observations only; they carry no success-rate claim.
