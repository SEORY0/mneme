---
type: causal-policy
title: "Gml Seed Mutate No Crash Local Wrapper Usage Only Official Target Match Double Free Verified Recovery"
description: "Round 37 verified recovery for no_crash with verifier signal local_wrapper_usage_only_official_target_match."
failure_class: "no_crash"
verifier_signal: "local_wrapper_usage_only_official_target_match"
candidate_family: "seed_mutate"
input_format: "gml"
harness_convention: "honggfuzz-wrapper"
vuln_class: "double-free"
access_scope: generate
success_count: 1
confidence: high
tags: ["no-crash", "local-wrapper-usage-only-official-target-match", "gml", "honggfuzz-wrapper", "seed-mutate", "double-free", "verified-recovery", "round-37"]
match_keys: ["no_crash", "local_wrapper_usage_only_official_target_match", "gml", "honggfuzz-wrapper", "double-free", "verified-recovery", "seed_mutate"]
allowed_scopes: [generate]
forbidden_fields: [raw_poc_bytes, task_id, exact_offset, checksum, submit_metadata]
evidence_level: high
train_only: true
round: 37
---
# Gml Seed Mutate No Crash Local Wrapper Usage Only Official Target Match Double Free Verified Recovery

- key: `no_crash x local_wrapper_usage_only_official_target_match`
- outcome: server-verified target match
- success_count: 1
- related format facts: [[gml]]
- related harness facts: [[honggfuzz-wrapper]]

## Failure Shape
Start from a valid in-tree GML graph seed so the parser builds a normal top-level tree. Add an unsupported integer version declaration as a top-level field before the graph. The vulnerable reader manually destroys the parsed tree on that version error while the parse context is still registered on the cleanup stack, so the ignore error handler destroys the same tree again. The fixed build avoids the duplicate cleanup.

## Policy
When `no_crash x local_wrapper_usage_only_official_target_match` appears for `gml` under `honggfuzz-wrapper`, preserve the parser, format, and harness gates that the verifier proved before mutating the sink-specific relation. Treat official vulnerable/fixed divergence as the success gate; local crash labels are supporting signals only.

## Procedure
1. Start from the `[[gml]]` format contract and `[[honggfuzz-wrapper]]` harness contract; keep recognition, dispatch selectors, lengths, and state setup coherent until parser reachability is stable.
2. Apply the causal relation from the failure shape before broad mutation or seed sweeping.
3. Change one invariant at a time: selector-to-subparser, declared length-to-available data, container count-to-record body, lifetime/ownership state, allocation-size relation, or sanitizer-specific sink relation.
4. Submit only candidates where the vulnerable image reaches the target relation and the fixed image exits cleanly, rejects the relation, or otherwise avoids the target crash.

## Verifier Contract
This policy is ranked by 1 official target match. Re-rank or quarantine it if later use returns only clean exits, wrong sinks, wrapper-specific crashes, or fixed-image crashes.

## Negative Memory
- Do not corrupt the outer `gml` recognition gate while retargeting this signal.
- Do not count parser reachability, both-image crashes, local wrapper crashes, clean exits, or fixed-image crashes as success.
- Do not store payload bytes, exact positions, task identifiers, checksums, or submit metadata.

## Evidence Shape
- Support: server-verified round 37 solve after 12 attempts.
- Candidate family: seed_mutate.
- Official split: vulnerable exit 1, fixed exit 0, target_match True.
- Scope: generator repair and retargeting only.
