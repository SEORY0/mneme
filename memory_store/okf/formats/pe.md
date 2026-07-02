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

## Round 22 Factual Contract

### Schema / Invariants
- PE files begin with an MZ header and PE signature, followed by COFF and optional headers, data-directory entries, and a section table. The YARA PE module maps RVAs to file positions through section virtual locations, raw data positions, and raw sizes.

### Harness Links
- [[libfuzzer]]

### Notes
- These are descriptive format facts only; they carry no success-rate claim.

## Round 23 Factual Contract

### Schema / Invariants
- A PE image needs an MZ header, an e_lfanew pointer to the PE signature, a COFF header, an optional header, data directories, and a section table. YARA's PE module maps RVAs through section virtual addresses, raw data offsets, raw sizes, and file alignment.

### Harness Links
- [[libfuzzer]]

### Notes
- These are descriptive format facts only; they carry no success-rate claim.

## Round 29 Factual Contract

### Schema / Invariants
- A PE input needs an MZ header, a PE signature reached through the DOS header pointer, a COFF header, an optional header, and a section table. YARA resolves slash-prefixed section names through the COFF symbol/string-table convention, while section address translation depends on the section virtual address, raw-data offset, and size fields being mutually consistent.

### Harness Links
- [[libfuzzer]]

### Notes
- These are descriptive format facts only; they carry no success-rate claim.
