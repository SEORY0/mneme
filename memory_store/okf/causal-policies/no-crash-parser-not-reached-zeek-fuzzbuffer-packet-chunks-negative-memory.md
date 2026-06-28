---
type: negative-memory
title: "No Crash Parser Not Reached Zeek Fuzzbuffer Packet Chunks Negative Memory"
description: "Round 22 negative memory for no_crash with verifier signal parser_not_reached."
failure_class: "no_crash"
verifier_signal: "parser_not_reached"
candidate_family: "construct"
input_format: "zeek-fuzzbuffer-packet-chunks"
harness_convention: "honggfuzz packet fuzzer"
vuln_class: "out-of-bounds-read"
access_scope: generate
success_count: 0
confidence: medium
tags: ["no-crash", "parser-not-reached", "zeek-fuzzbuffer-packet-chunks", "honggfuzz-packet-fuzzer", "construct", "negative-memory", "round-22"]
match_keys: ["no-crash", "parser-not-reached", "zeek-fuzzbuffer-packet-chunks", "honggfuzz-packet-fuzzer", "out-of-bounds-read"]
allowed_scopes: [generate]
forbidden_fields: [raw_poc_bytes, task_id, exact_offset, checksum, submit_metadata]
evidence_level: medium
train_only: true
round: 22
---
# No Crash Parser Not Reached Zeek Fuzzbuffer Packet Chunks Negative Memory

- key: `no_crash x parser_not_reached`
- outcome: persistent failure / basin to avoid
- success_count: 0
- failure_count: 1
- related format facts: [[zeek-fuzzbuffer-packet-chunks]]
- harnesses: [[honggfuzz-packet-fuzzer]]

## Failure Shape
Chunked packet envelopes were accepted by the harness, but both a raw-IP packet with VLAN-like payload and an Ethernet-looking VLAN frame failed to reach the target VLAN analyzer. The likely missing gate is a tunnel or packet-manager dispatch path that invokes VLAN analysis despite the harness initializing packets as raw link type.

## Policy
Treat `no_crash x parser_not_reached` on `zeek-fuzzbuffer-packet-chunks` as negative memory for the attempted carrier. Preserve only reachability that was actually observed, then retarget the missing parser gate, feature selector, length relation, stateful subobject, or official sink before spending more verification attempts.

## Procedure
1. Keep any parser or harness envelope that the verifier proved was reached.
2. Identify the missing causal relation from the signal: parser selection, feature gate, length relation, stateful subobject, or official target sink.
3. Change one relation at a time and reject variants that return to this same clean-exit, off-target, usage-only, wrapper-crash, or nonreproducible basin.
4. Promote a recovery from this basin only after a later server-confirmed target match.

## Negative Memory
- Do not resubmit another candidate with this exact failure signal unless it changes the causal gate being tested.
- Do not broaden random mutation after reachability is known; move to the smallest missing format or state contract.
- Do not treat local generic crashes, wrapper usage paths, clean parser exits, or wrong-sink labels as success.
- Never store raw payload bytes, exact offsets, checksums, or task-local identifiers in memory.

## Evidence Shape
- Support: 1 diagnosed persistent failure from round 22.
- Scope: generator repair and basin avoidance only.
