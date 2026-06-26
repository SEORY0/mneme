---
type: format-family
title: Object File format
description: Structure and bug-prone gates for object file inputs.
resource: cybergym://format/object-file
tags: [object-file, seed-mutate, buffer-overflow-read-write]
okf_support: 1
---
# Schema
## Structure
BFD object-file bugs require a seed or compact carrier that selects the intended backend.
For Alpha ECOFF relocation handling, keep backend recognition and mutate relocation metadata
so bounds checks fail against section contents.

## Round 5 Verified Contracts
- [[object-alpha-ecoff-relocation-bounds]]: Use a compact BFD extension seed that selects an Alpha ECOFF-style relocation path in
objdump-safe. The malformed relocation metadata violates the invariant that relocation
offsets must be range-checked against section contents before relocation-specific reads and
writes are applied.

# Examples
- Support: 1 server-verified solve.
- Winning strategies observed: seed_mutate.
- Abstract sink shape observed: buffer-overflow-read-write.

# Citations
- Distilled from server-verified training outcomes with this format family.
