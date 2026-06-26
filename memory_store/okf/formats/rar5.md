---
type: format-family
title: "Rar5 format"
description: "Round 8 descriptive format facts for rar5."
resource: cybergym://format/rar5
tags: ["rar5", "round-8"]
okf_support: 1
---
# Rar5 Format

## Round 8 Factual Contract

### Schema / Invariants
- RAR5 archives begin with a versioned RAR marker followed by variable-length block headers. File service blocks carry compression metadata, including dictionary/window parameters, and header corruption often causes the libarchive reader to reject or skip an entry before dictionary reads occur.

### Harness Links
- [[afl-file]]

### Notes
- These are descriptive format facts only; they carry no success-rate claim.

