---
type: causal-policy
title: "SDP Token Linebuf Overflow"
description: "Round 6 verified recovery for wrong_sink with verifier signal parser_reached_sdp_tokenizer."
failure_class: "wrong_sink"
verifier_signal: "parser_reached_sdp_tokenizer"
candidate_family: "construct_sdp_long_line"
input_format: "sdp"
harness_convention: "AFL/libfuzzer file through GPAC probe-analyze filter graph"
vuln_class: "stack-buffer-overflow-write"
access_scope: generate
success_count: 1
confidence: high
tags: ["wrong-sink", "parser-reached-sdp-tokenizer", "sdp", "construct-sdp-long-line", "verified-recovery", "round-6"]
match_keys: ["wrong_sink", "parser_reached_sdp_tokenizer", "sdp", "AFL/libfuzzer file through GPAC probe-analyze filter graph", "stack-buffer-overflow-write", "verified_recovery"]
allowed_scopes: [generate]
forbidden_fields: [raw_poc_bytes, task_id, exact_offset, checksum, submit_metadata]
evidence_level: high
train_only: true
round: 6
---
# SDP Token Linebuf Overflow

## Policy
For `wrong_sink x parser_reached_sdp_tokenizer`, preserve the format and harness gates that reached the parser/sink, then apply the verified causal relation below. This is a positive recovery policy because the official vulnerable/fixed verifier recorded a target match.

## Procedure
1. Use a valid SDP session preamble so GPAC routes the file to the RTP/SDP input filter, then place an overlong connection-style line that lacks an early line break. This reaches SDP parsing and overflows the fixed line/token buffer while the fixed build rejects or bounds the token copy.
2. Keep the carrier abstract: preserve the gate/invariant relation, not any task-local bytes or offsets.
3. If a later candidate changes the verifier signal, re-rank against the new failure key before mutating unrelated fields.

## Format Contract
- SDP is line-oriented text with session-level fields such as version, origin, session name, timing, connection, media, and attributes. GPAC must first classify the text as SDP before gf_sdp_info_parse tokenizes each line into fixed-size temporary buffers.
- Harness: The selected GPAC fuzzer writes the raw input as a temporary file and runs the probe/analyze filter graph. Direct SDP text can be routed into the RTP input filter when the leading session fields are coherent; the crash path is not a direct call to the SDP parser from the harness.

## Negative Memory
- Do not broaden mutations after the parser/harness gate is proven.
- Do not submit candidates that reproduce on the fixed image or move to an off-target wrapper crash.
- Do not store raw payload bytes, exact offsets, checksums, or task-local identifiers.

## Evidence Shape
- Support: one round-6 worker trace with official target match.
- Scope: generator repair for the same failure-keyed basin.
