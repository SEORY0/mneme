---
type: causal-policy
title: "UDP A21 GCSNA Cdma2k Construct Parser Reached Sink Match Stack Buffer Overflow Read Verified Recovery"
description: "Round 26 verified recovery for wrong_sink with verifier signal parser_reached_sink_match."
failure_class: "wrong_sink"
verifier_signal: "parser_reached_sink_match"
candidate_family: "construct"
input_format: "udp-a21-gcsna-cdma2k"
harness_convention: "afl-fuzzshark"
vuln_class: "stack-buffer-overflow-read"
access_scope: generate
success_count: 1
confidence: high
tags: ["wrong-sink", "parser-reached-sink-match", "udp-a21-gcsna-cdma2k", "afl-fuzzshark", "construct", "verified-recovery", "round-26"]
match_keys: ["wrong_sink", "parser_reached_sink_match", "udp-a21-gcsna-cdma2k", "afl-fuzzshark", "stack-buffer-overflow-read", "verified_recovery"]
allowed_scopes: [generate]
forbidden_fields: [raw_poc_bytes, task_id, exact_offset, checksum, submit_metadata]
evidence_level: high
train_only: true
round: 26
---
# UDP A21 GCSNA Cdma2k Construct Parser Reached Sink Match Stack Buffer Overflow Read Verified Recovery

- key: `wrong_sink x parser_reached_sink_match`
- outcome: verified recovery
- success_count: 1
- failure_count: 0
- formats: [[udp-a21-gcsna-cdma2k]]
- harnesses: [[afl-fuzzshark]]

## Failure Shape
Wrap the CDMA2000 bitstream in the actual UDP dissector path: UDP service selection for A21, an A21 message carrying a GCSNA PDU element, a GCSNA circuit-service header, and then the TLAC/CDMA2000 L3 payload. Inside the CDMA2000 handoff-direction message, keep optional branches minimal but set the active-set gates nonzero, include a pilot record, and enable the additional pilot-info record with a nonzero record length. That reaches the helper branch where the code increments the pointer variable instead of the pointed-to bit offset, producing a stack read in the vulnerable build while the fixed build stays clean.

## Policy
For `wrong_sink x parser_reached_sink_match` on `udp-a21-gcsna-cdma2k`, preserve the format recognition and harness contract before varying the vulnerable invariant. Prefer `construct` only while that carrier and harness contract remain stable.

## Procedure
1. Preserve the `udp-a21-gcsna-cdma2k` carrier and `afl-fuzzshark` harness contract until parser reachability is stable.
2. Apply the causal invariant in the failure shape before broad mutation or seed sweeping.
3. Treat local crash class as supporting signal only; keep the candidate only when vulnerable and fixed images diverge on the official target relation.

## Verifier Contract
The official vulnerable-versus-fixed target match is the confirmation gate for this recovery policy; local crash class is supporting evidence only.

## Negative Memory
- Do not corrupt the outer `udp-a21-gcsna-cdma2k` recognition gate while retargeting this signal.
- Do not treat off-target crashes, clean parser exits, fixed-build crashes, or both-image crashes as success for this policy.
- Never store raw payload bytes, exact offsets, checksums, or task-local identifiers in memory.

## Format Contract
The reachable packet is layered: UDP header, A21 header with correlation data, an A21 information element whose length covers a GCSNA PDU, a GCSNA circuit-service message, and a bit-packed CDMA2000 TLAC/L3 message. The CDMA2000 handoff-direction body is a dense bitstream; reachability depends on message type, active-set length, channel indicator, pilot count, and pilot-info inclusion bits.

## Harness Contract
The fuzzshark target is configured for the UDP dissector through the IP-protocol table. The input is a raw UDP datagram, not a full IP packet and not a direct CDMA2000 buffer. There is no FuzzedDataProvider; all structure is consumed by nested dissectors from the front of the byte stream.

## Evidence Shape
- Support: 1 server-verified round 26 solve after 2 attempts.
- Scope: generator repair and retargeting only.
