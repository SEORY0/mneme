---
type: causal-policy
title: "No Crash Document Rendered Or Rejected Before Type2 Charstring Interpreter Postscript Or PDF With Cff Type2 Font Negative Memory"
description: "Round 24 negative memory for no_crash with verifier signal document_rendered_or_rejected_before_type2_charstring_interpreter."
failure_class: "no_crash"
verifier_signal: "document_rendered_or_rejected_before_type2_charstring_interpreter"
candidate_family: "seed_mutate_and_construct"
input_format: "postscript-or-pdf-with-cff-type2-font"
harness_convention: "libfuzzer raw bytes to ghostscript pdfwrite device"
vuln_class: "type2-charstring-stack-bounds"
access_scope: generate
success_count: 0
confidence: medium
tags: ["no-crash", "document-rendered-or-rejected-before-type2-charstring-interpreter", "postscript-or-pdf-with-cff-type2-font", "libfuzzer-raw-bytes-to-ghostscript-pdfwrite-device", "seed-mutate-and-construct", "negative-memory", "round-24"]
match_keys: ["no-crash", "document-rendered-or-rejected-before-type2-charstring-interpreter", "postscript-or-pdf-with-cff-type2-font", "libfuzzer-raw-bytes-to-ghostscript-pdfwrite-device", "type2-charstring-stack-bounds"]
allowed_scopes: [generate]
forbidden_fields: [raw_poc_bytes, task_id, exact_offset, checksum, submit_metadata]
evidence_level: medium
train_only: true
round: 24
---
# No Crash Document Rendered Or Rejected Before Type2 Charstring Interpreter Postscript Or PDF With Cff Type2 Font Negative Memory

- key: `no_crash x document_rendered_or_rejected_before_type2_charstring_interpreter`
- outcome: negative memory
- success_count: 0
- failure_count: 1
- formats: [[postscript-or-pdf-with-cff-type2-font]]
- harnesses: [[libfuzzer-raw-bytes-to-ghostscript-pdfwrite-device]]

## Dead-End Shape
Valid PS/PDF samples and simple Type1/CFF-looking font dictionaries did not reach the Type 2 charstring interpreter. The target likely requires a structurally valid embedded CFF/OTF font whose glyph is selected and rendered by the pdfwrite path.

## Policy
For `no_crash x document_rendered_or_rejected_before_type2_charstring_interpreter` on `postscript-or-pdf-with-cff-type2-font`, avoid replaying the observed dead end. This negative memory is co-equal with positive policies and should redirect generation before another official submission. Prefer `seed_mutate_and_construct` only while this format and harness contract are present.

## Procedure
1. When `no_crash x document_rendered_or_rejected_before_type2_charstring_interpreter` appears for `postscript-or-pdf-with-cff-type2-font`, treat this candidate family as a basin-to-avoid rather than evidence of proximity.
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
