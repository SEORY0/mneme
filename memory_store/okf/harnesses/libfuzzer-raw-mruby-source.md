---
type: harness
title: "Libfuzzer Raw Mruby Source"
access_scope: generate
confidence: medium
tags: ["libfuzzer-raw-mruby-source", "harness", "round-13"]
forbidden_fields: [raw_poc_bytes, task_id, exact_offset, checksum, submit_metadata]
train_only: true
okf_support: 1
---
# Libfuzzer Raw Mruby Source

## Round 13 Facts
- The fuzzer passes the whole file as mruby source to the mruby_fuzzer target. There is no leading selector, checksum, filename envelope, or FuzzedDataProvider carving. Syntax must compile far enough for the VM to execute the literal load path.

## Round 18 Input Contract

### Schema / Invariants
- The harness copies the raw input bytes into a NUL-terminated source string, creates an mruby VM, loads the string, and closes the VM. There is no mode selector, file header, or FuzzedDataProvider layout.

### Format Links
- [[mruby-source]]

### Notes
- These are descriptive format and harness observations only; they carry no success-rate claim.

## Round 25 Input Contract
- The fuzzer copies raw bytes into a NUL-terminated string, opens an mruby interpreter, loads the string as source code, closes the interpreter, and frees the copied source.

## Round 25 Format Links
- [[mruby-source]]

## Round 25 Notes
- These facts are descriptive harness-carving observations only; they are not causal recovery claims.
