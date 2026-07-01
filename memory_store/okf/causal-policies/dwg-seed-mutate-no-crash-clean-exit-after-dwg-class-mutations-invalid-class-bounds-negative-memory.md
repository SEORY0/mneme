---
type: "negative-memory"
title: "DWG Seed Mutate No Crash Clean Exit After DWG Class Mutations Invalid Class Bounds Negative Memory"
description: "Round 38 negative memory for no_crash with verifier signal clean_exit_after_dwg_class_mutations."
failure_class: "no_crash"
verifier_signal: "clean_exit_after_dwg_class_mutations"
candidate_family: "seed_mutate"
input_format: "dwg"
harness_convention: "libfuzzer"
vuln_class: "invalid-class-bounds"
access_scope: "generate"
success_count: 0
failure_count: 1
confidence: "medium"
tags: ["no-crash", "clean-exit-after-dwg-class-mutations", "dwg", "libfuzzer", "seed-mutate", "invalid-class-bounds", "negative-memory", "round-38"]
match_keys: ["no_crash", "clean_exit_after_dwg_class_mutations", "dwg", "libfuzzer", "invalid-class-bounds", "negative-memory", "seed_mutate"]
allowed_scopes: ["generate"]
forbidden_fields: ["raw_poc_bytes", "task_id", "exact_offset", "checksum", "submit_metadata"]
evidence_level: "medium"
train_only: true
round: 38
---
# DWG Seed Mutate No Crash Clean Exit After DWG Class Mutations Invalid Class Bounds Negative Memory

- key: `no_crash x clean_exit_after_dwg_class_mutations`
- outcome: persistent failure / basin to avoid
- success_count: 0
- failure_count: 1
- related format facts: [[dwg]]
- related harness facts: [[libfuzzer]]

## Failure Shape
A valid R2000-family drawing seed reached the DWG decoder cleanly, but mutations to dynamic object type bounds, class-section span, and in-range class-name dispatch all exited without a sanitizer signal. The likely missing relation is a coherent malformed class record whose metadata survives class parsing and is later consumed by an object stream that exercises a fragile class-specific decoder, not merely an out-of-range class index.

## Observed Basin
- Failure trajectory classes: no_crash.
- Official confirmation: no server target match for this basin.

## Policy
Treat `no_crash x clean_exit_after_dwg_class_mutations` on `[[dwg]]` under `[[libfuzzer]]` as a basin to avoid unless a new candidate changes the parser gate, state relation, or sink relation described above. Preserve any proven reachability, but reject variants that return to the same clean-exit, off-target-crash, wrapper-mismatch, usage-only, timeout, both-image-crash, or fixed-image-crash behavior.

## Procedure
1. Keep only the smallest parser or harness envelope that was actually reached.
2. Identify the missing relation from the verifier signal: parser selection, container acceptance, length relation, stateful subobject, allocation state, or official target sink.
3. Change one relation at a time and discard candidates that return to the same `clean_exit_after_dwg_class_mutations` basin.
4. Promote a recovery from this basin only after a later official target match.

## Negative Memory
- Do not resubmit broad mutations that only reproduce `clean_exit_after_dwg_class_mutations`.
- Do not count parser reachability, both-image crashes, local wrapper crashes, clean exits, timeouts, or fixed-image crashes as success.
- Do not store payload bytes, exact positions, task identifiers, checksums, or submit metadata.

## Evidence Shape
- Support: one diagnosed persistent failure from round 38 after 11 attempts.
- Candidate family: seed_mutate.
- Scope: generator repair and basin avoidance only.
