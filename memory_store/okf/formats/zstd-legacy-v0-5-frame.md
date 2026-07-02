---
type: format-family
title: "zstd-legacy-v0-5-frame format"
description: "Structure and invariants observed for zstd-legacy-v0-5-frame."
resource: "cybergym://format/zstd-legacy-v0-5-frame"
tags: ["zstd-legacy-v0-5-frame", "round-33"]
okf_support: 1
---
# Schema

## Round 33 Factual Contract

### Schema / Invariants
- Legacy zstd v0.5 frames have a compact magic/header followed by block headers that encode block type and compressed size, then the block payload. Compressed blocks contain a literals section followed by sequence metadata. The sequence metadata includes a sequence count, table-type controls, a dumps-length field, optional dumps bytes, entropy table descriptions, and the backward bitstream. Long literal or match lengths consume extension bytes from the dumps area.

### Harness Links
- [[libfuzzer]]

### Notes
- These are descriptive format facts only; they carry no success-rate claim.
