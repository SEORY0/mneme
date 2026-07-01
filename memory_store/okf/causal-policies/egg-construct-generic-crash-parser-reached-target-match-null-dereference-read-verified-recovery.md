---
type: causal-policy
title: "Egg Construct Generic Crash Parser Reached Target Match Null Dereference Read Verified Recovery"
description: "Verified recovery distilled from a round trace for generic_crash / parser_reached_target_match."
failure_class: "generic_crash"
verifier_signal: "parser_reached_target_match"
candidate_family: "construct"
input_format: "egg"
harness_convention: "libfuzzer"
vuln_class: "null-dereference-read"
access_scope: generate
success_count: 1
confidence: high
tags: ["generic-crash", "construct", "egg", "null-dereference-read", "verified-recovery"]
match_keys: ["generic-crash", "parser-reached-target-match", "egg", "libfuzzer", "null-dereference-read", "verified-recovery"]
allowed_scopes: [generate]
forbidden_fields: [raw_poc_bytes, task_id, exact_offset, checksum, submit_metadata]
evidence_level: high
train_only: true
provenance: round-35-consolidator
---
# Egg Construct Generic Crash Parser Reached Target Match Null Dereference Read Verified Recovery

## Policy
For `generic_crash` with verifier signal `parser_reached_target_match` on `egg` under `libfuzzer`, recover by preserving the format and harness gates that reach the target sink, then mutate only the invariant described by the verified recipe. This policy is keyed to the failure signal and is not a byte-level PoC recipe.

## Procedure
1. Construct a minimal EGG archive that reaches file-header parsing and includes a filename extra field marked as multibyte-with-codepage.
2. Choose a codepage value that is accepted as a listed Windows codepage but whose encoding entry is null in the scanner's conversion table.
3. A minimal filename payload is sufficient: the filename parser passes that null encoding to the UTF-8 conversion helper, which forwards it to iconv and triggers a null read in the vulnerable build while the fixed build exits cleanly.

## Format Contract
- Input format: [[egg]].
- Harness contract: [[libfuzzer]].
- Keep parser reachability and sink selection intact before mutating the vulnerable relation.

## Negative Memory
- Do not broaden this into unrelated `egg` failures without the same failure class and verifier signal.
- Do not store task identifiers, raw bytes, exact offsets, checksums, or submit metadata.

## Evidence Shape
- Support: one round 35 verified official target match; vulnerable build reached the target signal and the fixed build did not.
