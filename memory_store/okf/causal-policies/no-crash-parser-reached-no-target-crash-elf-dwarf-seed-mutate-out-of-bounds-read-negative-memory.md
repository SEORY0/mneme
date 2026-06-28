---
type: negative-memory
title: "No Crash Parser Reached No Target Crash Elf Dwarf Seed Mutate Out Of Bounds Read Negative Memory"
description: "Round 23 negative memory for no_crash with verifier signal parser_reached_no_target_crash."
failure_class: "no_crash"
verifier_signal: "parser_reached_no_target_crash"
candidate_family: "seed_mutate"
input_format: "elf-dwarf"
harness_convention: "libfuzzer"
vuln_class: "out-of-bounds-read"
access_scope: generate
success_count: 0
confidence: medium
tags: ["no-crash", "parser-reached-no-target-crash", "elf-dwarf", "libfuzzer", "seed-mutate", "negative-memory", "round-23"]
match_keys: ["no-crash", "parser-reached-no-target-crash", "elf-dwarf", "libfuzzer", "out-of-bounds-read"]
allowed_scopes: [generate]
forbidden_fields: [raw_poc_bytes, task_id, exact_offset, checksum, submit_metadata]
evidence_level: medium
train_only: true
round: 23
---
# No Crash Parser Reached No Target Crash Elf Dwarf Seed Mutate Out Of Bounds Read Negative Memory

- key: `no_crash x parser_reached_no_target_crash`
- outcome: persistent failure / basin to avoid
- success_count: 0
- failure_count: 1
- related format facts: [[elf-dwarf]]
- harnesses: [[libfuzzer]]

## Failure Shape
Seed ELF/DWARF objects parsed cleanly. Mutating abbreviation-table reference forms from wider references to one-byte references, including selected payload-byte changes, did not cause fuzz_findfuncbypc to dereference an invalid DW_FORM_ref1 target. The likely missing requirement is a coherent DIE graph where the specific attribute is reached by the find-function-by-PC traversal.

## Policy
Treat `no_crash x parser_reached_no_target_crash` on `elf-dwarf` as negative memory for the attempted carrier. Preserve only reachability that was actually observed, then retarget the missing gate, harness contract, or sink-specific state before spending more verification attempts.

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
- Support: 1 diagnosed persistent failure from round 23 after 9 attempts.
- Scope: generator repair and basin avoidance only.
