---
type: causal-policy
title: "OPC UA Binary Message Seed Mutate Verified Recovery"
description: "Round 6 verified recovery for generic_crash with verifier signal parser_reached_target_crash_vul_only."
failure_class: "generic_crash"
verifier_signal: "parser_reached_target_crash_vul_only"
candidate_family: "seed_mutate"
input_format: "opc-ua-binary-message"
harness_convention: "libfuzzer"
vuln_class: "allocation-failure-null-dereference"
access_scope: generate
success_count: 1
confidence: high
tags: ["generic-crash", "parser-reached-target-crash-vul-only", "opc-ua-binary-message", "seed-mutate", "verified-recovery", "round-6"]
match_keys: ["generic_crash", "parser_reached_target_crash_vul_only", "opc-ua-binary-message", "libfuzzer", "allocation-failure-null-dereference", "verified_recovery"]
allowed_scopes: [generate]
forbidden_fields: [raw_poc_bytes, task_id, exact_offset, checksum, submit_metadata]
evidence_level: high
train_only: true
round: 6
---
# OPC UA Binary Message Seed Mutate Verified Recovery

## Policy
For `generic_crash x parser_reached_target_crash_vul_only`, preserve the format and harness gates that reached the parser/sink, then apply the verified causal relation below. This is a positive recovery policy because the official vulnerable/fixed verifier recorded a target match.

## Procedure
1. Start from a generated valid OPC UA binary message corpus input so the stack parser accepts the envelope. Preserve the message bytes and change only the harness memory-limit suffix so the server-side/network-layer allocation fails inside the stack path; the vulnerable build continues through the failed allocation while the fixed build rejects it.
2. Keep the carrier abstract: preserve the gate/invariant relation, not any task-local bytes or offsets.
3. If a later candidate changes the verifier signal, re-rank against the new failure key before mutating unrelated fields.

## Format Contract
- The accepted input is an OPC UA binary message blob; valid corpus messages contain the message header and body structure needed to reach the open62541 stack parser. Mutating the parser payload itself is less useful than preserving a known-good message and changing the harness-controlled resource limit.
- Harness: The libFuzzer harness treats the input prefix as the binary message and consumes a fixed-width suffix from the back as a memory limit. The crash depends on satisfying the binary message parser and then forcing allocation failure through that suffix.

## Negative Memory
- Do not broaden mutations after the parser/harness gate is proven.
- Do not submit candidates that reproduce on the fixed image or move to an off-target wrapper crash.
- Do not store raw payload bytes, exact offsets, checksums, or task-local identifiers.

## Evidence Shape
- Support: one round-6 worker trace with official target match.
- Scope: generator repair for the same failure-keyed basin.
