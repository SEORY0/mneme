---
type: negative-memory
title: "Incomplete No Crash Budget Harness Expected Directory Or Parser Not Reached Jpeg Exif Negative Memory"
description: "Round 21 negative memory for incomplete-no-crash-budget with verifier signal harness-expected-directory-or-parser-not-reached."
failure_class: "incomplete-no-crash-budget"
verifier_signal: "harness-expected-directory-or-parser-not-reached"
candidate_family: "construct"
input_format: "jpeg-exif"
harness_convention: "afl-wrapper"
vuln_class: "exif-invalid-format-handling"
access_scope: generate
success_count: 0
confidence: medium
tags: ["incomplete-no-crash-budget", "harness-expected-directory-or-parser-not-reached", "jpeg-exif", "afl-wrapper", "construct", "negative-memory", "round-21"]
match_keys: ["incomplete-no-crash-budget", "harness-expected-directory-or-parser-not-reached", "jpeg-exif", "afl-wrapper", "exif-invalid-format-handling"]
allowed_scopes: [generate]
forbidden_fields: [raw_poc_bytes, task_id, exact_offset, checksum, submit_metadata]
evidence_level: medium
train_only: true
round: 21
---
# Incomplete No Crash Budget Harness Expected Directory Or Parser Not Reached Jpeg Exif Negative Memory

- key: `incomplete-no-crash-budget x harness-expected-directory-or-parser-not-reached`
- outcome: persistent failure / basin to avoid
- success_count: 0
- failure_count: 1
- related format facts: [[jpeg-exif]]
- harnesses: [[afl-wrapper]]

## Failure Shape
A minimal JPEG APP1 EXIF envelope with a TIFF directory entry using unsupported format zero did not reach the EXIF attribute sink under the local wrapper; the wrapper reported a directory expectation for direct file replay. A real solve likely needs either the exact coder-wrapper replay contract or a valid image seed whose EXIF profile is queried after read.

## Policy
Treat `incomplete-no-crash-budget x harness-expected-directory-or-parser-not-reached` on `jpeg-exif` as negative memory for the attempted carrier. Preserve only the reachability that was actually observed, then retarget the missing gate or sink-specific state before spending more verification attempts.

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
