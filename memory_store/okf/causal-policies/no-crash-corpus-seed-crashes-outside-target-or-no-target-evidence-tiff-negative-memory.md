---
type: negative-memory
title: "No Crash Corpus Seed Crashes Outside Target Or No Target Evidence Tiff Negative Memory"
description: "Round 22 negative memory for no_crash with verifier signal corpus_seed_crashes_outside_target_or_no_target_evidence."
failure_class: "no_crash"
verifier_signal: "corpus_seed_crashes_outside_target_or_no_target_evidence"
candidate_family: "seed_probe"
input_format: "tiff"
harness_convention: "libfuzzer"
vuln_class: "uninitialized-or-wrong-class-pixel-use"
access_scope: generate
success_count: 0
confidence: medium
tags: ["no-crash", "corpus-seed-crashes-outside-target-or-no-target-evidence", "tiff", "libfuzzer", "seed-probe", "negative-memory", "round-22"]
match_keys: ["no-crash", "corpus-seed-crashes-outside-target-or-no-target-evidence", "tiff", "libfuzzer", "uninitialized-or-wrong-class-pixel-use"]
allowed_scopes: [generate]
forbidden_fields: [raw_poc_bytes, task_id, exact_offset, checksum, submit_metadata]
evidence_level: medium
train_only: true
round: 22
---
# No Crash Corpus Seed Crashes Outside Target Or No Target Evidence Tiff Negative Memory

- key: `no_crash x corpus_seed_crashes_outside_target_or_no_target_evidence`
- outcome: persistent failure / basin to avoid
- success_count: 0
- failure_count: 1
- related format facts: [[tiff]]
- harnesses: [[libfuzzer]]

## Failure Shape
In-tree TIFF samples reached the GraphicsMagick TIFF coder, but the tested palette, truecolor, tiled, stripped, matte, and high-depth samples either completed without sanitizer output or crashed generically without target evidence. No candidate isolated the libtiff RGBA-reader path with a class-mode mismatch.

## Policy
Treat `no_crash x corpus_seed_crashes_outside_target_or_no_target_evidence` on `tiff` as negative memory for the attempted carrier. Preserve only reachability that was actually observed, then retarget the missing parser gate, feature selector, length relation, stateful subobject, or official sink before spending more verification attempts.

## Procedure
1. Keep any parser or harness envelope that the verifier proved was reached.
2. Identify the missing causal relation from the signal: parser selection, feature gate, length relation, stateful subobject, or official target sink.
3. Change one relation at a time and reject variants that return to this same clean-exit, off-target, usage-only, wrapper-crash, or nonreproducible basin.
4. Promote a recovery from this basin only after a later server-confirmed target match.

## Negative Memory
- Do not resubmit another candidate with this exact failure signal unless it changes the causal gate being tested.
- Do not broaden random mutation after reachability is known; move to the smallest missing format or state contract.
- Do not treat local generic crashes, wrapper usage paths, clean parser exits, or wrong-sink labels as success.
- Never store raw payload bytes, exact offsets, checksums, or task-local identifiers in memory.

## Evidence Shape
- Support: 1 diagnosed persistent failure from round 22.
- Scope: generator repair and basin avoidance only.
