---
type: causal-policy
title: "No Crash Parser Target Ran Without Sanitizer Finding Fluent Bit Parser Fuzzer Control Block Plus Record Payload Negative Memory"
description: "Round 24 negative memory for no_crash with verifier signal parser target ran without sanitizer finding."
failure_class: "no_crash"
verifier_signal: "parser target ran without sanitizer finding"
candidate_family: "construct"
input_format: "fluent-bit parser-fuzzer control-block plus record payload"
harness_convention: "libfuzzer fluent-bit parser_fuzzer"
vuln_class: "string-null-termination"
access_scope: generate
success_count: 0
confidence: medium
tags: ["no-crash", "parser-target-ran-without-sanitizer-finding", "fluent-bit-parser-fuzzer-control-block-plus-record-payload", "libfuzzer-fluent-bit-parser-fuzzer", "construct", "negative-memory", "round-24"]
match_keys: ["no-crash", "parser-target-ran-without-sanitizer-finding", "fluent-bit-parser-fuzzer-control-block-plus-record-payload", "libfuzzer-fluent-bit-parser-fuzzer", "string-null-termination"]
allowed_scopes: [generate]
forbidden_fields: [raw_poc_bytes, task_id, exact_offset, checksum, submit_metadata]
evidence_level: medium
train_only: true
round: 24
---
# No Crash Parser Target Ran Without Sanitizer Finding Fluent Bit Parser Fuzzer Control Block Plus Record Payload Negative Memory

- key: `no_crash x parser target ran without sanitizer finding`
- outcome: negative memory
- success_count: 0
- failure_count: 1
- formats: [[fluent-bit-parser-fuzzer-control-block-plus-record-payload]]
- harnesses: [[libfuzzer-fluent-bit-parser-fuzzer]]

## Dead-End Shape
Mode-correct JSON, LTSV, and logfmt inputs with time and type options reached parser creation and record parsing but did not expose a non-null-terminated string consumer. The remaining missing piece is likely a specific parser option or decoder backend combination that passes a length-bounded field into a C-string API.

## Policy
For `no_crash x parser target ran without sanitizer finding` on `fluent-bit-parser-fuzzer-control-block-plus-record-payload`, avoid replaying the observed dead end. This negative memory is co-equal with positive policies and should redirect generation before another official submission. Prefer `construct` only while this format and harness contract are present.

## Procedure
1. When `no_crash x parser target ran without sanitizer finding` appears for `fluent-bit-parser-fuzzer-control-block-plus-record-payload`, treat this candidate family as a basin-to-avoid rather than evidence of proximity.
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
