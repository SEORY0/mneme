---
type: causal-policy
title: "No Crash Clean Exit PHP Hashcontext Unserialize Negative Memory"
description: "Round 9 negative memory for no_crash with verifier signal clean_exit."
failure_class: "no_crash"
verifier_signal: "clean_exit"
candidate_family: "construct"
input_format: "php-hashcontext-unserialize"
harness_convention: "libfuzzer"
vuln_class: "buffer-overflow"
access_scope: generate
success_count: 0
confidence: medium
tags: ["no-crash", "clean-exit", "php-hashcontext-unserialize", "negative-memory", "round-9"]
match_keys: ["no_crash", "clean_exit", "php-hashcontext-unserialize", "libfuzzer", "buffer-overflow", "negative_memory"]
allowed_scopes: [generate]
forbidden_fields: [raw_poc_bytes, task_id, exact_offset, checksum, submit_metadata]
evidence_level: medium
train_only: true
round: 9
---
# No Crash Clean Exit PHP Hashcontext Unserialize Negative Memory

- key: `no_crash x clean_exit`
- outcome: persistent failure / basin to avoid
- success_count: 0
- failure_count: 1
- related format facts: [[php-hashcontext-unserialize]]
- related harness facts: [[libfuzzer]]

## Failure Shape
- Serialized HashContext-shaped candidates with xxhash algorithm names and oversized internal string
  fields were accepted by the runner but exited cleanly, indicating the serialized envelope did not
  instantiate a valid HashContext state that reached the vulnerable xxhash unserializer.

## Policy
Treat `no_crash x clean_exit` on `php-hashcontext-unserialize` as a basin to avoid unless a new candidate changes the parser gate, state relation, or official target sink. Preserve any proven reachability, but reject variants that return to the same verifier signal without changing the causal gate under test.

## Procedure
1. Keep only the smallest parser or harness envelope that the verifier proved was reached.
2. Identify the missing causal relation from the signal: parser selection, container acceptance, length relation, stateful subobject, allocation state, or official target sink.
3. Change one relation at a time and discard candidates that return to the same clean-exit, off-target-crash, wrong-sink, usage-only, or both-image-crash basin.
4. If a local crash is not an official target match, shrink or discard it before mutating deeper fields.
5. Promote a recovery from this basin only after a later verifier-confirmed target match.

## Format Contract
- The fuzzer splits raw input at a separator into an update string and a PHP serialized value.
- Only if the serialized value becomes a HashContext object does it call hash_update and hash_final.
- HashContext unserialization expects an array carrying algorithm, options, internal hash state,
  magic value, and object members.

## Harness Contract
- The target is a libFuzzer single-input runner.
- It consumes the raw file directly, searches for the front separator, unserializes the remaining
  bytes, and conditionally invokes PHP hash operations on the resulting object.

## Negative Memory
- Do not resubmit broad mutations that only reproduce `clean_exit`.
- Do not count parser reachability, both-image crashes, local wrapper crashes, clean exits, or fixed-image crashes as success.
- Do not store raw payload bytes, exact positions, task identifiers, or submit metadata.

## Evidence Shape
- Support: one diagnosed persistent failure from round 9.
- Scope: generator repair and basin avoidance only.
