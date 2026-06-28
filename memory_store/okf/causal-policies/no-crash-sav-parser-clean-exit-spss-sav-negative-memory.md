---
type: negative-memory
title: "No Crash Sav Parser Clean Exit Spss Sav Negative Memory"
description: "Round 19 negative memory for no_crash with verifier signal sav_parser_clean_exit."
failure_class: "no_crash"
verifier_signal: "sav_parser_clean_exit"
candidate_family: "construct"
input_format: "spss-sav"
harness_convention: "libfuzzer"
vuln_class: "heap-buffer-overflow-read"
access_scope: generate
success_count: 0
confidence: medium
tags: ["no-crash", "sav-parser-clean-exit", "spss-sav", "libfuzzer", "construct", "negative-memory", "round-19"]
match_keys: ["no-crash", "sav-parser-clean-exit", "spss-sav", "libfuzzer", "heap-buffer-overflow-read"]
allowed_scopes: [generate]
forbidden_fields: [raw_poc_bytes, task_id, exact_offset, checksum, submit_metadata]
evidence_level: medium
train_only: true
round: 19
---
# No Crash Sav Parser Clean Exit Spss Sav Negative Memory

- key: `no_crash x sav_parser_clean_exit`
- outcome: persistent failure / basin to avoid
- success_count: 0
- failure_count: 1
- related format facts: [[spss-sav]]
- harnesses: [[libfuzzer]]

## Failure Shape
Hand-built SAV envelopes with long-string variable markers, character-encoding metadata, zero and nonzero row segments, and compressed-row markers exited cleanly. Local generation of real SAV seeds was blocked by a missing autotools iconv macro, leaving the valid dictionary/data-section gate unsatisfied.

## Policy
Treat `no_crash x sav_parser_clean_exit` on `spss-sav` as negative memory for the attempted carrier. Preserve only the reachability that was actually observed, then retarget the missing gate or sink-specific state before spending more verification attempts.

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
