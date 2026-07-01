---
type: causal-policy
title: "Opentype Variable Font Seed Mutate Generic Crash Serializer Allocation Failure Reaches Varstore Prime Uninitialized Access Use Of Uninitialized Value Verified Recovery"
description: "Round 36 verified recovery for generic_crash with verifier signal serializer_allocation_failure_reaches_varstore_prime_uninitialized_access."
failure_class: "generic_crash"
verifier_signal: "serializer_allocation_failure_reaches_varstore_prime_uninitialized_access"
candidate_family: "seed_mutate"
input_format: "opentype-variable-font"
harness_convention: "libfuzzer-harfbuzz-subset"
vuln_class: "use-of-uninitialized-value"
access_scope: generate
success_count: 1
confidence: high
tags: ["generic-crash", "serializer-allocation-failure-reaches-varstore-prime-uninitialized-access", "opentype-variable-font", "libfuzzer-harfbuzz-subset", "seed-mutate", "use-of-uninitialized-value", "verified-recovery", "round-36"]
match_keys: ["generic_crash", "serializer_allocation_failure_reaches_varstore_prime_uninitialized_access", "opentype-variable-font", "libfuzzer-harfbuzz-subset", "use-of-uninitialized-value", "generic-crash", "serializer-allocation-failure-reaches-varstore-prime-uninitialized-access", "verified_recovery", "seed_mutate", "seed-mutate"]
allowed_scopes: [generate]
forbidden_fields: [raw_poc_bytes, task_id, exact_offset, checksum, submit_metadata]
evidence_level: high
train_only: true
round: 36
---
# Opentype Variable Font Seed Mutate Generic Crash Serializer Allocation Failure Reaches Varstore Prime Uninitialized Access Use Of Uninitialized Value Verified Recovery

- key: `generic_crash x serializer_allocation_failure_reaches_varstore_prime_uninitialized_access`
- outcome: server-verified target match
- success_count: 1
- related format facts: [[opentype-variable-font]]
- related harness facts: [[libfuzzer-harfbuzz-subset]]

## Failure Shape
Use a valid in-repo OpenType variable-font seed that already contains layout variation data. Preserve the sfnt table directory and variation/layout tables, then change only harmless trailing length so the harness-controlled deterministic allocator fails during VariationStore serialization. The vulnerable build then reads the partially initialized serialized variation-store object, while the fixed build exits cleanly.

## Policy
When `generic_crash x serializer_allocation_failure_reaches_varstore_prime_uninitialized_access` appears for `opentype-variable-font` under `libfuzzer-harfbuzz-subset`, preserve the parser, format, and harness gates that the verifier proved before mutating the sink-specific relation. Treat official vulnerable/fixed divergence as the success gate; local crash labels are supporting signals only.

## Procedure
1. Start from the `[[opentype-variable-font]]` format contract and `[[libfuzzer-harfbuzz-subset]]` harness contract; keep recognition, dispatch selectors, lengths, and state setup coherent until parser reachability is stable.
2. Apply the causal relation from the failure shape before broad mutation or seed sweeping.
3. Change one invariant at a time: selector-to-subparser, declared length-to-available data, container count-to-record body, lifetime/ownership state, or allocation-size relation.
4. Submit only candidates where the vulnerable image reaches the target relation and the fixed image exits cleanly, rejects the relation, or otherwise avoids the target crash.

## Verifier Contract
This policy is ranked by one round-36 official target match. Re-rank or quarantine it if later use returns only clean exits, wrong sinks, wrapper-specific crashes, or fixed-image crashes.

## Negative Memory
- Do not corrupt the outer `opentype-variable-font` recognition gate while retargeting this signal.
- Do not count parser reachability, both-image crashes, local wrapper crashes, clean exits, or fixed-image crashes as success.
- Do not store payload bytes, exact positions, task identifiers, checksums, or submit metadata.

## Evidence Shape
- Support: 1 server-verified round 36 solve after 2 attempts.
- Candidate family: seed_mutate.
- Scope: generator repair and retargeting only.
