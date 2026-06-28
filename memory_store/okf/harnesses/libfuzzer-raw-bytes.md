---
type: harness-contract
title: "Libfuzzer Raw Bytes Harness"
description: "Round 7 input contract facts for libfuzzer-raw-bytes."
tags: ["libfuzzer-raw-bytes", "harness-contract", "round-7"]
okf_support: 4
train_only: true
---
# Libfuzzer Raw Bytes Harness

## Round 7 Input Contract
- LibFuzzer calls the entrypoint with raw file bytes and a size. The vulnerable entrypoint declaration
uses a character pointer where libFuzzer expects a byte pointer, producing a callback ABI/type
mismatch.

## Round {ROUND} Format Links
- [[yara-rule-text]]

## Round {ROUND} Notes
- These are descriptive harness-carving facts only; they are not causal recovery claims.

## Round 24 Factual Contract

### Input Contract
- Raw bytes are passed to a TIFF parser and decoder-selection fuzzer. The harness parses the byte buffer as a TIFF tree, instantiates the selected decoder, disables crop/support checks, and calls raw and metadata decode methods while catching RawSpeed exceptions.
- Raw libFuzzer bytes are passed directly to Gfx::load_bmp_from_memory by FuzzBMPLoader. There is no fuzzer prefix or mode byte; format selection is entirely by the BMP file bytes.
- Raw libFuzzer bytes are passed directly to PGMImageDecoderPlugin and frame decoding is requested. There is no prefix, mode selector, or FuzzedDataProvider carving.

### Format Links
- [[bmp]]
- [[pgm]]
- [[tiff-or-orf-raw-camera-file]]

### Notes
- These are descriptive facts only; they carry no success-rate claim.
