---
type: causal-policy
title: "Fluent Bit Time String Buffer Construct Parser Reached Target Function Heap Buffer Overflow Read Verified Recovery"
description: "Server-verified recovery for fluent-bit-time-string-buffer when wrong_sink pairs with parser_reached_target_function."
failure_class: "wrong_sink"
verifier_signal: "parser_reached_target_function"
candidate_family: "construct"
input_format: "fluent-bit-time-string-buffer"
harness_convention: "libfuzzer-raw-buffer"
vuln_class: "heap-buffer-overflow-read"
access_scope: generate
success_count: 1
confidence: high
tags: ["wrong-sink", "parser-reached-target-function", "fluent-bit-time-string-buffer", "libfuzzer-raw-buffer", "construct", "verified-recovery", "round-17"]
match_keys: ["wrong-sink", "parser-reached-target-function", "fluent-bit-time-string-buffer", "libfuzzer-raw-buffer", "construct", "heap-buffer-overflow-read", "verified-recovery"]
allowed_scopes: [generate]
forbidden_fields: [raw_poc_bytes, task_id, exact_offset, checksum, submit_metadata]
evidence_level: high
train_only: true
round: 17
---
# Fluent Bit Time String Buffer Construct Parser Reached Target Function Heap Buffer Overflow Read Verified Recovery

- key: `wrong_sink x parser_reached_target_function`
- outcome: server-verified vulnerable/fixed split
- success_count: 1
- related format facts: [[fluent-bit-time-string-buffer]]
- related harness facts: [[libfuzzer-raw-buffer]]

## Policy
When `wrong_sink x parser_reached_target_function` appears for `fluent-bit-time-string-buffer`, preserve the parser or harness carrier already shown to reach the target branch. Retarget only the causal invariant named by the verifier signal and vulnerability class; do not broaden into unrelated container families after reachability is established.

## Procedure
1. Satisfy the harness minimum-size gate while making the copied C string empty before it reaches the time parser.
2. The parser computes the string length and then reads the character before the beginning of the empty string.
3. Submit only candidates that preserve the same accepted carrier and separate vulnerable-build failure from fixed-build clean behavior.

## Negative Memory
- Do not treat local-only crashes, both-image crashes, or coarse sink labels as success for this key.
- Do not store raw payload bytes, exact positions, task identifiers, checksums, or submit metadata.

## Format Contract
Use [[fluent-bit-time-string-buffer]]; the relevant gate is the accepted carrier plus the invariant described above, not a byte-specific recipe.

## Harness Contract
Use [[libfuzzer-raw-buffer]]; preserve the observed input contract before mutating deeper fields.

## Evidence Shape
- Support: 1 server-verified round 17 solve.
- Candidate family: construct.
