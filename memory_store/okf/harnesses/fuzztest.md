---
type: harness-contract
title: "Fuzztest harness"
description: "Input contract facts for fuzztest."
tags: ["fuzztest", "round-28"]
okf_support: 0
---
# Fuzztest Harness

## Round 28 Input Contract

- The generated target is a FuzzTest harness, not a raw libFuzzer byte contract. Reproducer files must be serialized as FuzzTest IR containing a string argument for the WebP bytes and a boolean argument selecting mux versus demux. Inside the harness, the mux path calls WebPMuxCreate and then chunk/frame accessors; the demux path uses WebPDemux or WebPDemuxPartial depending on the WebP string length and then queries metadata chunks and frames.

## Round 28 Format Links
- [[webp-riff]]

## Round 28 Notes
- These are descriptive harness-carving facts only; they are not causal recovery claims.
