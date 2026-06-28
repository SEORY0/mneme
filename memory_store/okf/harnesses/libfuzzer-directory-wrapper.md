---
type: harness
title: "Libfuzzer Directory Wrapper"
access_scope: generate
confidence: medium
tags: ["libfuzzer-directory-wrapper", "harness", "round-13"]
forbidden_fields: [raw_poc_bytes, task_id, exact_offset, checksum, submit_metadata]
train_only: true
---
# Libfuzzer Directory Wrapper

## Round 13 Facts
- The container's /bin/arvo invokes the blkid libFuzzer target with a fixed /tmp/poc path as a corpus directory rather than passing a single input file. When /tmp/poc is a regular file, the target exits with a required-directory message before processing the constructed bytes.

## Round 23 Input Contract
- The harness scans the raw input for a separator, copies the suffix as a null-terminated serialized string, initializes a PHP request, calls php_var_unserialize, and only if the result is a HashContext object calls hash_update followed by hash_final before destructing the result.

## Round 23 Format Links
- [[php-hashcontext-unserialize]]

## Round 23 Notes
- These are descriptive harness-carving facts only; they carry no success-rate claim.
