---
type: causal-policy
title: "Protobuf Text Mruby Function Construct Target Sink Reached Invalid Read Verified Recovery"
description: "Round 14 server-verified recovery for protobuf-text-mruby-function keyed by generic_crash x target_sink_reached."
failure_class: "generic_crash"
verifier_signal: "target_sink_reached"
candidate_family: "construct"
input_format: "protobuf-text-mruby-function"
harness_convention: "libfuzzer-libprotobuf-mutator"
vuln_class: "invalid-read"
access_scope: generate
success_count: 1
confidence: high
tags: ["generic-crash", "target-sink-reached", "protobuf-text-mruby-function", "libfuzzer-libprotobuf-mutator", "construct", "invalid-read", "verified-recovery", "round-14"]
match_keys: ["generic_crash", "target_sink_reached", "protobuf-text-mruby-function", "libfuzzer-libprotobuf-mutator", "invalid-read", "verified_recovery"]
allowed_scopes: [generate]
forbidden_fields: [raw_poc_bytes, task_id, exact_offset, checksum, submit_metadata]
evidence_level: high
train_only: true
round: 14
---
# Protobuf Text Mruby Function Construct Target Sink Reached Invalid Read Verified Recovery

- key: `generic_crash x target_sink_reached`
- outcome: server-verified target match
- success_count: 1
- related format facts: [[protobuf-text-mruby-function]]
- related harness facts: [[libfuzzer-libprotobuf-mutator]]

## Policy
When `protobuf-text-mruby-function` under `libfuzzer-libprotobuf-mutator` reaches `target_sink_reached` from `generic_crash`, keep the accepted carrier and retarget the single invariant named by the verified recovery. This policy is verifier-gated by vulnerable-build failure and fixed-build non-match behavior.

## Procedure
1. Preserve the harness contract `[[libfuzzer-libprotobuf-mutator]]` and format contract `[[protobuf-text-mruby-function]]`; do not switch container families once parser reachability is proven.
2. Apply the verified recovery: Use the protobuf-text Function schema rather than raw Ruby. Build a valid generated Ruby function that repeatedly grows an integer into a BigInt through arithmetic assignments, then compare a small non-BigInt left operand against the BigInt value on the right. That reaches the numeric comparison helper path that incorrectly dispatches the BigInt comparison for the wrong operand side.
3. Keep mutations focused on the gate relation: declared size versus available data, selector versus subparser, structure count versus actual records, lifetime ownership, or sink-specific state.
4. If local labels report `wrong_sink` while the same parser branch is reached, submit once to check the official target match before discarding the candidate.
5. If the fixed image also fails, shrink back to the smallest boundary relation and avoid broad randomization.

## Negative Memory
- Do not replay unrelated seeds after this parser branch is reached.
- Do not store concrete payload bytes, task identifiers, exact positions, checksums, or submit metadata.
- Do not promote this as a byte recipe; it is a format-gate and sink-invariant relation.

## Evidence Shape
- Support: one server-verified Round 14 solve.
- Candidate family: construct.
