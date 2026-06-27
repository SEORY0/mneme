---
type: negative-memory
title: "No Crash Objdump Rejected Minimal Coff Coff Object Negative Memory"
description: "Round 19 negative memory for no_crash with verifier signal objdump_rejected_minimal_coff."
failure_class: "no_crash"
verifier_signal: "objdump_rejected_minimal_coff"
candidate_family: "construct"
input_format: "coff-object"
harness_convention: "honggfuzz/libfuzzer-driver"
vuln_class: "coff-aarch64-relocation"
access_scope: generate
success_count: 0
confidence: medium
tags: ["no-crash", "objdump-rejected-minimal-coff", "coff-object", "honggfuzz-libfuzzer-driver", "construct", "negative-memory", "round-19"]
match_keys: ["no-crash", "objdump-rejected-minimal-coff", "coff-object", "honggfuzz-libfuzzer-driver", "coff-aarch64-relocation"]
allowed_scopes: [generate]
forbidden_fields: [raw_poc_bytes, task_id, exact_offset, checksum, submit_metadata]
evidence_level: medium
train_only: true
round: 19
---
# No Crash Objdump Rejected Minimal Coff Coff Object Negative Memory

- key: `no_crash x objdump_rejected_minimal_coff`
- outcome: persistent failure / basin to avoid
- success_count: 0
- failure_count: 1
- related format facts: [[coff-object]]
- harnesses: [[honggfuzz-libfuzzer-driver]]

## Failure Shape
A minimal ARM64 COFF object with a text section and relocation was rejected or did not reach the relocation install helpers. The missing condition is an objdump/objcopy path that applies AArch64 COFF relocations through BFD relocation processing, not just symbol-table reading.

## Policy
Treat `no_crash x objdump_rejected_minimal_coff` on `coff-object` as negative memory for the attempted carrier. Preserve only the reachability that was actually observed, then retarget the missing gate or sink-specific state before spending more verification attempts.

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
