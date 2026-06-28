---
type: causal-policy
title: "No Crash Selected Ip6 Send Harness Clean Exit Openthread Ip6 Message Negative Memory"
description: "Round 6 negative memory for no_crash with verifier signal selected_ip6_send_harness_clean_exit."
failure_class: "no_crash"
verifier_signal: "selected_ip6_send_harness_clean_exit"
candidate_family: "raw_cli_then_ipv6_payloads"
input_format: "openthread-ip6-message"
harness_convention: "libfuzzer ip6-send-fuzzer"
vuln_class: "buffer-overrun"
access_scope: generate
success_count: 0
confidence: medium
tags: ["no-crash", "selected-ip6-send-harness-clean-exit", "openthread-ip6-message", "negative-memory", "round-6"]
match_keys: ["no_crash", "selected_ip6_send_harness_clean_exit", "openthread-ip6-message", "libfuzzer ip6-send-fuzzer", "negative_memory"]
allowed_scopes: [generate]
forbidden_fields: [raw_poc_bytes, task_id, exact_offset, checksum, submit_metadata]
evidence_level: medium
train_only: true
round: 6
---
# No Crash Selected Ip6 Send Harness Clean Exit Openthread Ip6 Message Negative Memory

- key: `no_crash x selected_ip6_send_harness_clean_exit`
- outcome: persistent failure / basin to avoid
- success_count: 0
- failure_count: 1
- related format facts: [[openthread-ip6-message]]

## Failure Shape
- The wrapper selected the ip6-send fuzzer, not a direct energy-scan receive-results harness. CLI-like energy scan text, raw TLV-like payloads, and IPv6 UDP-style messages executed cleanly and did not reach a crashing energy-report receive path.

## Policy
Treat `no_crash x selected_ip6_send_harness_clean_exit` on this format family as negative memory for the attempted carrier. Preserve only verifier-proven reachability, then retarget the missing gate or sink-specific state instead of resubmitting candidates with the same signal.

## Procedure
1. Keep any parser or harness envelope that the verifier proved was reached.
2. Identify the missing causal relation from the signal: parser selection, feature gate, length relation, stateful subobject, or official target sink.
3. Change one relation at a time and reject variants that return to the same clean-exit, off-target-crash, wrong-sink, usage-only, or nonreproducible basin.
4. If a local crash is not an official target match, shrink or discard it before mutating deeper fields.
5. Promote a recovery from this basin only after a later verifier-confirmed target match.

## Negative Memory
- Do not treat local generic crashes, wrapper usage paths, clean parser exits, or wrong-sink labels as success.
- Do not broaden random mutation after reachability is known; move to the smallest missing format contract.
- Do not submit another candidate with this exact failure signal unless the candidate changes the causal gate being tested.
- Do not store raw payload bytes, exact offsets, checksums, or task-local identifiers.

## Evidence Shape
- Support: 1 diagnosed persistent failure(s) from round 6.
- Scope: generator repair and basin avoidance only.
