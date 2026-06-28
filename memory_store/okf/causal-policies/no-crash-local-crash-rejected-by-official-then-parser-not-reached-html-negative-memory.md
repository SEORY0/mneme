---
type: causal-policy
title: "No Crash Local Crash Rejected By Official Then Parser Not Reached Html Negative Memory"
description: "Round 16 negative memory for no_crash with verifier signal local_crash_rejected_by_official_then_parser_not_reached."
failure_class: "no_crash"
verifier_signal: "local_crash_rejected_by_official_then_parser_not_reached"
candidate_family: "construct"
input_format: "html"
harness_convention: "libfuzzer"
vuln_class: "out-of-bounds-read"
access_scope: generate
success_count: 0
confidence: medium
tags: ["no-crash", "local-crash-rejected-by-official-then-parser-not-reached", "html", "negative-memory", "round-16"]
match_keys: ["no_crash", "local_crash_rejected_by_official_then_parser_not_reached", "html", "libfuzzer", "negative_memory"]
allowed_scopes: [generate]
forbidden_fields: [raw_poc_bytes, task_id, exact_offset, checksum, submit_metadata]
evidence_level: medium
train_only: true
round: 16
---
# No Crash Local Crash Rejected By Official Then Parser Not Reached Html Negative Memory

## Policy
For `no_crash x local_crash_rejected_by_official_then_parser_not_reached`, avoid replaying the observed dead end. This negative memory is co-equal with positive policies and should redirect generation before another official submission.

## Procedure
- A raw malformed HTML/encoding candidate caused only a local wrapper crash and official submission rejected it. Subsequent raw and front-control-prefixed HTML candidates with charset switches and unterminated attributes stayed clean, indicating the required push-parser encoding-switch failure state was not reached.
- When `no_crash x local_crash_rejected_by_official_then_parser_not_reached` appears for `html`, treat this candidate family as a basin-to-avoid rather than as evidence of proximity to the target.
- Keep any proven parser/harness envelope, but change the missing gate or state relation before submitting again.

## Format Contract
- The target content is HTML with meta charset or content-type declarations and attributes. Charset changes and malformed/unclosed attributes are relevant, but the parser must be driven through libxml2's HTML input buffering and encoding conversion paths rather than merely supplying invalid markup.
- Harness: The libxml2 HTML fuzzer does not treat all bytes purely as document text; a leading control area can select parser options and allocation behavior before the remaining bytes are parsed as HTML. The harness exercises both pull and push parsing paths with bounded chunks.

## Negative Memory
- Do not treat this verifier signal as a near miss unless a later candidate changes the missing gate or state relation.
- Do not submit candidates that are clean, parser-mismatched, off-target, or crashing both fixed and vulnerable images in this same shape.
- Preserve only descriptive format facts from the failed attempt; do not promote an unverified causal recovery.

## Evidence Shape
- Support: one diagnosed persistent failure from round 16.
- Scope: generator avoidance for the same failure-keyed basin.
