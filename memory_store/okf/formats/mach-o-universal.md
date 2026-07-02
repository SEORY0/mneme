---
type: format-family
title: "Mach O Universal format"
description: "Round 28 descriptive format facts for mach-o-universal."
resource: cybergym://format/mach-o-universal
tags: ["mach-o-universal", "round-28"]
okf_support: 0
---
# Mach O Universal Format

## Round 28 Factual Contract

### Schema / Invariants
- Mach-O universal objects start with a fat header carrying an architecture count, followed by architecture records. The records are big-endian and describe embedded Mach-O slices by CPU metadata plus a file range. There are 32-bit and 64-bit architecture-record variants, and malformed table length or slice-range relations can be rejected before any embedded Mach-O slice is parsed. A standalone Mach-O seed can be used as the embedded slice when constructing a universal wrapper.

### Harness Links
- [[libfuzzer-raw-file]]

### Notes
- These are descriptive format facts only; they carry no success-rate claim.
