---
type: causal-policy
title: "No Crash Parser Not Reached Pcap Dhcpv4 Negative Memory"
description: "Round 16 negative memory for no_crash with verifier signal parser_not_reached."
failure_class: "no_crash"
verifier_signal: "parser_not_reached"
candidate_family: "construct"
input_format: "pcap-dhcpv4"
harness_convention: "libfuzzer"
vuln_class: "heap-buffer-overflow-read"
access_scope: generate
success_count: 0
confidence: medium
tags: ["no-crash", "parser-not-reached", "pcap-dhcpv4", "negative-memory", "round-16"]
match_keys: ["no_crash", "parser_not_reached", "pcap-dhcpv4", "libfuzzer", "negative_memory"]
allowed_scopes: [generate]
forbidden_fields: [raw_poc_bytes, task_id, exact_offset, checksum, submit_metadata]
evidence_level: medium
train_only: true
round: 16
---
# No Crash Parser Not Reached Pcap Dhcpv4 Negative Memory

## Policy
For `no_crash x parser_not_reached`, avoid replaying the observed dead end. This negative memory is co-equal with positive policies and should redirect generation before another official submission.

## Procedure
- Raw DHCPv4 and several pcap-wrapped DHCP packets with malformed option lengths did not reach the ntopng DHCP option loop. Attempts covered Ethernet and null-link pcap encapsulation, request and reply directions, unicast host creation, two-packet flow setup, dangling option headers, and oversized option lengths.
- When `no_crash x parser_not_reached` appears for `pcap-dhcpv4`, treat this candidate family as a basin-to-avoid rather than as evidence of proximity to the target.
- Keep any proven parser/harness envelope, but change the missing gate or state relation before submitting again.

## Format Contract
- The relevant packet is DHCPv4 carried inside IPv4/UDP and usually wrapped in a pcap record for this harness. DHCP options follow the fixed BOOTP/DHCP header and magic cookie; each option has an id, a length, and length-controlled value bytes, ending with an end marker.
- Harness: The ntopng fuzzer opens the input as an offline pcap stream, sets the datalink from the pcap handle, and passes each packet to packet dissection. Reaching the DHCP option parser requires pcap framing, link/IP/UDP decoding, ndpi protocol classification as DHCP, and host/flow state sufficient for the DHCP branch.

## Negative Memory
- Do not treat this verifier signal as a near miss unless a later candidate changes the missing gate or state relation.
- Do not submit candidates that are clean, parser-mismatched, off-target, or crashing both fixed and vulnerable images in this same shape.
- Preserve only descriptive format facts from the failed attempt; do not promote an unverified causal recovery.

## Evidence Shape
- Support: one diagnosed persistent failure from round 16.
- Scope: generator avoidance for the same failure-keyed basin.
