---
type: causal-policy
title: "Iso9660 Seed Mutate Parser Reached Target Sink Stack Buffer Overflow Write Verified Recovery"
description: "Round 26 verified recovery for generic_crash with verifier signal parser_reached_target_sink."
failure_class: "generic_crash"
verifier_signal: "parser_reached_target_sink"
candidate_family: "seed_mutate"
input_format: "iso9660"
harness_convention: "libfuzzer"
vuln_class: "stack-buffer-overflow-write"
access_scope: generate
success_count: 1
confidence: high
tags: ["generic-crash", "parser-reached-target-sink", "iso9660", "libfuzzer", "seed-mutate", "verified-recovery", "round-26"]
match_keys: ["generic_crash", "parser_reached_target_sink", "iso9660", "libfuzzer", "stack-buffer-overflow-write", "verified_recovery"]
allowed_scopes: [generate]
forbidden_fields: [raw_poc_bytes, task_id, exact_offset, checksum, submit_metadata]
evidence_level: high
train_only: true
round: 26
---
# Iso9660 Seed Mutate Parser Reached Target Sink Stack Buffer Overflow Write Verified Recovery

- key: `generic_crash x parser_reached_target_sink`
- outcome: verified recovery
- success_count: 1
- failure_count: 0
- formats: [[iso9660]]
- harnesses: [[libfuzzer]]

## Failure Shape
Start from a valid ISO9660 image that already contains both a primary descriptor and a Joliet supplementary descriptor. Preserve the descriptor signatures and Joliet escape gate, then mutate a long paired metadata field so the ASCII side begins with replacement placeholders and continues with ordinary ASCII while the Joliet side begins with high-codepoint UTF-16BE surrogate pairs. This keeps the merge predicate true while making the decoded output require more bytes than the fixed local buffer.

## Policy
For `generic_crash x parser_reached_target_sink` on `iso9660`, preserve the format recognition and harness contract before varying the vulnerable invariant. Prefer `seed_mutate` only while that carrier and harness contract remain stable.

## Procedure
1. Preserve the `iso9660` carrier and `libfuzzer` harness contract until parser reachability is stable.
2. Apply the causal invariant in the failure shape before broad mutation or seed sweeping.
3. Treat local crash class as supporting signal only; keep the candidate only when vulnerable and fixed images diverge on the official target relation.

## Verifier Contract
The official vulnerable-versus-fixed target match is the confirmation gate for this recovery policy; local crash class is supporting evidence only.

## Negative Memory
- Do not corrupt the outer `iso9660` recognition gate while retargeting this signal.
- Do not treat off-target crashes, clean parser exits, fixed-build crashes, or both-image crashes as success for this policy.
- Never store raw payload bytes, exact offsets, checksums, or task-local identifiers in memory.

## Format Contract
ISO9660 probing expects volume descriptors after the reserved leading area. A primary descriptor provides ASCII metadata, a Joliet supplementary descriptor provides UTF-16BE metadata, and the supplementary descriptor is accepted only when its escape sequence identifies a Joliet variant. Several metadata identifiers are merged by treating the Joliet value as a prefix of the ASCII value with replacement placeholders for non-ASCII characters.

## Harness Contract
The fuzzer writes the whole PoC to a temporary file, opens a libblkid probe on that file, enables partition and superblock probing, and calls safe probing. There is no FuzzedDataProvider layout, mode byte, external checksum repair, or stdin protocol; the PoC must be a coherent disk-image-like byte stream.

## Evidence Shape
- Support: 1 server-verified round 26 solve after 1 attempts.
- Scope: generator repair and retargeting only.
