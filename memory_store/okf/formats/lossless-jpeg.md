---
type: format-family
title: "Lossless JPEG"
description: "Round 19 factual format contract for lossless-jpeg."
resource: cybergym://format/lossless-jpeg
tags: ["lossless-jpeg", "format-contract", "round-19"]
okf_support: 0
train_only: true
---

# Lossless JPEG

## Round 19 Factual Contract

- Lossless JPEG uses the normal JPEG marker stream but a lossless start-of-frame marker and entropy-coded sample differences instead of DCT coefficients. A valid sample needs normal image framing, component metadata, Huffman coding metadata, scan metadata, and image data sufficient for the header parser and decoder to accept it.
- Harness link: [[libfuzzer]].

### Notes
- These facts are descriptive observations only; they are not causal recovery claims.
