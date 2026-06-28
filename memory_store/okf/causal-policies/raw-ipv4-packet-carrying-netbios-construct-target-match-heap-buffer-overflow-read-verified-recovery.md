---
type: causal-policy
title: Raw Ipv4 Packet Carrying Netbios Target Match Verified Recovery
description: Server-verified recovery for raw IPv4 packet carrying NetBIOS when generic_crash pairs with target_match.
failure_class: generic_crash
verifier_signal: target_match
candidate_family: construct
input_format: raw IPv4 packet carrying NetBIOS
harness_convention: libfuzzer raw packet processor
vuln_class: heap-buffer-overflow-read
access_scope: generate
success_count: 1
confidence: high
tags: [generic-crash, target-match, raw-ipv4-packet-carrying-netbios, libfuzzer-raw-packet-processor, construct, heap-buffer-overflow-read, verified-recovery]
match_keys: [generic-crash, target-match, raw-ipv4-packet-carrying-netbios, libfuzzer-raw-packet-processor, construct, heap-buffer-overflow-read, verified-recovery]
allowed_scopes: [generate]
forbidden_fields: [raw_poc_bytes, task_id, exact_offset, checksum, submit_metadata]
evidence_level: high
train_only: true
---
## Policy
When a raw IPv4 packet carrying NetBIOS candidate reaches `target_match` under `generic_crash`, preserve the accepted carrier and target the single invariant named by the verifier and vulnerability class. This pattern is server-verified for vulnerable-build failure with fixed-build clean behavior, so it outranks generic local sink labels for the same format and harness family.

## Procedure
1. Start from the smallest format-valid carrier that reaches the described parser or decoder path.
2. Preserve harness contract `[[libfuzzer-raw-packet-processor]]` and format contract `[[raw-ipv4-packet-carrying-netbios]]`; do not switch container families after parser reachability is proven.
3. Apply the causal recovery: Build a complete raw IP packet carrying NetBIOS traffic on the expected name-service or session-service path. Satisfy the IP transport and NetBIOS header gates, then make the encoded NetBIOS name length advertise more name pairs than are actually present in the packet payload. The parser reaches the NetBIOS name interpreter and reads past the captured packet buffer.
4. If local verify reports `wrong_sink` or a generic crash inside the same parser branch, submit once and let the official server decide target match.
5. If fixed-build behavior is not clean, shrink the mutation back to the minimal boundary relation before trying a different carrier.

## Negative Memory
- Do not randomize unrelated record families after this signal is reached.
- Do not discard a plausible parser-branch crash solely because local sink labeling is coarse.
- Do not promote this as a byte recipe; it is a format-gate and invariant relation.

## Evidence Shape
- Support: 1 server-verified Round 11 solve.
- Candidate family: construct.
