---
type: format-family
title: "Hdf5 format"
description: "Round 28 descriptive format facts for hdf5."
resource: cybergym://format/hdf5
tags: ["hdf5", "round-28"]
okf_support: 0
---
# Hdf5 Format

## Round 28 Factual Contract

### Schema / Invariants
- Old-style HDF5 files can store root group links in a local heap plus v1 symbol-table node behind a v1 B-tree. Symbol-table entries carry a heap-name reference and a link to the target object header, while the B-tree key range also stores heap-name references used to decide whether lookup enters the leaf. Dataset object headers contain typed messages with a small type, size, flags header followed by aligned raw message bodies. The fill-new message has version-dependent layouts; the later layout uses a flags byte, and the have-value flag causes a fill-size field followed by fill bytes.

### Harness Links
- [[libfuzzer-aflpp-file-h5-extended]]

### Notes
- These are descriptive format facts only; they carry no success-rate claim.
