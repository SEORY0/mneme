---
type: causal-policy
title: "No Crash Decoder Opened And Frames Decoded Without Target Msan Vc1 Elementary Stream Seed Mutate Use Of Uninitialized Value Negative Memory"
description: "Round 30 negative memory for no_crash with verifier signal decoder_opened_and_frames_decoded_without_target_msan."
failure_class: "no_crash"
verifier_signal: "decoder_opened_and_frames_decoded_without_target_msan"
candidate_family: "seed_mutate"
input_format: "vc1-elementary-stream"
harness_convention: "libfuzzer-ffmpeg-target-decoder"
vuln_class: "use-of-uninitialized-value"
access_scope: generate
success_count: 0
confidence: medium
tags: ["no-crash", "decoder-opened-and-frames-decoded-without-target-msan", "vc1-elementary-stream", "libfuzzer-ffmpeg-target-decoder", "seed-mutate", "negative-memory", "round-30"]
match_keys: ["no-crash", "decoder-opened-and-frames-decoded-without-target-msan", "vc1-elementary-stream", "libfuzzer-ffmpeg-target-decoder", "use-of-uninitialized-value", "negative-memory"]
allowed_scopes: [generate]
forbidden_fields: [raw_poc_bytes, task_id, exact_offset, checksum, submit_metadata]
evidence_level: medium
train_only: true
round: 30
---
# No Crash Decoder Opened And Frames Decoded Without Target Msan Vc1 Elementary Stream Seed Mutate Use Of Uninitialized Value Negative Memory

- key: `no-crash x decoder-opened-and-frames-decoded-without-target-msan`
- outcome: persistent failure / basin to avoid
- success_count: 0
- formats: [[vc1-elementary-stream]]
- harnesses: [[libfuzzer-ffmpeg-target-decoder]]

## Failure Shape
The decoder could be opened only after preserving VC1 sequence and entrypoint bytes as harness extradata and feeding frame and slice units as packet bytes. With that contract in place, valid seed replay, controlled fuzzer-tail options, parser and no-parser modes, packet separator variants, slice deletion, frame truncation, field and interlaced samples, RCV-style samples, and slice-row retargeting all exited cleanly. The missing relation appears to require a more specific decoded-frame or error-concealment state than simply removing or retargeting VC1 slice units.

## Negative Policy
For `no-crash x decoder-opened-and-frames-decoded-without-target-msan` on `vc1-elementary-stream`, do not continue broad mutation inside the same basin. The recorded trajectory was `no-crash, no-crash, no-crash, no-crash, no-crash, no-crash, no-crash, no-crash` without a verified vulnerable-only target match.

## Avoid
1. Do not submit candidates that only prove parser reachability, clean exit, fixed-image crash, or a coarse local crash.
2. Do not widen mutations across multiple independent metadata families after this signal; first identify the missing gate or state transition.
3. Preserve the useful format and harness facts, but retarget a different causal invariant before spending more attempts.
4. If the verifier signal says the parser or state was not reached, rebuild the carrier/state path before touching sink-specific fields.

## Recovery Direction
Keep the accepted envelope facts from [[vc1-elementary-stream]] and [[libfuzzer-ffmpeg-target-decoder]], then search for the smallest missing gate named by the diagnosis instead of repeating the failed candidate family.

## Evidence Shape
- Support: diagnosed round 30 failure.
- Scope: generator repair only; no success-rate credit.
