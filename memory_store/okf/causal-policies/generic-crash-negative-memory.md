---
type: causal-policy
title: Generic Crash Negative Memory
description: Abstract negative memory for crashes without enough sink or target evidence.
failure_class: generic_crash
verifier_signal: sanitizer_crash
candidate_family: unknown
input_format: any
harness_convention: any
access_scope: generate
success_count: 4
confidence: low
tags: [generic_crash, sanitizer_crash, unknown, overlarge_mutation_trap, negative_memory]
match_keys: [generic_crash, sanitizer_crash, unknown, overlarge_mutation_trap, negative_memory]
allowed_scopes: [generate]
forbidden_fields: [raw_poc_bytes, task_id, exact_offset, checksum, submit_metadata]
evidence_level: low
train_only: true
---
## Policy
Treat a crash without target evidence as a basin to escape. It may prove the input is accepted, but
it should not anchor the next candidate unless a later verifier signal links it to the expected
sink.

## Procedure
1. Shrink the candidate to the smallest form that still reaches parsing.
2. Remove broad corruption and keep only fields that can plausibly affect the target invariant.
3. Replace extreme integer, length, and count values with near-boundary values.
4. If the crash remains generic, switch candidate family: seed mutation to declarative skeleton, or
   skeleton to seed mutation.
5. Record the failed family as negative memory for this attempt only.

## Negative Memory
- Overlarge lengths, counts, and recursion depths often create fixed-build crashes or parser aborts.
- Random byte corruption after the magic gate usually destroys causal attribution.
- Generic sanitizer output is insufficient for final confidence.

## Evidence Shape
- Support: 4 abstract train-set observations.
- Confidence: low.
- Scope: generator repair only.
