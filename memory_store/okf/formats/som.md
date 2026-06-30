---
type: format-family
title: "Som format"
description: "Round 28 descriptive format facts for som."
resource: cybergym://format/som
tags: ["som", "round-28"]
okf_support: 0
---
# Som Format

## Round 28 Factual Contract

### Schema / Invariants
- SOM objects are recognized through a big-endian fixed header with HPPA system id, SOM magic, accepted version id, and table location/count pairs. The space dictionary points into a NUL-terminated space string table and names subspace records. A subspace record carries load/access flags, content location and length, alignment as a power-of-two value, a name offset into the same string table, and a relocation fixup index and byte count. The object-level fixup request location is the base of the relocation stream, while each subspace supplies an index into that stream. Symbol-bearing relocation opcodes consume operands from the variable-length fixup stream and use those operands as indexes into objdump's canonical symbol pointer array.

### Harness Links
- [[libfuzzer]]

### Notes
- These are descriptive format facts only; they carry no success-rate claim.
