---
type: causal-policy
title: "No Crash Local Wrapper Target Mismatch Msgpack Ext Negative Memory"
description: "Round 7 negative memory for no_crash with verifier signal local_wrapper_target_mismatch."
failure_class: "no_crash"
verifier_signal: "local_wrapper_target_mismatch"
candidate_family: "construct"
input_format: "msgpack-ext"
harness_convention: "libfuzzer"
vuln_class: "assertion-or-invalid-extension-handling"
access_scope: generate
success_count: 0
confidence: medium
tags: ["no-crash", "local-wrapper-target-mismatch", "msgpack-ext", "negative-memory", "round-7"]
match_keys: ["no_crash", "local_wrapper_target_mismatch", "msgpack-ext", "libfuzzer", "assertion-or-invalid-extension-handling", "negative_memory"]
allowed_scopes: [generate]
forbidden_fields: [raw_poc_bytes, task_id, exact_offset, checksum, submit_metadata]
evidence_level: medium
train_only: true
round: 7
---
# No Crash Local Wrapper Target Mismatch Msgpack Ext Negative Memory

- key: `no_crash x local_wrapper_target_mismatch`
- outcome: persistent failure / basin to avoid
- success_count: 0
- failure_count: 1
- related format facts: [[msgpack-ext]]
- related harness facts: [[libfuzzer]]

## Failure Shape
Task-specific MessagePack datetime extension candidates did not solve officially, and local verify
ran a Lua-loadbuffer target rather than the datetime/MessagePack target. The likely missing gate is
the exact Tarantool MsgPack decoder path that installs and relies on the custom extension checker.

## Policy
Treat `no_crash x local_wrapper_target_mismatch` on `msgpack-ext` as a basin to avoid unless a new candidate changes the specific parser gate, state relation, or sink relation described below. Preserve any proven reachability, but reject variants that return the same verifier signal without changing the causal gate under test.

## Procedure
1. Keep only the smallest parser or harness envelope that the verifier proved was reached.
2. Identify the missing causal relation from the signal: parser selection, container acceptance, length relation, stateful subobject, allocation state, or official target sink.
3. Change one relation at a time and discard candidates that return to the same clean-exit, off-target-crash, wrong-sink, usage-only, or both-image-crash basin.
4. If a local crash is not an official target match, shrink or discard it before mutating deeper fields.
5. Promote a recovery from this basin only after a later verifier-confirmed target match.

## Negative Memory
- Do not resubmit broad mutations that only reproduce `local_wrapper_target_mismatch`.
- Do not count parser reachability, both-image crashes, local wrapper crashes, or clean exits as success.
- Do not store raw payload bytes, exact positions, task identifiers, or submit metadata.

## Format Contract
Tarantool datetime values are encoded as MessagePack extension values with a datetime extension type
and either a required epoch payload or an epoch plus tail fields. The datetime unpacker validates
epoch range, nanosecond range, timezone offset, and timezone index after decoding raw payload
fields.

## Harness Contract
The source tree contains a raw mp_datetime fuzzer that passes bytes directly to datetime_unpack, but
the local wrapper output for this image showed a different protobuf-backed Lua fuzzer. This mismatch
made local parser-reachability feedback unreliable for the described MsgPack extension bug.

## Evidence Shape
- Support: 1 diagnosed persistent failure from round 7.
- Scope: generator repair and basin avoidance only.
