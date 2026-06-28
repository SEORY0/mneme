---
type: negative-memory
title: "No Crash Analyzer Reported Negative Plain Delivery Without Crash Zeek Fuzzbuffer Smtp Stream Negative Memory"
description: "Round 19 negative memory for no_crash with verifier signal analyzer_reported_negative_plain_delivery_without_crash."
failure_class: "no_crash"
verifier_signal: "analyzer_reported_negative_plain_delivery_without_crash"
candidate_family: "construct"
input_format: "zeek-fuzzbuffer-smtp-stream"
harness_convention: "libfuzzer"
vuln_class: "integer-conversion-behavioral-bug"
access_scope: generate
success_count: 0
confidence: medium
tags: ["no-crash", "analyzer-reported-negative-plain-delivery-without-crash", "zeek-fuzzbuffer-smtp-stream", "libfuzzer", "construct", "negative-memory", "round-19"]
match_keys: ["no-crash", "analyzer-reported-negative-plain-delivery-without-crash", "zeek-fuzzbuffer-smtp-stream", "libfuzzer", "integer-conversion-behavioral-bug"]
allowed_scopes: [generate]
forbidden_fields: [raw_poc_bytes, task_id, exact_offset, checksum, submit_metadata]
evidence_level: medium
train_only: true
round: 19
---
# No Crash Analyzer Reported Negative Plain Delivery Without Crash Zeek Fuzzbuffer Smtp Stream Negative Memory

- key: `no_crash x analyzer_reported_negative_plain_delivery_without_crash`
- outcome: persistent failure / basin to avoid
- success_count: 0
- failure_count: 1
- related format facts: [[zeek-fuzzbuffer-smtp-stream]]
- harnesses: [[libfuzzer]]

## Failure Shape
Constructed SMTP streams reached the BDAT command handling and caused the analyzer to report a negative plain-delivery length, but that condition exited cleanly rather than producing a target differential. The likely missing trigger is a stream state where the oversized chunk length propagates into ContentLine processing after the BDAT analyzer accepts it, instead of being stopped at plain-delivery setup.

## Policy
Treat `no_crash x analyzer_reported_negative_plain_delivery_without_crash` on `zeek-fuzzbuffer-smtp-stream` as negative memory for the attempted carrier. Preserve only the reachability that was actually observed, then retarget the missing gate or sink-specific state before spending more verification attempts.

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
