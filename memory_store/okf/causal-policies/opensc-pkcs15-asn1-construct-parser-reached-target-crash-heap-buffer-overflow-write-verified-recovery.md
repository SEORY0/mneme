---
type: causal-policy
title: "Opensc Pkcs15 Asn1 Construct Parser Reached Target Crash Heap Buffer Overflow Write Verified Recovery"
description: "Server-verified recovery for opensc-pkcs15-asn1 when wrong_sink pairs with parser_reached_target_crash."
failure_class: "wrong_sink"
verifier_signal: "parser_reached_target_crash"
candidate_family: "construct"
input_format: "opensc-pkcs15-asn1"
harness_convention: "honggfuzz"
vuln_class: "heap-buffer-overflow-write"
access_scope: generate
success_count: 1
confidence: high
tags: ["wrong-sink", "parser-reached-target-crash", "opensc-pkcs15-asn1", "honggfuzz", "construct", "verified-recovery", "round-17"]
match_keys: ["wrong-sink", "parser-reached-target-crash", "opensc-pkcs15-asn1", "honggfuzz", "construct", "heap-buffer-overflow-write", "verified-recovery"]
allowed_scopes: [generate]
forbidden_fields: [raw_poc_bytes, task_id, exact_offset, checksum, submit_metadata]
evidence_level: high
train_only: true
round: 17
---
# Opensc Pkcs15 Asn1 Construct Parser Reached Target Crash Heap Buffer Overflow Write Verified Recovery

- key: `wrong_sink x parser_reached_target_crash`
- outcome: server-verified vulnerable/fixed split
- success_count: 1
- related format facts: [[opensc-pkcs15-asn1]]
- related harness facts: [[honggfuzz]]

## Policy
When `wrong_sink x parser_reached_target_crash` appears for `opensc-pkcs15-asn1`, preserve the parser or harness carrier already shown to reach the target branch. Retarget only the causal invariant named by the verifier signal and vulnerability class; do not broaden into unrelated container families after reachability is established.

## Procedure
1. Use a DER-like PKCS#15 reader input with a valid outer constructed envelope and an oversized nested object carrying a long path-like byte string.
2. The reader reaches AuthentIC PKCS#15 path handling, where an unsafe copy can overlap or overrun when processing long path material.
3. The fixed image rejects or copies the path safely.
4. Submit only candidates that preserve the same accepted carrier and separate vulnerable-build failure from fixed-build clean behavior.

## Negative Memory
- Do not treat local-only crashes, both-image crashes, or coarse sink labels as success for this key.
- Do not store raw payload bytes, exact positions, task identifiers, checksums, or submit metadata.

## Format Contract
Use [[opensc-pkcs15-asn1]]; the relevant gate is the accepted carrier plus the invariant described above, not a byte-specific recipe.

## Harness Contract
Use [[honggfuzz]]; preserve the observed input contract before mutating deeper fields.

## Evidence Shape
- Support: 1 server-verified round 17 solve.
- Candidate family: construct.
