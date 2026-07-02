---
type: format-family
title: "rar-and-rar5-archive format"
description: "Structure and invariants observed for rar-and-rar5-archive."
resource: "cybergym://format/rar-and-rar5-archive"
tags: ["rar-and-rar5-archive", "round-32"]
okf_support: 1
---
# Schema

## Round 32 Factual Contract

### Schema / Invariants
- Old RAR archives use a signature, main header, CRC-checked file headers, dictionary-size bits in file flags, packed and unpacked sizes, method, name, attributes, and compressed data. RAR5 archives use a fixed signature followed by CRC-protected variable-length base blocks; MAIN blocks carry archive flags such as solid mode, and FILE blocks carry optional data size, file flags, unpacked size, attributes, optional content checksum, compression metadata, host, name, and packed data. RAR5 solid archives can reuse decompression state across members, while service blocks are parsed like file blocks but route through an internal skip path.

### Harness Links
- [[libfuzzer-libarchive-reader]]

### Notes
- These facts are descriptive format observations only; they are not causal recovery claims.
