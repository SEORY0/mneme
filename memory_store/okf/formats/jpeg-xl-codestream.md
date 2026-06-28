---
type: format-family
title: jpeg-xl-codestream format
description: Structure and reachability facts for jpeg-xl-codestream inputs.
tags: [jpeg-xl-codestream]
okf_support: 0
---
# Jpeg Xl Codestream Format

## Round 10 Factual Contract

### Schema / Invariants
- The selected decoder target expects a JPEG XL codestream followed by a compact option suffix. The suffix controls alpha/grayscale output, streaming, JPEG reconstruction, callback output, orientation preservation, output type, endianness, alignment, and CPU target selection.

### Harness Links
- [[libfuzzer]]

### Notes
- These are descriptive format facts only; they carry no success-rate claim.

## Round 19 Factual Contract

- JPEG XL inputs are binary codestream/container bytes. Valid seeds carry enough codestream structure to reach the decoder, but feature groups such as noise require specific image metadata and frame data rather than arbitrary padding.
- Harness link: [[libfuzzer]].

### Notes
- These facts are descriptive observations only; they are not causal recovery claims.
