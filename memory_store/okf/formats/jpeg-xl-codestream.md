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

## Round 30 Factual Contract

### Schema / Invariants
- JPEG XL decoder inputs may be raw codestreams or containers. Compact codestream seeds begin with the JPEG XL codestream signature and contain entropy-coded image data protected by ANS final-state checks. Mutating arbitrary headers usually prevents decoding; useful corruption keeps the image envelope intact and perturbs only the compressed payload relation.

### Harness Links
- [[libfuzzer-djxl]]

### Notes
- These facts are descriptive format observations only; they are not causal recovery claims.
