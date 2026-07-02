---
type: causal-policy
title: "VMS Ia64 Library Archive Construct Parser Reached Target Sink Heap Buffer Overflow Write Verified Recovery"
description: "Round 27 verified recovery for generic_crash with verifier signal parser_reached_target_sink."
failure_class: "generic_crash"
verifier_signal: "parser_reached_target_sink"
candidate_family: "construct"
input_format: "vms-ia64-library-archive"
harness_convention: "libfuzzer-bfd-tempfile"
vuln_class: "heap-buffer-overflow-write"
access_scope: generate
success_count: 1
confidence: high
tags: ["generic-crash", "parser-reached-target-sink", "vms-ia64-library-archive", "libfuzzer-bfd-tempfile", "construct", "heap-buffer-overflow-write", "verified-recovery", "round-27"]
match_keys: ["generic_crash", "parser_reached_target_sink", "vms-ia64-library-archive", "libfuzzer-bfd-tempfile", "heap-buffer-overflow-write", "verified_recovery"]
allowed_scopes: [generate]
forbidden_fields: [raw_poc_bytes, task_id, exact_offset, checksum, submit_metadata]
evidence_level: high
train_only: true
round: 27
---
# VMS Ia64 Library Archive Construct Parser Reached Target Sink Heap Buffer Overflow Write Verified Recovery

## Policy
For `generic_crash x parser_reached_target_sink`, preserve the format and harness gates that reached the parser or sink, then apply the verified causal relation below. This is a positive recovery policy because the official vulnerable/fixed verifier recorded a target match.

## Procedure
1. Construct a BFD-recognized IA-64 VMS library with a valid library header and coherent index descriptors.
2. Keep the module index self-consistent, make the symbol index use the list-reference path, and provide a finite list that crosses the first dynamic table reallocation boundary by the smallest useful margin before terminating.
3. This reaches the VMS index-add path with archive gates satisfied and triggers the vulnerable reallocation-size mismatch while the fixed build handles the growth cleanly.
4. Keep the carrier abstract: preserve the gate/invariant relation, not any task-local bytes or offsets.
5. If a later candidate changes the verifier signal, re-rank against the new failure key before mutating unrelated fields.

## Format Contract
- A VMS IA-64 library archive is block-oriented.
- The first block carries a library header, sanity and version fields, a type field, index counts, and index descriptors.
- Index blocks carry used-byte counts followed by IA-64 index records with an RFA, key length, flags, and key bytes.
- Harness [[libfuzzer-bfd-tempfile]]:
  - libFuzzer supplies raw bytes.
  - The harness writes them unchanged to a temporary file, opens that file through BFD auto-detection, and asks BFD to check archive format.
  - There is no selector byte and no FuzzedDataProvider carving.

## Negative Memory
- Do not broaden mutations after the parser or harness gate is proven.
- Do not submit candidates that reproduce on the fixed image or move to an off-target wrapper crash.
- Do not store payload bytes, exact offsets, checksums, or task-local identifiers.

## Evidence Shape
- Support: one round-27 worker trace with official target match.
- Scope: generator repair for the same failure-keyed basin; pair with [[vms-ia64-library-archive]] and [[libfuzzer-bfd-tempfile]].
