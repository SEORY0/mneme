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
