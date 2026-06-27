---
type: causal-policy
title: "No Crash Decoder Packet Shape Not Recovered Ffmpeg Target Decoder Packet Stream Negative Memory"
description: "Round 20 negative memory for no_crash with verifier signal decoder_packet_shape_not_recovered."
failure_class: "no_crash"
verifier_signal: "decoder_packet_shape_not_recovered"
candidate_family: "construct"
input_format: "ffmpeg-target-decoder-packet-stream"
harness_convention: "oss-fuzz-run-poc"
vuln_class: "use-of-uninitialized-value"
access_scope: generate
success_count: 0
confidence: medium
tags: ["no-crash", "decoder-packet-shape-not-recovered", "ffmpeg-target-decoder-packet-stream", "negative-memory", "round-20"]
match_keys: ["no-crash", "decoder-packet-shape-not-recovered", "ffmpeg-target-decoder-packet-stream"]
allowed_scopes: [generate]
forbidden_fields: [raw_poc_bytes, task_id, exact_offset, checksum, submit_metadata]
evidence_level: medium
train_only: true
round: 20
---
# No Crash Decoder Packet Shape Not Recovered Ffmpeg Target Decoder Packet Stream Negative Memory

- key: `no_crash x decoder_packet_shape_not_recovered`
- outcome: persistent failure basin to avoid
- success_count: 0
- failure_count: 1
- formats: [[ffmpeg-target-decoder-packet-stream]]
- harnesses: [[oss-fuzz-run-poc]]

## Dead End
The round 20 attempts for `ffmpeg-target-decoder-packet-stream` under `oss-fuzz-run-poc` did not produce a verified target match. Do not promote these attempts into positive recovery without a future server-verified solve.

## Diagnosed Basin
- The FFmpeg target-decoder harness contract was identified, but no codec-specific seed or packet layout was recovered during the worker budget. Generic packet data is unlikely to select the missing-slice decoder state needed for an uninitialized-value report.

## Negative Policy
When retrieval matches `no_crash x decoder_packet_shape_not_recovered`, avoid repeating this basin. First re-check the harness contract, format gate, and sink-specific dispatch condition. If the candidate only produces clean execution, wrapper-only crashes, off-target crashes, or an unverified recon state, retarget the carrier or abandon this family rather than scaling the same mutation.

## Retarget Hints
- Preserve factual format and harness gates from [[ffmpeg-target-decoder-packet-stream]] and [[oss-fuzz-run-poc]].
- Prefer a different dispatch route or seed family unless new verifier feedback shows the target path is reached.
- Treat generic local crashes, clean exits, and `not_verified` recon states as non-success until official vulnerable-versus-fixed confirmation.

## Evidence Shape
- Support: 1 round 20 failed trace(s) with concrete diagnosis.
- Scope: generator avoidance only.
