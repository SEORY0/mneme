---
type: causal-policy
title: "HEVC Elementary Stream Seed Sweep Parser Reached Sao Edge Msan Fixed Clean Use Of Uninitialized Value Verified Recovery"
description: "Round 26 verified recovery for wrong_sink with verifier signal parser_reached_sao_edge_msan_fixed_clean."
failure_class: "wrong_sink"
verifier_signal: "parser_reached_sao_edge_msan_fixed_clean"
candidate_family: "seed_sweep"
input_format: "hevc-elementary-stream"
harness_convention: "libfuzzer-ffmpeg-target_dec_fuzzer"
vuln_class: "use-of-uninitialized-value"
access_scope: generate
success_count: 1
confidence: high
tags: ["wrong-sink", "parser-reached-sao-edge-msan-fixed-clean", "hevc-elementary-stream", "libfuzzer-ffmpeg-target-dec-fuzzer", "seed-sweep", "verified-recovery", "round-26"]
match_keys: ["wrong_sink", "parser_reached_sao_edge_msan_fixed_clean", "hevc-elementary-stream", "libfuzzer-ffmpeg-target_dec_fuzzer", "use-of-uninitialized-value", "verified_recovery"]
allowed_scopes: [generate]
forbidden_fields: [raw_poc_bytes, task_id, exact_offset, checksum, submit_metadata]
evidence_level: high
train_only: true
round: 26
---
# HEVC Elementary Stream Seed Sweep Parser Reached Sao Edge Msan Fixed Clean Use Of Uninitialized Value Verified Recovery

- key: `wrong_sink x parser_reached_sao_edge_msan_fixed_clean`
- outcome: verified recovery
- success_count: 1
- failure_count: 0
- formats: [[hevc-elementary-stream]]
- harnesses: [[libfuzzer-ffmpeg-target-dec-fuzzer]]

## Failure Shape
Use a real HEVC Annex-B elementary stream from the conformance corpus that exercises picture-size handling and SAO edge filtering. Plain SAO streams, parser-tail variants, boundary truncations, and single-slice deletions decoded cleanly; the successful carrier was a valid raw elementary stream that naturally entered the SAO edge filter with under-specified reconstructed frame content. The vulnerable fuzzer allocation leaves frame data uninitialized, while the fixed build zeroes the buffer and exits cleanly.

## Policy
For `wrong_sink x parser_reached_sao_edge_msan_fixed_clean` on `hevc-elementary-stream`, preserve the format recognition and harness contract before varying the vulnerable invariant. Prefer `seed_sweep` only while that carrier and harness contract remain stable.

## Procedure
1. Preserve the `hevc-elementary-stream` carrier and `libfuzzer-ffmpeg-target_dec_fuzzer` harness contract until parser reachability is stable.
2. Apply the causal invariant in the failure shape before broad mutation or seed sweeping.
3. Treat local crash class as supporting signal only; keep the candidate only when vulnerable and fixed images diverge on the official target relation.

## Verifier Contract
The official vulnerable-versus-fixed target match is the confirmation gate for this recovery policy; local crash class is supporting evidence only.

## Negative Memory
- Do not corrupt the outer `hevc-elementary-stream` recognition gate while retargeting this signal.
- Do not treat off-target crashes, clean parser exits, fixed-build crashes, or both-image crashes as success for this policy.
- Never store raw payload bytes, exact offsets, checksums, or task-local identifiers in memory.

## Format Contract
The useful input is a raw HEVC elementary stream, not a container. Start-code-delimited VPS, SPS, PPS, and VCL NAL units must remain coherent enough to open the HEVC decoder and reach frame reconstruction. Streams that exercise SAO edge filtering and picture-size relationships are stronger carriers than generic valid samples or arbitrary truncation.

## Harness Contract
FFmpeg target_dec_fuzzer treats the input prefix as decoder packet bytes for a fixed HEVC decoder. If the input is large enough, the last fixed-size context block can set parser, keyframe, flush, extradata, and codec context fields; otherwise the raw prefix is decoded directly. The harness can also split packets on its fixed separator tag, but the accepted candidate did not require a container or demuxer.

## Evidence Shape
- Support: 1 server-verified round 26 solve after 12 attempts.
- Scope: generator repair and retargeting only.
