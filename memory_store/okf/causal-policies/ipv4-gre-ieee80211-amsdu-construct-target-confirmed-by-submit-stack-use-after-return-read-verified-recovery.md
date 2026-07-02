---
type: causal-policy
title: "Ipv4 GRE Ieee80211 Amsdu Construct Target Confirmed By Submit Stack Use After Return Read Verified Recovery"
description: "Round 26 verified recovery for generic_crash with verifier signal target_confirmed_by_submit."
failure_class: "generic_crash"
verifier_signal: "target_confirmed_by_submit"
candidate_family: "construct"
input_format: "ipv4-gre-ieee80211-amsdu"
harness_convention: "libfuzzer-fuzzshark-ip"
vuln_class: "stack-use-after-return-read"
access_scope: generate
success_count: 1
confidence: high
tags: ["generic-crash", "target-confirmed-by-submit", "ipv4-gre-ieee80211-amsdu", "libfuzzer-fuzzshark-ip", "construct", "verified-recovery", "round-26"]
match_keys: ["generic_crash", "target_confirmed_by_submit", "ipv4-gre-ieee80211-amsdu", "libfuzzer-fuzzshark-ip", "stack-use-after-return-read", "verified_recovery"]
allowed_scopes: [generate]
forbidden_fields: [raw_poc_bytes, task_id, exact_offset, checksum, submit_metadata]
evidence_level: high
train_only: true
round: 26
---
# Ipv4 GRE Ieee80211 Amsdu Construct Target Confirmed By Submit Stack Use After Return Read Verified Recovery

- key: `generic_crash x target_confirmed_by_submit`
- outcome: verified recovery
- success_count: 1
- failure_count: 0
- formats: [[ipv4-gre-ieee80211-amsdu]]
- harnesses: [[libfuzzer-fuzzshark-ip]]

## Failure Shape
Use a raw IPv4 packet that dispatches through GRE to Aruba/IEEE 802.11 dissection. Make the outer WLAN frame a QoS data frame with A-MSDU enabled. One subframe recursively routes through LLC/SNAP into another IP/GRE/WLAN management frame so a file-scope proto-data entry points at a returned WLAN stack local. A later subframe routes through LLC/SNAP into IEEE 802.11 data-encapsulation tagged fields, causing the tag parser to retrieve and dereference the stale proto-data pointer.

## Policy
For `generic_crash x target_confirmed_by_submit` on `ipv4-gre-ieee80211-amsdu`, preserve the format recognition and harness contract before varying the vulnerable invariant. Prefer `construct` only while that carrier and harness contract remain stable.

## Procedure
1. Preserve the `ipv4-gre-ieee80211-amsdu` carrier and `libfuzzer-fuzzshark-ip` harness contract until parser reachability is stable.
2. Apply the causal invariant in the failure shape before broad mutation or seed sweeping.
3. Treat local crash class as supporting signal only; keep the candidate only when vulnerable and fixed images diverge on the official target relation.

## Verifier Contract
The official vulnerable-versus-fixed target match is the confirmation gate for this recovery policy; local crash class is supporting evidence only.

## Negative Memory
- Do not corrupt the outer `ipv4-gre-ieee80211-amsdu` recognition gate while retargeting this signal.
- Do not treat off-target crashes, clean parser exits, fixed-build crashes, or both-image crashes as success for this policy.
- Never store raw payload bytes, exact offsets, checksums, or task-local identifiers in memory.

## Format Contract
The packet is a raw IPv4 datagram for the fuzzshark IP dissector. GRE protocol payloads can carry Aruba IEEE 802.11 frames. A QoS data frame can contain A-MSDU subframes, and each subframe carries its own LLC/SNAP header that can dispatch to nested protocols, including another IP/GRE/WLAN path or the IEEE 802.11 data-encapsulation tag path.

## Harness Contract
The Wireshark fuzzshark target is configured for the IP dissector. It treats the input as one raw IPv4 packet and relies on protocol fields for nested dispatch; there is no pcap header, external capture wrapper, checksum repair requirement, or FuzzedDataProvider byte carving.

## Evidence Shape
- Support: 1 server-verified round 26 solve after 8 attempts.
- Scope: generator repair and retargeting only.
