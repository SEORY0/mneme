---
type: causal-policy
title: "No Crash Clean Execution Ipv4 Udp Kerberos Packet Negative Memory"
description: "Round 15 negative memory for no_crash with verifier signal clean_execution."
failure_class: "no_crash"
verifier_signal: "clean_execution"
candidate_family: "construct"
input_format: "ipv4-udp-kerberos-packet"
harness_convention: "afl-file-wrapper"
vuln_class: "off-by-one"
access_scope: generate
success_count: 0
confidence: medium
tags: ["no-crash", "clean-execution", "ipv4-udp-kerberos-packet", "negative-memory", "round-15"]
match_keys: ["no_crash", "clean_execution", "ipv4-udp-kerberos-packet", "afl-file-wrapper", "off-by-one", "negative_memory"]
allowed_scopes: [generate]
forbidden_fields: [raw_poc_bytes, task_id, exact_offset, checksum, submit_metadata]
evidence_level: medium
train_only: true
round: 15
---
# No Crash Clean Execution Ipv4 Udp Kerberos Packet Negative Memory

- key: `no_crash x clean_execution`
- outcome: persistent failure / basin to avoid
- success_count: 0
- failure_count: 1
- related format facts: [[ipv4-udp-kerberos-packet]]
- related harness facts: [[afl-file-wrapper]]

## Failure Shape
- A valid IPv4 UDP packet with Kerberos port selection and an ASN.1-like request body executed
  cleanly. The likely missing gate is a more faithful Kerberos request body that places the counted
  principal or realm string at the exact parser branch used by the off-by-one check.

## Policy
Treat `no_crash x clean_execution` on `ipv4-udp-kerberos-packet` as a basin to avoid unless a new candidate changes the parser gate, state relation, or official target sink. Preserve any proven reachability, but reject variants that return to the same verifier signal without changing the causal gate under test.

## Procedure
1. Keep only the smallest parser or harness envelope that the verifier proved was reached.
2. Identify the missing causal relation from the signal: parser selection, container acceptance, length relation, stateful subobject, allocation state, or official target sink.
3. Change one relation at a time and discard candidates that return to the same clean-exit, off-target-crash, wrong-sink, usage-only, or both-image-crash basin.
4. If a local crash is not an official target match, shrink or discard it before mutating deeper fields.
5. Promote a recovery from this basin only after a later verifier-confirmed target match.

## Format Contract
- The nDPI packet harness receives a raw layer-three packet, not a pcap. To reach Kerberos, the IP
  header and UDP or TCP transport fields must be coherent and the payload must satisfy the Kerberos
  dissector's length equality and message-type probes before counted string extraction occurs.

## Harness Contract
- The AFL-style wrapper feeds the PoC file bytes to fuzz_process_packet. The fuzzer initializes nDPI
  once, clears flow/source/destination state per input, and calls ndpi_detection_process_packet with
  the raw buffer.

## Negative Memory
- Do not resubmit variants that only reproduce `clean_execution`.
- Do not count parser reachability, both-image crashes, local wrapper crashes, clean exits, or fixed-image crashes as success.
- Do not store raw payload bytes, exact positions, task identifiers, or submit metadata.

## Evidence Shape
- Support: one diagnosed persistent failure from Round 15.
- Scope: generator repair and basin avoidance only.
