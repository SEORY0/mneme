---
type: causal-policy
title: "No Crash XML Parser Clean Exit XML Negative Memory"
description: "Round 10 negative memory for no_crash with verifier signal xml_parser_clean_exit."
failure_class: "no_crash"
verifier_signal: "xml_parser_clean_exit"
candidate_family: "construct"
input_format: "xml"
harness_convention: "libfuzzer"
vuln_class: "use-after-free"
access_scope: generate
success_count: 0
confidence: medium
tags: ["no-crash", "xml-parser-clean-exit", "negative-memory", "round-10"]
match_keys: ["no_crash", "xml_parser_clean_exit", "xml", "libfuzzer", "negative_memory"]
allowed_scopes: [generate]
forbidden_fields: [raw_poc_bytes, task_id, exact_offset, checksum, submit_metadata]
evidence_level: medium
train_only: true
round: 10
---
# No Crash XML Parser Clean Exit XML Negative Memory

## Policy
For `no_crash x xml_parser_clean_exit`, avoid replaying the observed dead end. This negative memory is co-equal with positive policies and should redirect generation before another official submission.

## Procedure
1. Raw XML documents and allocation-envelope hypotheses executed the XML fuzzer cleanly.
2. When `no_crash x xml_parser_clean_exit` appears for `xml`, treat this candidate family as a basin-to-avoid rather than as evidence of proximity to the target.
3. Keep any proven parser/harness envelope, but change the missing gate or state relation before submitting again.

## Format Contract
- The useful format is XML text with optional declarations, encodings, entities, and nested content that can drive libxml2 input-buffer growth and error handling. Merely malformed XML or entity expansion is insufficient without the allocation/reset timing.
- Harness: The active verifier binary consumes raw file bytes as the XML fuzzer input. Some libxml2 fuzzers support option and allocation-limit fields, but the observed target accepted raw XML-style files directly and did not expose a separate mode byte in these attempts.

## Negative Memory
- Do not treat this verifier signal as a near miss unless a later candidate changes the missing gate or state relation.
- Do not submit candidates that are clean, parser-mismatched, off-target, or crashing both fixed and vulnerable images in this same shape.
- Preserve only descriptive format facts from the failed attempt; do not promote an unverified causal recovery.

## Evidence Shape
- Support: one diagnosed round-10 persistent failure.
- Scope: generator avoidance for the same failure-keyed basin.
