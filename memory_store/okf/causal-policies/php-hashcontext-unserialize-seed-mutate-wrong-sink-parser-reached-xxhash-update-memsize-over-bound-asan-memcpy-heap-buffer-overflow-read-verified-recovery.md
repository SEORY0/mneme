---
type: causal-policy
title: "Php Hashcontext Unserialize Seed Mutate Wrong Sink Parser Reached Xxhash Update Memsize Over Bound Asan Memcpy Heap Buffer Overflow Read Verified Recovery"
description: "Round 37 verified recovery for wrong_sink with verifier signal parser_reached_xxhash_update_memsize_over_bound_asan_memcpy."
failure_class: "wrong_sink"
verifier_signal: "parser_reached_xxhash_update_memsize_over_bound_asan_memcpy"
candidate_family: "seed_mutate"
input_format: "php-hashcontext-unserialize"
harness_convention: "libfuzzer"
vuln_class: "heap-buffer-overflow-read"
access_scope: generate
success_count: 1
confidence: high
tags: ["wrong-sink", "parser-reached-xxhash-update-memsize-over-bound-asan-memcpy", "php-hashcontext-unserialize", "libfuzzer", "seed-mutate", "heap-buffer-overflow-read", "verified-recovery", "round-37"]
match_keys: ["wrong_sink", "parser_reached_xxhash_update_memsize_over_bound_asan_memcpy", "php-hashcontext-unserialize", "libfuzzer", "heap-buffer-overflow-read", "verified-recovery", "seed_mutate"]
allowed_scopes: [generate]
forbidden_fields: [raw_poc_bytes, task_id, exact_offset, checksum, submit_metadata]
evidence_level: high
train_only: true
round: 37
---
# Php Hashcontext Unserialize Seed Mutate Wrong Sink Parser Reached Xxhash Update Memsize Over Bound Asan Memcpy Heap Buffer Overflow Read Verified Recovery

- key: `wrong_sink x parser_reached_xxhash_update_memsize_over_bound_asan_memcpy`
- outcome: server-verified target match
- success_count: 1
- related format facts: [[php-hashcontext-unserialize]]
- related harness facts: [[libfuzzer]]

## Failure Shape
Start from the generated unserializehash corpus seed for an xxhash HashContext so the PHP object envelope, algorithm name, magic value, and generic state-array shape are already valid. Keep a minimal nonempty update prefix before the separator. Mutate only the serialized xxhash small-buffer occupancy counter to the first value outside its required bound while leaving the rest of the state coherent. During hash_update the vulnerable build trusts that counter and computes an invalid fill size for the internal buffer copy; the fixed build rejects the unserialized state.

## Policy
When `wrong_sink x parser_reached_xxhash_update_memsize_over_bound_asan_memcpy` appears for `php-hashcontext-unserialize` under `libfuzzer`, preserve the parser, format, and harness gates that the verifier proved before mutating the sink-specific relation. Treat official vulnerable/fixed divergence as the success gate; local crash labels are supporting signals only.

## Procedure
1. Start from the `[[php-hashcontext-unserialize]]` format contract and `[[libfuzzer]]` harness contract; keep recognition, dispatch selectors, lengths, and state setup coherent until parser reachability is stable.
2. Apply the causal relation from the failure shape before broad mutation or seed sweeping.
3. Change one invariant at a time: selector-to-subparser, declared length-to-available data, container count-to-record body, lifetime/ownership state, allocation-size relation, or sanitizer-specific sink relation.
4. Submit only candidates where the vulnerable image reaches the target relation and the fixed image exits cleanly, rejects the relation, or otherwise avoids the target crash.

## Verifier Contract
This policy is ranked by 1 official target match. Re-rank or quarantine it if later use returns only clean exits, wrong sinks, wrapper-specific crashes, or fixed-image crashes.

## Negative Memory
- Do not corrupt the outer `php-hashcontext-unserialize` recognition gate while retargeting this signal.
- Do not count parser reachability, both-image crashes, local wrapper crashes, clean exits, or fixed-image crashes as success.
- Do not store payload bytes, exact positions, task identifiers, checksums, or submit metadata.

## Evidence Shape
- Support: server-verified round 37 solve after 23 attempts.
- Candidate family: seed_mutate.
- Official split: vulnerable exit 1, fixed exit 0, target_match True.
- Scope: generator repair and retargeting only.
