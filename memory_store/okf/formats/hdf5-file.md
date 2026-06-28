---
type: format-family
title: "Hdf5 File"
description: "Round 7 factual format contract for hdf5-file."
resource: cybergym://format/hdf5-file
tags: ["hdf5-file", "format-contract", "round-7"]
okf_support: 1
train_only: true
---
# Hdf5 File

## Round 7 Factual Contract

### Schema / Invariants
- HDF5 files contain a signature, superblock, size/address-size metadata, object headers, heaps,
B-trees, and encoded file addresses. The target address decoder reads an address field byte-by-byte
using an address length derived from file metadata.

### Harness Links
- [[libfuzzer-carved-file]]

### Notes
- These are descriptive format facts only; they carry no success-rate claim.
