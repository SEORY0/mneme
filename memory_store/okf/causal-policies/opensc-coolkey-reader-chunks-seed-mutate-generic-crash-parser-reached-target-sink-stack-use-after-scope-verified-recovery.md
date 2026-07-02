---
type: causal-policy
title: "Opensc Coolkey Reader Chunks Seed Mutate Generic Crash Parser Reached Target Sink Stack Use After Scope Verified Recovery"
description: "Verified recovery distilled from a round trace for generic_crash / parser_reached_target_sink."
failure_class: "generic_crash"
verifier_signal: "parser_reached_target_sink"
candidate_family: "seed_mutate"
input_format: "opensc-coolkey-reader-chunks"
harness_convention: "libfuzzer"
vuln_class: "stack-use-after-scope"
access_scope: generate
success_count: 1
confidence: high
tags: ["generic-crash", "seed-mutate", "opensc-coolkey-reader-chunks", "stack-use-after-scope", "verified-recovery"]
match_keys: ["generic-crash", "parser-reached-target-sink", "opensc-coolkey-reader-chunks", "libfuzzer", "stack-use-after-scope", "verified-recovery"]
allowed_scopes: [generate]
forbidden_fields: [raw_poc_bytes, task_id, exact_offset, checksum, submit_metadata]
evidence_level: high
train_only: true
provenance: round-35-consolidator
---
# Opensc Coolkey Reader Chunks Seed Mutate Generic Crash Parser Reached Target Sink Stack Use After Scope Verified Recovery

## Policy
For `generic_crash` with verifier signal `parser_reached_target_sink` on `opensc-coolkey-reader-chunks` under `libfuzzer`, recover by preserving the format and harness gates that reach the target sink, then mutate only the invariant described by the verified recipe. This policy is keyed to the failure signal and is not a byte-level PoC recipe.

## Procedure
1. Start from a valid CoolKey reader transcript and preserve the ATR, lifecycle, applet selection, object-list, combined-object read, and end-of-list gates.
2. Mutate the embedded combined object so a private-key record has usable RSA public parameters and explicit signing capability, then provide enough later success APDU responses for post-bind key selection to succeed.
3. A small signing input then reaches the short RSA operation, where a stack-scoped response pointer is passed to the APDU helper after its lifetime has ended.

## Format Contract
- Input format: [[opensc-coolkey-reader-chunks]].
- Harness contract: [[libfuzzer]].
- Keep parser reachability and sink selection intact before mutating the vulnerable relation.

## Negative Memory
- Do not broaden this into unrelated `opensc-coolkey-reader-chunks` failures without the same failure class and verifier signal.
- Do not store task identifiers, raw bytes, exact offsets, checksums, or submit metadata.

## Evidence Shape
- Support: one round 35 verified official target match; vulnerable build reached the target signal and the fixed build did not.
