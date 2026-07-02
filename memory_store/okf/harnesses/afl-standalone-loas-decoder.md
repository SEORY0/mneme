---
type: harness-contract
title: "Afl Standalone Loas Decoder Harness"
description: "Input contract facts for afl-standalone-loas-decoder."
tags: ["afl-standalone-loas-decoder", "round-37", "harness-contract"]
okf_support: 1
train_only: true
---
# Afl Standalone Loas Decoder Harness
## Round 37 Input Contract

### Input Contract
- The wrapper runs the AAC decoder target on a raw file path.
- The target reads the whole file as a LOAS/LATM byte stream, opens the FDK AAC decoder in LOAS transport mode, fills the decoder from the file buffer, and repeatedly asks for decoded frames.
- There is no FuzzedDataProvider; all structure is parsed from the raw stream.

### Format Links
- [[aac-loas-latm]]

### Notes
- These are descriptive harness-carving facts only; they are not causal recovery claims.
