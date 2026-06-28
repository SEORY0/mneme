---
type: negative-memory
title: "No Crash Target Dissector Not Configured Wireshark Fuzzshark Udp Payload Construct Out Of Bounds Read Negative Memory"
description: "Round 23 negative memory for no_crash with verifier signal target_dissector_not_configured."
failure_class: "no_crash"
verifier_signal: "target_dissector_not_configured"
candidate_family: "construct"
input_format: "wireshark-fuzzshark-udp-payload"
harness_convention: "honggfuzz-fuzzshark"
vuln_class: "out-of-bounds-read"
access_scope: generate
success_count: 0
confidence: medium
tags: ["no-crash", "target-dissector-not-configured", "wireshark-fuzzshark-udp-payload", "honggfuzz-fuzzshark", "construct", "negative-memory", "round-23"]
match_keys: ["no-crash", "target-dissector-not-configured", "wireshark-fuzzshark-udp-payload", "honggfuzz-fuzzshark", "out-of-bounds-read"]
allowed_scopes: [generate]
forbidden_fields: [raw_poc_bytes, task_id, exact_offset, checksum, submit_metadata]
evidence_level: medium
train_only: true
round: 23
---
# No Crash Target Dissector Not Configured Wireshark Fuzzshark Udp Payload Construct Out Of Bounds Read Negative Memory

- key: `no_crash x target_dissector_not_configured`
- outcome: persistent failure / basin to avoid
- success_count: 0
- failure_count: 1
- related format facts: [[wireshark-fuzzshark-udp-payload]]
- harnesses: [[honggfuzz-fuzzshark]]

## Failure Shape
Raw GSM_RLP-like probes did not reach the described dissector. The local output shows this image is configured for the UDP dissector in the ip.proto table, so the actual active harness surface does not match the packet-gsm_rlp description.

## Policy
Treat `no_crash x target_dissector_not_configured` on `wireshark-fuzzshark-udp-payload` as negative memory for the attempted carrier. Preserve only reachability that was actually observed, then retarget the missing gate, harness contract, or sink-specific state before spending more verification attempts.

## Procedure
1. Keep any parser, envelope, or harness contract that the trace showed was reached.
2. Identify the missing causal relation from the verifier signal: parser selection, feature gate, length relation, stateful subobject, or official target sink.
3. Change one relation at a time and reject variants that return to this same clean-exit, off-target, usage-only, nonreproducible, or both-crash basin.
4. Promote a recovery from this basin only after a later server-confirmed target match.

## Negative Memory
- Do not resubmit another candidate with this exact failure signal unless it changes the causal gate being tested.
- Do not broaden random mutation after reachability is known; move to the smallest missing format or state contract.
- Do not treat local generic crashes, wrapper usage paths, clean parser exits, fixed-build crashes, or wrong-sink labels as success.
- Never store raw payload bytes, exact offsets, checksums, or task-local identifiers in memory.

## Evidence Shape
- Support: 1 diagnosed persistent failure from round 23 after 5 attempts.
- Scope: generator repair and basin avoidance only.
