---
type: negative-memory
title: "Generic Crash Generic Non Target Rawspeed Cr2 Decompressor Envelope Construct Uninitialized Memory Read Negative Memory"
description: "Round 23 negative memory for generic_crash with verifier signal generic_non_target."
failure_class: "generic_crash"
verifier_signal: "generic_non_target"
candidate_family: "construct"
input_format: "rawspeed-cr2-decompressor-envelope"
harness_convention: "libfuzzer-rawspeed-cr2-decompressor"
vuln_class: "uninitialized-memory-read"
access_scope: generate
success_count: 0
confidence: medium
tags: ["generic-crash", "generic-non-target", "rawspeed-cr2-decompressor-envelope", "libfuzzer-rawspeed-cr2-decompressor", "construct", "negative-memory", "round-23"]
match_keys: ["generic-crash", "generic-non-target", "rawspeed-cr2-decompressor-envelope", "libfuzzer-rawspeed-cr2-decompressor", "uninitialized-memory-read"]
allowed_scopes: [generate]
forbidden_fields: [raw_poc_bytes, task_id, exact_offset, checksum, submit_metadata]
evidence_level: medium
train_only: true
round: 23
---
# Generic Crash Generic Non Target Rawspeed Cr2 Decompressor Envelope Construct Uninitialized Memory Read Negative Memory

- key: `generic_crash x generic_non_target`
- outcome: persistent failure / basin to avoid
- success_count: 0
- failure_count: 1
- related format facts: [[rawspeed-cr2-decompressor-envelope]]
- harnesses: [[libfuzzer-rawspeed-cr2-decompressor]]

## Failure Shape
A synthetic RawSpeed CR2 decompressor envelope with minimal lossless-JPEG scan data produced a local generic crash for one component/slice combination, but it did not reproduce as an official vulnerable-image failure. Other envelopes passed or returned cleanly, indicating the compressed scan and slice geometry did not reliably reach the intended insufficient-slice uninitialized-pixel check.

## Policy
Treat `generic_crash x generic_non_target` on `rawspeed-cr2-decompressor-envelope` as negative memory for the attempted carrier. Preserve only reachability that was actually observed, then retarget the missing gate, harness contract, or sink-specific state before spending more verification attempts.

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
- Support: 1 diagnosed persistent failure from round 23 after 5 attempts.
- Scope: generator repair and basin avoidance only.
