---
type: format-family
title: "PE format"
description: "Round 8 descriptive format facts for pe."
resource: cybergym://format/pe
tags: ["pe", "round-8"]
okf_support: 1
---
# PE Format

## Round 8 Factual Contract

### Schema / Invariants
- A PE image needs a DOS magic and e_lfanew pointer to a PE signature, a COFF file header, an optional header with data directories, and at least one section whose virtual address and raw file offset let YARA translate RVAs. The debug data directory stores an RVA and size; each debug entry contains a type plus an RVA for the raw CodeView data.

### Harness Links
- [[libfuzzer]]

### Notes
- These are descriptive format facts only; they carry no success-rate claim.

