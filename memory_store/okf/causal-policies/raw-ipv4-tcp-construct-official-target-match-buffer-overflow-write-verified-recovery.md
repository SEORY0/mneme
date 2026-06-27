---
type: causal-policy
title: "Raw Ipv4 Tcp Construct Official Target Match Buffer Overflow Write Verified Recovery"
description: "Server-verified recovery for raw-ipv4-tcp when none pairs with official_target_match."
failure_class: "none"
verifier_signal: "official_target_match"
candidate_family: "construct"
input_format: "raw-ipv4-tcp"
harness_convention: "libfuzzer-fuzzshark"
vuln_class: "buffer-overflow-write"
access_scope: generate
success_count: 1
confidence: high
tags: ["none", "official-target-match", "raw-ipv4-tcp", "libfuzzer-fuzzshark", "construct", "verified-recovery", "round-17"]
match_keys: ["none", "official-target-match", "raw-ipv4-tcp", "libfuzzer-fuzzshark", "construct", "buffer-overflow-write", "verified-recovery"]
allowed_scopes: [generate]
forbidden_fields: [raw_poc_bytes, task_id, exact_offset, checksum, submit_metadata]
evidence_level: high
train_only: true
round: 17
---
# Raw Ipv4 Tcp Construct Official Target Match Buffer Overflow Write Verified Recovery

- key: `none x official_target_match`
- outcome: server-verified vulnerable/fixed split
- success_count: 1
- related format facts: [[raw-ipv4-tcp]]
- related harness facts: [[libfuzzer-fuzzshark]]

## Policy
When `none x official_target_match` appears for `raw-ipv4-tcp`, preserve the parser or harness carrier already shown to reach the target branch. Retarget only the causal invariant named by the verifier signal and vulnerability class; do not broaden into unrelated container families after reachability is established.

## Procedure
1. Use a raw IPv4/TCP packet rather than a pcap container.
2. Satisfy the IP and TCP header-length gates, include a syntactically accepted TCP option area, and make the SACK option carry enough range entries that the dissector's missing range bound is violated during TCP option analysis.
3. Submit only candidates that preserve the same accepted carrier and separate vulnerable-build failure from fixed-build clean behavior.

## Negative Memory
- Do not treat local-only crashes, both-image crashes, or coarse sink labels as success for this key.
- Do not store raw payload bytes, exact positions, task identifiers, checksums, or submit metadata.

## Format Contract
Use [[raw-ipv4-tcp]]; the relevant gate is the accepted carrier plus the invariant described above, not a byte-specific recipe.

## Harness Contract
Use [[libfuzzer-fuzzshark]]; preserve the observed input contract before mutating deeper fields.

## Evidence Shape
- Support: 1 server-verified round 17 solve.
- Candidate family: construct.
