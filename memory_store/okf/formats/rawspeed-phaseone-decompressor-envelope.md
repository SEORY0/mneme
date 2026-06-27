---
type: format-family
title: "rawspeed-phaseone-decompressor-envelope format"
description: "Descriptive format contract facts for rawspeed-phaseone-decompressor-envelope."
tags: ["rawspeed-phaseone-decompressor-envelope", "round-18"]
okf_support: 1
train_only: true
---
# Rawspeed Phaseone Decompressor Envelope Format

## Round 18 Factual Contract

### Schema / Invariants
- The fuzzer input is a RawSpeed decompressor envelope, not a camera raw file. It describes image dimensions, pixel type, component count, CFA flag, then a strip list where each strip has a row selector, a length, and strip payload bytes. PhaseOne construction requires a single 16-bit component image with even positive width and sane dimensions before strips are prepared.

### Harness Links
- [[libfuzzer]]

### Notes
- These are descriptive format and harness observations only; they carry no success-rate claim.
