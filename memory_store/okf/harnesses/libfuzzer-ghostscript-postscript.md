---
type: harness-contract
title: "Libfuzzer Ghostscript Postscript harness"
description: "Input contract facts for libfuzzer-ghostscript-postscript."
tags: ["libfuzzer-ghostscript-postscript", "round-24"]
okf_support: 1
---
# Libfuzzer Ghostscript Postscript Harness

## Round 24 Factual Contract

### Input Contract
- The selected gstoraster PostScript fuzzer passes raw PostScript bytes to Ghostscript. There is no leading mode byte; interpreter-visible operators and setpagedevice dictionaries drive the state.

### Format Links
- [[postscript]]

### Notes
- These are descriptive facts only; they carry no success-rate claim.
