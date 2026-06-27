---
type: format-family
title: Faad2 Decode Split Buffer format
description: Format contract for faad2-decode-split-buffer inputs.
resource: cybergym://format/faad2-decode-split-buffer
tags: [faad2-decode-split-buffer, stack-buffer-overflow, round-11]
okf_support: 1
train_only: true
---
# Schema
## Structure
This fuzzer input is not a standalone AAC file. It begins with a little-endian length for decoder initialization bytes, followed by that init chunk and then one decode chunk. The init chunk must make NeAACDecInit succeed before any frame bytes are decoded. PNS decoding depends on AAC individual channel stream fields such as window grouping, max scale-factor band, scale factors, codebooks, and scale-factor-band offsets.

## Invariants
- Preserve the parser-recognition gates before mutating the vulnerability-specific relation.
- Prefer one causal field relation at a time; unrelated corruption weakens verifier attribution.

## Harness Links
- [[libfuzzer-faad2-decode]]

## Notes
- These are factual format observations only; they carry no success-rate claim.
