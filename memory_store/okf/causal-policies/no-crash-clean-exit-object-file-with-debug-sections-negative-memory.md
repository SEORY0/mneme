---
type: causal-policy
title: "No Crash Clean Exit Object File With Debug Sections Negative Memory"
description: "Round 9 negative memory for no_crash with verifier signal clean_exit."
failure_class: "no_crash"
verifier_signal: "clean_exit"
candidate_family: "construct"
input_format: "object-file-with-debug-sections"
harness_convention: "libfuzzer"
vuln_class: "unintended-debug-section-processing"
access_scope: generate
success_count: 0
confidence: medium
tags: ["no-crash", "clean-exit", "object-file-with-debug-sections", "negative-memory", "round-9"]
match_keys: ["no_crash", "clean_exit", "object-file-with-debug-sections", "libfuzzer", "unintended-debug-section-processing", "negative_memory"]
allowed_scopes: [generate]
forbidden_fields: [raw_poc_bytes, task_id, exact_offset, checksum, submit_metadata]
evidence_level: medium
train_only: true
round: 9
---
# No Crash Clean Exit Object File With Debug Sections Negative Memory

- key: `no_crash x clean_exit`
- outcome: persistent failure / basin to avoid
- success_count: 0
- failure_count: 1
- related format facts: [[object-file-with-debug-sections]]
- related harness facts: [[libfuzzer]]

## Failure Shape
- ELF-like and debug-section-name candidates were consumed by the fuzz_dwarf runner but did not
  become valid objects with loadable debug sections, so load_debug_section was not driven into the
  unwanted processing path.

## Policy
Treat `no_crash x clean_exit` on `object-file-with-debug-sections` as a basin to avoid unless a new candidate changes the parser gate, state relation, or official target sink. Preserve any proven reachability, but reject variants that return to the same verifier signal without changing the causal gate under test.

## Procedure
1. Keep only the smallest parser or harness envelope that the verifier proved was reached.
2. Identify the missing causal relation from the signal: parser selection, container acceptance, length relation, stateful subobject, allocation state, or official target sink.
3. Change one relation at a time and discard candidates that return to the same clean-exit, off-target-crash, wrong-sink, usage-only, or both-image-crash basin.
4. If a local crash is not an official target match, shrink or discard it before mutating deeper fields.
5. Promote a recovery from this basin only after a later verifier-confirmed target match.

## Format Contract
- The target requires an object file accepted by BFD as a real object, with separate or embedded
  debug-section metadata that can be discovered by the debug-loading routines even when the dump
  mode does not request debug output.

## Harness Contract
- The fuzzer writes raw bytes to a temporary file, opens that file through BFD, checks object format
  acceptance, and only then calls the separate-debug-file loading path.

## Negative Memory
- Do not resubmit broad mutations that only reproduce `clean_exit`.
- Do not count parser reachability, both-image crashes, local wrapper crashes, clean exits, or fixed-image crashes as success.
- Do not store raw payload bytes, exact positions, task identifiers, or submit metadata.

## Evidence Shape
- Support: one diagnosed persistent failure from round 9.
- Scope: generator repair and basin avoidance only.
