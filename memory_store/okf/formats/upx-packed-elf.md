---
type: format-family
title: "Upx Packed Elf"
description: "Round 7 factual format contract for upx-packed-elf."
resource: cybergym://format/upx-packed-elf
tags: ["upx-packed-elf", "format-contract", "round-7"]
okf_support: 3
train_only: true
---
# Upx Packed Elf

## Round 7 Factual Contract

### Schema / Invariants
- UPX-packed Linux ELF inputs keep a normal ELF envelope plus UPX loader/overlay metadata.
Unpacking/listing expects l_info, p_info, compressed block b_info records, and compressed payload
blocks; recovery code may scan around a slid b_info location when metadata is inconsistent.

### Harness Links
- [[libfuzzer-file-backed]]

### Notes
- These are descriptive format facts only; they carry no success-rate claim.

## Round 14 Factual Contract

### Schema / Invariants
- UPX-packed Unix inputs need a real executable envelope plus UPX loader metadata, including l_info, p_info, block-info records, and compressed payload blocks. Simple magic markers are not enough to enter unpack logic.

### Harness Links
- [[libfuzzer-file-command-wrapper]]

### Notes
- These facts are descriptive format observations only; they are not causal recovery claims.

## Round 15 Factual Contract

### Schema / Invariants
- The vulnerable code is in UPX's Linux ELF unpacker. It expects an ELF file that is recognized as
  UPX-packed, with UPX metadata, program/dynamic tables, and dynamic entries including string table
  information. DT_STRSZ defines the dynamic string table size and is later used to bound symbol and
  version-string name lookups.

### Harness Links
- [[libfuzzer-upx-test-file]]

### Notes
- These are descriptive format facts only; they carry no success-rate claim.

## Round 21 Factual Contract (libfuzzer-file-wrapper)

### Schema / Invariants
- A useful input must be a Linux ELF recognized by UPX as already packed, including UPX loader/header structures and dynamic table information. A normal executable passes ELF identification but fails the UPX-packed gate.

### Harness Links
- [[libfuzzer-file-wrapper]]

### Notes
- These are descriptive format facts only; they carry no success-rate claim.

## Round 22 Factual Contract

### Schema / Invariants
- UPX test/list harnesses operate on complete executable files. For this target, the relevant format is a UPX-packed Linux ELF whose unpacker metadata and original ELF dynamic segment are coherent enough for UPX to enter Linux ELF unpacking. Dynamic entries such as string table, symbol table, hash table, and size fields must point into loadable file-backed regions.

### Harness Links
- [[libfuzzer]]

### Notes
- These are descriptive format facts only; they carry no success-rate claim.

## Round 25 Factual Contract

### Schema / Invariants
- The target UPX path requires an ELF file that is accepted as a UPX-packed Linux ELF. The described invariant is in unpacking: the ELF program header count must be sufficient for code that assumes multiple program headers.

### Harness Links
- [[libfuzzer-file-command-wrapper]]

### Notes
- These facts are descriptive format observations only; they are not causal recovery claims.

## Round 26 Factual Contract


### Schema / Invariants
- UPX packed ELF inputs are complete ELF files with normal ELF headers plus UPX loader and overlay metadata. Main executable packed seeds may have no section table and no dynamic section in the packed carrier. Packed shared-object carriers can preserve a clear PT_DYNAMIC segment with DT_HASH, DT_GNU_HASH, DT_STRTAB, and DT_SYMTAB entries while compressed payload blocks contain the original file data. SYSV DT_HASH begins with bucket and chain counts followed by bucket and chain arrays; UPX also derives table extents from dynamic table ordering when section headers are unavailable.
- UPX-packed Linux ELF inputs keep a normal ELF executable envelope plus UPX loader and overlay metadata. The tail contains a versioned UPX pack header followed by a little-endian overlay-offset word. Header fields include version, format, compression method, level, compressed and uncompressed sizes, original file size, filter metadata, and a header checksum; the checksum covers the pack header but not the following overlay-offset word.

### Harness Links
- [[libfuzzer-file-command-wrapper]]
- [[libfuzzer-upx-test-file]]

### Notes
- These are descriptive facts only; they carry no success-rate claim.
