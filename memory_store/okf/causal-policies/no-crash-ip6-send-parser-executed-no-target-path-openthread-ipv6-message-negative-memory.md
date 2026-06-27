---
type: negative-memory
title: "No Crash Ip6 Send Parser Executed No Target Path Openthread Ipv6 Message Negative Memory"
description: "Round 19 negative memory for no_crash with verifier signal ip6_send_parser_executed_no_target_path."
failure_class: "no_crash"
verifier_signal: "ip6_send_parser_executed_no_target_path"
candidate_family: "seed_mutate"
input_format: "openthread-ipv6-message"
harness_convention: "libfuzzer"
vuln_class: "input-validation-bypass"
access_scope: generate
success_count: 0
confidence: medium
tags: ["no-crash", "ip6-send-parser-executed-no-target-path", "openthread-ipv6-message", "libfuzzer", "seed-mutate", "negative-memory", "round-19"]
match_keys: ["no-crash", "ip6-send-parser-executed-no-target-path", "openthread-ipv6-message", "libfuzzer", "input-validation-bypass"]
allowed_scopes: [generate]
forbidden_fields: [raw_poc_bytes, task_id, exact_offset, checksum, submit_metadata]
evidence_level: medium
train_only: true
round: 19
---
# No Crash Ip6 Send Parser Executed No Target Path Openthread Ipv6 Message Negative Memory

- key: `no_crash x ip6_send_parser_executed_no_target_path`
- outcome: persistent failure / basin to avoid
- success_count: 0
- failure_count: 1
- related format facts: [[openthread-ipv6-message]]
- harnesses: [[libfuzzer]]

## Failure Shape
Tried the available seed plus IP6-send variants covering link-security selection, UDP-like payload, ICMP-like payload, and MeshCoP-looking payload bytes. None drove ChannelMaskBaseTlv validation under the verifier-selected IP6 send harness. A useful next attempt needs a syntactically routed IPv6/Thread path that causes OpenThread to process MeshCoP TLVs rather than just append and send a generic message.

## Policy
Treat `no_crash x ip6_send_parser_executed_no_target_path` on `openthread-ipv6-message` as negative memory for the attempted carrier. Preserve only the reachability that was actually observed, then retarget the missing gate or sink-specific state before spending more verification attempts.

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
