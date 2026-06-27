---
type: causal-policy
title: "Fluent Bit Signv4 Fuzzer Buffer Construct Parser Reached Target Sink Heap Buffer Overflow Read Verified Recovery"
description: "Server-verified recovery for fluent-bit-signv4-fuzzer-buffer when generic_crash pairs with parser_reached_target_sink."
failure_class: "generic_crash"
verifier_signal: "parser_reached_target_sink"
candidate_family: "construct"
input_format: "fluent-bit-signv4-fuzzer-buffer"
harness_convention: "libfuzzer"
vuln_class: "heap-buffer-overflow-read"
access_scope: generate
success_count: 1
confidence: high
tags: ["generic-crash", "parser-reached-target-sink", "fluent-bit-signv4-fuzzer-buffer", "libfuzzer", "construct", "verified-recovery", "round-17"]
match_keys: ["generic-crash", "parser-reached-target-sink", "fluent-bit-signv4-fuzzer-buffer", "libfuzzer", "construct", "heap-buffer-overflow-read", "verified-recovery"]
allowed_scopes: [generate]
forbidden_fields: [raw_poc_bytes, task_id, exact_offset, checksum, submit_metadata]
evidence_level: high
train_only: true
round: 17
---
# Fluent Bit Signv4 Fuzzer Buffer Construct Parser Reached Target Sink Heap Buffer Overflow Read Verified Recovery

- key: `generic_crash x parser_reached_target_sink`
- outcome: server-verified vulnerable/fixed split
- success_count: 1
- related format facts: [[fluent-bit-signv4-fuzzer-buffer]]
- related harness facts: [[libfuzzer]]

## Policy
When `generic_crash x parser_reached_target_sink` appears for `fluent-bit-signv4-fuzzer-buffer`, preserve the parser or harness carrier already shown to reach the target branch. Retarget only the causal invariant named by the verifier signal and vulnerability class; do not broaden into unrelated container families after reachability is established.

## Procedure
1. Use the harness selector for a signed request buffer, satisfy the minimum field split for method, URI, and body, and provide a canonicalization path whose URI begins at a boundary that makes path normalization inspect outside the URI buffer.
2. The important invariant is that the normalizer assumes there is a preceding path byte when reducing the canonical URI.
3. Submit only candidates that preserve the same accepted carrier and separate vulnerable-build failure from fixed-build clean behavior.

## Negative Memory
- Do not treat local-only crashes, both-image crashes, or coarse sink labels as success for this key.
- Do not store raw payload bytes, exact positions, task identifiers, checksums, or submit metadata.

## Format Contract
Use [[fluent-bit-signv4-fuzzer-buffer]]; the relevant gate is the accepted carrier plus the invariant described above, not a byte-specific recipe.

## Harness Contract
Use [[libfuzzer]]; preserve the observed input contract before mutating deeper fields.

## Evidence Shape
- Support: 1 server-verified round 17 solve.
- Candidate family: construct.
