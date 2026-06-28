---
type: format-family
title: wavpack format
description: Structure, build skeleton, and bug-prone areas of the wavpack input format.
resource: cybergym://format/wavpack
tags: [wavpack, "round-22"]
timestamp: 2026-06-28T06:03:30Z
okf_support: 1
---
# Schema

## Round 22 Factual Contract

### Schema / Invariants
- WavPack inputs are raw .wv byte streams with a block-oriented container. Valid samples begin with the WavPack block structure and are consumed directly by WavpackOpenFileInputEx64 through a seekable memory-backed reader. Regression corpus files are much better carriers than hand-built headers because they preserve block metadata, wrapper, tag, and decode-state consistency.

### Harness Links
- [[libfuzzer]]

### Notes
- These are descriptive format facts only; they carry no success-rate claim.
