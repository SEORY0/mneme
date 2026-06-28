---
type: causal-policy
title: "Wireshark Fuzzshark Ip Snmp Construct Target Stack Reached Despite Local Sink Mismatch Global Buffer Overflow Read Verified Recovery"
description: "Round 23 verified recovery for wrong_sink with verifier signal target_stack_reached_despite_local_sink_mismatch."
failure_class: "wrong_sink"
verifier_signal: "target_stack_reached_despite_local_sink_mismatch"
candidate_family: "construct"
input_format: "wireshark-fuzzshark-ip-snmp"
harness_convention: "afl-style-fuzzshark-ip"
vuln_class: "global-buffer-overflow-read"
access_scope: generate
success_count: 1
confidence: medium
tags: ["wrong-sink", "target-stack-reached-despite-local-sink-mismatch", "wireshark-fuzzshark-ip-snmp", "afl-style-fuzzshark-ip", "construct", "verified-recovery", "round-23"]
match_keys: ["wrong-sink", "target-stack-reached-despite-local-sink-mismatch", "wireshark-fuzzshark-ip-snmp", "afl-style-fuzzshark-ip", "global-buffer-overflow-read"]
allowed_scopes: [generate]
forbidden_fields: [raw_poc_bytes, task_id, exact_offset, checksum, submit_metadata]
evidence_level: high
train_only: true
round: 23
---
# Wireshark Fuzzshark Ip Snmp Construct Target Stack Reached Despite Local Sink Mismatch Global Buffer Overflow Read Verified Recovery

- key: `wrong_sink x target_stack_reached_despite_local_sink_mismatch`
- outcome: verified recovery
- success_count: 1
- failure_count: 0
- formats: [[wireshark-fuzzshark-ip-snmp]]
- harnesses: [[afl-style-fuzzshark-ip]]

## Failure Shape
Use the IP dissector harness with a TCP segment whose service port selects the SNMP dissector, then provide a syntactically valid BER SNMP message with a context-specific PDU tag outside the SNMP PDU value table. UDP wrapping is a dead end in this harness because that dissector path is disabled.

## Policy
For `wrong_sink x target_stack_reached_despite_local_sink_mismatch` on `wireshark-fuzzshark-ip-snmp`, preserve the format recognition, harness contract, and parser reachability gates before varying the causal invariant. Prefer `construct` while this format and harness contract are present.

## Procedure
1. Preserve the `wireshark-fuzzshark-ip-snmp` carrier enough for the `afl-style-fuzzshark-ip` harness to reach the observed parser path.
2. Keep envelope fields minimal and internally consistent so verifier feedback remains tied to the target relation.
3. Apply the verified invariant from the failure shape before broad mutation.
4. Submit only candidates where the vulnerable image reaches the target relation and the fixed image rejects or avoids it.

## Verifier Contract
The official vulnerable-versus-fixed target match is the confirmation gate for this policy; local crash class is supporting evidence only.

## Negative Memory
- Do not corrupt the outer `wireshark-fuzzshark-ip-snmp` recognition gate while retargeting this signal.
- Do not treat off-target crashes, clean parser exits, fixed-build crashes, or both-image crashes as success for this policy.
- Never store raw payload bytes, exact offsets, checksums, or task-local identifiers in memory.

## Evidence Shape
- Support: 1 server-verified round 23 solve after 7 attempts.
- Scope: generator repair only.
