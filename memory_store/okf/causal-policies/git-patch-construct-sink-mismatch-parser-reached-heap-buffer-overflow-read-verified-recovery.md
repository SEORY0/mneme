---
type: causal-policy
title: "Git Patch Construct Sink Mismatch Parser Reached Heap Buffer Overflow Read Verified Recovery"
description: "Round 27 verified recovery for wrong_sink with verifier signal sink_mismatch_parser_reached."
failure_class: "wrong_sink"
verifier_signal: "sink_mismatch_parser_reached"
candidate_family: "construct"
input_format: "git-patch"
harness_convention: "libfuzzer"
vuln_class: "heap-buffer-overflow-read"
access_scope: generate
success_count: 1
confidence: high
tags: ["wrong-sink", "sink-mismatch-parser-reached", "git-patch", "libfuzzer", "construct", "heap-buffer-overflow-read", "verified-recovery", "round-27"]
match_keys: ["wrong_sink", "sink_mismatch_parser_reached", "git-patch", "libfuzzer", "heap-buffer-overflow-read", "verified_recovery"]
allowed_scopes: [generate]
forbidden_fields: [raw_poc_bytes, task_id, exact_offset, checksum, submit_metadata]
evidence_level: high
train_only: true
round: 27
---
# Git Patch Construct Sink Mismatch Parser Reached Heap Buffer Overflow Read Verified Recovery

## Policy
For `wrong_sink x sink_mismatch_parser_reached`, preserve the format and harness gates that reached the parser or sink, then apply the verified causal relation below. This is a positive recovery policy because the official vulnerable/fixed verifier recorded a target match.

## Procedure
1. Use the harness prefix selector followed by a syntactically valid git binary patch envelope.
2. Reach the binary-patch side parser, then terminate a base85 data line immediately after the decoded-length marker so the remaining-line length check underflows and the decoder reads past the input buffer.
3. Keep the carrier abstract: preserve the gate/invariant relation, not any task-local bytes or offsets.
4. If a later candidate changes the verifier signal, re-rank against the new failure key before mutating unrelated fields.

## Format Contract
- The patch parser accepts a git diff header, an index header, then a GIT binary patch body.
- Binary sides start with a literal or delta size line followed by base85 data lines whose first character encodes decoded length.
- The parser expects encoded data and a newline after that marker.
- Harness [[libfuzzer]]:
  - The libFuzzer harness consumes the first raw input byte as the patch prefix length option and passes all remaining bytes directly to git_patch_from_buffer.
  - There is no checksum, file container, or FuzzedDataProvider layout.

## Negative Memory
- Do not broaden mutations after the parser or harness gate is proven.
- Do not submit candidates that reproduce on the fixed image or move to an off-target wrapper crash.
- Do not store payload bytes, exact offsets, checksums, or task-local identifiers.

## Evidence Shape
- Support: one round-27 worker trace with official target match.
- Scope: generator repair for the same failure-keyed basin; pair with [[git-patch]] and [[libfuzzer]].
