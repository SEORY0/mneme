---
type: causal-policy
title: Ffmpeg Hevc Target Decoder Frame Decoder Reached Clean Negative Memory
description: Negative memory for ffmpeg-hevc-target-decoder-frame candidates that ended in no_crash with verifier signal `decoder_reached_clean`.
failure_class: no_crash
verifier_signal: decoder_reached_clean
candidate_family: seed_mutate
input_format: ffmpeg-hevc-target-decoder-frame
harness_convention: libfuzzer-ffmpeg-target-decoder
vuln_class: use-of-uninitialized-value
access_scope: generate
success_count: 0
confidence: medium
tags: [no-crash, decoder-reached-clean, ffmpeg-hevc-target-decoder-frame, libfuzzer-ffmpeg-target-decoder, seed-mutate, use-of-uninitialized-value, negative-memory]
match_keys: [no-crash, decoder-reached-clean, ffmpeg-hevc-target-decoder-frame, libfuzzer-ffmpeg-target-decoder, seed-mutate, use-of-uninitialized-value, negative-memory]
allowed_scopes: [generate]
forbidden_fields: [raw_poc_bytes, task_id, exact_offset, checksum, submit_metadata]
evidence_level: medium
train_only: true
---
## Policy
Treat `no_crash with verifier signal `decoder_reached_clean`` for `ffmpeg-hevc-target-decoder-frame` as evidence that the current carrier reached a clean or wrong harness basin, not the vulnerable invariant. Retarget by preserving only the proven parser gate and changing the missing relation named below.

## Procedure
1. Keep any parser-recognition envelope that reached `decoder_reached_clean`.
2. Stop repeating the dead-end basin: HEVC-like candidates reached decoding and produced decoded pixel counts, but did not construct the missing-slice condition that exposes uninitialized frame-buffer content. Context-tail variations changed decoder setup without triggering the described allocation/zeroing invariant.
3. Rebuild around `[[ffmpeg-hevc-target-decoder-frame]]` and `[[libfuzzer-ffmpeg-target-decoder]]`, then mutate the narrow missing relation instead of adding unrelated padding or broad corruption.
4. Submit only after local verify produces a vulnerable-build crash or a plausible parser-branch wrong-sink crash; clean exits under this signal are not submit candidates.

## Negative Memory
- This is a persistent Round 11 failure basin, not a recovery recipe.
- Do not spend retries on the same carrier shape unless new evidence changes the verifier signal.
- If the harness itself reports usage or setup failure, fix the invocation/carrier contract before mutating vulnerability fields.

## Evidence Shape
- Support: 1 diagnosed Round 11 failed solve attempt.
- Attempts observed: 6.
