---
type: causal-policy
title: "MNG Construct Local Classifier Missed Fuzz Target Exit Fatal Error After Unsupported MNG Magnification Method Verified Recovery"
description: "Round 16 verified recovery for no_crash with verifier signal local_classifier_missed_fuzz_target_exit."
failure_class: "no_crash"
verifier_signal: "local_classifier_missed_fuzz_target_exit"
candidate_family: "construct"
input_format: "mng"
harness_convention: "libfuzzer"
vuln_class: "fatal-error after unsupported MNG magnification method"
access_scope: generate
success_count: 1
confidence: high
tags: ["no-crash", "local-classifier-missed-fuzz-target-exit", "mng", "construct", "verified-recovery", "round-16"]
match_keys: ["no_crash", "local_classifier_missed_fuzz_target_exit", "mng", "libfuzzer", "fatal-error after unsupported MNG magnification method", "verified_recovery"]
allowed_scopes: [generate]
forbidden_fields: [raw_poc_bytes, task_id, exact_offset, checksum, submit_metadata]
evidence_level: high
train_only: true
round: 16
---
# MNG Construct Local Classifier Missed Fuzz Target Exit Fatal Error After Unsupported MNG Magnification Method Verified Recovery

## Policy
For `no_crash x local_classifier_missed_fuzz_target_exit`, preserve the format and harness gates that reached the parser/sink, then apply the verified causal relation below. This is a positive recovery policy because the official vulnerable/fixed verifier recorded a target match.

## Procedure
- Build a minimal MNG stream with valid PNG-style chunk framing, an initial image header, and a magnification control chunk for the default object. Use unsupported magnification method values while keeping the factors and embedded tiny image coherent, so the vulnerable reader only warns and later exercises the magnification path; the fixed reader rejects the unsupported method cleanly.
- Keep the carrier abstract: preserve the gate/invariant relation, not any task-local bytes or offsets.
- If a later candidate changes the verifier signal, re-rank against the new failure key before mutating unrelated fields.

## Format Contract
- MNG uses a distinct stream signature followed by PNG-style chunks with lengths and CRCs. MHDR establishes the animation canvas, control chunks such as MAGN can precede image chunks, and a tiny embedded PNG-like image can be closed before the final MNG terminator.
- Harness: The GraphicsMagick coder fuzzer feeds the raw input bytes as a Magick blob to the MNG reader. There is no leading mode byte, container wrapper, or FuzzedDataProvider carving.

## Negative Memory
- Do not broaden mutations after the parser/harness gate is proven.
- Do not submit candidates that reproduce on the fixed image or move to an off-target wrapper crash.
- Do not store raw payload bytes, exact offsets, checksums, or task-local identifiers.

## Evidence Shape
- Support: one round-16 worker trace with official target match.
- Scope: generator repair for the same failure-keyed basin.
