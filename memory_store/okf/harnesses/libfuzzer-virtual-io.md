---
type: harness-contract
title: "Libfuzzer Virtual Io harness"
description: "Input contract facts for libfuzzer-virtual-io."
tags: ["libfuzzer-virtual-io", "round-15"]
okf_support: 1
---
# Libfuzzer Virtual Io Harness

## Round 15 Input Contract
- The fuzz target exposes the raw input through libsndfile virtual I/O and calls sf_open_virtual.
  After open it rejects zero or extremely large channel counts, allocates a float buffer proportional
  to channels, and reads frames. No FuzzedDataProvider carving or leading mode byte is used.

## Format Links
- [[audio-container]]

## Notes
- These are descriptive harness-carving facts only; they are not causal recovery claims.
