---
type: format-family
title: "Rar5 format"
description: "Round 8 descriptive format facts for rar5."
resource: cybergym://format/rar5
tags: ["rar5", "round-8"]
okf_support: 2
---
# Rar5 Format

## Round 8 Factual Contract

### Schema / Invariants
- RAR5 archives begin with a versioned RAR marker followed by variable-length block headers. File service blocks carry compression metadata, including dictionary/window parameters, and header corruption often causes the libarchive reader to reject or skip an entry before dictionary reads occur.

### Harness Links
- [[afl-file]]

### Notes
- These are descriptive format facts only; they carry no success-rate claim.


## Round 13 Facts
- RAR5 inputs start with the RAR5 marker, then CRC-protected variable-length base block headers. FILE base blocks carry split-before/split-after flags, data size, unpacked size, compression metadata, and a dictionary/window-size selector; header CRC validity is a hard parser gate.

## Round 24 Factual Contract

### Schema / Invariants
- RAR5 archives start with a fixed signature and then variable-length records. File-service records carry flags and attributes that distinguish directories from files, while compressed data is referenced by block sizes. Mutating a real RAR5 seed preserves the signature and record framing better than constructing from scratch.

### Harness Links
- [[afl-libfuzzer-libarchive-archive-reader]]

### Notes
- These are descriptive facts only; they carry no success-rate claim.

## Round 28 Factual Contract

### Schema / Invariants
- RAR5 archives begin with a fixed marker followed by CRC-protected base blocks. A base block carries a variable-length header-size field, then a header type and flags; file/service blocks may additionally carry extra-data and data-size varints before file metadata. The vulnerable path computes the checksum over only the declared header-size span, so a too-small declared span can leave later header fields outside the checksum-covered area.

### Harness Links
- [[libfuzzer]]

### Notes
- These are descriptive format facts only; they carry no success-rate claim.

## Round 30 Factual Contract

### Schema / Invariants
- RAR5 inputs begin with the RAR5 signature followed by CRC-protected base blocks such as MAIN, FILE, SERVICE, and ENDARC. The base-block CRC covers the variable-size header field and the remaining header fields, so any header metadata mutation must update that CRC. FILE headers can carry optional extra-data and data-size fields, then file flags, unpacked size, attributes, optional stored content CRC, compression info, host OS, name, and extra records. Compressed member data is split into RAR5 compressed blocks with their own compact header checksum; Huffman-coded commands can emit literals/copies or define filters. Filter descriptors are bitstream fields containing a relative block start, block length, and filter type, and the parser requires filter ranges to stay ordered and non-overlapping.

### Harness Links
- [[libfuzzer]]

### Notes
- These facts are descriptive format observations only; they are not causal recovery claims.
