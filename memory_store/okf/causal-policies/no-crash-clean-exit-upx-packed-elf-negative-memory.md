---
type: negative-memory
title: "No Crash Clean Exit Upx Packed Elf Negative Memory"
description: "Round 22 negative memory for no_crash with verifier signal clean_exit."
failure_class: "no_crash"
verifier_signal: "clean_exit"
candidate_family: "construct"
input_format: "upx-packed-elf"
harness_convention: "libfuzzer"
vuln_class: "bad-elf-dynamic-table-handling"
access_scope: generate
success_count: 0
confidence: medium
tags: ["no-crash", "clean-exit", "upx-packed-elf", "libfuzzer", "construct", "negative-memory", "round-22"]
match_keys: ["no-crash", "clean-exit", "upx-packed-elf", "libfuzzer", "bad-elf-dynamic-table-handling"]
allowed_scopes: [generate]
forbidden_fields: [raw_poc_bytes, task_id, exact_offset, checksum, submit_metadata]
evidence_level: medium
train_only: true
round: 22
---
# No Crash Clean Exit Upx Packed Elf Negative Memory

- key: `no_crash x clean_exit`
- outcome: persistent failure / basin to avoid
- success_count: 0
- failure_count: 1
- related format facts: [[upx-packed-elf]]
- harnesses: [[libfuzzer]]

## Failure Shape
A normal dynamically linked ELF reached UPX file handling but was rejected as not packed. The known dead-end is raw ELF or UPX-marker-only construction; this target needs a complete UPX-packed ELF carrier, likely with Go-style dynamic table placement around string and symbol tables, before the Linux ELF unpacker traverses the vulnerable relation.

## Policy
Treat `no_crash x clean_exit` on `upx-packed-elf` as negative memory for the attempted carrier. Preserve only reachability that was actually observed, then retarget the missing parser gate, feature selector, length relation, stateful subobject, or official sink before spending more verification attempts.

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
