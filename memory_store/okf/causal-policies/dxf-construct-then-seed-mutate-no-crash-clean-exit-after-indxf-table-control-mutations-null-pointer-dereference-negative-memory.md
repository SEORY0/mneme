---
type: "negative-memory"
title: "DXF Construct Then Seed Mutate No Crash Clean Exit After Indxf Table Control Mutations Null Pointer Dereference Negative Memory"
description: "Round 38 negative memory for no_crash with verifier signal clean_exit_after_indxf_table_control_mutations."
failure_class: "no_crash"
verifier_signal: "clean_exit_after_indxf_table_control_mutations"
candidate_family: "construct_then_seed_mutate"
input_format: "dxf"
harness_convention: "libfuzzer"
vuln_class: "null-pointer-dereference"
access_scope: "generate"
success_count: 0
failure_count: 1
confidence: "medium"
tags: ["no-crash", "clean-exit-after-indxf-table-control-mutations", "dxf", "libfuzzer", "construct-then-seed-mutate", "null-pointer-dereference", "negative-memory", "round-38"]
match_keys: ["no_crash", "clean_exit_after_indxf_table_control_mutations", "dxf", "libfuzzer", "null-pointer-dereference", "negative-memory", "construct_then_seed_mutate"]
allowed_scopes: ["generate"]
forbidden_fields: ["raw_poc_bytes", "task_id", "exact_offset", "checksum", "submit_metadata"]
evidence_level: "medium"
train_only: true
round: 38
---
# DXF Construct Then Seed Mutate No Crash Clean Exit After Indxf Table Control Mutations Null Pointer Dereference Negative Memory

- key: `no_crash x clean_exit_after_indxf_table_control_mutations`
- outcome: persistent failure / basin to avoid
- success_count: 0
- failure_count: 1
- related format facts: [[dxf]]
- related harness facts: [[libfuzzer]]

## Failure Shape
Minimal DXF table-control envelopes and seed-shaped table mutations reached clean exits. Declared entry counts, built-in table names, high count values, missing handles, zero handles, and unsupported table-name variants did not create the required state where a control object has a positive entry count with a null entries vector. The missing trigger is likely a narrower indxf state transition that decouples the stored table-control count from allocation of the handle vector.

## Observed Basin
- Failure trajectory classes: no_crash.
- Official confirmation: no server target match for this basin.

## Policy
Treat `no_crash x clean_exit_after_indxf_table_control_mutations` on `[[dxf]]` under `[[libfuzzer]]` as a basin to avoid unless a new candidate changes the parser gate, state relation, or sink relation described above. Preserve any proven reachability, but reject variants that return to the same clean-exit, off-target-crash, wrapper-mismatch, usage-only, timeout, both-image-crash, or fixed-image-crash behavior.

## Procedure
1. Keep only the smallest parser or harness envelope that was actually reached.
2. Identify the missing relation from the verifier signal: parser selection, container acceptance, length relation, stateful subobject, allocation state, or official target sink.
3. Change one relation at a time and discard candidates that return to the same `clean_exit_after_indxf_table_control_mutations` basin.
4. Promote a recovery from this basin only after a later official target match.

## Negative Memory
- Do not resubmit broad mutations that only reproduce `clean_exit_after_indxf_table_control_mutations`.
- Do not count parser reachability, both-image crashes, local wrapper crashes, clean exits, timeouts, or fixed-image crashes as success.
- Do not store payload bytes, exact positions, task identifiers, checksums, or submit metadata.

## Evidence Shape
- Support: one diagnosed persistent failure from round 38 after 10 attempts.
- Candidate family: construct_then_seed_mutate.
- Scope: generator repair and basin avoidance only.
