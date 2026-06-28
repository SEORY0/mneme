---
type: format-family
title: "upx-packed-pe format"
description: "Structure and reachability facts for upx-packed-pe."
resource: cybergym://format/upx-packed-pe
tags: ["upx-packed-pe"]
okf_support: 1
---
# UPX Packed Pe Format

## Round 9 Factual Contract

### Schema / Invariants
- The target path is for UPX-packed PE files.
- The outer file must be recognized by UPX as packed, then decompression/rebuild metadata must
  describe PE imports including DLL names and imported symbol names.
- Ordinary PE stubs are insufficient because they do not reach UPX unpack/rebuild logic.

### Harness Links
- [[afl-libfuzzer-wrapper]]

### Notes
- These are descriptive format facts only; they carry no success-rate claim.
