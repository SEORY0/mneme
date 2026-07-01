---
type: causal-policy
title: "Pcap Ethernet Ipv4 Tcp Tls Clienthello Seed Mutate Wrong Sink Parser Reached Msan Ndpi Strdup Supported Versions Use Of Uninitialized Value Verified Recovery"
description: "Verified recovery distilled from a round trace for wrong_sink / parser_reached_msan_ndpi_strdup_supported_versions."
failure_class: "wrong_sink"
verifier_signal: "parser_reached_msan_ndpi_strdup_supported_versions"
candidate_family: "seed_mutate"
input_format: "pcap-ethernet-ipv4-tcp-tls-clienthello"
harness_convention: "libfuzzer-pcap-reader"
vuln_class: "use-of-uninitialized-value"
access_scope: generate
success_count: 1
confidence: high
tags: ["wrong-sink", "seed-mutate", "pcap-ethernet-ipv4-tcp-tls-clienthello", "use-of-uninitialized-value", "verified-recovery"]
match_keys: ["wrong-sink", "parser-reached-msan-ndpi-strdup-supported-versions", "pcap-ethernet-ipv4-tcp-tls-clienthello", "libfuzzer-pcap-reader", "use-of-uninitialized-value", "verified-recovery"]
allowed_scopes: [generate]
forbidden_fields: [raw_poc_bytes, task_id, exact_offset, checksum, submit_metadata]
evidence_level: high
train_only: true
provenance: round-35-consolidator
---
# Pcap Ethernet Ipv4 Tcp Tls Clienthello Seed Mutate Wrong Sink Parser Reached Msan Ndpi Strdup Supported Versions Use Of Uninitialized Value Verified Recovery

## Policy
For `wrong_sink` with verifier signal `parser_reached_msan_ndpi_strdup_supported_versions` on `pcap-ethernet-ipv4-tcp-tls-clienthello` under `libfuzzer-pcap-reader`, recover by preserving the format and harness gates that reach the target sink, then mutate only the invariant described by the verified recipe. This policy is keyed to the failure signal and is not a byte-level PoC recipe.

## Procedure
1. Use a real TLS ClientHello PCAP as the carrier so the nDPI reader, flow setup, TCP reassembly path, and TLS extension parser all stay valid.
2. Preserve the capture and packet framing, then make the Supported Versions vector length inconsistent with a complete sequence of version entries while leaving the extension otherwise reachable.
3. The vulnerable build leaves the supported-version string stack buffer uninitialized and duplicates it; the fixed build exits cleanly.

## Format Contract
- Input format: [[pcap-ethernet-ipv4-tcp-tls-clienthello]].
- Harness contract: [[libfuzzer-pcap-reader]].
- Keep parser reachability and sink selection intact before mutating the vulnerable relation.

## Negative Memory
- Do not broaden this into unrelated `pcap-ethernet-ipv4-tcp-tls-clienthello` failures without the same failure class and verifier signal.
- Do not store task identifiers, raw bytes, exact offsets, checksums, or submit metadata.

## Evidence Shape
- Support: one round 35 verified official target match; vulnerable build reached the target signal and the fixed build did not.
