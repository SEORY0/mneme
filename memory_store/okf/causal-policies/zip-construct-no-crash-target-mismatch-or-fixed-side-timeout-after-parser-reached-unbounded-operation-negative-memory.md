---
type: negative-memory
title: "Zip Construct No Crash Target Mismatch Or Fixed Side Timeout After Parser Reached Unbounded Operation Negative Memory"
description: "Round 37 negative memory for no_crash with verifier signal target_mismatch_or_fixed_side_timeout_after_parser_reached."
failure_class: "no_crash"
verifier_signal: "target_mismatch_or_fixed_side_timeout_after_parser_reached"
candidate_family: "construct"
input_format: "zip"
harness_convention: "libfuzzer"
vuln_class: "unbounded-operation"
access_scope: generate
success_count: 0
failure_count: 1
confidence: medium
tags: ["no-crash", "target-mismatch-or-fixed-side-timeout-after-parser-reached", "zip", "libfuzzer", "construct", "unbounded-operation", "negative-memory", "round-37"]
match_keys: ["no_crash", "target_mismatch_or_fixed_side_timeout_after_parser_reached", "zip", "libfuzzer", "unbounded-operation", "negative-memory", "construct"]
allowed_scopes: [generate]
forbidden_fields: [raw_poc_bytes, task_id, exact_offset, checksum, submit_metadata]
evidence_level: medium
train_only: true
round: 37
---
# Zip Construct No Crash Target Mismatch Or Fixed Side Timeout After Parser Reached Unbounded Operation Negative Memory

- key: `no_crash x target_mismatch_or_fixed_side_timeout_after_parser_reached`
- outcome: persistent failure / basin to avoid
- success_count: 0
- failure_count: 1
- related format facts: [[zip]]
- related harness facts: [[libfuzzer]]

## Failure Shape
Structurally valid many-entry ZIPs reached the miniz zip fuzzer but stayed clean. Duplicate central-directory entries and CRC or local-name validation violations increased work or produced local crashes, but the official or confirm differential rejected them because the fixed side also took the expensive or crashing path, or the target did not match.

## Observed Basin
- Failure trajectory classes: generic_crash, no_crash, no_crash, no_crash, no_crash, no_crash.
- Official confirmation: no server target match for this basin.

## Policy
Treat `no_crash x target_mismatch_or_fixed_side_timeout_after_parser_reached` on `zip` under `libfuzzer` as a basin to avoid unless a new candidate changes the parser gate, state relation, or sink relation described above. Preserve any proven reachability, but reject variants that return to the same clean-exit, off-target-crash, wrapper-mismatch, usage-only, timeout, or fixed-image-crash behavior.

## Procedure
1. Keep only the smallest parser or harness envelope that was actually reached.
2. Identify the missing relation from the signal: parser selection, container acceptance, length relation, stateful subobject, allocation state, or official target sink.
3. Change one relation at a time and discard candidates that return to the same `target_mismatch_or_fixed_side_timeout_after_parser_reached` basin.
4. Promote a recovery from this basin only after a later official target match.

## Negative Memory
- Do not resubmit broad mutations that only reproduce `target_mismatch_or_fixed_side_timeout_after_parser_reached`.
- Do not count parser reachability, both-image crashes, local wrapper crashes, clean exits, timeouts, or fixed-image crashes as success.
- Do not store payload bytes, exact positions, task identifiers, checksums, or submit metadata.

## Evidence Shape
- Support: one diagnosed persistent failure from round 37 after 6 attempts.
- Candidate family: construct.
- Scope: generator repair and basin avoidance only.
