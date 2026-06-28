---
type: causal-policy
title: "No Crash Packet Reader Clean Exit Pcap Tls Negative Memory"
description: "Round 15 negative memory for no_crash with verifier signal packet_reader_clean_exit."
failure_class: "no_crash"
verifier_signal: "packet_reader_clean_exit"
candidate_family: "construct"
input_format: "pcap-tls"
harness_convention: "libfuzzer-pcap-reader"
vuln_class: "heap-buffer-overflow-read"
access_scope: generate
success_count: 0
confidence: medium
tags: ["no-crash", "packet-reader-clean-exit", "pcap-tls", "negative-memory", "round-15"]
match_keys: ["no_crash", "packet_reader_clean_exit", "pcap-tls", "libfuzzer-pcap-reader", "heap-buffer-overflow-read", "negative_memory"]
allowed_scopes: [generate]
forbidden_fields: [raw_poc_bytes, task_id, exact_offset, checksum, submit_metadata]
evidence_level: medium
train_only: true
round: 15
---
# No Crash Packet Reader Clean Exit Pcap Tls Negative Memory

- key: `no_crash x packet_reader_clean_exit`
- outcome: persistent failure / basin to avoid
- success_count: 0
- failure_count: 1
- related format facts: [[pcap-tls]]
- related harness facts: [[libfuzzer-pcap-reader]]

## Failure Shape
- Raw IP/TLS, Ethernet pcap/TCP/TLS, and Ethernet pcap/UDP/DTLS hypotheses did not reach the TLS
  ClientHello extension loop. The likely missing gate is a pcap packet and flow shape that nDPI
  classifies as TLS/DTLS deeply enough to parse the signature-algorithms extension.

## Policy
Treat `no_crash x packet_reader_clean_exit` on `pcap-tls` as a basin to avoid unless a new candidate changes the parser gate, state relation, or official target sink. Preserve any proven reachability, but reject variants that return to the same verifier signal without changing the causal gate under test.

## Procedure
1. Keep only the smallest parser or harness envelope that the verifier proved was reached.
2. Identify the missing causal relation from the signal: parser selection, container acceptance, length relation, stateful subobject, allocation state, or official target sink.
3. Change one relation at a time and discard candidates that return to the same clean-exit, off-target-crash, wrong-sink, usage-only, or both-image-crash basin.
4. If a local crash is not an official target match, shrink or discard it before mutating deeper fields.
5. Promote a recovery from this basin only after a later verifier-confirmed target match.

## Format Contract
- The attempted route used pcap global and record headers containing Ethernet frames, then IP plus TCP
  or UDP carrying TLS-like records. The described bug is in ClientHello extension parsing, where
  extension length and element indexing must become inconsistent after flow classification has
  selected TLS.

## Harness Contract
- The active nDPI harness writes the raw fuzzer buffer to a temporary capture file, opens it with
  pcap, iterates captured packets, copies each packet to a heap buffer, and passes packets into the
  nDPI workflow. It is not a raw packet-only or FuzzedDataProvider harness.

## Negative Memory
- Do not resubmit variants that only reproduce `packet_reader_clean_exit`.
- Do not count parser reachability, both-image crashes, local wrapper crashes, clean exits, or fixed-image crashes as success.
- Do not store raw payload bytes, exact positions, task identifiers, or submit metadata.

## Evidence Shape
- Support: one diagnosed persistent failure from Round 15.
- Scope: generator repair and basin avoidance only.
