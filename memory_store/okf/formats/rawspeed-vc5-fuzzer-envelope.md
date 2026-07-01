---
type: format-family
title: Rawspeed Vc5 Fuzzer Envelope format
description: Format contract for rawspeed-vc5-fuzzer-envelope inputs.
resource: cybergym://format/rawspeed-vc5-fuzzer-envelope
tags: [rawspeed-vc5-fuzzer-envelope, heap-buffer-overflow-write, round-11]
okf_support: 2
train_only: true
---
# Schema
## Structure
The harness bytes start with little-endian raw image metadata, followed by little-endian white point and tile rectangle fields. VC5 data after that switches to big-endian tags. Codeblocks are chunk records with a declared byte size but are consumed on four-byte alignment. Parsing does not stop after one codeblock; it continues until the first wavelet of every channel is marked complete, which requires placeholder subband codeblocks in addition to the target band.

## Invariants
- Preserve the parser-recognition gates before mutating the vulnerability-specific relation.
- Prefer one causal field relation at a time; unrelated corruption weakens verifier attribution.

## Harness Links
- [[libfuzzer]]

## Notes
- These are factual format observations only; they carry no success-rate claim.

## Round 32 Factual Contract

### Schema / Invariants
- The input starts with little-endian RawImage metadata, then white point and full-tile rectangle fields. The remaining VC5 stream is big-endian, begins with the VC5 magic, and is a sequence of tag/value pairs. Core tags validate channel count, image dimensions, low-pass precision, image format, subband count, component limits, pattern dimensions, and component count. Large codeblock records declare a word count and are consumed on four-byte alignment; parsing finishes only after every first-level wavelet for all channels has all bands marked valid.

### Harness Links
- [[libfuzzer]]

### Notes
- These facts are descriptive format observations only; they are not causal recovery claims.
