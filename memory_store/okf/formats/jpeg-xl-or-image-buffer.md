---
type: format-family
title: "Jpeg Xl Or Image Buffer Format"
description: "Input contract facts for jpeg-xl-or-image-buffer."
tags: ["jpeg-xl-or-image-buffer", "round-30"]
okf_support: 0
train_only: true
---
# Jpeg Xl Or Image Buffer Format

## Round 30 Factual Contract

### Schema / Invariants
- JPEG XL can be supplied as a codestream or container image buffer. Frame metadata may enable features such as splines, patches, blending, extra channels, and noise. When noise is enabled, decoder setup and noise stages expect three additional noise-related pipeline channels after the color and extra-channel planes.

### Harness Links
- [[libfuzzer-smartcrop]]

### Notes
- These facts are descriptive format observations only; they are not causal recovery claims.
