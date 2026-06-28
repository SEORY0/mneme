---
type: negative-memory
title: "No Crash Parser Reached Clean Or Syntax Rejected Php Source Construct Null Deref Or Invalid Token Metadata Negative Memory"
description: "Round 25 negative memory for no_crash with verifier signal parser_reached_clean_or_syntax_rejected."
failure_class: "no_crash"
verifier_signal: "parser_reached_clean_or_syntax_rejected"
candidate_family: "construct"
input_format: "php-source"
harness_convention: "libfuzzer"
vuln_class: "null-deref-or-invalid-token-metadata"
access_scope: generate
success_count: 0
confidence: medium
tags: ["no-crash", "parser-reached-clean-or-syntax-rejected", "php-source", "libfuzzer", "construct", "negative-memory", "round-25"]
match_keys: ["no_crash", "parser_reached_clean_or_syntax_rejected", "php-source", "libfuzzer", "null-deref-or-invalid-token-metadata", "negative_memory"]
allowed_scopes: [generate]
forbidden_fields: [raw_poc_bytes, task_id, exact_offset, checksum, submit_metadata]
evidence_level: medium
train_only: true
round: 25
---
# No Crash Parser Reached Clean Or Syntax Rejected Php Source Construct Null Deref Or Invalid Token Metadata Negative Memory

- key: `no_crash x parser_reached_clean_or_syntax_rejected`
- outcome: persistent failure / basin to avoid
- success_count: 0
- failure_count: 1
- related format facts: [[php-source]]
- related harness facts: [[libfuzzer]]

## Failure Shape
The short-echo token can be produced without identifier metadata, but the attempted source layouts did not place that token in a grammar position that calls the semi-reserved identifier conversion. Closing-tag and short-echo transitions either injected a statement boundary, parsed as normal output syntax, or were rejected before the vulnerable identifier path.

## Policy
Treat `no_crash x parser_reached_clean_or_syntax_rejected` on `php-source` as a basin to avoid unless a new candidate changes the parser gate, state relation, or sink relation described below. Preserve any proven reachability, but reject variants that return to the same clean-exit, off-target-crash, wrong-sink, usage-only, wrapper-mismatch, or both-image-crash basin.

## Procedure
1. Keep only the smallest parser or harness envelope that was actually reached.
2. Identify the missing causal relation from the signal: parser selection, container acceptance, length relation, stateful subobject, allocation state, or official target sink.
3. Change one relation at a time and discard candidates that return to the same `parser_reached_clean_or_syntax_rejected` basin.
4. If a local crash is not an official target match, shrink or discard it before mutating deeper fields.
5. Promote a recovery from this basin only after a later verifier-confirmed target match.

## Negative Memory
- Do not resubmit broad mutations that only reproduce `parser_reached_clean_or_syntax_rejected`.
- Do not count parser reachability, both-image crashes, local wrapper crashes, usage banners, or clean exits as success.
- Do not store raw payload bytes, exact positions, task identifiers, checksums, or submit metadata.

## Format Contract
The input is PHP source text. Ordinary reserved words in identifier-capable grammar positions carry identifier metadata; the short echo opener can produce the same token kind without that metadata. Namespace import aliases, function names, class/member names, and trait alias constructs are candidate identifier contexts.

## Harness Contract
The harness copies the raw libFuzzer input into a nul-terminated request body and runs the PHP parser/execute fuzzer on it. There is no byte carving or FuzzedDataProvider layout; normal PHP opening and closing tag state transitions determine lexer mode.

## Evidence Shape
- Support: 1 diagnosed persistent failure from round 25 after 12 attempts.
- Scope: generator repair and basin avoidance only.
