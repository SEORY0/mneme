---
type: negative-memory
title: "No Crash Parser Clean Exit Ipv4 Tcp Http Negative Memory"
description: "Round 21 negative memory for no-crash with verifier signal parser-clean-exit."
failure_class: "no-crash"
verifier_signal: "parser-clean-exit"
candidate_family: "construct"
input_format: "ipv4-tcp-http"
harness_convention: "libfuzzer"
vuln_class: "stack-buffer-overflow-read"
access_scope: generate
success_count: 0
confidence: medium
tags: ["no-crash", "parser-clean-exit", "ipv4-tcp-http", "libfuzzer", "construct", "negative-memory", "round-21"]
match_keys: ["no-crash", "parser-clean-exit", "ipv4-tcp-http", "libfuzzer", "stack-buffer-overflow-read"]
allowed_scopes: [generate]
forbidden_fields: [raw_poc_bytes, task_id, exact_offset, checksum, submit_metadata]
evidence_level: medium
train_only: true
round: 21
---
# No Crash Parser Clean Exit Ipv4 Tcp Http Negative Memory

- key: `no-crash x parser-clean-exit`
- outcome: persistent failure / basin to avoid
- success_count: 0
- failure_count: 1
- related format facts: [[ipv4-tcp-http]]
- harnesses: [[libfuzzer]]

## Failure Shape
Raw HTTP text, IPv4/TCP HTTP responses with overlong Content-Type, and IPv4/TCP requests/responses with overlong Host/User-Agent/Server-style fields were accepted or ignored without a sanitizer signal. The missing piece is likely a more specific HTTP classification path or a two-packet flow state that reaches check_content_type_and_change_protocol with a vulnerable bounded diagnostic string.

## Policy
Treat `no-crash x parser-clean-exit` on `ipv4-tcp-http` as negative memory for the attempted carrier. Preserve only the reachability that was actually observed, then retarget the missing gate or sink-specific state before spending more verification attempts.

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
