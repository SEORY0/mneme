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
