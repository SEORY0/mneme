---
type: causal-policy
title: "No Crash Ucasemap Titlecase Clean Exit Icu Ucasemap Fuzzer Bytes Negative Memory"
description: "Round 6 negative memory for no_crash with verifier signal ucasemap_titlecase_clean_exit."
failure_class: "no_crash"
verifier_signal: "ucasemap_titlecase_clean_exit"
candidate_family: "raw_headered_utf8_dutch_ij_sequences"
input_format: "icu-ucasemap-fuzzer-bytes"
harness_convention: "libfuzzer ucasemap_fuzzer"
vuln_class: "buffer-overflow"
access_scope: generate
success_count: 0
confidence: medium
tags: ["no-crash", "ucasemap-titlecase-clean-exit", "icu-ucasemap-fuzzer-bytes", "negative-memory", "round-6"]
match_keys: ["no_crash", "ucasemap_titlecase_clean_exit", "icu-ucasemap-fuzzer-bytes", "libfuzzer ucasemap_fuzzer", "negative_memory"]
allowed_scopes: [generate]
forbidden_fields: [raw_poc_bytes, task_id, exact_offset, checksum, submit_metadata]
evidence_level: medium
train_only: true
round: 6
---
# No Crash Ucasemap Titlecase Clean Exit Icu Ucasemap Fuzzer Bytes Negative Memory

- key: `no_crash x ucasemap_titlecase_clean_exit`
- outcome: persistent failure / basin to avoid
- success_count: 0
- failure_count: 1
- related format facts: [[icu-ucasemap-fuzzer-bytes]]

## Failure Shape
- Inputs selected the titlecase operation and stressed Dutch IJ/lowercase-ligature sequences, long runs, and a partial trailing UTF-8 sequence, but all executed cleanly. The missing ingredient is likely the exact locale selector/options combination or segment-boundary condition that makes Dutch IJ titlecase adjustment overrun the destination.

## Policy
Treat `no_crash x ucasemap_titlecase_clean_exit` on this format family as negative memory for the attempted carrier. Preserve only verifier-proven reachability, then retarget the missing gate or sink-specific state instead of resubmitting candidates with the same signal.

## Procedure
1. Keep any parser or harness envelope that the verifier proved was reached.
2. Identify the missing causal relation from the signal: parser selection, feature gate, length relation, stateful subobject, or official target sink.
3. Change one relation at a time and reject variants that return to the same clean-exit, off-target-crash, wrong-sink, usage-only, or nonreproducible basin.
4. If a local crash is not an official target match, shrink or discard it before mutating deeper fields.
5. Promote a recovery from this basin only after a later verifier-confirmed target match.

## Negative Memory
- Do not treat local generic crashes, wrapper usage paths, clean parser exits, or wrong-sink labels as success.
- Do not broaden random mutation after reachability is known; move to the smallest missing format contract.
- Do not submit another candidate with this exact failure signal unless the candidate changes the causal gate being tested.
- Do not store raw payload bytes, exact offsets, checksums, or task-local identifiers.

## Evidence Shape
- Support: 1 diagnosed persistent failure(s) from round 6.
- Scope: generator repair and basin avoidance only.
