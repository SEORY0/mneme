---
type: negative-memory
title: "No Crash Tiff Decoder Reached No Target Crash Samsung Srw Tiff Raw Negative Memory"
description: "Round 21 negative memory for no-crash with verifier signal tiff-decoder-reached-no-target-crash."
failure_class: "no-crash"
verifier_signal: "tiff-decoder-reached-no-target-crash"
candidate_family: "construct"
input_format: "samsung-srw-tiff-raw"
harness_convention: "afl-libfuzzer-wrapper"
vuln_class: "decoder-memory-safety"
access_scope: generate
success_count: 0
confidence: medium
tags: ["no-crash", "tiff-decoder-reached-no-target-crash", "samsung-srw-tiff-raw", "afl-libfuzzer-wrapper", "construct", "negative-memory", "round-21"]
match_keys: ["no-crash", "tiff-decoder-reached-no-target-crash", "samsung-srw-tiff-raw", "afl-libfuzzer-wrapper", "decoder-memory-safety"]
allowed_scopes: [generate]
forbidden_fields: [raw_poc_bytes, task_id, exact_offset, checksum, submit_metadata]
evidence_level: medium
train_only: true
round: 21
---
# No Crash Tiff Decoder Reached No Target Crash Samsung Srw Tiff Raw Negative Memory

- key: `no-crash x tiff-decoder-reached-no-target-crash`
- outcome: persistent failure / basin to avoid
- success_count: 0
- failure_count: 1
- related format facts: [[samsung-srw-tiff-raw]]
- harnesses: [[afl-libfuzzer-wrapper]]

## Failure Shape
A minimal Samsung-flavored TIFF/SRW envelope reached the SRW decoder fuzzer but did not reach a vulnerable SamsungV2 row decompression state. The missing pieces are likely valid raw image strip/tile metadata and compressed row payload shaped like a real Samsung V2 stream.

## Policy
Treat `no-crash x tiff-decoder-reached-no-target-crash` on `samsung-srw-tiff-raw` as negative memory for the attempted carrier. Preserve only the reachability that was actually observed, then retarget the missing gate or sink-specific state before spending more verification attempts.

## Procedure
1. Keep any parser or harness envelope that the verifier proved was reached.
2. Identify the missing causal relation from the signal: parser selection, feature gate, length relation, stateful subobject, or official target sink.
3. Change one relation at a time and reject variants that return to this same clean-exit, off-target, usage-only, both-crash, or nonreproducible basin.
4. Promote a recovery from this basin only after a later server-confirmed target match.

## Negative Memory
- Do not resubmit another candidate with this exact failure signal unless it changes the causal gate being tested.
- Do not broaden random mutation after reachability is known; move to the smallest missing format or state contract.
- Do not treat local generic crashes, wrapper usage paths, clean parser exits, fixed-build crashes, or wrong-sink labels as success.
- Never store raw payload bytes, exact offsets, checksums, or task-local identifiers in memory.

## Evidence Shape
- Support: 1 diagnosed persistent failure from round 21.
- Scope: generator repair and basin avoidance only.
