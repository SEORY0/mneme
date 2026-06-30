---
type: causal-policy
title: "H264 Annex B Construct Parser Reached Target UBSAN Site Undefined Behavior Out Of Bounds Verified Recovery"
description: "Round 26 verified recovery for wrong_sink with verifier signal parser_reached_target_ubsan_site."
failure_class: "wrong_sink"
verifier_signal: "parser_reached_target_ubsan_site"
candidate_family: "construct"
input_format: "h264-annex-b"
harness_convention: "libfuzzer"
vuln_class: "undefined-behavior-out-of-bounds"
access_scope: generate
success_count: 1
confidence: high
tags: ["wrong-sink", "parser-reached-target-ubsan-site", "h264-annex-b", "libfuzzer", "construct", "verified-recovery", "round-26"]
match_keys: ["wrong_sink", "parser_reached_target_ubsan_site", "h264-annex-b", "libfuzzer", "undefined-behavior-out-of-bounds", "verified_recovery"]
allowed_scopes: [generate]
forbidden_fields: [raw_poc_bytes, task_id, exact_offset, checksum, submit_metadata]
evidence_level: high
train_only: true
round: 26
---
# H264 Annex B Construct Parser Reached Target UBSAN Site Undefined Behavior Out Of Bounds Verified Recovery

- key: `wrong_sink x parser_reached_target_ubsan_site`
- outcome: verified recovery
- success_count: 1
- failure_count: 0
- formats: [[h264-annex-b]]
- harnesses: [[libfuzzer]]

## Failure Shape
Build a tiny raw Annex-B H.264 stream with coherent SPS, PPS, and one IDR slice using Baseline CAVLC entropy. Keep the picture minimal and enter an intra luma residual block with a nonzero CAVLC coeff_token so total-zero decoding is reached before the block is complete; this exercises the decoder's one-before-array VLC expression while the fixed build rejects or avoids the undefined access.

## Policy
For `wrong_sink x parser_reached_target_ubsan_site` on `h264-annex-b`, preserve the format recognition and harness contract before varying the vulnerable invariant. Prefer `construct` only while that carrier and harness contract remain stable.

## Procedure
1. Preserve the `h264-annex-b` carrier and `libfuzzer` harness contract until parser reachability is stable.
2. Apply the causal invariant in the failure shape before broad mutation or seed sweeping.
3. Treat local crash class as supporting signal only; keep the candidate only when vulnerable and fixed images diverge on the official target relation.

## Verifier Contract
The official vulnerable-versus-fixed target match is the confirmation gate for this recovery policy; local crash class is supporting evidence only.

## Negative Memory
- Do not corrupt the outer `h264-annex-b` recognition gate while retargeting this signal.
- Do not treat off-target crashes, clean parser exits, fixed-build crashes, or both-image crashes as success for this policy.
- Never store raw payload bytes, exact offsets, checksums, or task-local identifiers in memory.

## Format Contract
The input is a raw H.264 Annex-B byte stream, not a media container. The parser expects start-code-delimited NAL units; SPS and PPS must select CAVLC rather than CABAC, define a small frame, and make the slice header fields consistent with frame number and picture-order widths. Residual syntax follows macroblock prediction, coded-block-pattern, and quantizer-delta fields.

## Harness Contract
The harness is the FFmpeg H.264 decoder libFuzzer target and consumes the raw file bytes directly as an elementary H.264 packet stream. There is no FuzzedDataProvider prefix or mode byte; keeping the input compact avoids unrelated harness behavior.

## Evidence Shape
- Support: 1 server-verified round 26 solve after 1 attempts.
- Scope: generator repair and retargeting only.
