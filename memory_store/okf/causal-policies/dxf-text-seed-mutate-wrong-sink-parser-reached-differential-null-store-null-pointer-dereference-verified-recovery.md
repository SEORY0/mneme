---
type: "causal-policy"
title: "DXF Text Seed Mutate Wrong Sink Parser Reached Differential Null Store Null Pointer Dereference Verified Recovery"
description: "Round 38 verified recovery for wrong_sink with verifier signal parser_reached_differential_null_store."
failure_class: "wrong_sink"
verifier_signal: "parser_reached_differential_null_store"
candidate_family: "seed_mutate"
input_format: "dxf-text"
harness_convention: "libfuzzer"
vuln_class: "null-pointer-dereference"
access_scope: "generate"
success_count: 1
confidence: "high"
tags: ["wrong-sink", "parser-reached-differential-null-store", "dxf-text", "libfuzzer", "seed-mutate", "null-pointer-dereference", "verified-recovery", "round-38"]
match_keys: ["wrong_sink", "parser_reached_differential_null_store", "dxf-text", "libfuzzer", "null-pointer-dereference", "verified-recovery", "seed_mutate"]
allowed_scopes: ["generate"]
forbidden_fields: ["raw_poc_bytes", "task_id", "exact_offset", "checksum", "submit_metadata"]
evidence_level: "high"
train_only: true
round: 38
---
# DXF Text Seed Mutate Wrong Sink Parser Reached Differential Null Store Null Pointer Dereference Verified Recovery

- key: `wrong_sink x parser_reached_differential_null_store`
- outcome: server-verified target match
- success_count: 1
- related format facts: [[dxf-text]]
- related harness facts: [[libfuzzer]]

## Failure Shape
Start from a real DXF seed that already registers and reaches an extended entity with counted point-vector fields. Keep the section, class, entity, subclass, and common entity records intact. Mutate the counted point-vector shape so the point count is nonzero but a coordinate continuation appears before the corresponding first coordinate has allocated the vector storage. The vulnerable generic DXF entity-field handler stores through the still-null point-vector pointer, while the fixed build rejects or ignores that malformed point sequence.

## Policy
When `wrong_sink x parser_reached_differential_null_store` appears for `[[dxf-text]]` under `[[libfuzzer]]`, preserve every recognition, length, selector, allocation-state, lifetime, and checksum-equivalent gate needed to reach the target parser before changing the sink-specific relation. Treat vulnerable/fixed divergence from the official verifier as the success gate; local parser reachability and local crash labels are supporting signals only.

## Procedure
1. Start from the `[[dxf-text]]` format contract and `[[libfuzzer]]` harness contract; keep the accepted envelope, dispatch selectors, declared lengths, and state setup coherent until parser reachability is stable.
2. Recreate the causal relation described in the failure shape before broad mutation or seed sweeping.
3. Change one invariant at a time: selector-to-subparser, declared length-to-available data, count-to-record body, lifetime/ownership state, allocation-size relation, or sanitizer-specific sink relation.
4. Submit only candidates where the vulnerable image reaches the target relation and the fixed image exits cleanly, rejects the relation, or otherwise avoids the target crash.

## Verifier Contract
This policy is ranked by one official target match. Re-rank or quarantine it if later use returns only clean exits, wrong sinks, wrapper-specific crashes, or fixed-image crashes.

## Negative Memory
- Do not corrupt the outer `[[dxf-text]]` recognition gate while retargeting this signal.
- Do not count parser reachability, both-image crashes, local wrapper crashes, clean exits, or fixed-image crashes as success.
- Do not store payload bytes, exact positions, task identifiers, checksums, or submit metadata.

## Evidence Shape
- Support: server-verified round 38 solve after 9 attempts.
- Candidate family: seed_mutate.
- Official split: vulnerable exit 1, fixed exit 0, target_match True.
- Scope: generator repair and retargeting only.
