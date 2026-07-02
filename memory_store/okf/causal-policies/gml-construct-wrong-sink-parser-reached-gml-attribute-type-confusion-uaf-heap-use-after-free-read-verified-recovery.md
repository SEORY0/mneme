---
type: causal-policy
title: "Gml Construct Wrong Sink Parser Reached Gml Attribute Type Confusion Uaf Heap Use After Free Read Verified Recovery"
description: "Round 37 verified recovery for wrong_sink with verifier signal parser_reached_gml_attribute_type_confusion_uaf."
failure_class: "wrong_sink"
verifier_signal: "parser_reached_gml_attribute_type_confusion_uaf"
candidate_family: "construct"
input_format: "gml"
harness_convention: "honggfuzz-wrapper-libfuzzer-file"
vuln_class: "heap-use-after-free-read"
access_scope: generate
success_count: 1
confidence: high
tags: ["wrong-sink", "parser-reached-gml-attribute-type-confusion-uaf", "gml", "honggfuzz-wrapper-libfuzzer-file", "construct", "heap-use-after-free-read", "verified-recovery", "round-37"]
match_keys: ["wrong_sink", "parser_reached_gml_attribute_type_confusion_uaf", "gml", "honggfuzz-wrapper-libfuzzer-file", "heap-use-after-free-read", "verified-recovery", "construct"]
allowed_scopes: [generate]
forbidden_fields: [raw_poc_bytes, task_id, exact_offset, checksum, submit_metadata]
evidence_level: high
train_only: true
round: 37
---
# Gml Construct Wrong Sink Parser Reached Gml Attribute Type Confusion Uaf Heap Use After Free Read Verified Recovery

- key: `wrong_sink x parser_reached_gml_attribute_type_confusion_uaf`
- outcome: server-verified target match
- success_count: 1
- related format facts: [[gml]]
- related harness facts: [[honggfuzz-wrapper-libfuzzer-file]]

## Failure Shape
Build a complete GML graph with a valid graph list and a node id. On the same node, repeat one vertex attribute name first as a numeric value and later as a nested list value, then include another attribute so iteration continues after the conversion error. The first pass keeps the attribute record numeric because composite values do not retag it as string-like. The second pass sends the nested-list value through numeric conversion, the ignore-error handler frees cleanup records, and the still-running loop reads a freed attribute record.

## Policy
When `wrong_sink x parser_reached_gml_attribute_type_confusion_uaf` appears for `gml` under `honggfuzz-wrapper-libfuzzer-file`, preserve the parser, format, and harness gates that the verifier proved before mutating the sink-specific relation. Treat official vulnerable/fixed divergence as the success gate; local crash labels are supporting signals only.

## Procedure
1. Start from the `[[gml]]` format contract and `[[honggfuzz-wrapper-libfuzzer-file]]` harness contract; keep recognition, dispatch selectors, lengths, and state setup coherent until parser reachability is stable.
2. Apply the causal relation from the failure shape before broad mutation or seed sweeping.
3. Change one invariant at a time: selector-to-subparser, declared length-to-available data, container count-to-record body, lifetime/ownership state, allocation-size relation, or sanitizer-specific sink relation.
4. Submit only candidates where the vulnerable image reaches the target relation and the fixed image exits cleanly, rejects the relation, or otherwise avoids the target crash.

## Verifier Contract
This policy is ranked by 1 official target match. Re-rank or quarantine it if later use returns only clean exits, wrong sinks, wrapper-specific crashes, or fixed-image crashes.

## Negative Memory
- Do not corrupt the outer `gml` recognition gate while retargeting this signal.
- Do not count parser reachability, both-image crashes, local wrapper crashes, clean exits, or fixed-image crashes as success.
- Do not store payload bytes, exact positions, task identifiers, checksums, or submit metadata.

## Evidence Shape
- Support: server-verified round 37 solve after 5 attempts.
- Candidate family: construct.
- Official split: vulnerable exit 1, fixed exit 0, target_match True.
- Scope: generator repair and retargeting only.
