---
type: negative-memory
title: "No Crash Parser Not Reached Libredwg Json Dxf Construct Buffer Overflow Read Negative Memory"
description: "Round 23 negative memory for no_crash with verifier signal parser_not_reached."
failure_class: "no_crash"
verifier_signal: "parser_not_reached"
candidate_family: "construct"
input_format: "libredwg-json-dxf"
harness_convention: "libfuzzer-libredwg-multiformat"
vuln_class: "buffer-overflow-read"
access_scope: generate
success_count: 0
confidence: medium
tags: ["no-crash", "parser-not-reached", "libredwg-json-dxf", "libfuzzer-libredwg-multiformat", "construct", "negative-memory", "round-23"]
match_keys: ["no-crash", "parser-not-reached", "libredwg-json-dxf", "libfuzzer-libredwg-multiformat", "buffer-overflow-read"]
allowed_scopes: [generate]
forbidden_fields: [raw_poc_bytes, task_id, exact_offset, checksum, submit_metadata]
evidence_level: medium
train_only: true
round: 23
---
# No Crash Parser Not Reached Libredwg Json Dxf Construct Buffer Overflow Read Negative Memory

- key: `no_crash x parser_not_reached`
- outcome: persistent failure / basin to avoid
- success_count: 0
- failure_count: 1
- related format facts: [[libredwg-json-dxf]]
- harnesses: [[libfuzzer-libredwg-multiformat]]

## Failure Shape
Constructed JSON and DXF inputs with truncated Unicode escapes did not reach the vulnerable UTF conversion routine. The likely missing gate is a parsed DWG/DXF object field that is later emitted through the text-value conversion path, rather than an arbitrary string in a top-level JSON or minimal DXF record.

## Policy
Treat `no_crash x parser_not_reached` on `libredwg-json-dxf` as negative memory for the attempted carrier. Preserve only reachability that was actually observed, then retarget the missing gate, harness contract, or sink-specific state before spending more verification attempts.

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
