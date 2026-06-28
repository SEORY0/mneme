---
type: causal-policy
title: "No Crash Clean Exit Mmo Object Negative Memory"
description: "Round 9 negative memory for no_crash with verifier signal clean_exit."
failure_class: "no_crash"
verifier_signal: "clean_exit"
candidate_family: "construct"
input_format: "mmo-object"
harness_convention: "honggfuzz-file"
vuln_class: "heap-buffer-overflow-read"
access_scope: generate
success_count: 0
confidence: medium
tags: ["no-crash", "clean-exit", "mmo-object", "negative-memory", "round-9"]
match_keys: ["no_crash", "clean_exit", "mmo-object", "honggfuzz-file", "heap-buffer-overflow-read", "negative_memory"]
allowed_scopes: [generate]
forbidden_fields: [raw_poc_bytes, task_id, exact_offset, checksum, submit_metadata]
evidence_level: medium
train_only: true
round: 9
---
# No Crash Clean Exit Mmo Object Negative Memory

- key: `no_crash x clean_exit`
- outcome: persistent failure / basin to avoid
- success_count: 0
- failure_count: 1
- related format facts: [[mmo-object]]
- related harness facts: [[honggfuzz-file]]

## Failure Shape
- Constructed MMO files exercised valid preamble/end framing, high-address location records, and
  special-section descriptors, but the runner exited cleanly.
- The candidates did not create the exact chunk-list relation where an address-plus-size calculation
  wraps and a later chunk lookup returns an out-of-bounds pointer.

## Policy
Treat `no_crash x clean_exit` on `mmo-object` as a basin to avoid unless a new candidate changes the parser gate, state relation, or official target sink. Preserve any proven reachability, but reject variants that return to the same verifier signal without changing the causal gate under test.

## Procedure
1. Keep only the smallest parser or harness envelope that the verifier proved was reached.
2. Identify the missing causal relation from the signal: parser selection, container acceptance, length relation, stateful subobject, allocation state, or official target sink.
3. Change one relation at a time and discard candidates that return to the same clean-exit, off-target-crash, wrong-sink, usage-only, or both-image-crash basin.
4. If a local crash is not an official target match, shrink or discard it before mutating deeper fields.
5. Promote a recovery from this basin only after a later verifier-confirmed target match.

## Format Contract
- MMO files are word-aligned record streams with a preamble, location records, optional special-
  section descriptors, data words, symbol-table marker, and final end record.
- The vulnerable allocator stores section-content chunks by virtual address and checks whether
  requested ranges fit existing chunks using address plus size arithmetic.

## Harness Contract
- The fuzzer writes the submitted bytes to a temporary file, opens it with BFD, accepts only
  recognized object files, and then calls the dwarf separate-debug-file path.
- In this image the wrapper accepts a file path but does not report parser reachability beyond clean
  execution.

## Negative Memory
- Do not resubmit broad mutations that only reproduce `clean_exit`.
- Do not count parser reachability, both-image crashes, local wrapper crashes, clean exits, or fixed-image crashes as success.
- Do not store raw payload bytes, exact positions, task identifiers, or submit metadata.

## Evidence Shape
- Support: one diagnosed persistent failure from round 9.
- Scope: generator repair and basin avoidance only.
