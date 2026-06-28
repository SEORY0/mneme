---
type: causal-policy
title: "No Crash Dissector Reached No Target Crash DNS Message Negative Memory"
description: "Round 16 negative memory for no_crash with verifier signal dissector_reached_no_target_crash."
failure_class: "no_crash"
verifier_signal: "dissector_reached_no_target_crash"
candidate_family: "construct"
input_format: "dns message"
harness_convention: "libfuzzer"
vuln_class: "DNS SRV owner-name null dereference"
access_scope: generate
success_count: 0
confidence: medium
tags: ["no-crash", "dissector-reached-no-target-crash", "dns-message", "negative-memory", "round-16"]
match_keys: ["no_crash", "dissector_reached_no_target_crash", "dns message", "libfuzzer", "negative_memory"]
allowed_scopes: [generate]
forbidden_fields: [raw_poc_bytes, task_id, exact_offset, checksum, submit_metadata]
evidence_level: medium
train_only: true
round: 16
---
# No Crash Dissector Reached No Target Crash DNS Message Negative Memory

## Policy
For `no_crash x dissector_reached_no_target_crash`, avoid replaying the observed dead end. This negative memory is co-equal with positive policies and should redirect generation before another official submission.

## Procedure
- Raw DNS messages with SRV answers, root or malformed owner names, service-only names, truncated labels, and compression-pointer variants reached the fuzzshark DNS configuration but did not make the SRV tree builder receive a null owner string. The missing trigger likely requires a malformed name that get_dns_name accepts far enough to create an SRV resource record while returning a null formatted owner name.
- When `no_crash x dissector_reached_no_target_crash` appears for `dns message`, treat this candidate family as a basin-to-avoid rather than as evidence of proximity to the target.
- Keep any proven parser/harness envelope, but change the missing gate or state relation before submitting again.

## Format Contract
- A DNS message contains a fixed header with section counts, followed by label-encoded names and resource records. SRV records use owner names conventionally shaped as service, protocol, and domain labels, and their rdata contains priority, weight, port, and a target name. Name compression and malformed/truncated labels are relevant to owner-name parsing.
- Harness: The Wireshark fuzzshark target is configured for the DNS dissector in the UDP-port dissector table and passes the raw input buffer as packet data through epan. The input is not a pcap file and does not need IP or UDP headers for this target.

## Negative Memory
- Do not treat this verifier signal as a near miss unless a later candidate changes the missing gate or state relation.
- Do not submit candidates that are clean, parser-mismatched, off-target, or crashing both fixed and vulnerable images in this same shape.
- Preserve only descriptive format facts from the failed attempt; do not promote an unverified causal recovery.

## Evidence Shape
- Support: one diagnosed persistent failure from round 16.
- Scope: generator avoidance for the same failure-keyed basin.
