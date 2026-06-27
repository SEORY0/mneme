---
type: format-family
title: ers-fuzzer-archive format
description: Format contract for ers-fuzzer-archive.
resource: cybergym://format/ers-fuzzer-archive
tags: [ers-fuzzer-archive]
okf_support: 1
train_only: true
---
# Schema
## Structure
Inputs follow the `ers-fuzzer-archive` family contract.

## Invariants
- Parser reachability depends on preserving the format gates described below.

## Round 15 Factual Contract

### Schema / Invariants
- The specialized archive format has a magic header line and repeated named-file markers. ERS headers
  include a DatasetHeader block, dataset type, data file reference, raster metadata, dimensions, and
  band count. PAM sidecars use a PAMDataset root with PAMRasterBand child nodes.

### Harness Links
- [[libfuzzer]]

### Notes
- These are descriptive format facts only; they carry no success-rate claim.
