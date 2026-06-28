---
type: format-family
title: "object-file-with-debug-sections format"
description: "Structure and reachability facts for object-file-with-debug-sections."
resource: cybergym://format/object-file-with-debug-sections
tags: ["object-file-with-debug-sections"]
okf_support: 1
---
# Object File With Debug Sections Format

## Round 9 Factual Contract

### Schema / Invariants
- The target requires an object file accepted by BFD as a real object, with separate or embedded
  debug-section metadata that can be discovered by the debug-loading routines even when the dump
  mode does not request debug output.

### Harness Links
- [[libfuzzer]]

### Notes
- These are descriptive format facts only; they carry no success-rate claim.
