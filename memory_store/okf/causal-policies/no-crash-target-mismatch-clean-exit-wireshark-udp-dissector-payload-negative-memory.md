---
type: causal-policy
title: "No Crash Target Mismatch Clean Exit Wireshark UDP Dissector Payload Negative Memory"
description: "Round 10 negative memory for no_crash with verifier signal target_mismatch_clean_exit."
failure_class: "no_crash"
verifier_signal: "target_mismatch_clean_exit"
candidate_family: "construct"
input_format: "wireshark-udp-dissector-payload"
harness_convention: "libfuzzer"
vuln_class: "formatting/out-of-bounds-read"
access_scope: generate
success_count: 0
confidence: medium
tags: ["no-crash", "target-mismatch-clean-exit", "negative-memory", "round-10"]
match_keys: ["no_crash", "target_mismatch_clean_exit", "wireshark-udp-dissector-payload", "libfuzzer", "negative_memory"]
allowed_scopes: [generate]
forbidden_fields: [raw_poc_bytes, task_id, exact_offset, checksum, submit_metadata]
evidence_level: medium
train_only: true
round: 10
---
# No Crash Target Mismatch Clean Exit Wireshark UDP Dissector Payload Negative Memory

## Policy
For `no_crash x target_mismatch_clean_exit`, avoid replaying the observed dead end. This negative memory is co-equal with positive policies and should redirect generation before another official submission.

## Procedure
1. The described NSAP/IS-IS CLV formatter was not reachable through the selected fuzzshark binary, which was configured for the UDP dissector via the IP protocol table.
2. When `no_crash x target_mismatch_clean_exit` appears for `wireshark-udp-dissector-payload`, treat this candidate family as a basin-to-avoid rather than as evidence of proximity to the target.
3. Keep any proven parser/harness envelope, but change the missing gate or state relation before submitting again.

## Format Contract
- The vulnerable IS-IS area-address CLV is a type-length-value record whose value contains one or more length-prefixed area addresses; the formatting bug is associated with a specific address length. The selected target, however, receives UDP payload structure, beginning with UDP header fields when routed through the UDP dissector.
- Harness: Fuzzshark initializes Wireshark epan and passes raw bytes to one configured dissector handle. In this run the handle was the UDP dissector from the IP protocol table, not an IS-IS or CLNP dissector.

## Negative Memory
- Do not treat this verifier signal as a near miss unless a later candidate changes the missing gate or state relation.
- Do not submit candidates that are clean, parser-mismatched, off-target, or crashing both fixed and vulnerable images in this same shape.
- Preserve only descriptive format facts from the failed attempt; do not promote an unverified causal recovery.

## Evidence Shape
- Support: one diagnosed round-10 persistent failure.
- Scope: generator avoidance for the same failure-keyed basin.
