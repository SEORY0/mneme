---
type: causal-policy
title: "AAC SBR Fuzzer Buffer Seed Mutate Parser Reached Sink Mismatch Label But Stack Matches Hf Adjustment Global Buffer Overflow Read Verified Recovery"
description: "Round 8 verified recovery for wrong_sink with verifier signal parser_reached_sink_mismatch_label_but_stack_matches_hf_adjustment."
failure_class: "wrong_sink"
verifier_signal: "parser_reached_sink_mismatch_label_but_stack_matches_hf_adjustment"
candidate_family: "seed_mutate"
input_format: "aac-sbr-fuzzer-buffer"
harness_convention: "libfuzzer"
vuln_class: "global-buffer-overflow-read"
access_scope: generate
success_count: 1
confidence: high
tags: ["wrong-sink", "parser-reached-sink-mismatch-label-but-stack-matches-hf-adjustment", "aac-sbr-fuzzer-buffer", "seed-mutate", "verified-recovery", "round-8"]
match_keys: ["wrong_sink", "parser_reached_sink_mismatch_label_but_stack_matches_hf_adjustment", "aac-sbr-fuzzer-buffer", "libfuzzer", "global-buffer-overflow-read", "verified_recovery"]
allowed_scopes: [generate]
forbidden_fields: [raw_poc_bytes, task_id, exact_offset, checksum, submit_metadata]
evidence_level: high
train_only: true
round: 8
---
# AAC SBR Fuzzer Buffer Seed Mutate Parser Reached Sink Mismatch Label But Stack Matches Hf Adjustment Global Buffer Overflow Read Verified Recovery

## Policy
For `wrong_sink x parser_reached_sink_mismatch_label_but_stack_matches_hf_adjustment`, preserve the format and harness gates that reached the target path, then apply the verified causal relation below. This is a positive recovery policy because the official vulnerable/fixed verifier recorded a target match.

## Procedure
1. Use the FAAD2 decoder fuzzer envelope to split input into decoder-initialization bytes, a first decode chunk, and a second decode chunk. The AAC payload must initialize successfully, reach SBR coupled-channel HF adjustment, and carry out-of-range envelope or pan-energy values so find_log2_E indexes beyond the valid pan-log table during gain calculation. The fixed build rejects these SBR scalar ranges before table lookup.
2. Keep the carrier abstract: preserve the gate/invariant relation, not task-local bytes, offsets, checksums, or submission metadata.
3. If a later candidate changes the verifier signal, re-rank against the new failure key before mutating unrelated fields.

## Format Contract
- This harness input is not a standalone AAC file. It begins with two little-endian chunk lengths, a flag byte, a NeAACDecConfiguration struct image, then three byte regions consumed by NeAACDecInit or NeAACDecInit2 and subsequent NeAACDecDecode calls. The audio payload must be coherent enough for AAC frame decoding, channel-pair reconstruction, and SBR processing to run.
- Harness: The libFuzzer target reads raw bytes with a fixed front matter: len1, len2, flags, decoder configuration, then three payload chunks. Flags select Init versus Init2, optional post-seek resets, optional Decode2 output-buffer mode, and optional DRM initialization. There is no file-extension or container detection outside this harness-specific split.

## Negative Memory
- Do not broaden mutations after the parser/harness gate is proven.
- Do not submit candidates that reproduce on the fixed image or move to an off-target wrapper crash.
- Do not store raw payload bytes, exact offsets, checksums, or task-local identifiers.

## Evidence Shape
- Support: one round-8 worker trace with official target match.
- Scope: generator repair for the same failure-keyed basin.
