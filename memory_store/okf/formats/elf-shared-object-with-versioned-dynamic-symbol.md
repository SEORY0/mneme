---
type: format
title: "Elf Shared Object With Versioned Dynamic Symbol"
input_format: elf-shared-object-with-versioned-dynamic-symbol
access_scope: generate
forbidden_fields: [raw_poc_bytes, task_id, exact_offset, checksum, submit_metadata]
---
# Elf Shared Object With Versioned Dynamic Symbol

## Schema
- The ELF must be recognized as a dynamic object and include accepted dynamic-symbol and version metadata. The vulnerable relation is not a corrupt section table; it is a valid versioned symbol whose version string is too long for readelf's temporary formatting buffer.
