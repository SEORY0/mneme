---
type: causal-policy
title: "No Crash Parser Not Reached Pcap Ethernet Ip Icmp Negative Memory"
description: "Round 16 negative memory for no_crash with verifier signal parser_not_reached."
failure_class: "no_crash"
verifier_signal: "parser_not_reached"
candidate_family: "construct"
input_format: "pcap-ethernet-ip-icmp"
harness_convention: "libfuzzer"
vuln_class: "heap-buffer-overflow-read"
access_scope: generate
success_count: 0
confidence: medium
tags: ["no-crash", "parser-not-reached", "pcap-ethernet-ip-icmp", "negative-memory", "round-16"]
match_keys: ["no_crash", "parser_not_reached", "pcap-ethernet-ip-icmp", "libfuzzer", "negative_memory"]
allowed_scopes: [generate]
forbidden_fields: [raw_poc_bytes, task_id, exact_offset, checksum, submit_metadata]
evidence_level: medium
train_only: true
round: 16
---
# No Crash Parser Not Reached Pcap Ethernet Ip Icmp Negative Memory

## Policy
For `no_crash x parser_not_reached`, avoid replaying the observed dead end. This negative memory is co-equal with positive policies and should redirect generation before another official submission.

## Procedure
- Constructed classic PCAP files with Ethernet/IPv4/ICMP destination-unreachable packets reached clean execution. Varying the embedded IPv4 header length and captured ICMP payload length did not produce an ASan-visible overread, likely because the crafted packet did not reach `ICMPinfo::dissectICMP` in the expected flow state or the overread stayed inside libpcap-provided padding.
- When `no_crash x parser_not_reached` appears for `pcap-ethernet-ip-icmp`, treat this candidate family as a basin-to-avoid rather than as evidence of proximity to the target.
- Keep any proven parser/harness envelope, but change the missing gate or state relation before submitting again.

## Format Contract
- The input must be a complete classic PCAP file with a global header, packet record header and captured packet bytes. For Ethernet IPv4 ICMP, the packet contains an outer Ethernet header, outer IPv4 header, ICMP destination-unreachable header and embedded inner IPv4/transport header data.
- Harness: The ntopng harness wraps the raw bytes with `fmemopen`, opens them through libpcap offline parsing, sets the datalink from the PCAP and passes each packet record to the packet dissector. Packet record captured length and original length influence the trusted L4 length used by the ICMP parser.

## Negative Memory
- Do not treat this verifier signal as a near miss unless a later candidate changes the missing gate or state relation.
- Do not submit candidates that are clean, parser-mismatched, off-target, or crashing both fixed and vulnerable images in this same shape.
- Preserve only descriptive format facts from the failed attempt; do not promote an unverified causal recovery.

## Evidence Shape
- Support: one diagnosed persistent failure from round 16.
- Scope: generator avoidance for the same failure-keyed basin.
