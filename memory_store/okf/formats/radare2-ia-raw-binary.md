---
type: format-family
title: "Radare2 Ia Raw Binary format"
description: "Round 34 factual contract for radare2-ia-raw-binary."
tags: ["radare2-ia-raw-binary", "round-34"]
okf_support: 1
train_only: true
---
# Radare2 Ia Raw Binary format

## Round 34 Factual Contract

### Schema / Invariants
- The harness accepts arbitrary raw binary bytes and radare2 auto-detects formats from the memory buffer. The bundled corpus covers common executable and object formats plus generic binary blobs. The ia command asks radare2 for file information, imports, exports, classes, sections, maps, symbols, and raw or parsed strings, so reachability usually depends on satisfying a format magic plus enough coherent table structure for those metadata queries.

### Harness Links
- [[libfuzzer]]

### Notes
- These facts are descriptive observations only; they carry no success-rate claim.
