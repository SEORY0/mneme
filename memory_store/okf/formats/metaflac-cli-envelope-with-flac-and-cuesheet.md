---
type: format-family
title: metaflac-cli-envelope-with-flac-and-cuesheet format
description: Format contract for metaflac-cli-envelope-with-flac-and-cuesheet.
resource: cybergym://format/metaflac-cli-envelope-with-flac-and-cuesheet
tags: [metaflac-cli-envelope-with-flac-and-cuesheet]
okf_support: 1
train_only: true
---
# Schema
## Structure
Inputs follow the `metaflac-cli-envelope-with-flac-and-cuesheet` family contract.

## Invariants
- Parser reachability depends on preserving the format gates described below.

## Round 15 Factual Contract

### Schema / Invariants
- The underlying file is a FLAC stream with metadata blocks; the imported side input is a textual
  cuesheet containing CATALOG, FILE, TRACK, and INDEX records. Importing a cuesheet can automatically
  create seekpoint specifications for cue indices unless cued seekpoints are disabled.

### Harness Links
- [[libfuzzer-cli-envelope]]

### Notes
- These are descriptive format facts only; they carry no success-rate claim.
