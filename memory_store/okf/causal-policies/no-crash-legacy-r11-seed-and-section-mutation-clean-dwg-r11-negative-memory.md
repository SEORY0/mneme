---
type: negative-memory
title: "No Crash Legacy R11 Seed And Section Mutation Clean DWG R11 Negative Memory"
description: "Round 19 negative memory for no_crash with verifier signal legacy_r11_seed_and_section_mutation_clean."
failure_class: "no_crash"
verifier_signal: "legacy_r11_seed_and_section_mutation_clean"
candidate_family: "seed_mutate"
input_format: "dwg-r11"
harness_convention: "libfuzzer-raw-dwg-dxf-json-dispatcher"
vuln_class: "heap-buffer-overflow-write"
access_scope: generate
success_count: 0
confidence: medium
tags: ["no-crash", "legacy-r11-seed-and-section-mutation-clean", "dwg-r11", "libfuzzer-raw-dwg-dxf-json-dispatcher", "seed-mutate", "negative-memory", "round-19"]
match_keys: ["no-crash", "legacy-r11-seed-and-section-mutation-clean", "dwg-r11", "libfuzzer-raw-dwg-dxf-json-dispatcher", "heap-buffer-overflow-write"]
allowed_scopes: [generate]
forbidden_fields: [raw_poc_bytes, task_id, exact_offset, checksum, submit_metadata]
evidence_level: medium
train_only: true
round: 19
---
# No Crash Legacy R11 Seed And Section Mutation Clean DWG R11 Negative Memory

- key: `no_crash x legacy_r11_seed_and_section_mutation_clean`
- outcome: persistent failure / basin to avoid
- success_count: 0
- failure_count: 1
- related format facts: [[dwg-r11]]
- harnesses: [[libfuzzer-raw-dwg-dxf-json-dispatcher]]

## Failure Shape
Real R11 DWG seeds reached the legacy decoder cleanly, and a small section-count mutation did not trigger the off-by-one. The missing condition is a valid R11 pre-header/entity/auxheader relation that makes decode_r11 allocate one element too small while still passing sentinels and table checks.

## Policy
Treat `no_crash x legacy_r11_seed_and_section_mutation_clean` on `dwg-r11` as negative memory for the attempted carrier. Preserve only the reachability that was actually observed, then retarget the missing gate or sink-specific state before spending more verification attempts.

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
