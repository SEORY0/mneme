---
type: harness-contract
title: "Libfuzzer Libarchive Reader harness"
description: "Input contract facts for libfuzzer libarchive reader."
tags: ["libfuzzer-libarchive-reader", "round-17"]
okf_support: 1
train_only: true
---
# Libfuzzer Libarchive Reader Harness

## Round 17 Input Contract
- The libarchive fuzzer treats the raw input as an archive stream, enables all filters and formats, iterates headers, and reads entry data until EOF or fatal archive error.

## Round 17 Format Links
- [[zipx-lzma]]

## Round 17 Notes
- These are descriptive harness-carving facts only; they carry no success-rate claim.

## Round 17 Format Links
- [[zipx-lzma]]

## Round 17 Notes
- These are descriptive harness-carving facts only; they carry no success-rate claim.

## Round 25 Input Contract
- The libarchive fuzzer treats raw bytes as an archive stream, enables broad filter and format support, opens memory input, iterates archive headers, queries entry metadata, reads entry data, and then frees the archive reader.

## Round 25 Format Links
- [[rar5-archive]]

## Round 25 Notes
- These facts are descriptive harness-carving observations only; they are not causal recovery claims.

## Round 26 Factual Contract


### Input Contract
- The libarchive fuzzer consumes the whole raw archive byte stream from memory, enables all filters and formats, opens the archive, iterates headers, drains entry data, and frees the archive. There is no mode byte and no FuzzedDataProvider carving; the input must be a complete archive stream.

### Format Links
- [[rar]]

### Notes
- These are descriptive facts only; they carry no success-rate claim.
