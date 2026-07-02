---
type: causal-policy
title: "Sip Message Construct Parser Reached Via Boundary Read Off By One Read Overflow Verified Recovery"
description: "Round 28 verified recovery for wrong_sink with verifier signal parser_reached_via_boundary_read."
failure_class: "wrong_sink"
verifier_signal: "parser_reached_via_boundary_read"
candidate_family: "construct"
input_format: "sip-message"
harness_convention: "libfuzzer"
vuln_class: "off-by-one-read-overflow"
access_scope: generate
success_count: 1
confidence: high
tags: ["wrong-sink", "parser-reached-via-boundary-read", "sip-message", "libfuzzer", "construct", "off-by-one-read-overflow", "verified-recovery", "round-28"]
match_keys: ["wrong_sink", "parser_reached_via_boundary_read", "sip-message", "libfuzzer", "off-by-one-read-overflow", "verified_recovery", "construct", "other"]
allowed_scopes: [generate]
forbidden_fields: [raw_poc_bytes, task_id, exact_offset, checksum, submit_metadata]
evidence_level: high
train_only: true
round: 28
---
# Sip Message Construct Parser Reached Via Boundary Read Off By One Read Overflow Verified Recovery

## Policy
For `wrong_sink x parser_reached_via_boundary_read`, preserve the format and harness gates that reached the parser or sink, then apply the verified causal relation below. This is a positive recovery policy because the official vulnerable/fixed verifier recorded a target match.

## Procedure
1. Build a minimal raw SIP request with a syntactically valid start line and route parsing into the Via header parser. Terminate the fuzzer buffer immediately after a Via component that normally expects a NUL terminator or more header text, so the parser performs its one-byte lookahead past the supplied buffer while staying in the intended Via parsing path.
2. Keep the carrier abstract: preserve the gate, invariant, and sink relation rather than task-local bytes, exact offsets, checksums, or identifiers.
3. If the verifier signal changes, re-rank against the new failure key before mutating unrelated fields.

## Format Contract
- Format [[sip-message]]: SIP messages are ASCII start-line plus CRLF-delimited headers. A Via header carries a protocol/transport prefix followed by a sent-by host and optional port or parameters. Fuzzer inputs can omit the final header terminator, so a final truncated header is still enough to enter header-specific parsing before the buffer boundary is reached.
- Harness [[libfuzzer]]: The harness feeds the raw input bytes directly to the OpenSIPS message parser through the sip_msg buffer and length fields. There is no leading mode byte, checksum, size table, or FuzzedDataProvider carving; after parse, the harness frees the parsed sip_msg structure.

## Negative Memory
- Do not broaden mutations after parser or harness reachability is proven.
- Do not submit candidates that reproduce on the fixed image, crash both images, or move to an off-target wrapper crash.
- Do not store payload bytes, exact offsets, checksums, or task-local identifiers.

## Evidence Shape
- Support: one round-28 worker trace with official target match.
- Scope: generator repair for the same failure-keyed basin; pair with [[sip-message]] and [[libfuzzer]].
