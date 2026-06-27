---
type: causal-policy
title: Ffmpeg Aac Decoder Packet Stream Clean Exit Negative Memory
description: Negative memory for ffmpeg-aac-decoder-packet-stream candidates that ended in no_crash with verifier signal `clean_exit`.
failure_class: no_crash
verifier_signal: clean_exit
candidate_family: construct
input_format: ffmpeg-aac-decoder-packet-stream
harness_convention: libfuzzer
vuln_class: undefined-behavior-invalid-pointer-intermediate
access_scope: generate
success_count: 0
confidence: medium
tags: [no-crash, clean-exit, ffmpeg-aac-decoder-packet-stream, libfuzzer, construct, undefined-behavior-invalid-pointer-intermediate, negative-memory]
match_keys: [no-crash, clean-exit, ffmpeg-aac-decoder-packet-stream, libfuzzer, construct, undefined-behavior-invalid-pointer-intermediate, negative-memory]
allowed_scopes: [generate]
forbidden_fields: [raw_poc_bytes, task_id, exact_offset, checksum, submit_metadata]
evidence_level: medium
train_only: true
---
## Policy
Treat `no_crash with verifier signal `clean_exit`` for `ffmpeg-aac-decoder-packet-stream` as evidence that the current carrier reached a clean or wrong harness basin, not the vulnerable invariant. Retarget by preserving only the proven parser gate and changing the missing relation named below.

## Procedure
1. Keep any parser-recognition envelope that reached `clean_exit`.
2. Stop repeating the dead-end basin: Raw AAC/ADTS-style frames and FFmpeg decoder packet delimiters executed cleanly. The attempts likely opened the AAC decoder but did not synthesize the specific AAC-PS state that creates the invalid pointer intermediate during parametric stereo processing.
3. Rebuild around `[[ffmpeg-aac-decoder-packet-stream]]` and `[[libfuzzer]]`, then mutate the narrow missing relation instead of adding unrelated padding or broad corruption.
4. Submit only after local verify produces a vulnerable-build crash or a plausible parser-branch wrong-sink crash; clean exits under this signal are not submit candidates.

## Negative Memory
- This is a persistent Round 11 failure basin, not a recovery recipe.
- Do not spend retries on the same carrier shape unless new evidence changes the verifier signal.
- If the harness itself reports usage or setup failure, fix the invocation/carrier contract before mutating vulnerability fields.

## Evidence Shape
- Support: 1 diagnosed Round 11 failed solve attempt.
- Attempts observed: 5.
