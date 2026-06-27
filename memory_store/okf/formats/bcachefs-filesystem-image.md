---
type: format
title: "Bcachefs Filesystem Image"
input_format: bcachefs-filesystem-image
access_scope: generate
forbidden_fields: [raw_poc_bytes, task_id, exact_offset, checksum, submit_metadata]
---
# Bcachefs Filesystem Image

## Schema
- The bcachefs probe looks for bcache/bcachefs magic at the filesystem superblock location, validates a superblock offset field, checks device index versus device count, computes the superblock size from a u64-count field, and walks typed superblock fields. Members fields contain an array of device records used for UUID and size calculation.
