---
type: format-family
title: gdbm-database format
description: "Round 23 descriptive structure and invariant facts for gdbm-database."
resource: cybergym://format/gdbm-database
tags: ["gdbm-database", "round-23"]
okf_support: 1
train_only: true
---
# Gdbm Database Format

## Round 23 Factual Contract

### Schema / Invariants
- GDBM inputs are database file images with a header, block-size-dependent directory and bucket structures, hash entries, and key/data records. Sequential access depends on a valid open database, current bucket metadata, and directory entries that map hash buckets to file blocks.

### Harness Links
- [[libfuzzer]]

### Notes
- These are descriptive format facts only; they carry no success-rate claim.
