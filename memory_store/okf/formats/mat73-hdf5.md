---
type: format-family
title: "Mat73 Hdf5"
description: "Round 12 factual format contract for mat73-hdf5."
resource: cybergym://format/mat73-hdf5
tags: ["mat73-hdf5", "format-contract", "round-12"]
okf_support: 0
train_only: true
---
# Mat73 Hdf5

## Round 12 Factual Contract

### Schema / Invariants
- MAT version 7.3 files are HDF5 containers with MATLAB-specific attributes and datasets. Variable iteration opens HDF5 links, reads MATLAB class/type metadata, obtains dataspaces, and asks HDF5 for simple extent dimensions into buffers sized from the interpreted rank or object kind.

### Harness Links
- [[libfuzzer]]

### Notes
- These are descriptive format facts only; they carry no success-rate claim.

## Round 30 Factual Contract

### Schema / Invariants
- MAT v7.3 files are HDF5 files with a MATLAB user block followed by the HDF5 signature and normal HDF5 metadata. Matio discovers variables by opening the root group, iterating directory entries and references, then dereferencing HDF5 dataset object headers. Compact datasets store their data inside a layout object-header message; the message contains a layout version/class, a declared inline data length, and the inline payload. Fill-value messages are separate object-header messages and can also contain declared payload sizes, but that broader mutation was not fixed by this task.

### Harness Links
- [[libfuzzer]]

### Notes
- These facts are descriptive format observations only; they are not causal recovery claims.
