---
type: negative-memory
title: "No Crash Parser Not Reached Ip Carried Wcp Negative Memory"
description: "Round 22 negative memory for no_crash with verifier signal parser_not_reached."
failure_class: "no_crash"
verifier_signal: "parser_not_reached"
candidate_family: "construct"
input_format: "ip-carried-wcp"
harness_convention: "afl-libfuzzer-wrapper"
vuln_class: "buffer-overflow-write"
access_scope: generate
success_count: 0
confidence: medium
tags: ["no-crash", "parser-not-reached", "ip-carried-wcp", "afl-libfuzzer-wrapper", "construct", "negative-memory", "round-22"]
match_keys: ["no-crash", "parser-not-reached", "ip-carried-wcp", "afl-libfuzzer-wrapper", "buffer-overflow-write"]
allowed_scopes: [generate]
forbidden_fields: [raw_poc_bytes, task_id, exact_offset, checksum, submit_metadata]
evidence_level: medium
train_only: true
round: 22
---
# No Crash Parser Not Reached Ip Carried Wcp Negative Memory

- key: `no_crash x parser_not_reached`
- outcome: persistent failure / basin to avoid
- success_count: 0
- failure_count: 1
- related format facts: [[ip-carried-wcp]]
- harnesses: [[afl-libfuzzer-wrapper]]

## Failure Shape
The WCP dissector is registered behind Frame Relay NLPID and EtherType dispatch, but the executed fuzzshark target is configured as an IP dissector. Raw WCP bytes, GRE EtherType carrying WCP, GRE transparent Ethernet bridging, EtherIP with an Ethernet WCP frame, a direct IP payload, and a compressed-data variant all executed cleanly. The likely blocker is dispatch into WCP from the selected IP target rather than the WCP length invariant itself.

## Policy
Treat `no_crash x parser_not_reached` on `ip-carried-wcp` as negative memory for the attempted carrier. Preserve only reachability that was actually observed, then retarget the missing parser gate, feature selector, length relation, stateful subobject, or official sink before spending more verification attempts.

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
