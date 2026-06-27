---
type: harness-contract
title: "Afl Style Raw Stdin Image Fuzzer harness"
description: "Input contract facts for afl-style raw stdin image fuzzer."
tags: ["afl-style-raw-stdin-image-fuzzer", "round-16"]
okf_support: 1
---
# Afl Style Raw Stdin Image Fuzzer Harness

## Round 16 Input Contract
- The kimageformats harness feeds the same raw input bytes through several QImageIOHandler implementations using a QBuffer; no filename extension or outer container is provided. A valid TGA header must survive other handlers and the TGA support checks before pixel data is read.

## Round 16 Format Links
- [[tga]]

## Round 16 Notes
- These are descriptive harness-carving facts only; they are not causal recovery claims.
