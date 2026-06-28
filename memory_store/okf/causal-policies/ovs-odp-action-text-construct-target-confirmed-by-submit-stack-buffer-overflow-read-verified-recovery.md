---
type: causal-policy
title: "Ovs Odp Action Text Construct Target Confirmed By Submit Stack Buffer Overflow Read Verified Recovery"
description: "Round 25 verified recovery for generic_crash with verifier signal target_confirmed_by_submit."
failure_class: "generic_crash"
verifier_signal: "target_confirmed_by_submit"
candidate_family: "construct"
input_format: "ovs-odp-action-text"
harness_convention: "libfuzzer"
vuln_class: "stack-buffer-overflow-read"
access_scope: generate
success_count: 1
confidence: medium
tags: ["generic-crash", "target-confirmed-by-submit", "ovs-odp-action-text", "libfuzzer", "construct", "verified-recovery", "round-25"]
match_keys: ["generic_crash", "target_confirmed_by_submit", "ovs-odp-action-text", "libfuzzer", "stack-buffer-overflow-read"]
allowed_scopes: [generate]
forbidden_fields: [raw_poc_bytes, task_id, exact_offset, checksum, submit_metadata]
evidence_level: high
train_only: true
round: 25
---
# Ovs Odp Action Text Construct Target Confirmed By Submit Stack Buffer Overflow Read Verified Recovery

- key: `generic_crash x target_confirmed_by_submit`
- outcome: verified recovery
- success_count: 1
- failure_count: 0
- formats: [[ovs-odp-action-text]]
- harnesses: [[libfuzzer]]

## Failure Shape
Use the raw OVS datapath action text contract: a NUL-terminated action string with no newline. Select the NSH push action with metadata type 2 and provide md2 metadata large enough to force backing-buffer growth/padding while preserving valid action syntax. The vulnerable path serializes from the stale stack metadata area; the fixed path rejects or avoids that relation.

## Policy
For `generic_crash x target_confirmed_by_submit` on `ovs-odp-action-text`, preserve the format recognition and harness contract before varying the vulnerable invariant. Prefer `construct` only while that carrier and harness contract remain stable.

## Procedure
1. Preserve the `ovs-odp-action-text` carrier and `libfuzzer` harness contract until parser reachability is stable.
2. Apply the causal invariant in the failure shape before broad mutation or seed sweeping.
3. Treat local crash class as supporting signal only; keep the candidate only when vulnerable and fixed images diverge on the official target relation.

## Verifier Contract
The official vulnerable-versus-fixed target match is the confirmation gate for this recovery policy; local crash class is supporting evidence only.

## Negative Memory
- Do not corrupt the outer `ovs-odp-action-text` recognition gate while retargeting this signal.
- Do not treat off-target crashes, clean parser exits, fixed-build crashes, or both-image crashes as success for this policy.
- Never store raw payload bytes, exact offsets, checksums, or task-local identifiers in memory.

## Format Contract
OVS ODP action text is comma-delimited C-string action syntax. The push_nsh action accepts named fields including metadata type and an md2 hexadecimal metadata field. The md2 text is decoded to bytes, padded to word alignment, and serialized into a nested action attribute.

## Harness Contract
The fuzzer passes the whole input as a C string only if it has at least one payload byte, a final NUL terminator, and no newline. The same string is tried as key text and action text; there is no binary netlink envelope, or provider-carved layout.

## Evidence Shape
- Support: 1 server-verified round 25 solve after 1 attempt.
- Scope: generator repair and retargeting only.
