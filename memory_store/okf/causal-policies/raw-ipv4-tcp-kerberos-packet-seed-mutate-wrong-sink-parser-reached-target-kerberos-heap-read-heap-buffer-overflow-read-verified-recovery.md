---
type: causal-policy
title: "Raw Ipv4 Tcp Kerberos Packet Seed Mutate Wrong Sink Parser Reached Target Kerberos Heap Read Heap Buffer Overflow Read Verified Recovery"
description: "Verified recovery distilled from a round trace for wrong_sink / parser_reached_target_kerberos_heap_read."
failure_class: "wrong_sink"
verifier_signal: "parser_reached_target_kerberos_heap_read"
candidate_family: "seed_mutate"
input_format: "raw-ipv4-tcp-kerberos-packet"
harness_convention: "libfuzzer"
vuln_class: "heap-buffer-overflow-read"
access_scope: generate
success_count: 1
confidence: high
tags: ["wrong-sink", "seed-mutate", "raw-ipv4-tcp-kerberos-packet", "heap-buffer-overflow-read", "verified-recovery"]
match_keys: ["wrong-sink", "parser-reached-target-kerberos-heap-read", "raw-ipv4-tcp-kerberos-packet", "libfuzzer", "heap-buffer-overflow-read", "verified-recovery"]
allowed_scopes: [generate]
forbidden_fields: [raw_poc_bytes, task_id, exact_offset, checksum, submit_metadata]
evidence_level: high
train_only: true
provenance: round-35-consolidator
---
# Raw Ipv4 Tcp Kerberos Packet Seed Mutate Wrong Sink Parser Reached Target Kerberos Heap Read Heap Buffer Overflow Read Verified Recovery

## Policy
For `wrong_sink` with verifier signal `parser_reached_target_kerberos_heap_read` on `raw-ipv4-tcp-kerberos-packet` under `libfuzzer`, recover by preserving the format and harness gates that reach the target sink, then mutate only the invariant described by the verified recipe. This policy is keyed to the failure signal and is not a byte-level PoC recipe.

## Procedure
1. Use a real Kerberos TCP packet as the envelope, feed it as a raw IPv4 packet rather than a pcap, and preserve the IP/TCP length fields, port selection, Kerberos stream-length equality, and request message selector.
2. Mutate only the inner request padding length so the later ASN.1 tag scan starts beyond the packet payload; the fixed build rejects this relation cleanly.

## Format Contract
- Input format: [[raw-ipv4-tcp-kerberos-packet]].
- Harness contract: [[libfuzzer]].
- Keep parser reachability and sink selection intact before mutating the vulnerable relation.

## Negative Memory
- Do not broaden this into unrelated `raw-ipv4-tcp-kerberos-packet` failures without the same failure class and verifier signal.
- Do not store task identifiers, raw bytes, exact offsets, checksums, or submit metadata.

## Evidence Shape
- Support: one round 35 verified official target match; vulnerable build reached the target signal and the fixed build did not.
