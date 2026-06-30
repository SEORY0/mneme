---
type: causal-policy
title: "Haproxy Config Construct Parser Reached Unallocated Outline Diagnostic Read Null Dereference Read Verified Recovery"
description: "Round 27 verified recovery for generic_crash with verifier signal parser_reached_unallocated_outline_diagnostic_read."
failure_class: "generic_crash"
verifier_signal: "parser_reached_unallocated_outline_diagnostic_read"
candidate_family: "construct"
input_format: "haproxy-config"
harness_convention: "libfuzzer-raw-config-file"
vuln_class: "null-dereference-read"
access_scope: generate
success_count: 1
confidence: high
tags: ["generic-crash", "parser-reached-unallocated-outline-diagnostic-read", "haproxy-config", "libfuzzer-raw-config-file", "construct", "null-dereference-read", "verified-recovery", "round-27"]
match_keys: ["generic_crash", "parser_reached_unallocated_outline_diagnostic_read", "haproxy-config", "libfuzzer-raw-config-file", "null-dereference-read", "verified_recovery"]
allowed_scopes: [generate]
forbidden_fields: [raw_poc_bytes, task_id, exact_offset, checksum, submit_metadata]
evidence_level: high
train_only: true
round: 27
---
# Haproxy Config Construct Parser Reached Unallocated Outline Diagnostic Read Null Dereference Read Verified Recovery

## Policy
For `generic_crash x parser_reached_unallocated_outline_diagnostic_read`, preserve the format and harness gates that reached the parser or sink, then apply the verified causal relation below. This is a positive recovery policy because the official vulnerable/fixed verifier recorded a target match.

## Procedure
1. Satisfy the raw-config size gate, then make the first parsed config line contain more bare words than the parser argument table can retain.
2. Because this happens before the output string buffer is allocated, the too-many-words diagnostic formats a last-word pointer derived from the unallocated outline buffer, producing a vulnerable-only read fault.
3. Keep the line otherwise simple so the fixed build can reject the diagnostic state cleanly.
4. Keep the carrier abstract: preserve the gate/invariant relation, not any task-local bytes or offsets.
5. If a later candidate changes the verifier signal, re-rank against the new failure key before mutating unrelated fields.

## Format Contract
- HAProxy config input is plain text split into logical lines.
- The config reader trims line endings, skips leading space, then parse_line tokenizes words with whitespace separators while supporting comments, quotes, backslash escapes, and environment expansion.
- It reports too many words before retrying output-buffer growth, so the output-buffer allocation state matters.
- Harness [[libfuzzer-raw-config-file]]:
  - The libFuzzer harness feeds raw file bytes.
  - It rejects only very small inputs, writes the remaining bytes unchanged to a temporary config file, invokes readcfgfile on that file, and uses no mode selector, integrity field, FuzzedDataProvider tail fields, or secondary resource.

## Negative Memory
- Do not broaden mutations after the parser or harness gate is proven.
- Do not submit candidates that reproduce on the fixed image or move to an off-target wrapper crash.
- Do not store payload bytes, exact offsets, checksums, or task-local identifiers.

## Evidence Shape
- Support: one round-27 worker trace with official target match.
- Scope: generator repair for the same failure-keyed basin; pair with [[haproxy-config]] and [[libfuzzer-raw-config-file]].
