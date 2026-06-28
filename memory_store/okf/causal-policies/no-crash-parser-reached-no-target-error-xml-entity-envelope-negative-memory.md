---
type: causal-policy
title: "No Crash Parser Reached No Target Error Xml Entity Envelope Negative Memory"
description: "Round 24 negative memory for no_crash with verifier signal parser_reached_no_target_error."
failure_class: "no_crash"
verifier_signal: "parser_reached_no_target_error"
candidate_family: "construct"
input_format: "xml-entity-envelope"
harness_convention: "afl-libxml2-xml"
vuln_class: "xml-tree-attachment-logic"
access_scope: generate
success_count: 0
confidence: medium
tags: ["no-crash", "parser-reached-no-target-error", "xml-entity-envelope", "afl-libxml2-xml", "construct", "negative-memory", "round-24"]
match_keys: ["no-crash", "parser-reached-no-target-error", "xml-entity-envelope", "afl-libxml2-xml", "xml-tree-attachment-logic"]
allowed_scopes: [generate]
forbidden_fields: [raw_poc_bytes, task_id, exact_offset, checksum, submit_metadata]
evidence_level: medium
train_only: true
round: 24
---
# No Crash Parser Reached No Target Error Xml Entity Envelope Negative Memory

- key: `no_crash x parser_reached_no_target_error`
- outcome: negative memory
- success_count: 0
- failure_count: 1
- formats: [[xml-entity-envelope]]
- harnesses: [[afl-libxml2-xml]]

## Dead-End Shape
Entity-envelope XML documents with XInclude, external parsed entities, xpointer selection, and parser option variations executed successfully but did not create the specific child/sibling attachment inconsistency needed for the bug.

## Policy
For `no_crash x parser_reached_no_target_error` on `xml-entity-envelope`, avoid replaying the observed dead end. This negative memory is co-equal with positive policies and should redirect generation before another official submission. Prefer `construct` only while this format and harness contract are present.

## Procedure
1. When `no_crash x parser_reached_no_target_error` appears for `xml-entity-envelope`, treat this candidate family as a basin-to-avoid rather than evidence of proximity.
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
