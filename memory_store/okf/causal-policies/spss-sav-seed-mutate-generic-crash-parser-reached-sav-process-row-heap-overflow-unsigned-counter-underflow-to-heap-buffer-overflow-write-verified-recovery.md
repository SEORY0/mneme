---
type: "causal-policy"
title: "Spss Sav Seed Mutate Generic Crash Parser Reached Sav Process Row Heap Overflow Unsigned Counter Underflow To Heap Buffer Overflow Write Verified Recovery"
description: "Round 38 verified recovery for generic_crash with verifier signal parser_reached_sav_process_row_heap_overflow."
failure_class: "generic_crash"
verifier_signal: "parser_reached_sav_process_row_heap_overflow"
candidate_family: "seed_mutate"
input_format: "spss-sav"
harness_convention: "libfuzzer-raw-sav"
vuln_class: "unsigned-counter-underflow-to-heap-buffer-overflow-write"
access_scope: "generate"
success_count: 1
confidence: "high"
tags: ["generic-crash", "parser-reached-sav-process-row-heap-overflow", "spss-sav", "libfuzzer-raw-sav", "seed-mutate", "unsigned-counter-underflow-to-heap-buffer-overflow-write", "verified-recovery", "round-38"]
match_keys: ["generic_crash", "parser_reached_sav_process_row_heap_overflow", "spss-sav", "libfuzzer-raw-sav", "unsigned-counter-underflow-to-heap-buffer-overflow-write", "verified-recovery", "seed_mutate"]
allowed_scopes: ["generate"]
forbidden_fields: ["raw_poc_bytes", "task_id", "exact_offset", "checksum", "submit_metadata"]
evidence_level: "high"
train_only: true
round: 38
---
# Spss Sav Seed Mutate Generic Crash Parser Reached Sav Process Row Heap Overflow Unsigned Counter Underflow To Heap Buffer Overflow Write Verified Recovery

- key: `generic_crash x parser_reached_sav_process_row_heap_overflow`
- outcome: server-verified target match
- success_count: 1
- related format facts: [[spss-sav]]
- related harness facts: [[libfuzzer-raw-sav]]

## Failure Shape
Start from a valid SAV seed that already declares UTF-8 text handling and a very-long string whose logical value spans multiple row segments. Preserve the header, dictionary, info records, terminator, and row width, but make the first segment of the multi-segment UTF-8 string contain only skipped characters. The UTF-8 row compaction leaves the raw-string counter empty; the segment transition then decrements it and the following segment write uses the wrapped counter.

## Policy
When `generic_crash x parser_reached_sav_process_row_heap_overflow` appears for `[[spss-sav]]` under `[[libfuzzer-raw-sav]]`, preserve every recognition, length, selector, allocation-state, lifetime, and checksum-equivalent gate needed to reach the target parser before changing the sink-specific relation. Treat vulnerable/fixed divergence from the official verifier as the success gate; local parser reachability and local crash labels are supporting signals only.

## Procedure
1. Start from the `[[spss-sav]]` format contract and `[[libfuzzer-raw-sav]]` harness contract; keep the accepted envelope, dispatch selectors, declared lengths, and state setup coherent until parser reachability is stable.
2. Recreate the causal relation described in the failure shape before broad mutation or seed sweeping.
3. Change one invariant at a time: selector-to-subparser, declared length-to-available data, count-to-record body, lifetime/ownership state, allocation-size relation, or sanitizer-specific sink relation.
4. Submit only candidates where the vulnerable image reaches the target relation and the fixed image exits cleanly, rejects the relation, or otherwise avoids the target crash.

## Verifier Contract
This policy is ranked by one official target match. Re-rank or quarantine it if later use returns only clean exits, wrong sinks, wrapper-specific crashes, or fixed-image crashes.

## Negative Memory
- Do not corrupt the outer `[[spss-sav]]` recognition gate while retargeting this signal.
- Do not count parser reachability, both-image crashes, local wrapper crashes, clean exits, or fixed-image crashes as success.
- Do not store payload bytes, exact positions, task identifiers, checksums, or submit metadata.

## Evidence Shape
- Support: server-verified round 38 solve after 1 attempts.
- Candidate family: seed_mutate.
- Official split: vulnerable exit 1, fixed exit 0, target_match True.
- Scope: generator repair and retargeting only.
