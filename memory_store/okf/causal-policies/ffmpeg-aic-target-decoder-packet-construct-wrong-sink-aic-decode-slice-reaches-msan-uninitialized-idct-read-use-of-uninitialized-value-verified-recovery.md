---
type: causal-policy
title: "Ffmpeg Aic Target Decoder Packet Construct Wrong Sink Aic Decode Slice Reaches Msan Uninitialized Idct Read Use Of Uninitialized Value Verified Recovery"
description: "Round 30 verified recovery for wrong_sink with verifier signal aic_decode_slice_reaches_msan_uninitialized_idct_read."
failure_class: "wrong_sink"
verifier_signal: "aic_decode_slice_reaches_msan_uninitialized_idct_read"
candidate_family: "construct"
input_format: "ffmpeg-aic-target-decoder-packet"
harness_convention: "oss-fuzz-run-poc-ffmpeg-target-decoder"
vuln_class: "use-of-uninitialized-value"
access_scope: generate
success_count: 1
confidence: medium
tags: ["wrong-sink", "aic-decode-slice-reaches-msan-uninitialized-idct-read", "ffmpeg-aic-target-decoder-packet", "oss-fuzz-run-poc-ffmpeg-target-decoder", "construct", "verified-recovery", "round-30"]
match_keys: ["wrong-sink", "aic-decode-slice-reaches-msan-uninitialized-idct-read", "ffmpeg-aic-target-decoder-packet", "oss-fuzz-run-poc-ffmpeg-target-decoder", "use-of-uninitialized-value"]
allowed_scopes: [generate]
forbidden_fields: [raw_poc_bytes, task_id, exact_offset, checksum, submit_metadata]
evidence_level: high
train_only: true
round: 30
---
# Ffmpeg Aic Target Decoder Packet Construct Wrong Sink Aic Decode Slice Reaches Msan Uninitialized Idct Read Use Of Uninitialized Value Verified Recovery

- key: `wrong-sink x aic-decode-slice-reaches-msan-uninitialized-idct-read`
- outcome: verified recovery
- success_count: 1
- failure_count: 0
- formats: [[ffmpeg-aic-target-decoder-packet]]
- harnesses: [[oss-fuzz-run-poc-ffmpeg-target-decoder]]

## Failure Shape
Construct a raw AIC decoder frame rather than a media container. Supply matching video dimensions through the target-decoder configuration trailer and the AIC frame header. Keep the frame header, slice table, and slice-size units internally consistent, then encode each coefficient band as skipped so the decoder reaches recombination and IDCT with coefficient storage that the vulnerable build allocated but did not clear. The fixed build clears or rejects that uninitialized state and exits cleanly.

## Policy
For `wrong-sink x aic-decode-slice-reaches-msan-uninitialized-idct-read` on `ffmpeg-aic-target-decoder-packet`, preserve the parser and harness gates first, then mutate only the causal invariant described by the verified trace. Prefer `construct` while this format and harness contract are present.

## Procedure
1. Preserve the `ffmpeg-aic-target-decoder-packet` carrier enough for the `oss-fuzz-run-poc-ffmpeg-target-decoder` harness to reach the parser path.
2. Keep unrelated envelope fields minimal and stable so verifier feedback stays tied to the target sink.
3. Apply the verified invariant from the failure shape rather than random broad mutation.
4. Submit only candidates where the vulnerable image reaches the target relation and the fixed image rejects or avoids it.

## Verifier Contract
The local class may remain coarse. Treat the official vulnerable-versus-fixed target match as the confirmation gate for this policy.

## Negative Memory
- Do not corrupt the outer `ffmpeg-aic-target-decoder-packet` recognition gate while retargeting this signal.
- Do not treat off-target crashes, clean parser reachability, or both-image crashes as success for this policy.
- Never store raw payload bytes, exact offsets, checksums, or task-local identifiers in memory.

## Evidence Shape
- Support: 1 server-verified solve(s), including round 30.
- Scope: generator repair only.
