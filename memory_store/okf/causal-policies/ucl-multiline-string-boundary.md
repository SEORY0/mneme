---
type: causal-policy
title: UCL Multiline String Boundary Recovery
description: Failure-keyed recovery for UCL multiline terminator inputs that crash at the post-terminator newline invariant.
failure_class: wrong_sink
verifier_signal: sanitizer_crash
candidate_family: construct
input_format: ucl
harness_convention: libfuzzer
vuln_class: heap-buffer-overflow-read
access_scope: generate
success_count: 1
confidence: medium
tags: [wrong_sink, sanitizer_crash, ucl, multiline_string, terminator_boundary]
match_keys: [wrong_sink, sanitizer_crash, ucl, multiline_string, terminator_boundary]
allowed_scopes: [generate]
forbidden_fields: [raw_poc_bytes, task_id, exact_offset, checksum, submit_metadata]
evidence_level: medium
train_only: true
related: [wrong-sink-repair]
---
## Policy
When a UCL parser accepts the assignment and then crashes near a helper sink, keep the wrapper minimal and target the multiline-string terminator boundary. A helper-level sanitizer crash can be server-relevant when the malformed end-of-input is inside the described parser feature.

## Procedure
1. Build a valid assignment that selects the multiline string scanner.
2. Open and close the multiline marker correctly so the string gate is reached.
3. End the input immediately after the marker terminator instead of supplying the following line break the parser expects.
4. Keep the key, assignment operator, and marker syntax ordinary; the only violation should be the missing byte after the terminator.
5. If local classification says wrong sink but the crash is inside the multiline scanner, submit once for server confirmation.

## Negative Memory
- Do not corrupt the opening marker or assignment syntax; that becomes bad-format evidence.
- Do not pad past the terminator while searching for this bug; padding satisfies the invariant.
- Do not discard a parser-helper crash solely because local sink naming is narrower than the task description.

## Evidence Shape
- Support: 1 server-verified round observation.
- Scope: generator repair for UCL multiline string boundary bugs.
