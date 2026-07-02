---
type: causal-policy
title: "Opentype Sfnt Font Construct Generic Crash Parser Reached Invalid Table Slice Dereference Unsigned Overflow To Out Of Bounds Read Verified Recovery"
description: "Round 37 verified recovery for generic_crash with verifier signal parser_reached_invalid_table_slice_dereference."
failure_class: "generic_crash"
verifier_signal: "parser_reached_invalid_table_slice_dereference"
candidate_family: "construct"
input_format: "opentype-sfnt-font"
harness_convention: "libfuzzer"
vuln_class: "unsigned-overflow-to-out-of-bounds-read"
access_scope: generate
success_count: 1
confidence: high
tags: ["generic-crash", "parser-reached-invalid-table-slice-dereference", "opentype-sfnt-font", "libfuzzer", "construct", "unsigned-overflow-to-out-of-bounds-read", "verified-recovery", "round-37"]
match_keys: ["generic_crash", "parser_reached_invalid_table_slice_dereference", "opentype-sfnt-font", "libfuzzer", "unsigned-overflow-to-out-of-bounds-read", "verified-recovery", "construct"]
allowed_scopes: [generate]
forbidden_fields: [raw_poc_bytes, task_id, exact_offset, checksum, submit_metadata]
evidence_level: high
train_only: true
round: 37
---
# Opentype Sfnt Font Construct Generic Crash Parser Reached Invalid Table Slice Dereference Unsigned Overflow To Out Of Bounds Read Verified Recovery

- key: `generic_crash x parser_reached_invalid_table_slice_dereference`
- outcome: server-verified target match
- success_count: 1
- related format facts: [[opentype-sfnt-font]]
- related harness facts: [[libfuzzer]]

## Failure Shape
Construct a minimal SFNT font that keeps the required companion tables valid enough for the loader to progress past table discovery. Make the vulnerable table directory entry use a large table offset and large table length whose narrow-width addition wraps to a small accepted extent, while the offset itself later participates in signed pointer arithmetic. The bounds check accepts the entry, then later parsing of that table dereferences a slice outside the original font buffer in the vulnerable build.

## Policy
When `generic_crash x parser_reached_invalid_table_slice_dereference` appears for `opentype-sfnt-font` under `libfuzzer`, preserve the parser, format, and harness gates that the verifier proved before mutating the sink-specific relation. Treat official vulnerable/fixed divergence as the success gate; local crash labels are supporting signals only.

## Procedure
1. Start from the `[[opentype-sfnt-font]]` format contract and `[[libfuzzer]]` harness contract; keep recognition, dispatch selectors, lengths, and state setup coherent until parser reachability is stable.
2. Apply the causal relation from the failure shape before broad mutation or seed sweeping.
3. Change one invariant at a time: selector-to-subparser, declared length-to-available data, container count-to-record body, lifetime/ownership state, allocation-size relation, or sanitizer-specific sink relation.
4. Submit only candidates where the vulnerable image reaches the target relation and the fixed image exits cleanly, rejects the relation, or otherwise avoids the target crash.

## Verifier Contract
This policy is ranked by 1 official target match. Re-rank or quarantine it if later use returns only clean exits, wrong sinks, wrapper-specific crashes, or fixed-image crashes.

## Negative Memory
- Do not corrupt the outer `opentype-sfnt-font` recognition gate while retargeting this signal.
- Do not count parser reachability, both-image crashes, local wrapper crashes, clean exits, or fixed-image crashes as success.
- Do not store payload bytes, exact positions, task identifiers, checksums, or submit metadata.

## Evidence Shape
- Support: server-verified round 37 solve after 6 attempts.
- Candidate family: construct.
- Official split: vulnerable exit 1, fixed exit 0, target_match True.
- Scope: generator repair and retargeting only.
