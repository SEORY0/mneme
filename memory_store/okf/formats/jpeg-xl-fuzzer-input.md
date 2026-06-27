---
type: format-family
title: "Jpeg Xl Fuzzer Input"
description: "Round 12 factual format contract for jpeg-xl-fuzzer-input."
resource: cybergym://format/jpeg-xl-fuzzer-input
tags: ["jpeg-xl-fuzzer-input", "format-contract", "round-12"]
okf_support: 0
train_only: true
---
# Jpeg Xl Fuzzer Input

## Round 12 Factual Contract

### Schema / Invariants
- The main JPEG XL fuzzer input is a JPEG XL codestream or container followed by a small option footer. The footer controls decoder modes such as streaming, callback output, orientation handling, pixel format, and generated target selection. The target bug involves modular squeeze transforms and metadata channel counts.

### Harness Links
- [[libfuzzer]]

### Notes
- These are descriptive format facts only; they carry no success-rate claim.
