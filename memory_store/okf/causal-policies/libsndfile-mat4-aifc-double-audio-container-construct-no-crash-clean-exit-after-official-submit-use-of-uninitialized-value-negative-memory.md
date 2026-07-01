---
type: negative-memory
title: "Libsndfile Mat4 Aifc Double Audio Container Construct No Crash Clean Exit After Official Submit Use Of Uninitialized Value Negative Memory"
description: "Round 36 negative memory for no_crash with verifier signal clean_exit_after_official_submit."
failure_class: "no_crash"
verifier_signal: "clean_exit_after_official_submit"
candidate_family: "construct"
input_format: "libsndfile MAT4/AIFC double audio container"
harness_convention: "libfuzzer"
vuln_class: "use-of-uninitialized-value"
access_scope: generate
success_count: 0
failure_count: 1
confidence: medium
tags: ["no-crash", "clean-exit-after-official-submit", "libsndfile-mat4-aifc-double-audio-container", "libfuzzer", "construct", "use-of-uninitialized-value", "negative-memory", "round-36"]
match_keys: ["no_crash", "clean_exit_after_official_submit", "libsndfile MAT4/AIFC double audio container", "libfuzzer", "use-of-uninitialized-value", "no-crash", "clean-exit-after-official-submit", "libsndfile-mat4-aifc-double-audio-container", "negative_memory", "construct"]
allowed_scopes: [generate]
forbidden_fields: [raw_poc_bytes, task_id, exact_offset, checksum, submit_metadata]
evidence_level: medium
train_only: true
round: 36
---
# Libsndfile Mat4 Aifc Double Audio Container Construct No Crash Clean Exit After Official Submit Use Of Uninitialized Value Negative Memory

- key: `no_crash x clean_exit_after_official_submit`
- outcome: persistent failure / basin to avoid
- success_count: 0
- failure_count: 1
- related format facts: [[libsndfile-mat4-aifc-double-audio-container]]
- related harness facts: [[libfuzzer]]

## Failure Shape
Constructed big-endian double audio containers reached recognizable libsndfile envelope logic, but the standard double initializer recomputed frame count from actual virtual-file data length before the harness read loop. Short or partial sample regions therefore either left no readable frame, consumed fully initialized trailing bytes, or produced low-confidence off-target/transient signals that did not reproduce as a target match under submit.

## Observed Basin
- Failure trajectory classes: no_crash, generic_crash, submit_target_miss.
- Official confirmation: no server target match for this basin.

## Policy
Treat `no_crash x clean_exit_after_official_submit` on `libsndfile MAT4/AIFC double audio container` under `libfuzzer` as a basin to avoid unless a new candidate changes the parser gate, state relation, or sink relation described above. Preserve any proven reachability, but reject variants that return to the same clean-exit, off-target-crash, wrapper-mismatch, usage-only, or fixed-image-crash behavior.

## Procedure
1. Keep only the smallest parser or harness envelope that was actually reached.
2. Identify the missing relation from the signal: parser selection, container acceptance, length relation, stateful subobject, allocation state, or official target sink.
3. Change one relation at a time and discard candidates that return to the same `clean_exit_after_official_submit` basin.
4. Promote a recovery from this basin only after a later official target match.

## Negative Memory
- Do not resubmit broad mutations that only reproduce `clean_exit_after_official_submit`.
- Do not count parser reachability, both-image crashes, local wrapper crashes, clean exits, or fixed-image crashes as success.
- Do not store payload bytes, exact positions, task identifiers, checksums, or submit metadata.

## Evidence Shape
- Support: 1 diagnosed persistent failure from round 36 after 12 attempts.
- Scope: generator repair and basin avoidance only.
