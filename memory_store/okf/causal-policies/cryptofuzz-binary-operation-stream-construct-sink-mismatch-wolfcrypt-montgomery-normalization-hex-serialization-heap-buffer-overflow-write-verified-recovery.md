---
type: causal-policy
title: "Cryptofuzz Binary Operation Stream Construct Sink Mismatch Wolfcrypt Montgomery Normalization Hex Serialization Heap Buffer Overflow Write Verified Recovery"
description: "Server-verified recovery for cryptofuzz-binary-operation-stream when wrong_sink pairs with sink_mismatch."
failure_class: "wrong_sink"
verifier_signal: "sink_mismatch"
candidate_family: "construct"
input_format: "cryptofuzz-binary-operation-stream"
harness_convention: "libfuzzer-cryptofuzz-binary-operation-stream"
vuln_class: "heap-buffer-overflow-write"
access_scope: generate
success_count: 1
confidence: high
tags: ["wrong-sink", "sink-mismatch", "cryptofuzz-binary-operation-stream", "libfuzzer-cryptofuzz-binary-operation-stream", "construct", "verified-recovery", "round-31"]
match_keys: ["wrong-sink", "sink-mismatch", "cryptofuzz-binary-operation-stream", "libfuzzer-cryptofuzz-binary-operation-stream", "construct", "heap-buffer-overflow-write", "verified-recovery"]
allowed_scopes: [generate]
forbidden_fields: [raw_poc_bytes, task_id, exact_offset, checksum, submit_metadata]
evidence_level: high
train_only: true
round: 31
---
# Cryptofuzz Binary Operation Stream Construct Sink Mismatch Wolfcrypt Montgomery Normalization Hex Serialization Heap Buffer Overflow Write Verified Recovery

- key: `wrong_sink x sink_mismatch`
- outcome: server-verified vulnerable/fixed split
- success_count: 1
- related format facts: [[cryptofuzz-binary-operation-stream]]
- related harness facts: [[libfuzzer-cryptofuzz-binary-operation-stream]]

## Policy
When `wrong_sink x sink_mismatch` appears for `cryptofuzz-binary-operation-stream`, first preserve the front-consumed operation envelope, then retarget modifier-controlled base conversion on the wolfCrypt normalization temporary instead of mutating bignum digits alone.

## Procedure
1. Use the Cryptofuzz binary operation stream envelope with a BignumCalc operation, not JSON or a raw wolfCrypt call.
2. Select the wolfCrypt modular-arithmetic wrapper and the Montgomery-normalization reduction path.
3. Use a unit single-word modulus so the normalization temporary has a stale zero representation in the vulnerable build.
4. Route the modifier stream through a hexadecimal base-conversion round trip on that temporary before it is consumed.

## Format Contract
Use [[cryptofuzz-binary-operation-stream]] with ordered operation payload, modifier blob, module selector, and continuation fields intact.

## Harness Contract
Use [[libfuzzer-cryptofuzz-binary-operation-stream]]; preserve the observed input contract before mutating deeper fields.

## Evidence Shape
- Support: 1 server-verified round 31 solve.
- Candidate family: construct.
- Verifier key: `wrong_sink x sink_mismatch`.
- Vulnerability class: `heap-buffer-overflow-write`.
- Recovery summary: The verified split depended on stale zero representation during hex serialization after Montgomery normalization.

## Negative Memory
- Do not count local-only crashes, both-image crashes, coarse sink labels, clean parser reachability, or fixed-build crashes as success for this key.
- Do not store raw payload bytes, exact positions, task identifiers, checksums, or submit metadata.
