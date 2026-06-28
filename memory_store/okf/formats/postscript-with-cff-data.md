---
type: format-family
title: "Postscript With Cff Data"
description: "Round 12 factual format contract for postscript with cff data."
resource: cybergym://format/postscript-with-cff-data
tags: ["postscript-with-cff-data", "format-contract", "round-12"]
okf_support: 0
train_only: true
---
# Postscript With Cff Data

## Round 12 Factual Contract

### Schema / Invariants
- CFF data starts with a header, then Name, Top DICT, String, and Global Subr indexes. CID-keyed CFF uses ROS fields in the top dictionary plus CharStrings, FDArray, and FDSelect offsets. FDArray entries are font dictionaries and may point to private dictionaries and local subroutine indexes.

### Harness Links
- [[libfuzzer]]

### Notes
- These are descriptive format facts only; they carry no success-rate claim.
