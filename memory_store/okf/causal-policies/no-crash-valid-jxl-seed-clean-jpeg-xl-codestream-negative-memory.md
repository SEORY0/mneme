---
type: negative-memory
title: "No Crash Valid Jxl Seed Clean JPEG Xl Codestream Negative Memory"
description: "Round 19 negative memory for no_crash with verifier signal valid_jxl_seed_clean."
failure_class: "no_crash"
verifier_signal: "valid_jxl_seed_clean"
candidate_family: "seed_replay"
input_format: "jpeg-xl-codestream"
harness_convention: "libfuzzer"
vuln_class: "use-of-uninitialized-memory"
access_scope: generate
success_count: 0
confidence: medium
tags: ["no-crash", "valid-jxl-seed-clean", "jpeg-xl-codestream", "libfuzzer", "seed-replay", "negative-memory", "round-19"]
match_keys: ["no-crash", "valid-jxl-seed-clean", "jpeg-xl-codestream", "libfuzzer", "use-of-uninitialized-memory"]
allowed_scopes: [generate]
forbidden_fields: [raw_poc_bytes, task_id, exact_offset, checksum, submit_metadata]
evidence_level: medium
train_only: true
round: 19
---
# No Crash Valid Jxl Seed Clean JPEG Xl Codestream Negative Memory

- key: `no_crash x valid_jxl_seed_clean`
- outcome: persistent failure / basin to avoid
- success_count: 0
- failure_count: 1
- related format facts: [[jpeg-xl-codestream]]
- harnesses: [[libfuzzer]]

## Failure Shape
A real in-repo JXL seed reached the decoder harness cleanly. The missing condition is enabling the noise decoding feature and SIMD lane state that exposes the poison/unpoison mismatch; ordinary image decode is insufficient.

## Policy
Treat `no_crash x valid_jxl_seed_clean` on `jpeg-xl-codestream` as negative memory for the attempted carrier. Preserve only the reachability that was actually observed, then retarget the missing gate or sink-specific state before spending more verification attempts.

## Procedure
1. Keep any parser or harness envelope that the verifier proved was reached.
2. Identify the missing causal relation from the signal: parser selection, feature gate, length relation, stateful subobject, or official target sink.
3. Change one relation at a time and reject variants that return to this same clean-exit, off-target, usage-only, or nonreproducible basin.
4. Promote a recovery from this basin only after a later server-confirmed target match.

## Negative Memory
- Do not resubmit another candidate with this exact failure signal unless it changes the causal gate being tested.
- Do not broaden random mutation after reachability is known; move to the smallest missing format or state contract.
- Do not treat local generic crashes, wrapper usage paths, clean parser exits, or wrong-sink labels as success.
- Never store raw payload bytes, exact offsets, checksums, or task-local identifiers in memory.

## Evidence Shape
- Support: 1 diagnosed persistent failure from round 19.
- Scope: generator repair and basin avoidance only.
