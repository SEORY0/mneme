---
type: causal-policy
title: "Wireshark Fuzzshark Ip Gsmtap Rlcmac Construct Generic Crash Parser Reached Target Match Global Buffer Overflow Read Verified Recovery"
description: "Round 30 verified recovery for generic_crash with verifier signal parser_reached_target_match."
failure_class: "generic_crash"
verifier_signal: "parser_reached_target_match"
candidate_family: "construct"
input_format: "wireshark-fuzzshark-ip-gsmtap-rlcmac"
harness_convention: "libfuzzer-fuzzshark-ip"
vuln_class: "global-buffer-overflow-read"
access_scope: generate
success_count: 1
confidence: medium
tags: ["generic-crash", "parser-reached-target-match", "wireshark-fuzzshark-ip-gsmtap-rlcmac", "libfuzzer-fuzzshark-ip", "construct", "verified-recovery", "round-30"]
match_keys: ["generic-crash", "parser-reached-target-match", "wireshark-fuzzshark-ip-gsmtap-rlcmac", "libfuzzer-fuzzshark-ip", "global-buffer-overflow-read"]
allowed_scopes: [generate]
forbidden_fields: [raw_poc_bytes, task_id, exact_offset, checksum, submit_metadata]
evidence_level: high
train_only: true
round: 30
---
# Wireshark Fuzzshark Ip Gsmtap Rlcmac Construct Generic Crash Parser Reached Target Match Global Buffer Overflow Read Verified Recovery

- key: `generic-crash x parser-reached-target-match`
- outcome: verified recovery
- success_count: 1
- failure_count: 0
- formats: [[wireshark-fuzzshark-ip-gsmtap-rlcmac]]
- harnesses: [[libfuzzer-fuzzshark-ip]]

## Failure Shape
Wrap an uplink GSM RLC/MAC control block in GSMTAP over UDP over a raw IPv4 packet. Use GSMTAP fields that dispatch to the uplink Packet Resource Request parser, take the release-additions path into the IU-mode channel-request descriptor, then make the terminal next-exists predicate false so the CSN descriptor skip logic advances past the descriptor sentinel.

## Policy
For `generic-crash x parser-reached-target-match` on `wireshark-fuzzshark-ip-gsmtap-rlcmac`, preserve the parser and harness gates first, then mutate only the causal invariant described by the verified trace. Prefer `construct` while this format and harness contract are present.

## Procedure
1. Preserve the `wireshark-fuzzshark-ip-gsmtap-rlcmac` carrier enough for the `libfuzzer-fuzzshark-ip` harness to reach the parser path.
2. Keep unrelated envelope fields minimal and stable so verifier feedback stays tied to the target sink.
3. Apply the verified invariant from the failure shape rather than random broad mutation.
4. Submit only candidates where the vulnerable image reaches the target relation and the fixed image rejects or avoids it.

## Verifier Contract
The local class may remain coarse. Treat the official vulnerable-versus-fixed target match as the confirmation gate for this policy.

## Negative Memory
- Do not corrupt the outer `wireshark-fuzzshark-ip-gsmtap-rlcmac` recognition gate while retargeting this signal.
- Do not treat off-target crashes, clean parser reachability, or both-image crashes as success for this policy.
- Never store raw payload bytes, exact offsets, checksums, or task-local identifiers in memory.

## Evidence Shape
- Support: 1 server-verified solve(s), including round 30.
- Scope: generator repair only.
