---
type: negative-memory
title: "Generic Crash Wrapper Crash Not Official Jpeg Dct Fuzzer Raw Negative Memory"
description: "Round 22 negative memory for generic_crash with verifier signal wrapper_crash_not_official."
failure_class: "generic_crash"
verifier_signal: "wrapper_crash_not_official"
candidate_family: "seed_replay"
input_format: "jpeg-dct-fuzzer-raw"
harness_convention: "libfuzzer"
vuln_class: "use-of-uninitialized-value"
access_scope: generate
success_count: 0
confidence: medium
tags: ["generic-crash", "wrapper-crash-not-official", "jpeg-dct-fuzzer-raw", "libfuzzer", "seed-replay", "negative-memory", "round-22"]
match_keys: ["generic-crash", "wrapper-crash-not-official", "jpeg-dct-fuzzer-raw", "libfuzzer", "use-of-uninitialized-value"]
allowed_scopes: [generate]
forbidden_fields: [raw_poc_bytes, task_id, exact_offset, checksum, submit_metadata]
evidence_level: medium
train_only: true
round: 22
---
# Generic Crash Wrapper Crash Not Official Jpeg Dct Fuzzer Raw Negative Memory

- key: `generic_crash x wrapper_crash_not_official`
- outcome: persistent failure / basin to avoid
- success_count: 0
- failure_count: 1
- related format facts: [[jpeg-dct-fuzzer-raw]]
- harnesses: [[libfuzzer]]

## Failure Shape
The task description names a JPEG decompression smoothing path, but the executed wrapper runs a DCT fuzzer. JPEG files, BMP files, a minimal marker-like raw input, a raw block-pattern input, and the bundled seed-corpus archive did not produce an official vulnerable crash. The only local generic crash did not reproduce on the official vulnerable build.

## Policy
Treat `generic_crash x wrapper_crash_not_official` on `jpeg-dct-fuzzer-raw` as negative memory for the attempted carrier. Preserve only reachability that was actually observed, then retarget the missing parser gate, feature selector, length relation, stateful subobject, or official sink before spending more verification attempts.

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
