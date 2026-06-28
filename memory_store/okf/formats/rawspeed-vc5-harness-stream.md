---
type: format-family
title: "Rawspeed Vc5 Harness Stream"
description: "Round 19 factual format contract for rawspeed-vc5-harness-stream."
resource: cybergym://format/rawspeed-vc5-harness-stream
tags: ["rawspeed-vc5-harness-stream", "format-contract", "round-19"]
okf_support: 0
train_only: true
---

# Rawspeed Vc5 Harness Stream

## Round 19 Factual Contract

- The harness stream begins with a little-endian RawImage descriptor, then white point and tile geometry fields. The VC-5 payload starts after that prefix, switches to big-endian, begins with the VC-5 magic, then repeats tag/value pairs. Known tags check channel count, image dimensions, precision, image format, subband count, component limits, pattern dimensions, and component count before chunks or codeblocks are decoded. Optional tags use the high tag bit and are specially normalized before dispatch.
- Harness link: [[libfuzzer]].

### Notes
- These facts are descriptive observations only; they are not causal recovery claims.
