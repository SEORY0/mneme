---
type: causal-policy
title: "PHP Source Construct Generic Crash Parser Reached Target Crash Heap Use After Free Read Verified Recovery"
description: "Round 36 verified recovery for generic_crash with verifier signal parser_reached_target_crash."
failure_class: "generic_crash"
verifier_signal: "parser_reached_target_crash"
candidate_family: "construct"
input_format: "php-source"
harness_convention: "libfuzzer-parser"
vuln_class: "heap-use-after-free-read"
access_scope: generate
success_count: 1
confidence: high
tags: ["generic-crash", "parser-reached-target-crash", "php-source", "libfuzzer-parser", "construct", "heap-use-after-free-read", "verified-recovery", "round-36"]
match_keys: ["generic_crash", "parser_reached_target_crash", "php-source", "libfuzzer-parser", "heap-use-after-free-read", "generic-crash", "parser-reached-target-crash", "verified_recovery", "construct"]
allowed_scopes: [generate]
forbidden_fields: [raw_poc_bytes, task_id, exact_offset, checksum, submit_metadata]
evidence_level: high
train_only: true
round: 36
---
# PHP Source Construct Generic Crash Parser Reached Target Crash Heap Use After Free Read Verified Recovery

- key: `generic_crash x parser_reached_target_crash`
- outcome: server-verified target match
- success_count: 1
- related format facts: [[php-source]]
- related harness facts: [[libfuzzer-parser]]

## Failure Shape
Use valid raw PHP source for the parser fuzzer. Declare a disabled internal function name from the harness' hardcoded disable list, then add enough unique top-level function declarations to force the global function table through a resize or rehash after startup deletions have left disabled-function holes. The vulnerable build preserves a stale persistent-table boundary across that compaction, so a later parser-fuzzer replay observes user functions that should have been cleaned and reads freed compiler-arena function metadata while binding a duplicate declaration. The fixed build keeps the persistent/internal segment coherent and exits cleanly.

## Policy
When `generic_crash x parser_reached_target_crash` appears for `php-source` under `libfuzzer-parser`, preserve the parser, format, and harness gates that the verifier proved before mutating the sink-specific relation. Treat official vulnerable/fixed divergence as the success gate; local crash labels are supporting signals only.

## Procedure
1. Start from the `[[php-source]]` format contract and `[[libfuzzer-parser]]` harness contract; keep recognition, dispatch selectors, lengths, and state setup coherent until parser reachability is stable.
2. Apply the causal relation from the failure shape before broad mutation or seed sweeping.
3. Change one invariant at a time: selector-to-subparser, declared length-to-available data, container count-to-record body, lifetime/ownership state, or allocation-size relation.
4. Submit only candidates where the vulnerable image reaches the target relation and the fixed image exits cleanly, rejects the relation, or otherwise avoids the target crash.

## Verifier Contract
This policy is ranked by one round-36 official target match. Re-rank or quarantine it if later use returns only clean exits, wrong sinks, wrapper-specific crashes, or fixed-image crashes.

## Negative Memory
- Do not corrupt the outer `php-source` recognition gate while retargeting this signal.
- Do not count parser reachability, both-image crashes, local wrapper crashes, clean exits, or fixed-image crashes as success.
- Do not store payload bytes, exact positions, task identifiers, checksums, or submit metadata.

## Evidence Shape
- Support: 1 server-verified round 36 solve after 3 attempts.
- Candidate family: construct.
- Scope: generator repair and retargeting only.
