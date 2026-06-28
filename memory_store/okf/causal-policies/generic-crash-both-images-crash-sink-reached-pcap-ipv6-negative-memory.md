---
type: negative-memory
title: "Generic Crash Both Images Crash Sink Reached Pcap Ipv6 Negative Memory"
description: "Round 21 negative memory for generic-crash with verifier signal both-images-crash-sink-reached."
failure_class: "generic-crash"
verifier_signal: "both-images-crash-sink-reached"
candidate_family: "construct"
input_format: "pcap-ipv6"
harness_convention: "libfuzzer"
vuln_class: "heap-buffer-overflow-read"
access_scope: generate
success_count: 0
confidence: medium
tags: ["generic-crash", "both-images-crash-sink-reached", "pcap-ipv6", "libfuzzer", "construct", "negative-memory", "round-21"]
match_keys: ["generic-crash", "both-images-crash-sink-reached", "pcap-ipv6", "libfuzzer", "heap-buffer-overflow-read"]
allowed_scopes: [generate]
forbidden_fields: [raw_poc_bytes, task_id, exact_offset, checksum, submit_metadata]
evidence_level: medium
train_only: true
round: 21
---
# Generic Crash Both Images Crash Sink Reached Pcap Ipv6 Negative Memory

- key: `generic-crash x both-images-crash-sink-reached`
- outcome: persistent failure / basin to avoid
- success_count: 0
- failure_count: 1
- related format facts: [[pcap-ipv6]]
- harnesses: [[libfuzzer]]

## Failure Shape
Complete pcap files carrying Ethernet IPv6 packets reached IPv6Layer::parseExtensions and produced the described heap read, but the official fixed build also crashed. The attempts likely targeted a general extension-chain truncation that remains invalid in both images rather than the narrower vulnerable/fixed invariant.

## Policy
Treat `generic-crash x both-images-crash-sink-reached` on `pcap-ipv6` as negative memory for the attempted carrier. Preserve only the reachability that was actually observed, then retarget the missing gate or sink-specific state before spending more verification attempts.

## Procedure
1. Keep any parser or harness envelope that the verifier proved was reached.
2. Identify the missing causal relation from the signal: parser selection, feature gate, length relation, stateful subobject, or official target sink.
3. Change one relation at a time and reject variants that return to this same clean-exit, off-target, usage-only, both-crash, or nonreproducible basin.
4. Promote a recovery from this basin only after a later server-confirmed target match.

## Negative Memory
- Do not resubmit another candidate with this exact failure signal unless it changes the causal gate being tested.
- Do not broaden random mutation after reachability is known; move to the smallest missing format or state contract.
- Do not treat local generic crashes, wrapper usage paths, clean parser exits, fixed-build crashes, or wrong-sink labels as success.
- Never store raw payload bytes, exact offsets, checksums, or task-local identifiers in memory.

## Evidence Shape
- Support: 1 diagnosed persistent failure from round 21.
- Scope: generator repair and basin avoidance only.
