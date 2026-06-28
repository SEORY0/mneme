---
type: causal-policy
title: "Markdown Construct From Description Parser Reached Container Marker Overread Heap Buffer Overflow Read Verified Recovery"
description: "Round 9 verified recovery for wrong_sink with verifier signal parser_reached_container_marker_overread."
failure_class: "wrong_sink"
verifier_signal: "parser_reached_container_marker_overread"
candidate_family: "construct-from-description"
input_format: "markdown"
harness_convention: "libfuzzer"
vuln_class: "heap-buffer-overflow-read"
access_scope: generate
success_count: 1
confidence: high
tags: ["wrong-sink", "parser-reached-container-marker-overread", "markdown", "construct-from-description", "verified-recovery", "round-9"]
match_keys: ["wrong_sink", "parser_reached_container_marker_overread", "markdown", "libfuzzer", "heap-buffer-overflow-read", "verified_recovery"]
allowed_scopes: [generate]
forbidden_fields: [raw_poc_bytes, task_id, exact_offset, checksum, submit_metadata]
evidence_level: high
train_only: true
round: 9
---
# Markdown Construct From Description Parser Reached Container Marker Overread Heap Buffer Overflow Read Verified Recovery

## Policy
For `wrong_sink x parser_reached_container_marker_overread`, preserve the format and harness gates that reached the target path, then apply the verified causal relation below. This is a positive recovery policy because the official vulnerable/fixed verifier recorded a target match.

## Procedure
1. Provide the two fuzzer flag words, then a Markdown document that reaches md4c container-mark
  parsing with malformed or unterminated marker text near embedded string terminators.
1. The vulnerable scanner reads past the available marker buffer while classifying a container mark;
  the fixed build bounds the scan.

## Format Contract
- The document body is ordinary Markdown, and the target parser accepts raw text including embedded
  string terminators and punctuation-heavy heading/list markers.
- No file container, checksum, or length table is required.

## Harness Contract
- The md4c HTML fuzzer consumes two little-endian flag words from the front of the input, then
  passes all remaining bytes as the Markdown buffer to the HTML renderer.

## Related Knowledge
- Format facts: [[markdown]]
- Harness facts: [[libfuzzer]]

## Negative Memory
- Do not broaden mutations after the parser/harness gate is proven.
- Do not submit candidates that reproduce on the fixed image, move to an off-target wrapper crash, or only preserve a local-only crash signal.
- Do not store raw payload bytes, exact offsets, checksums, or task-local identifiers.

## Evidence Shape
- Support: one round-9 worker trace with official target match.
- Scope: generator repair for the same failure-keyed basin.
