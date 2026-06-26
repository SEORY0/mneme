---
type: format-family
title: "Upx Packed Elf"
description: "Round 7 factual format contract for upx-packed-elf."
resource: cybergym://format/upx-packed-elf
tags: ["upx-packed-elf", "format-contract", "round-7"]
okf_support: 1
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
