---
type: format-family
title: "Upx Packed Elf"
description: "Round 7 factual format contract for upx-packed-elf."
resource: cybergym://format/upx-packed-elf
tags: ["upx-packed-elf", "format-contract", "round-7"]
okf_support: 2
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
