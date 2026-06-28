---
type: causal-policy
title: "Not Verified Not Verified Ffmpeg Target Dec Packet Bytes Negative Memory"
description: "Round 20 negative memory for not_verified with verifier signal not_verified."
failure_class: "not_verified"
verifier_signal: "not_verified"
candidate_family: "recon_only"
input_format: "ffmpeg target_dec packet bytes"
harness_convention: "oss-fuzz ffmpeg target_dec_fuzzer"
vuln_class: "segv in rv60 decode_cu_r, use-of-uninitialized-value"
access_scope: generate
success_count: 0
confidence: medium
tags: ["not-verified", "not-verified", "ffmpeg-target-dec-packet-bytes", "negative-memory", "round-20"]
match_keys: ["not-verified", "not-verified", "ffmpeg-target-dec-packet-bytes"]
allowed_scopes: [generate]
forbidden_fields: [raw_poc_bytes, task_id, exact_offset, checksum, submit_metadata]
evidence_level: medium
train_only: true
round: 20
---
# Not Verified Not Verified Ffmpeg Target Dec Packet Bytes Negative Memory

- key: `not_verified x not_verified`
- outcome: persistent failure basin to avoid
- success_count: 0
- failure_count: 2
- formats: [[ffmpeg-target-dec-packet-bytes]]
- harnesses: [[oss-fuzz-ffmpeg-target-dec-fuzzer]]

## Dead End
The round 20 attempts for `ffmpeg target_dec packet bytes` under `oss-fuzz ffmpeg target_dec_fuzzer` did not produce a verified target match. Do not promote these attempts into positive recovery without a future server-verified solve.

## Diagnosed Basin
- Recon identified the FFmpeg target decoder fuzzer and RV60 recursive CU decoder sink, but no packet candidate was verified within this worker budget. The unresolved gate is a valid RV60 frame/slice bitstream that reaches decode_cu_r with vulnerable CU split state.
- Recon identified the msmpeg4 decoder block path where dc_pred_dir must be initialized before prediction use, but no packet candidate was verified within this worker budget. The missing gate is a valid MSMPEG4 intra block that exercises AC prediction after DC decode without early bitstream rejection.

## Negative Policy
When retrieval matches `not_verified x not_verified`, avoid repeating this basin. First re-check the harness contract, format gate, and sink-specific dispatch condition. If the candidate only produces clean execution, wrapper-only crashes, off-target crashes, or an unverified recon state, retarget the carrier or abandon this family rather than scaling the same mutation.

## Retarget Hints
- Preserve factual format and harness gates from [[ffmpeg-target-dec-packet-bytes]] and [[oss-fuzz-ffmpeg-target-dec-fuzzer]].
- Prefer a different dispatch route or seed family unless new verifier feedback shows the target path is reached.
- Treat generic local crashes, clean exits, and `not_verified` recon states as non-success until official vulnerable-versus-fixed confirmation.

## Evidence Shape
- Support: 2 round 20 failed trace(s) with concrete diagnosis.
- Scope: generator avoidance only.
