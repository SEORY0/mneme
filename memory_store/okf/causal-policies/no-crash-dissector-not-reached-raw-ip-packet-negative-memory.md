---
type: causal-policy
title: "No Crash Dissector Not Reached Raw Ip Packet Negative Memory"
description: "Round 15 negative memory for no_crash with verifier signal dissector_not_reached."
failure_class: "no_crash"
verifier_signal: "dissector_not_reached"
candidate_family: "construct"
input_format: "raw-ip-packet"
harness_convention: "libfuzzer"
vuln_class: "heap-buffer-overflow-read"
access_scope: generate
success_count: 0
confidence: medium
tags: ["no-crash", "dissector-not-reached", "raw-ip-packet", "negative-memory", "round-15"]
match_keys: ["no_crash", "dissector_not_reached", "raw-ip-packet", "libfuzzer", "heap-buffer-overflow-read", "negative_memory"]
allowed_scopes: [generate]
forbidden_fields: [raw_poc_bytes, task_id, exact_offset, checksum, submit_metadata]
evidence_level: medium
train_only: true
round: 15
---
# No Crash Dissector Not Reached Raw Ip Packet Negative Memory

- key: `no_crash x dissector_not_reached`
- outcome: persistent failure / basin to avoid
- success_count: 0
- failure_count: 1
- related format facts: [[raw-ip-packet]]
- related harness facts: [[libfuzzer]]

## Failure Shape
- A pcap-style wrapper was the wrong contract for the active target; verifier output showed the active
  Wireshark harness is configured for raw IP dissection. The DOF sink was therefore not reached.

## Policy
Treat `no_crash x dissector_not_reached` on `raw-ip-packet` as a basin to avoid unless a new candidate changes the parser gate, state relation, or official target sink. Preserve any proven reachability, but reject variants that return to the same verifier signal without changing the causal gate under test.

## Procedure
1. Keep only the smallest parser or harness envelope that the verifier proved was reached.
2. Identify the missing causal relation from the signal: parser selection, container acceptance, length relation, stateful subobject, allocation state, or official target sink.
3. Change one relation at a time and discard candidates that return to the same clean-exit, off-target-crash, wrong-sink, usage-only, or both-image-crash basin.
4. If a local crash is not an official target match, shrink or discard it before mutating deeper fields.
5. Promote a recovery from this basin only after a later verifier-confirmed target match.

## Format Contract
- The vulnerable area is a Wireshark dissector path behind raw IP packet dissection. A candidate must
  be a raw IP packet whose transport and payload select the relevant higher-level dissector; pcap
  global and per-packet headers are not part of the accepted input format.

## Harness Contract
- The fuzzshark target was configured for the IP dissector and consumes the PoC bytes directly as an
  IP packet. There is no pcap file envelope, no libpcap record header, and no external filename-based
  dispatch.

## Negative Memory
- Do not resubmit variants that only reproduce `dissector_not_reached`.
- Do not count parser reachability, both-image crashes, local wrapper crashes, clean exits, or fixed-image crashes as success.
- Do not store raw payload bytes, exact positions, task identifiers, or submit metadata.

## Evidence Shape
- Support: one diagnosed persistent failure from Round 15.
- Scope: generator repair and basin avoidance only.
