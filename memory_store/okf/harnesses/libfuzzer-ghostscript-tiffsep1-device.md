---
type: harness-contract
title: "Libfuzzer Ghostscript Tiffsep1 Device harness"
description: "Input contract facts for libfuzzer-ghostscript-tiffsep1-device."
tags: ["libfuzzer-ghostscript-tiffsep1-device", "round-20"]
okf_support: 1
---
# Libfuzzer Ghostscript Tiffsep1 Device Harness

## Round 20 Input Contract
- The target fuzzer calls a Ghostscript device helper with the tiffsep1 device. A related gstoraster PostScript fuzzer uses the first byte as a color-scheme selector and passes the remaining bytes as interpreter input; the device-specific target effectively uses raw interpreter input to drive output-device lifecycle.

## Round 20 Format Links
- [[postscript-to-tiffsep-device]]

## Round 20 Notes
- These are descriptive harness-carving facts only; they are not causal recovery claims.
