---
type: negative-memory
title: "Generic Crash Wrapper Crash Not Official Pdf Negative Memory"
description: "Round 22 negative memory for generic_crash with verifier signal wrapper_crash_not_official."
failure_class: "generic_crash"
verifier_signal: "wrapper_crash_not_official"
candidate_family: "construct"
input_format: "pdf"
harness_convention: "libfuzzer"
vuln_class: "use-of-uninitialized-value"
access_scope: generate
success_count: 0
confidence: medium
tags: ["generic-crash", "wrapper-crash-not-official", "pdf", "libfuzzer", "construct", "negative-memory", "round-22"]
match_keys: ["generic-crash", "wrapper-crash-not-official", "pdf", "libfuzzer", "use-of-uninitialized-value"]
allowed_scopes: [generate]
forbidden_fields: [raw_poc_bytes, task_id, exact_offset, checksum, submit_metadata]
evidence_level: medium
train_only: true
round: 22
---
# Generic Crash Wrapper Crash Not Official Pdf Negative Memory

- key: `generic_crash x wrapper_crash_not_official`
- outcome: persistent failure / basin to avoid
- success_count: 0
- failure_count: 1
- related format facts: [[pdf]]
- harnesses: [[libfuzzer]]

## Failure Shape
A minimal renderable PDF and a valid image-mask PDF both caused only a low-detail local wrapper segfault, while official submission showed the vulnerable build exiting cleanly. The constructed image-mask document targeted Splash mask scaling with an upscaled one-bit mask, but it did not reproduce the described scaleMaskYuXu error-handling bug in the official environment.

## Policy
Treat `generic_crash x wrapper_crash_not_official` on `pdf` as negative memory for the attempted carrier. Preserve only reachability that was actually observed, then retarget the missing parser gate, feature selector, length relation, stateful subobject, or official sink before spending more verification attempts.

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
