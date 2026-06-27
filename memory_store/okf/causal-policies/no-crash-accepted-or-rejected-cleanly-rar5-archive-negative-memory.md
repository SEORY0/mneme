---
type: negative-memory
title: "No Crash Accepted Or Rejected Cleanly Rar5 Archive Negative Memory"
description: "Round 19 negative memory for no_crash with verifier signal accepted_or_rejected_cleanly."
failure_class: "no_crash"
verifier_signal: "accepted_or_rejected_cleanly"
candidate_family: "seed_mutate_rar5_fixtures"
input_format: "rar5-archive"
harness_convention: "afl-libfuzzer-file"
vuln_class: "heap-buffer-overflow-read"
access_scope: generate
success_count: 0
confidence: medium
tags: ["no-crash", "accepted-or-rejected-cleanly", "rar5-archive", "afl-libfuzzer-file", "seed-mutate-rar5-fixtures", "negative-memory", "round-19"]
match_keys: ["no-crash", "accepted-or-rejected-cleanly", "rar5-archive", "afl-libfuzzer-file", "heap-buffer-overflow-read"]
allowed_scopes: [generate]
forbidden_fields: [raw_poc_bytes, task_id, exact_offset, checksum, submit_metadata]
evidence_level: medium
train_only: true
round: 19
---
# No Crash Accepted Or Rejected Cleanly Rar5 Archive Negative Memory

- key: `no_crash x accepted_or_rejected_cleanly`
- outcome: persistent failure / basin to avoid
- success_count: 0
- failure_count: 1
- related format facts: [[rar5-archive]]
- harnesses: [[afl-libfuzzer-file]]

## Failure Shape
Real RAR5 fixtures and focused mutations of compressed, solid, multi-file, and stored archive variants satisfied the outer archive signature and header checks but exited cleanly. The remaining missing relation appears to be a valid compressed-file block whose protected header and compression metadata reach the RAR5 Huffman table construction state while carrying an invalid table-size relation.

## Policy
Treat `no_crash x accepted_or_rejected_cleanly` on `rar5-archive` as negative memory for the attempted carrier. Preserve only the reachability that was actually observed, then retarget the missing gate or sink-specific state before spending more verification attempts.

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
