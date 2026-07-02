---
type: harness-contract
title: "Afl Style Raw Kimageformats Multi Handler Fuzzer harness"
description: "Input contract facts for afl-style-raw-kimageformats-multi-handler-fuzzer."
tags: ["afl-style-raw-kimageformats-multi-handler-fuzzer", "round-32"]
okf_support: 1
---
# Afl Style Raw Kimageformats Multi Handler Fuzzer Harness

## Round 32 Input Contract
- The kimageformats fuzzer feeds the same raw byte buffer through several QImageIOHandler implementations using QBuffer, including TGA. There is no filename extension, outer container, mode byte, checksum, or FuzzedDataProvider split; TGA reachability depends entirely on the bytes passing the TGA handler support checks inside the shared raw buffer.

## Round 32 Format Links
- [[tga]]

## Round 32 Notes
- These facts are descriptive harness-carving observations only; they are not causal recovery claims.
