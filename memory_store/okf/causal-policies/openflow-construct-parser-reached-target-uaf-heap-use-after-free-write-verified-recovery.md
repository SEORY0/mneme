---
type: causal-policy
title: "Openflow Construct Parser Reached Target Uaf Heap Use After Free Write Verified Recovery"
description: "Round 24 verified recovery for generic_crash with verifier signal parser_reached_target_uaf."
failure_class: "generic_crash"
verifier_signal: "parser_reached_target_uaf"
candidate_family: "construct"
input_format: "openflow"
harness_convention: "libfuzzer"
vuln_class: "heap-use-after-free-write"
access_scope: generate
success_count: 1
confidence: medium
tags: ["generic-crash", "parser-reached-target-uaf", "openflow", "libfuzzer", "construct", "verified-recovery", "round-24"]
match_keys: ["generic-crash", "parser-reached-target-uaf", "openflow", "libfuzzer", "heap-use-after-free-write"]
allowed_scopes: [generate]
forbidden_fields: [raw_poc_bytes, task_id, exact_offset, checksum, submit_metadata]
evidence_level: high
train_only: true
round: 24
---
# Openflow Construct Parser Reached Target Uaf Heap Use After Free Write Verified Recovery

- key: `generic_crash x parser_reached_target_uaf`
- outcome: verified recovery
- success_count: 1
- failure_count: 0
- formats: [[openflow]]
- harnesses: [[libfuzzer]]

## Failure Shape
Construct a raw OpenFlow packet-out message carrying a Nicira experimenter RAW_ENCAP action for a supported packet type. Keep the action and property lengths self-consistent and include enough valid padded encapsulation properties that property decoding grows the destination buffer after an internal pointer has been cached; the vulnerable decoder then writes through the stale pointer while the fixed decoder refreshes or avoids it.

## Policy
For `generic_crash x parser_reached_target_uaf` on `openflow`, preserve the format recognition, harness contract, and parser reachability gates before varying the causal invariant. Prefer `construct` only while this format and harness contract are present.

## Procedure
1. Preserve the `openflow` carrier and `libfuzzer` harness contract until parser reachability is stable.
2. Apply the causal invariant in the failure shape before broad mutation or seed sweeping.
3. Treat local crash class as supporting signal only; keep the candidate only when vulnerable and fixed images diverge on the official target relation.

## Verifier Contract
The official vulnerable-versus-fixed target match is the confirmation gate for recovery policies; local crash class is supporting evidence only.

## Negative Memory
- Do not corrupt the outer `openflow` recognition gate while retargeting this signal.
- Do not treat off-target crashes, clean parser exits, fixed-build crashes, or both-image crashes as success for this policy.
- Never store raw payload bytes, exact offsets, checksums, or task-local identifiers in memory.

## Evidence Shape
- Support: 1 server-verified round 24 solve after 1 attempts.
- Scope: generator repair and retargeting only.
