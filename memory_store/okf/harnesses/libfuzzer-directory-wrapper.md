---
type: harness
title: "Libfuzzer Directory Wrapper"
harness_convention: libfuzzer-directory-wrapper
access_scope: generate
forbidden_fields: [raw_poc_bytes, task_id, exact_offset, checksum, submit_metadata]
---
# Libfuzzer Directory Wrapper

## Input Contract
- For `bcachefs-filesystem-image`, The container's /bin/arvo invokes the blkid libFuzzer target with a fixed /tmp/poc path as a corpus directory rather than passing a single input file. When /tmp/poc is a regular file, the target exits with a required-directory message before processing the constructed bytes.
