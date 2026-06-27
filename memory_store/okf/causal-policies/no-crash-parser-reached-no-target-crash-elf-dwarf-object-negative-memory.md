---
type: causal-policy
title: "No Crash Parser Reached No Target Crash ELF Dwarf Object Negative Memory"
description: "Round 9 negative memory for no_crash with verifier signal parser_reached_no_target_crash."
failure_class: "no_crash"
verifier_signal: "parser_reached_no_target_crash"
candidate_family: "seed_mutate"
input_format: "ELF/DWARF object"
harness_convention: "libfuzzer"
vuln_class: "null-pointer-dereference-or-invalid-pointer-read"
access_scope: generate
success_count: 0
confidence: medium
tags: ["no-crash", "parser-reached-no-target-crash", "elf-dwarf-object", "negative-memory", "round-9"]
match_keys: ["no_crash", "parser_reached_no_target_crash", "ELF/DWARF object", "libfuzzer", "null-pointer-dereference-or-invalid-pointer-read", "negative_memory"]
allowed_scopes: [generate]
forbidden_fields: [raw_poc_bytes, task_id, exact_offset, checksum, submit_metadata]
evidence_level: medium
train_only: true
round: 9
---
# No Crash Parser Reached No Target Crash ELF Dwarf Object Negative Memory

- key: `no_crash x parser_reached_no_target_crash`
- outcome: persistent failure / basin to avoid
- success_count: 0
- failure_count: 1
- related format facts: [[elf-dwarf-object]]
- related harness facts: [[libfuzzer]]

## Failure Shape
- Real ELF/DWARF seeds for the exact libdwarf harness parsed cleanly.
- The attempted seed families did not create a CU/DIE attribute combination that passes enough
  validation to call the high-PC query with an invalid result pointer.
- The likely missing trigger is a malformed but traversable DIE with a high_pc attribute form that
  survives CU iteration and fails only at the high-PC helper boundary.

## Policy
Treat `no_crash x parser_reached_no_target_crash` on `ELF/DWARF object` as a basin to avoid unless a new candidate changes the parser gate, state relation, or official target sink. Preserve any proven reachability, but reject variants that return to the same verifier signal without changing the causal gate under test.

## Procedure
1. Keep only the smallest parser or harness envelope that the verifier proved was reached.
2. Identify the missing causal relation from the signal: parser selection, container acceptance, length relation, stateful subobject, allocation state, or official target sink.
3. Change one relation at a time and discard candidates that return to the same clean-exit, off-target-crash, wrong-sink, usage-only, or both-image-crash basin.
4. If a local crash is not an official target match, shrink or discard it before mutating deeper fields.
5. Promote a recovery from this basin only after a later verifier-confirmed target match.

## Format Contract
- The useful inputs are ELF-like objects carrying DWARF sections, including compile-unit
  information, abbreviations, and DIE attributes.
- The target family depends on a CU/DIE tree that remains structurally valid enough for attribute
  iteration and loclist processing.

## Harness Contract
- libFuzzer feeds raw object bytes directly to the libdwarf `fuzz_die_cu_attrs_loclist` harness.
- The harness opens the object through libdwarf, iterates compile units and DIE attributes, and
  exercises location-list and attribute helper paths; there is no wrapper-level mode byte.

## Negative Memory
- Do not resubmit broad mutations that only reproduce `parser_reached_no_target_crash`.
- Do not count parser reachability, both-image crashes, local wrapper crashes, clean exits, or fixed-image crashes as success.
- Do not store raw payload bytes, exact positions, task identifiers, or submit metadata.

## Evidence Shape
- Support: one diagnosed persistent failure from round 9.
- Scope: generator repair and basin avoidance only.
