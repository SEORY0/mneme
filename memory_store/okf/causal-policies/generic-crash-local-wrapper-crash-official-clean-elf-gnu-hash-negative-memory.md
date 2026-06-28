---
type: negative-memory
title: "Generic Crash Local Wrapper Crash Official Clean Elf Gnu Hash Negative Memory"
description: "Round 21 negative memory for generic-crash with verifier signal local-wrapper-crash-official-clean."
failure_class: "generic-crash"
verifier_signal: "local-wrapper-crash-official-clean"
candidate_family: "construct"
input_format: "elf-gnu-hash"
harness_convention: "libfuzzer-libdwfl"
vuln_class: "use-of-uninitialized-value"
access_scope: generate
success_count: 0
confidence: medium
tags: ["generic-crash", "local-wrapper-crash-official-clean", "elf-gnu-hash", "libfuzzer-libdwfl", "construct", "negative-memory", "round-21"]
match_keys: ["generic-crash", "local-wrapper-crash-official-clean", "elf-gnu-hash", "libfuzzer-libdwfl", "use-of-uninitialized-value"]
allowed_scopes: [generate]
forbidden_fields: [raw_poc_bytes, task_id, exact_offset, checksum, submit_metadata]
evidence_level: medium
train_only: true
round: 21
---
# Generic Crash Local Wrapper Crash Official Clean Elf Gnu Hash Negative Memory

- key: `generic-crash x local-wrapper-crash-official-clean`
- outcome: persistent failure / basin to avoid
- success_count: 0
- failure_count: 1
- related format facts: [[elf-gnu-hash]]
- harnesses: [[libfuzzer-libdwfl]]

## Failure Shape
A compact ELF64 carrier with a GNU hash section and non-word-aligned section sizes produced local wrapper crashes for several boundary sizes, but official submission reported the vulnerable build clean, so the local signal was not the target. Aligned variants were clean.

## Policy
Treat `generic-crash x local-wrapper-crash-official-clean` on `elf-gnu-hash` as negative memory for the attempted carrier. Preserve only the reachability that was actually observed, then retarget the missing gate or sink-specific state before spending more verification attempts.

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
