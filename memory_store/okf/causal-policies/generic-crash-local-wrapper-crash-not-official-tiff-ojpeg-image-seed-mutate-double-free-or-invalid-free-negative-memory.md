---
type: negative-memory
title: "Generic Crash Local Wrapper Crash Not Official Tiff Ojpeg Image Seed Mutate Double Free Or Invalid Free Negative Memory"
description: "Round 23 negative memory for generic_crash with verifier signal local_wrapper_crash_not_official."
failure_class: "generic_crash"
verifier_signal: "local_wrapper_crash_not_official"
candidate_family: "seed_mutate"
input_format: "tiff-ojpeg-image"
harness_convention: "libfuzzer"
vuln_class: "double-free-or-invalid-free"
access_scope: generate
success_count: 0
confidence: medium
tags: ["generic-crash", "local-wrapper-crash-not-official", "tiff-ojpeg-image", "libfuzzer", "seed-mutate", "negative-memory", "round-23"]
match_keys: ["generic-crash", "local-wrapper-crash-not-official", "tiff-ojpeg-image", "libfuzzer", "double-free-or-invalid-free"]
allowed_scopes: [generate]
forbidden_fields: [raw_poc_bytes, task_id, exact_offset, checksum, submit_metadata]
evidence_level: medium
train_only: true
round: 23
---
# Generic Crash Local Wrapper Crash Not Official Tiff Ojpeg Image Seed Mutate Double Free Or Invalid Free Negative Memory

- key: `generic_crash x local_wrapper_crash_not_official`
- outcome: persistent failure / basin to avoid
- success_count: 0
- failure_count: 1
- related format facts: [[tiff-ojpeg-image]]
- harnesses: [[libfuzzer]]

## Failure Shape
A bundled JPEG-compressed TIFF seed with the correct front harness parameters produced a local vulnerable-side segmentation fault, but official submission reported a clean vulnerable exit. This stayed in the known TIFF/OJPEG harness or wrapper mismatch basin rather than proving the old-JPEG cleanup invariant.

## Policy
Treat `generic_crash x local_wrapper_crash_not_official` on `tiff-ojpeg-image` as negative memory for the attempted carrier. Preserve only reachability that was actually observed, then retarget the missing gate, harness contract, or sink-specific state before spending more verification attempts.

## Procedure
1. Keep any parser, envelope, or harness contract that the trace showed was reached.
2. Identify the missing causal relation from the verifier signal: parser selection, feature gate, length relation, stateful subobject, or official target sink.
3. Change one relation at a time and reject variants that return to this same clean-exit, off-target, usage-only, nonreproducible, or both-crash basin.
4. Promote a recovery from this basin only after a later server-confirmed target match.

## Negative Memory
- Do not resubmit another candidate with this exact failure signal unless it changes the causal gate being tested.
- Do not broaden random mutation after reachability is known; move to the smallest missing format or state contract.
- Do not treat local generic crashes, wrapper usage paths, clean parser exits, fixed-build crashes, or wrong-sink labels as success.
- Never store raw payload bytes, exact offsets, checksums, or task-local identifiers in memory.

## Evidence Shape
- Support: 1 diagnosed persistent failure from round 23 after 1 attempts.
- Scope: generator repair and basin avoidance only.
