---
type: causal-policy
title: "No Crash Local Only Crash Not Official Ipv4 Tcp Tls Negative Memory"
description: "Round 16 negative memory for no_crash with verifier signal local_only_crash_not_official."
failure_class: "no_crash"
verifier_signal: "local_only_crash_not_official"
candidate_family: "construct"
input_format: "ipv4-tcp-tls"
harness_convention: "libfuzzer"
vuln_class: "TLS certificate printable-string uninitialized-memory"
access_scope: generate
success_count: 0
confidence: medium
tags: ["no-crash", "local-only-crash-not-official", "ipv4-tcp-tls", "negative-memory", "round-16"]
match_keys: ["no_crash", "local_only_crash_not_official", "ipv4-tcp-tls", "libfuzzer", "negative_memory"]
allowed_scopes: [generate]
forbidden_fields: [raw_poc_bytes, task_id, exact_offset, checksum, submit_metadata]
evidence_level: medium
train_only: true
round: 16
---
# No Crash Local Only Crash Not Official Ipv4 Tcp Tls Negative Memory

## Policy
For `no_crash x local_only_crash_not_official`, avoid replaying the observed dead end. This negative memory is co-equal with positive policies and should redirect generation before another official submission.

## Procedure
- Raw IPv4/TCP packets carrying TLS certificate handshakes with recognizable certificate attribute markers reached local processing and one variant crashed locally, but official submit was clean. The remaining gap is likely accurate nDPI TLS flow classification and certificate-fragment state so processCertificateElements reaches ndpi_is_printable_string with the intended uninitialized buffer contents.
- When `no_crash x local_only_crash_not_official` appears for `ipv4-tcp-tls`, treat this candidate family as a basin-to-avoid rather than as evidence of proximity to the target.
- Keep any proven parser/harness envelope, but change the missing gate or state relation before submitting again.

## Format Contract
- The packet format is raw IPv4 with a TCP segment and TLS record payload. A TLS Certificate handshake contains a handshake length, certificate-list length, and one or more length-prefixed certificate byte strings. The nDPI certificate parser scans certificate bytes for X.509 attribute markers and subject-alt-name style fields.
- Harness: The nDPI fuzzer passes the raw input bytes directly to ndpi_detection_process_packet. The input is not pcap-framed; IP/TCP headers, ports, and TLS record shape determine whether the TLS parser path is selected.

## Negative Memory
- Do not treat this verifier signal as a near miss unless a later candidate changes the missing gate or state relation.
- Do not submit candidates that are clean, parser-mismatched, off-target, or crashing both fixed and vulnerable images in this same shape.
- Preserve only descriptive format facts from the failed attempt; do not promote an unverified causal recovery.

## Evidence Shape
- Support: one diagnosed persistent failure from round 16.
- Scope: generator avoidance for the same failure-keyed basin.
