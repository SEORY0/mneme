---
type: format-family
title: "Ole Cfb Vba format"
description: "Round 8 descriptive format facts for ole-cfb-vba."
resource: cybergym://format/ole-cfb-vba
tags: ["ole-cfb-vba", "round-8"]
okf_support: 1
---
# Ole Cfb Vba Format

## Round 8 Factual Contract

### Schema / Invariants
- OLE Compound File inputs use a fixed file signature, sector allocation tables, directory entries, and named streams. VBA reachability requires a coherent storage tree with module streams rather than just a valid CFB header.

### Harness Links
- [[libfuzzer]]

### Notes
- These are descriptive format facts only; they carry no success-rate claim.

## Round 35 Factual Contract

### Schema / Invariants
- OLE CFB uses a header, FAT sectors, directory entries with UTF-16 stream names, and regular or mini stream storage. ClamAV extracts streams to temporary files and keys them by lowercased stream names. VBA dir streams are compressed and inflate to records shaped as a record kind, a declared size, and payload; module records then contain nested name, stream-name, docstring, offset, cookie, type, and terminator fields.

### Harness Links
- [[libfuzzer-scanfile]]

### Notes
- These facts are descriptive observations from round 35; they carry no success-rate claim.
