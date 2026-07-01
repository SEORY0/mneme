---
type: format-family
title: "Rar5 format"
description: "Round 8 descriptive format facts for rar5."
resource: cybergym://format/rar5
tags: ["rar5", "round-8"]
okf_support: 7
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

## Round 32 Factual Contract

### Schema / Invariants
- RAR5 archives begin with a fixed marker followed by CRC-protected variable-length base blocks. File blocks with data carry optional extra-data size, data-size, file flags, unpacked size, attributes, compression info, host OS, name, and optional extras before the compressed data region. Compressed data is divided into compressed blocks with a compact block header containing flags, a checksum byte, and a variable-width block-size field. If the table-present flag is set, the block payload starts with Huffman table metadata. The first Huffman metadata phase is nibble-coded and uses an escape nibble to either emit a literal escape value or run-length-fill zero bit lengths.
- RAR5 starts with a fixed marker followed by CRC-protected base headers using variable-length integers. File blocks carry optional data size, file metadata, compression information, host OS, and a name before compressed data. Compressed data begins with a compact block header containing bit-size, byte-count, last-block, and table-present flags plus a small checksum over the block header fields. Huffman table data follows the block header and starts with nibble-coded code lengths before a bitstream-encoded combined table.

### Harness Links
- [[libfuzzer]]
- [[libfuzzer-libarchive]]

### Notes
- These facts are descriptive format observations only; they are not causal recovery claims.

## Round 33 Factual Contract

### Schema / Invariants
- RAR5 archives begin with a fixed marker followed by integrity-protected variable-length base blocks. File blocks with data carry optional extra-data size, data size, file flags, unpacked size, attributes, optional content integrity metadata, compression info, host OS, filename, and then compressed member data. The compression info contains method, version, solid flag, and a dictionary/window selector. Compressed data uses a compact block header with an integrity field and table-present flag, followed by Huffman table metadata and command bits that can emit literals, filters, or dictionary-copy operations.
- RAR5 archives begin with a fixed marker followed by CRC-protected variable-length base blocks. Main blocks carry archive flags such as solid mode. File blocks can carry extra-data and packed-data sizes, then file flags such as directory and content checksum, unpacked size, attributes, compression information, host OS, filename, optional extras, and member data. Header metadata mutations must preserve varint widths or rebuild the block header CRC. Directory flags can force a zero decompression window, while host metadata controls how the archive entry mode is exposed.
- RAR5 archives begin with a fixed marker followed by CRC-protected variable-length base headers. Main headers carry archive flags such as volume and solid state. File and service headers can carry extra-data and data-size fields, file flags, unpacked size, attributes, optional content CRC, compression info, host OS, filename, and extra records before compressed data. Compression info encodes method/version, a solid bit, and a dictionary/window selector. Base-header CRC must be recomputed after metadata mutations. Service blocks are parsed through the file path and their data is skipped through the decompressor.

### Harness Links
- [[libfuzzer-libarchive]]

### Notes
- These are descriptive format facts only; they carry no success-rate claim.
