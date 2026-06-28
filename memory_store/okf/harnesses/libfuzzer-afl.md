---
type: harness-contract
title: "Libfuzzer Afl harness"
description: "Input contract facts for libfuzzer-afl."
tags: ["libfuzzer-afl", "round-15"]
okf_support: 3
---
# Libfuzzer Afl Harness

## Round 15 Input Contract
- The draw fuzzer treats the raw input as an OpenType font blob. It derives a coordinate count from
  the final byte, then consumes coordinate bytes from the end of the input and calls the normalized-
  variation-coordinate API before drawing the first few glyphs. The harness has no front selector, but
  it does have tail-carved coordinate controls.
- The decompression-frame fuzzer feeds the raw input as an in-memory blosc2 super-chunk frame. If
  frame opening succeeds, it allocates an output buffer from the frame metadata and decompresses
  chunks in order. There is no harness-level byte carving or mode selector.
- The fuzzer creates a fresh default server and dummy connection for each raw input, copies the entire
  input into a UA_ByteString, and calls the binary-message processor. There is no FuzzedDataProvider
  carving; all bytes are the OPC UA message chunk.

## Format Links
- [[blosc2-frame]]
- [[opc-ua-binary-message]]
- [[opentype-font]]

## Notes
- These are descriptive harness-carving facts only; they are not causal recovery claims.
