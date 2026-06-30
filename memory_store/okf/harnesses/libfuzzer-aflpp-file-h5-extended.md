---
type: harness-contract
title: "Libfuzzer Aflpp File H5 Extended harness"
description: "Input contract facts for libfuzzer-aflpp-file-h5-extended."
tags: ["libfuzzer-aflpp-file-h5-extended", "round-28"]
okf_support: 0
---
# Libfuzzer Aflpp File H5 Extended Harness

## Round 28 Input Contract

- The harness writes the fuzz input bytes directly to a temporary file and calls the extended HDF5 fuzzer entry point. There is no leading selector byte and no FuzzedDataProvider carving. After opening the file read-write, it attempts to open one fixed dataset name and then one fixed attribute name, so object-header bugs in datasets require the root group lookup metadata to resolve that fixed dataset name.

## Round 28 Format Links
- [[hdf5]]

## Round 28 Notes
- These are descriptive harness-carving facts only; they are not causal recovery claims.
