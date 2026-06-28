---
type: causal-policy
title: "Ffmpeg Target Dec Fuzzer Stream Construct Parser Reached Vul Only Decoder Write Heap Buffer Overflow Write Verified Recovery"
description: "Round 25 verified recovery for wrong_sink with verifier signal parser_reached_vul_only_decoder_write."
failure_class: "wrong_sink"
verifier_signal: "parser_reached_vul_only_decoder_write"
candidate_family: "construct"
input_format: "ffmpeg-target-dec-fuzzer-stream"
harness_convention: "libfuzzer"
vuln_class: "heap-buffer-overflow-write"
access_scope: generate
success_count: 1
confidence: medium
tags: ["wrong-sink", "parser-reached-vul-only-decoder-write", "ffmpeg-target-dec-fuzzer-stream", "libfuzzer", "construct", "verified-recovery", "round-25"]
match_keys: ["wrong_sink", "parser_reached_vul_only_decoder_write", "ffmpeg-target-dec-fuzzer-stream", "libfuzzer", "heap-buffer-overflow-write"]
allowed_scopes: [generate]
forbidden_fields: [raw_poc_bytes, task_id, exact_offset, checksum, submit_metadata]
evidence_level: high
train_only: true
round: 25
---
# Ffmpeg Target Dec Fuzzer Stream Construct Parser Reached Vul Only Decoder Write Heap Buffer Overflow Write Verified Recovery

- key: `wrong_sink x parser_reached_vul_only_decoder_write`
- outcome: verified recovery
- success_count: 1
- failure_count: 0
- formats: [[ffmpeg-target-dec-fuzzer-stream]]
- harnesses: [[libfuzzer]]

## Failure Shape
Use the codec fuzzer context footer to advertise a small positive video frame while the Tiertex packet itself requests video decoding over the codec's fixed block grid. A packet delimiter keeps the context footer out of the first decoded packet. Selecting a per-block write operation over all fixed-grid blocks makes the decoder write outside the frame allocated from the advertised dimensions; the fixed build establishes the codec's real fixed dimensions before allocation.

## Policy
For `wrong_sink x parser_reached_vul_only_decoder_write` on `ffmpeg-target-dec-fuzzer-stream`, preserve the format recognition and harness contract before varying the vulnerable invariant. Prefer `construct` only while that carrier and harness contract remain stable.

## Procedure
1. Preserve the `ffmpeg-target-dec-fuzzer-stream` carrier and `libfuzzer` harness contract until parser reachability is stable.
2. Apply the causal invariant in the failure shape before broad mutation or seed sweeping.
3. Treat local crash class as supporting signal only; keep the candidate only when vulnerable and fixed images diverge on the official target relation.

## Verifier Contract
The official vulnerable-versus-fixed target match is the confirmation gate for this recovery policy; local crash class is supporting evidence only.

## Negative Memory
- Do not corrupt the outer `ffmpeg-target-dec-fuzzer-stream` recognition gate while retargeting this signal.
- Do not treat off-target crashes, clean parser exits, fixed-build crashes, or both-image crashes as success for this policy.
- Never store raw payload bytes, exact offsets, checksums, or task-local identifiers in memory.

## Format Contract
The FFmpeg target decoder fuzzer uses raw packet bytes split by a fixed delimiter marker and, for sufficiently large inputs, consumes a trailing context block for fields such as width, height, bit rate, and sample depth. A Tiertex video packet starts with flags; when video data is present, a fixed-size two-bit operation table describes fixed 8x8 blocks, followed by per-operation data.

## Harness Contract
The harness is the FFmpeg targeted decoder fuzzer for the Tiertex codec. It is not a container demuxer: raw input bytes before a delimiter become an AVPacket, while trailing context bytes initialize AVCodecContext fields before avcodec_open2.

## Evidence Shape
- Support: 1 server-verified round 25 solve after 2 attempts.
- Scope: generator repair and retargeting only.
