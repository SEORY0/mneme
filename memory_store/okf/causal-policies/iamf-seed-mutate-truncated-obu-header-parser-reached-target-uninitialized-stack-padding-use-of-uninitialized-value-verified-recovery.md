---
type: causal-policy
title: "Iamf Seed Mutate Truncated Obu Header Parser Reached Target Uninitialized Stack Padding Use Of Uninitialized Value Verified Recovery"
description: "Round 28 verified recovery for wrong_sink with verifier signal parser_reached_target_uninitialized_stack_padding."
failure_class: "wrong_sink"
verifier_signal: "parser_reached_target_uninitialized_stack_padding"
candidate_family: "seed_mutate_truncated_obu_header"
input_format: "iamf"
harness_convention: "libfuzzer-ffmpeg-demuxer-iamf"
vuln_class: "use-of-uninitialized-value"
access_scope: generate
success_count: 1
confidence: high
tags: ["wrong-sink", "parser-reached-target-uninitialized-stack-padding", "iamf", "libfuzzer-ffmpeg-demuxer-iamf", "seed-mutate-truncated-obu-header", "use-of-uninitialized-value", "verified-recovery", "round-28"]
match_keys: ["wrong_sink", "parser_reached_target_uninitialized_stack_padding", "iamf", "libfuzzer-ffmpeg-demuxer-iamf", "use-of-uninitialized-value", "verified_recovery", "seed-mutate", "use-of-uninitialized-value"]
allowed_scopes: [generate]
forbidden_fields: [raw_poc_bytes, task_id, exact_offset, checksum, submit_metadata]
evidence_level: high
train_only: true
round: 28
---
# Iamf Seed Mutate Truncated Obu Header Parser Reached Target Uninitialized Stack Padding Use Of Uninitialized Value Verified Recovery

## Policy
For `wrong_sink x parser_reached_target_uninitialized_stack_padding`, preserve the format and harness gates that reached the parser or sink, then apply the verified causal relation below. This is a positive recovery policy because the official vulnerable/fixed verifier recorded a target match.

## Procedure
1. Start from a valid IAMF sample so demuxer probing and descriptor parsing create at least one stream. Preserve the descriptor prefix and a complete audio frame, then truncate the following OBU to only a header prefix. This reaches ff_iamf_read_packet after stream setup and makes the OBU header parser consume uninitialized stack padding from the reader's header buffer while parsing the incomplete next OBU.
2. Keep the carrier abstract: preserve the gate, invariant, and sink relation rather than task-local bytes, exact offsets, checksums, or identifiers.
3. If the verifier signal changes, re-rank against the new failure key before mutating unrelated fields.

## Format Contract
- Format [[iamf]]: IAMF streams are made of OBU records. Each OBU begins with a bit-packed type/flag byte and a LEB128 size, followed by optional trimming or extension fields before the payload. A sequence-header OBU identifies the stream, descriptor OBUs define codec configuration, audio elements, and mix presentation, and later parameter/audio-frame OBUs are read by the packet path.
- Harness [[libfuzzer-ffmpeg-demuxer-iamf]]: The FFmpeg demuxer fuzzer feeds raw bytes through an AVIOContext to the IAMF demuxer. With the IAMF demuxer selected, avformat_open_input and avformat_find_stream_info parse descriptors and then call av_read_frame/ff_iamf_read_packet. The packet reader reads a fixed-size OBU header window from the current stream position and passes that stack buffer to the IAMF OBU header parser.

## Negative Memory
- Do not broaden mutations after parser or harness reachability is proven.
- Do not submit candidates that reproduce on the fixed image, crash both images, or move to an off-target wrapper crash.
- Do not store payload bytes, exact offsets, checksums, or task-local identifiers.

## Evidence Shape
- Support: one round-28 worker trace with official target match.
- Scope: generator repair for the same failure-keyed basin; pair with [[iamf]] and [[libfuzzer-ffmpeg-demuxer-iamf]].
