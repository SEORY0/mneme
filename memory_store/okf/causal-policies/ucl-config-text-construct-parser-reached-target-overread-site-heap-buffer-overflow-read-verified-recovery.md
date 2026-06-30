---
type: causal-policy
title: "Ucl Config Text Construct Parser Reached Target Overread Site Heap Buffer Overflow Read Verified Recovery"
description: "Round 27 verified recovery for wrong_sink with verifier signal parser_reached_target_overread_site."
failure_class: "wrong_sink"
verifier_signal: "parser_reached_target_overread_site"
candidate_family: "construct"
input_format: "ucl-config-text"
harness_convention: "libfuzzer"
vuln_class: "heap-buffer-overflow-read"
access_scope: generate
success_count: 1
confidence: high
tags: ["wrong-sink", "parser-reached-target-overread-site", "ucl-config-text", "libfuzzer", "construct", "heap-buffer-overflow-read", "verified-recovery", "round-27"]
match_keys: ["wrong_sink", "parser_reached_target_overread_site", "ucl-config-text", "libfuzzer", "heap-buffer-overflow-read", "verified_recovery"]
allowed_scopes: [generate]
forbidden_fields: [raw_poc_bytes, task_id, exact_offset, checksum, submit_metadata]
evidence_level: high
train_only: true
round: 27
---
# Ucl Config Text Construct Parser Reached Target Overread Site Heap Buffer Overflow Read Verified Recovery

## Policy
For `wrong_sink x parser_reached_target_overread_site`, preserve the format and harness gates that reached the parser or sink, then apply the verified causal relation below. This is a positive recovery policy because the official vulnerable/fixed verifier recorded a target match.

## Procedure
1. Use the built-in include macro path rather than an ordinary key/value assignment.
2. Enable URL handling through macro arguments, then make the include target end immediately after the first character of the URL separator pattern so the URL detector sees a partial candidate with too little remaining haystack.
3. The vulnerable build compares the rest of the separator past the macro value boundary; the fixed build rejects the incomplete remainder.
4. Keep the carrier abstract: preserve the gate/invariant relation, not any task-local bytes or offsets.
5. If a later candidate changes the verifier signal, re-rank against the new failure key before mutating unrelated fields.

## Format Contract
- UCL configuration text accepts dot-prefixed built-in macros.
- Macro arguments are parsed as UCL option objects, and macro bodies can be unquoted atom text, quoted text, or braced text.
- The include-family macros pass their body bytes and explicit body length to include handling; URL handling is controlled by a boolean macro option.
- Harness [[libfuzzer]]:
  - The libFuzzer target passes the input buffer directly to a default UCL parser through the add-string API.
  - Empty input is ignored.
  - There is no selector byte, file envelope, integrity field, or FuzzedDataProvider front/back split.

## Negative Memory
- Do not broaden mutations after the parser or harness gate is proven.
- Do not submit candidates that reproduce on the fixed image or move to an off-target wrapper crash.
- Do not store payload bytes, exact offsets, checksums, or task-local identifiers.

## Evidence Shape
- Support: one round-27 worker trace with official target match.
- Scope: generator repair for the same failure-keyed basin; pair with [[ucl-config-text]] and [[libfuzzer]].
