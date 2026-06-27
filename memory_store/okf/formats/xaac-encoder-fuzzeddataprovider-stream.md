---
type: format-family
title: "Xaac Encoder Fuzzeddataprovider Stream"
description: "Round 19 factual format contract for xaac-encoder-fuzzeddataprovider-stream."
resource: cybergym://format/xaac-encoder-fuzzeddataprovider-stream
tags: ["xaac-encoder-fuzzeddataprovider-stream", "format-contract", "round-19"]
okf_support: 0
train_only: true
---

# Xaac Encoder Fuzzeddataprovider Stream

## Round 19 Factual Contract

- The encoder fuzzer uses many scalar configuration fields plus front-consumed audio bytes. Configuration controls include bitrate, transport flags, tool enable flags, PCM width, channel count, sample-rate selection, frame length, audio object type, SBR/USAC/MPS-related flags, bit reservoir, channel mask, DRC options, and codec mode. After setup, repeated frames are either copied from the front of the input or synthesized from a scalar byte.
- Harness link: [[libfuzzer]].

### Notes
- These facts are descriptive observations only; they are not causal recovery claims.
