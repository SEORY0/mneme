---
type: causal-policy
title: "Php Source Seed Mutate Parser Reached Target Sink Invalid Array Lifetime Dtor Crash Verified Recovery"
description: "Server-verified recovery for php-source when generic_crash pairs with parser_reached_target_sink."
failure_class: "generic_crash"
verifier_signal: "parser_reached_target_sink"
candidate_family: "seed_mutate"
input_format: "php-source"
harness_convention: "libfuzzer"
vuln_class: "invalid-array-lifetime-dtor-crash"
access_scope: generate
success_count: 1
confidence: high
tags: ["generic-crash", "parser-reached-target-sink", "php-source", "libfuzzer", "seed-mutate", "verified-recovery", "round-17"]
match_keys: ["generic-crash", "parser-reached-target-sink", "php-source", "libfuzzer", "seed-mutate", "invalid-array-lifetime-dtor-crash", "verified-recovery"]
allowed_scopes: [generate]
forbidden_fields: [raw_poc_bytes, task_id, exact_offset, checksum, submit_metadata]
evidence_level: high
train_only: true
round: 17
---
# Php Source Seed Mutate Parser Reached Target Sink Invalid Array Lifetime Dtor Crash Verified Recovery

- key: `generic_crash x parser_reached_target_sink`
- outcome: server-verified vulnerable/fixed split
- success_count: 1
- related format facts: [[php-source]]
- related harness facts: [[libfuzzer]]

## Policy
When `generic_crash x parser_reached_target_sink` appears for `php-source`, preserve the parser or harness carrier already shown to reach the target branch. Retarget only the causal invariant named by the verifier signal and vulnerability class; do not broaden into unrelated container families after reachability is established.

## Procedure
1. Use valid PHP source defining a class with declared hooked properties, create an uninitialized lazy ghost for that class whose initializer throws, then request foreach iteration over the object.
2. Iterator creation builds the hook-backed declared-properties array during failed lazy initialization and later destroys a zval that points at the immutable empty array sentinel.
3. Submit only candidates that preserve the same accepted carrier and separate vulnerable-build failure from fixed-build clean behavior.

## Negative Memory
- Do not treat local-only crashes, both-image crashes, or coarse sink labels as success for this key.
- Do not store raw payload bytes, exact positions, task identifiers, checksums, or submit metadata.

## Format Contract
Use [[php-source]]; the relevant gate is the accepted carrier plus the invariant described above, not a byte-specific recipe.

## Harness Contract
Use [[libfuzzer]]; preserve the observed input contract before mutating deeper fields.

## Evidence Shape
- Support: 1 server-verified round 17 solve.
- Candidate family: seed_mutate.
