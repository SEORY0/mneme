---
type: negative-memory
title: "SDP Construct SDP Long Line Null Attribute Fmtp Truncation SDP Parser Reached But Target Invariant Not Matched Null Pointer Dereference Or Tokenizer Crash Negative Memory"
description: "Round 29 negative memory for no_crash with verifier signal sdp_parser_reached_but_target_invariant_not_matched."
failure_class: "no_crash"
verifier_signal: "sdp_parser_reached_but_target_invariant_not_matched"
candidate_family: "construct_sdp_long_line|null_attribute|fmtp_truncation"
input_format: "sdp"
harness_convention: "libfuzzer"
vuln_class: "null-pointer-dereference-or-tokenizer-crash"
access_scope: generate
success_count: 0
failure_count: 1
confidence: medium
tags: ["no-crash", "sdp-parser-reached-but-target-invariant-not-matched", "sdp", "libfuzzer", "construct-sdp-long-line-null-attribute-fmtp-truncation", "null-pointer-dereference-or-tokenizer-crash", "negative-memory", "round-29"]
match_keys: ["no_crash", "sdp_parser_reached_but_target_invariant_not_matched", "sdp", "libfuzzer", "null-pointer-dereference-or-tokenizer-crash", "no-crash", "sdp-parser-reached-but-target-invariant-not-matched", "sdp", "libfuzzer", "null-pointer-dereference-or-tokenizer-crash", "negative_memory", "construct_sdp_long_line|null_attribute|fmtp_truncation", "construct-sdp-long-line-null-attribute-fmtp-truncation"]
allowed_scopes: [generate]
forbidden_fields: [raw_poc_bytes, task_id, exact_offset, checksum, submit_metadata]
evidence_level: medium
train_only: true
round: 29
---
# SDP Construct SDP Long Line Null Attribute Fmtp Truncation SDP Parser Reached But Target Invariant Not Matched Null Pointer Dereference Or Tokenizer Crash Negative Memory

- key: `no_crash x sdp_parser_reached_but_target_invariant_not_matched`
- outcome: persistent failure / basin to avoid
- success_count: 0
- failure_count: 1
- related format facts: [[sdp]]
- related harness facts: [[libfuzzer]]

## Failure Shape
Direct SDP text can reach the GPAC RTP/SDP path when the recognition markers and line terminators are present. Null-valued session, media, and FMTP attributes produced vulnerable crashes, but the fixed build also crashed, so those were overbroad off-target states. Terminated overlong connection lines reached parser and socket setup but did not produce a target sanitizer failure; unterminated final lines are not tokenized by this parser.

## Policy
Treat `no_crash x sdp_parser_reached_but_target_invariant_not_matched` on `sdp` for `null-pointer-dereference-or-tokenizer-crash` as a basin to avoid unless a new candidate changes the parser gate, state relation, or sink relation described below. Preserve any proven reachability, but reject variants that return to the same clean-exit, off-target-crash, wrong-sink, usage-only, wrapper-mismatch, or both-image-crash basin.

## Procedure
1. Keep only the smallest parser or harness envelope that was actually reached.
2. Identify the missing causal relation from the signal: parser selection, container acceptance, length relation, stateful subobject, allocation state, or official target sink.
3. Change one relation at a time and discard candidates that return to the same `sdp_parser_reached_but_target_invariant_not_matched` basin.
4. If a local crash is not an official target match, shrink or discard it before mutating deeper fields.
5. Promote a recovery from this basin only after a later verifier-confirmed target match.

## Negative Memory
- Do not resubmit broad mutations that only reproduce `sdp_parser_reached_but_target_invariant_not_matched`.
- Do not count parser reachability, both-image crashes, local wrapper crashes, usage banners, clean exits, or fixed-image crashes as success.
- Never store payload bytes, exact positions, task identifiers, checksums, or submit metadata.

## Format Contract
SDP is line-oriented text with session fields such as version, origin, session name, timing, connection, media, and attributes. GPAC's SDP probe recognizes text by line breaks plus version, origin, and connection markers. The SDP parser processes only terminated logical lines, tokenizes fields into fixed-size temporary buffers, and can represent generic or FMTP attributes with absent values.

## Harness Contract
The active binary is GPAC fuzz_probe_analyze. It writes the raw input bytes to a temporary extensionless file and runs the GPAC probe/analyze filter graph; there is no leading mode byte or FuzzedDataProvider layout. Format reachability depends on content probing into the RTP/SDP input filter.

## Evidence Shape
- Support: 1 diagnosed persistent failure from round 29 after 14 attempts.
- Scope: generator repair and basin avoidance only.
