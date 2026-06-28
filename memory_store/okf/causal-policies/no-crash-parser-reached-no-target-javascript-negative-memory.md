---
type: causal-policy
title: "No Crash Parser Reached No Target Javascript Negative Memory"
description: "Round 7 negative memory for no_crash with verifier signal parser_reached_no_target."
failure_class: "no_crash"
verifier_signal: "parser_reached_no_target"
candidate_family: "construct"
input_format: "javascript"
harness_convention: "libfuzzer"
vuln_class: "parser-differential"
access_scope: generate
success_count: 0
confidence: medium
tags: ["no-crash", "parser-reached-no-target", "javascript", "negative-memory", "round-7"]
match_keys: ["no_crash", "parser_reached_no_target", "javascript", "libfuzzer", "parser-differential", "negative_memory"]
allowed_scopes: [generate]
forbidden_fields: [raw_poc_bytes, task_id, exact_offset, checksum, submit_metadata]
evidence_level: medium
train_only: true
round: 7
---
# No Crash Parser Reached No Target Javascript Negative Memory

- key: `no_crash x parser_reached_no_target`
- outcome: persistent failure / basin to avoid
- success_count: 0
- failure_count: 1
- related format facts: [[javascript]]
- related harness facts: [[libfuzzer]]

## Failure Shape
Invalid UTF-8 lead bytes around string delimiters and Unicode line-separator bytes reached the JS
parser but did not trigger a crash or official differential.

## Policy
Treat `no_crash x parser_reached_no_target` on `javascript` as a basin to avoid unless a new candidate changes the specific parser gate, state relation, or sink relation described below. Preserve any proven reachability, but reject variants that return the same verifier signal without changing the causal gate under test.

## Procedure
1. Keep only the smallest parser or harness envelope that the verifier proved was reached.
2. Identify the missing causal relation from the signal: parser selection, container acceptance, length relation, stateful subobject, allocation state, or official target sink.
3. Change one relation at a time and discard candidates that return to the same clean-exit, off-target-crash, wrong-sink, usage-only, or both-image-crash basin.
4. If a local crash is not an official target match, shrink or discard it before mutating deeper fields.
5. Promote a recovery from this basin only after a later verifier-confirmed target match.

## Negative Memory
- Do not resubmit broad mutations that only reproduce `parser_reached_no_target`.
- Do not count parser reachability, both-image crashes, local wrapper crashes, or clean exits as success.
- Do not store raw payload bytes, exact positions, task identifiers, or submit metadata.

## Format Contract
The input is JavaScript source text. String literals are delimited by single or double quotes; the
lexer also treats ECMAScript line-separator and paragraph-separator byte sequences as line
terminators.

## Harness Contract
FuzzJs wraps the raw bytes in a StringView, lexes and parses a program, and only runs it if parsing
has no errors. There is no mode selector or length-prefixed layout.

## Evidence Shape
- Support: 1 diagnosed persistent failure from round 7.
- Scope: generator repair and basin avoidance only.
