---
type: format
title: "ELF Shared Object With Versioned Dynamic Symbol"
access_scope: generate
confidence: medium
tags: ["elf-shared-object-with-versioned-dynamic-symbol", "format", "round-13"]
forbidden_fields: [raw_poc_bytes, task_id, exact_offset, checksum, submit_metadata]
train_only: true
---
# ELF Shared Object With Versioned Dynamic Symbol

## Round 13 Facts
- The ELF must be recognized as a dynamic object and include accepted dynamic-symbol and version metadata. The vulnerable relation is not a corrupt section table; it is a valid versioned symbol whose version string is too long for readelf's temporary formatting buffer.
