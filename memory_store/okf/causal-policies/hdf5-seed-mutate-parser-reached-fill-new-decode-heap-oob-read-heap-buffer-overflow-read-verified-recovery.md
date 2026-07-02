---
type: causal-policy
title: "Hdf5 Seed Mutate Parser Reached Fill New Decode Heap Oob Read Heap Buffer Overflow Read Verified Recovery"
description: "Round 28 verified recovery for generic_crash with verifier signal parser_reached_fill_new_decode_heap_oob_read."
failure_class: "generic_crash"
verifier_signal: "parser_reached_fill_new_decode_heap_oob_read"
candidate_family: "seed_mutate"
input_format: "hdf5"
harness_convention: "libfuzzer-aflpp-file-h5-extended"
vuln_class: "heap-buffer-overflow-read"
access_scope: generate
success_count: 1
confidence: high
tags: ["generic-crash", "parser-reached-fill-new-decode-heap-oob-read", "hdf5", "libfuzzer-aflpp-file-h5-extended", "seed-mutate", "heap-buffer-overflow-read", "verified-recovery", "round-28"]
match_keys: ["generic_crash", "parser_reached_fill_new_decode_heap_oob_read", "hdf5", "libfuzzer-aflpp-file-h5-extended", "heap-buffer-overflow-read", "verified_recovery", "seed-mutate", "heap-buffer-overflow-read"]
allowed_scopes: [generate]
forbidden_fields: [raw_poc_bytes, task_id, exact_offset, checksum, submit_metadata]
evidence_level: high
train_only: true
round: 28
---
# Hdf5 Seed Mutate Parser Reached Fill New Decode Heap Oob Read Heap Buffer Overflow Read Verified Recovery

## Policy
For `generic_crash x parser_reached_fill_new_decode_heap_oob_read`, preserve the format and harness gates that reached the parser or sink, then apply the verified causal relation below. This is a positive recovery policy because the official vulnerable/fixed verifier recorded a target match.

## Procedure
1. Start from a valid old-style HDF5 seed that already has dataset object headers with fill-new messages. Make one dataset reachable under the harness's fixed lookup by updating the local-heap string allocation, symbol-table entry, and B-tree separator consistently. Then mutate that dataset's fill-new object-header message into the later layout with the have-value flag set and a declared fill payload larger than the message body. Preserve the HDF5 superblock, local heap free-list validity, root symbol-table ordering, and object-header framing so the dataset open reaches the decoder before the oversized fill copy.
2. Keep the carrier abstract: preserve the gate, invariant, and sink relation rather than task-local bytes, exact offsets, checksums, or identifiers.
3. If the verifier signal changes, re-rank against the new failure key before mutating unrelated fields.

## Format Contract
- Format [[hdf5]]: Old-style HDF5 files can store root group links in a local heap plus v1 symbol-table node behind a v1 B-tree. Symbol-table entries carry a heap-name reference and a link to the target object header, while the B-tree key range also stores heap-name references used to decide whether lookup enters the leaf. Dataset object headers contain typed messages with a small type, size, flags header followed by aligned raw message bodies. The fill-new message has version-dependent layouts; the later layout uses a flags byte, and the have-value flag causes a fill-size field followed by fill bytes.
- Harness [[libfuzzer-aflpp-file-h5-extended]]: The harness writes the fuzz input bytes directly to a temporary file and calls the extended HDF5 fuzzer entry point. There is no leading selector byte and no FuzzedDataProvider carving. After opening the file read-write, it attempts to open one fixed dataset name and then one fixed attribute name, so object-header bugs in datasets require the root group lookup metadata to resolve that fixed dataset name.

## Negative Memory
- Do not broaden mutations after parser or harness reachability is proven.
- Do not submit candidates that reproduce on the fixed image, crash both images, or move to an off-target wrapper crash.
- Do not store payload bytes, exact offsets, checksums, or task-local identifiers.

## Evidence Shape
- Support: one round-28 worker trace with official target match.
- Scope: generator repair for the same failure-keyed basin; pair with [[hdf5]] and [[libfuzzer-aflpp-file-h5-extended]].
