---
type: causal-policy
title: "No Crash Html Parser Clean Exit Html Negative Memory"
description: "Round 16 negative memory for no_crash with verifier signal html_parser_clean_exit."
failure_class: "no_crash"
verifier_signal: "html_parser_clean_exit"
candidate_family: "construct"
input_format: "html"
harness_convention: "libfuzzer-libxml2-html"
vuln_class: "algorithmic-complexity"
access_scope: generate
success_count: 0
confidence: medium
tags: ["no-crash", "html-parser-clean-exit", "html", "negative-memory", "round-16"]
match_keys: ["no_crash", "html_parser_clean_exit", "html", "libfuzzer-libxml2-html", "negative_memory"]
allowed_scopes: [generate]
forbidden_fields: [raw_poc_bytes, task_id, exact_offset, checksum, submit_metadata]
evidence_level: medium
train_only: true
round: 16
---
# No Crash Html Parser Clean Exit Html Negative Memory

## Policy
For `no_crash x html_parser_clean_exit`, avoid replaying the observed dead end. This negative memory is co-equal with positive policies and should redirect generation before another official submission.

## Procedure
- Large malformed HTML families, including repeated tag openings, unterminated comments and scripts, entity-heavy text, and attribute-heavy elements, reached the HTML fuzzer but did not trip the timeout/crash criterion. The unresolved gate is the narrower parser state that makes push parsing perform repeated quadratic rescans rather than quickly consuming or rejecting the input.
- When `no_crash x html_parser_clean_exit` appears for `html`, treat this candidate family as a basin-to-avoid rather than as evidence of proximity to the target.
- Keep any proven parser/harness envelope, but change the missing gate or state relation before submitting again.

## Format Contract
- The useful payload is not a standalone browser document requirement; it is an HTML byte stream consumed by libxml2. Long comments, script data, entity-like text, nested tags, and attributes are all syntactically tolerated enough to reach parser logic, but the expensive path depends on how tokenization state spans chunk boundaries.
- Harness: The first bytes are consumed as an integer options field. The remaining bytes are parsed through both the normal HTML parser and a push parser that feeds bounded chunks from the same buffer. There is no filename, archive wrapper, or checksum gate.

## Negative Memory
- Do not treat this verifier signal as a near miss unless a later candidate changes the missing gate or state relation.
- Do not submit candidates that are clean, parser-mismatched, off-target, or crashing both fixed and vulnerable images in this same shape.
- Preserve only descriptive format facts from the failed attempt; do not promote an unverified causal recovery.

## Evidence Shape
- Support: one diagnosed persistent failure from round 16.
- Scope: generator avoidance for the same failure-keyed basin.
