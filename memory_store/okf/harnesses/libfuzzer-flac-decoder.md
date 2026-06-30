---
type: harness-contract
title: "Libfuzzer Flac Decoder Harness"
description: "Input contract facts for libfuzzer-flac-decoder."
tags: ["libfuzzer-flac-decoder", "round-27"]
okf_support: 1
---
# Libfuzzer Flac Decoder Harness

## Round 27 Input Contract
- The active target is the FLAC oss-fuzz decoder harness.
- It uses a custom front-consuming datasource where every scalar or byte vector is encoded as a little-endian length-prefixed chunk.
- Initial boolean chunks choose native FLAC vs Ogg and decoder options; operation-loop chunks choose calls such as process_until_end_of_metadata.

## Round 27 Format Links
- [[flac]]

## Round 27 Notes
- These are descriptive harness-carving facts only; they are not causal recovery claims.
