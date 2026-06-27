---
type: format
title: "Opensc Pkcs15init Profile Plus Virtual Reader Stream"
input_format: opensc-pkcs15init-profile-plus-virtual-reader-stream
access_scope: generate
forbidden_fields: [raw_poc_bytes, task_id, exact_offset, checksum, submit_metadata]
---
# Opensc Pkcs15init Profile Plus Virtual Reader Stream

## Schema
- OpenSC virtual-reader fuzz inputs are synthetic smart-card transcripts. Reader chunks are length-prefixed; the first chunk is used as ATR/card identity data and later chunks are returned as APDU response data with trailing status words. For this bug, the semantic invariant is that SW1 indicating success must be paired with the correct SW2 before key material is consumed.
