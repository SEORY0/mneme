---
type: negative-memory
title: "No Crash Ip Fuzzer Selected Xcsl Not Reached Wireshark Fuzzshark Ip To Xcsl Negative Memory"
description: "Round 19 negative memory for no_crash with verifier signal ip_fuzzer_selected_xcsl_not_reached."
failure_class: "no_crash"
verifier_signal: "ip_fuzzer_selected_xcsl_not_reached"
candidate_family: "construct_xcsl_text_and_ip_tcp_wrapper"
input_format: "wireshark-fuzzshark-ip-to-xcsl"
harness_convention: "afl-fuzzshark-ip"
vuln_class: "off-by-one-read-or-write"
access_scope: generate
success_count: 0
confidence: medium
tags: ["no-crash", "ip-fuzzer-selected-xcsl-not-reached", "wireshark-fuzzshark-ip-to-xcsl", "afl-fuzzshark-ip", "construct-xcsl-text-and-ip-tcp-wrapper", "negative-memory", "round-19"]
match_keys: ["no-crash", "ip-fuzzer-selected-xcsl-not-reached", "wireshark-fuzzshark-ip-to-xcsl", "afl-fuzzshark-ip", "off-by-one-read-or-write"]
allowed_scopes: [generate]
forbidden_fields: [raw_poc_bytes, task_id, exact_offset, checksum, submit_metadata]
evidence_level: medium
train_only: true
round: 19
---
# No Crash Ip Fuzzer Selected Xcsl Not Reached Wireshark Fuzzshark Ip To Xcsl Negative Memory

- key: `no_crash x ip_fuzzer_selected_xcsl_not_reached`
- outcome: persistent failure / basin to avoid
- success_count: 0
- failure_count: 1
- related format facts: [[wireshark-fuzzshark-ip-to-xcsl]]
- harnesses: [[afl-fuzzshark-ip]]

## Failure Shape
Direct XCSL text and TCP/IP-wrapped XCSL-like messages exited cleanly under the selected fuzzshark IP target. The XCSL token-length invariant was identified, but the active harness did not provide a direct TCP-port or heuristic XCSL entry point for the tested payloads.

## Policy
Treat `no_crash x ip_fuzzer_selected_xcsl_not_reached` on `wireshark-fuzzshark-ip-to-xcsl` as negative memory for the attempted carrier. Preserve only the reachability that was actually observed, then retarget the missing gate or sink-specific state before spending more verification attempts.

## Procedure
1. Keep any parser or harness envelope that the verifier proved was reached.
2. Identify the missing causal relation from the signal: parser selection, feature gate, length relation, stateful subobject, or official target sink.
3. Change one relation at a time and reject variants that return to this same clean-exit, off-target, usage-only, or nonreproducible basin.
4. Promote a recovery from this basin only after a later server-confirmed target match.

## Negative Memory
- Do not resubmit another candidate with this exact failure signal unless it changes the causal gate being tested.
- Do not broaden random mutation after reachability is known; move to the smallest missing format or state contract.
- Do not treat local generic crashes, wrapper usage paths, clean parser exits, or wrong-sink labels as success.
- Never store raw payload bytes, exact offsets, checksums, or task-local identifiers in memory.

## Evidence Shape
- Support: 1 diagnosed persistent failure from round 19.
- Scope: generator repair and basin avoidance only.
