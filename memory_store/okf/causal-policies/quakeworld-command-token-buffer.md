---
type: causal-policy
title: QuakeWorld Command Token Buffer Recovery
description: Recover UDP-framed QuakeWorld tokenizer crashes by preserving dispatch and overflowing only the first connectionless command token.
failure_class: wrong_sink
verifier_signal: parser_reached_sink_mismatch
candidate_family: construct
input_format: udp-framed-quakeworld
harness_convention: fuzzshark-ip-proto-udp
vuln_class: global-buffer-overflow-write
access_scope: generate
success_count: 1
confidence: medium
tags: [wrong_sink, parser_reached_sink_mismatch, udp, quakeworld, command_token]
match_keys: [wrong_sink, parser_reached_sink_mismatch, udp-framed-quakeworld, command_token]
allowed_scopes: [generate]
forbidden_fields: [raw_poc_bytes, task_id, exact_offset, checksum, submit_metadata]
evidence_level: medium
train_only: true
---
## Policy
When a packet dissector task names QuakeWorld command parsing, a wrong-sink parser-reached crash can still be server-relevant if the candidate enters the server-port dispatch and the connectionless command tokenizer. Preserve packet framing and mutate only the first command token length.

## Procedure
1. Build an outer UDP-framed packet that selects the QuakeWorld dissector through the server-port path.
2. Use the connectionless text-command path rather than ordinary payload bytes.
3. Keep the command delimiter and packet length fields coherent.
4. Grow the first command token past the tokenizer's fixed internal buffer while leaving later command syntax ordinary.
5. If local sink naming points at a tokenizer helper but dispatch is correct, submit once for official comparison.

## Negative Memory
- Do not fuzz UDP payload bytes before confirming QuakeWorld dispatch.
- Do not change the port or framing while testing token length.
- Do not treat unrelated dissector crashes as progress for this policy.
