---
type: causal-policy
title: Ffmpeg Mv Container Clean Exit Negative Memory
description: Negative memory for ffmpeg-mv-container candidates that ended in no_crash with verifier signal `clean_exit`.
failure_class: no_crash
verifier_signal: clean_exit
candidate_family: construct
input_format: ffmpeg-mv-container
harness_convention: libfuzzer-or-file-demuxer
vuln_class: use-of-uninitialized-value
access_scope: generate
success_count: 0
confidence: medium
tags: [no-crash, clean-exit, ffmpeg-mv-container, libfuzzer-or-file-demuxer, construct, use-of-uninitialized-value, negative-memory]
match_keys: [no-crash, clean-exit, ffmpeg-mv-container, libfuzzer-or-file-demuxer, construct, use-of-uninitialized-value, negative-memory]
allowed_scopes: [generate]
forbidden_fields: [raw_poc_bytes, task_id, exact_offset, checksum, submit_metadata]
evidence_level: medium
train_only: true
---
## Policy
Treat `no_crash with verifier signal `clean_exit`` for `ffmpeg-mv-container` as evidence that the current carrier reached a clean or wrong harness basin, not the vulnerable invariant. Retarget by preserving only the proven parser gate and changing the missing relation named below.

## Procedure
1. Keep any parser-recognition envelope that reached `clean_exit`.
2. Stop repeating the dead-end basin: MV header and truncated-name table probes exited cleanly. The missing gate is a valid MV demux header/table sequence where a metadata or track-entry name read is short but later still consumed.
3. Rebuild around `[[ffmpeg-mv-container]]` and `[[libfuzzer-or-file-demuxer]]`, then mutate the narrow missing relation instead of adding unrelated padding or broad corruption.
4. Submit only after local verify produces a vulnerable-build crash or a plausible parser-branch wrong-sink crash; clean exits under this signal are not submit candidates.

## Negative Memory
- This is a persistent Round 11 failure basin, not a recovery recipe.
- Do not spend retries on the same carrier shape unless new evidence changes the verifier signal.
- If the harness itself reports usage or setup failure, fix the invocation/carrier contract before mutating vulnerability fields.

## Evidence Shape
- Support: 1 diagnosed Round 11 failed solve attempt.
- Attempts observed: 5.
