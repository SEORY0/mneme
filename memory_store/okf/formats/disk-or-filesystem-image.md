---
type: format-family
title: "Disk Or Filesystem Image format"
description: "Descriptive contract facts for Disk Or Filesystem Image."
resource: "cybergym://format/disk-or-filesystem-image"
tags: ["disk-or-filesystem-image", "round-6"]
okf_support: 1
---
# Schema
## Identification
Descriptive facts promoted from round traces; not a verified recovery policy.

## Round 6 Factual Contract

### Schema / Invariants
- Sleuthkit fuzzers expect raw disk or filesystem image bytes. Useful parser entry requires a recognizable volume system or filesystem structure before higher-level directory traversal can drive stack operations.

### Harness Links
- [[honggfuzz-wrapper]]

### Notes
- These are factual format and harness observations only; they carry no success-rate claim.
