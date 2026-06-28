---
type: causal-policy
title: "No Crash Html Parser Ran Without Target Crash Some Malformed Envelope Attempts Were Rejected By Wrapper Libxml2 Html Fuzzer Envelope Negative Memory"
description: "Round 24 negative memory for no_crash with verifier signal HTML parser ran without target crash; some malformed envelope attempts were rejected by wrapper."
failure_class: "no_crash"
verifier_signal: "HTML parser ran without target crash; some malformed envelope attempts were rejected by wrapper"
candidate_family: "construct"
input_format: "libxml2-html-fuzzer-envelope"
harness_convention: "libfuzzer libxml2 html parser"
vuln_class: "parser-input-buffer-growth"
access_scope: generate
success_count: 0
confidence: medium
tags: ["no-crash", "html-parser-ran-without-target-crash-some-malformed-envelope-attempts-were-rejected-by-wrapper", "libxml2-html-fuzzer-envelope", "libfuzzer-libxml2-html-parser", "construct", "negative-memory", "round-24"]
match_keys: ["no-crash", "html-parser-ran-without-target-crash-some-malformed-envelope-attempts-were-rejected-by-wrapper", "libxml2-html-fuzzer-envelope", "libfuzzer-libxml2-html-parser", "parser-input-buffer-growth"]
allowed_scopes: [generate]
forbidden_fields: [raw_poc_bytes, task_id, exact_offset, checksum, submit_metadata]
evidence_level: medium
train_only: true
round: 24
---
# No Crash Html Parser Ran Without Target Crash Some Malformed Envelope Attempts Were Rejected By Wrapper Libxml2 Html Fuzzer Envelope Negative Memory

- key: `no_crash x HTML parser ran without target crash; some malformed envelope attempts were rejected by wrapper`
- outcome: negative memory
- success_count: 0
- failure_count: 1
- formats: [[libxml2-html-fuzzer-envelope]]
- harnesses: [[libfuzzer-libxml2-html-parser]]

## Dead-End Shape
Boundary-aligned multibyte text, attribute values, long names, and truncated UTF-8 did not trigger insufficient input-buffer growth. The selected harness was the HTML parser, so XML entity-envelope attempts were partly misframed; the likely remaining trigger needs an HTML token kind where CUR_CHAR or NEXT crosses a push-parser chunk boundary before the buffer grows.

## Policy
For `no_crash x HTML parser ran without target crash; some malformed envelope attempts were rejected by wrapper` on `libxml2-html-fuzzer-envelope`, avoid replaying the observed dead end. This negative memory is co-equal with positive policies and should redirect generation before another official submission. Prefer `construct` only while this format and harness contract are present.

## Procedure
1. When `no_crash x HTML parser ran without target crash; some malformed envelope attempts were rejected by wrapper` appears for `libxml2-html-fuzzer-envelope`, treat this candidate family as a basin-to-avoid rather than evidence of proximity.
2. Preserve any proven format or harness envelope, but change the missing gate, state relation, or sink path before another official submission.
3. Prefer a different construction family if the same verifier signal repeats without new parser-depth evidence.

## Verifier Contract
The official vulnerable-versus-fixed target match is the confirmation gate for recovery policies; local crash class is supporting evidence only.

## Negative Memory
- Do not resubmit candidates that are clean, off-target, rejected before the target path, or crashing both fixed and vulnerable images in this same shape.
- Do not promote this trace as a recovery unless a later verifier run flips the target relation.
- Preserve only descriptive format and harness facts from this failed attempt.

## Evidence Shape
- Support: one diagnosed round 24 persistent failure.
- Scope: generator repair and retargeting only.
