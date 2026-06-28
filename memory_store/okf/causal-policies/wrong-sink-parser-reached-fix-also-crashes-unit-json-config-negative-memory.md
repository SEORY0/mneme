---
type: causal-policy
title: "Wrong Sink Parser Reached Fix Also Crashes Unit Json Config Negative Memory"
description: "Round 10 negative memory for wrong_sink with verifier signal parser_reached_fix_also_crashes."
failure_class: "wrong_sink"
verifier_signal: "parser_reached_fix_also_crashes"
candidate_family: "construct"
input_format: "unit-json-config"
harness_convention: "libfuzzer-json"
vuln_class: "use-of-uninitialized-value"
access_scope: generate
success_count: 0
confidence: medium
tags: ["wrong-sink", "parser-reached-fix-also-crashes", "negative-memory", "round-10"]
match_keys: ["wrong_sink", "parser_reached_fix_also_crashes", "unit-json-config", "libfuzzer-json", "negative_memory"]
allowed_scopes: [generate]
forbidden_fields: [raw_poc_bytes, task_id, exact_offset, checksum, submit_metadata]
evidence_level: medium
train_only: true
round: 10
---
# Wrong Sink Parser Reached Fix Also Crashes Unit Json Config Negative Memory

## Policy
For `wrong_sink x parser_reached_fix_also_crashes`, avoid replaying the observed dead end. This negative memory is co-equal with positive policies and should redirect generation before another official submission.

## Procedure
1. Backtick template strings in access-log templated fields reached the uninitialized error formatting path locally, but the official fixed image also exited nonzero for those candidates.
2. When `wrong_sink x parser_reached_fix_also_crashes` appears for `unit-json-config`, treat this candidate family as a basin-to-avoid rather than as evidence of proximity to the target.
3. Keep any proven parser/harness envelope, but change the missing gate or state relation before submitting again.

## Format Contract
- Unit configuration is JSON with top-level members such as access-log, routes, listeners, applications, and settings. Access-log objects require a nonempty path and can contain templated format and conditional fields. Backtick strings select the JavaScript-template branch, while dollar strings select the variable branch.
- Harness: The fuzzer consumes raw JSON bytes, parses them into a Unit configuration object, then validates the configuration. There is no outer file wrapper; schema validity is needed before templated-string validation is reached.

## Negative Memory
- Do not treat this verifier signal as a near miss unless a later candidate changes the missing gate or state relation.
- Do not submit candidates that are clean, parser-mismatched, off-target, or crashing both fixed and vulnerable images in this same shape.
- Preserve only descriptive format facts from the failed attempt; do not promote an unverified causal recovery.

## Evidence Shape
- Support: one diagnosed round-10 persistent failure.
- Scope: generator avoidance for the same failure-keyed basin.
