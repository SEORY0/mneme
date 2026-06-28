---
type: causal-policy
title: "No Crash Decoder Clean Exit Container Seed Wrong Contract Ffmpeg Ffv1 Elementary Packet Stream Negative Memory"
description: "Round 20 negative memory for no_crash with verifier signal decoder_clean_exit_container_seed_wrong_contract."
failure_class: "no_crash"
verifier_signal: "decoder_clean_exit_container_seed_wrong_contract"
candidate_family: "seed_probe-ffv1-container-and-packet-stream"
input_format: "ffmpeg-ffv1-elementary-packet-stream"
harness_convention: "libfuzzer-ffmpeg-target-decoder"
vuln_class: "use-of-uninitialized-value"
access_scope: generate
success_count: 0
confidence: medium
tags: ["no-crash", "decoder-clean-exit-container-seed-wrong-contract", "ffmpeg-ffv1-elementary-packet-stream", "negative-memory", "round-20"]
match_keys: ["no-crash", "decoder-clean-exit-container-seed-wrong-contract", "ffmpeg-ffv1-elementary-packet-stream"]
allowed_scopes: [generate]
forbidden_fields: [raw_poc_bytes, task_id, exact_offset, checksum, submit_metadata]
evidence_level: medium
train_only: true
round: 20
---
# No Crash Decoder Clean Exit Container Seed Wrong Contract Ffmpeg Ffv1 Elementary Packet Stream Negative Memory

- key: `no_crash x decoder_clean_exit_container_seed_wrong_contract`
- outcome: persistent failure basin to avoid
- success_count: 0
- failure_count: 1
- formats: [[ffmpeg-ffv1-elementary-packet-stream]]
- harnesses: [[libfuzzer-ffmpeg-target-decoder]]

## Dead End
The round 20 attempts for `ffmpeg-ffv1-elementary-packet-stream` under `libfuzzer-ffmpeg-target-decoder` did not produce a verified target match. Do not promote these attempts into positive recovery without a future server-verified solve.

## Diagnosed Basin
- FFV1 sample container prefixes, split chunks, and decoder-tail variants stayed clean. The missing gate is likely demuxed FFV1 frame data with an internal slice layout where some slices are omitted or truncated; feeding an AVI container prefix to the decoder harness does not reliably reach FFV1 slice reconstruction.

## Negative Policy
When retrieval matches `no_crash x decoder_clean_exit_container_seed_wrong_contract`, avoid repeating this basin. First re-check the harness contract, format gate, and sink-specific dispatch condition. If the candidate only produces clean execution, wrapper-only crashes, off-target crashes, or an unverified recon state, retarget the carrier or abandon this family rather than scaling the same mutation.

## Retarget Hints
- Preserve factual format and harness gates from [[ffmpeg-ffv1-elementary-packet-stream]] and [[libfuzzer-ffmpeg-target-decoder]].
- Prefer a different dispatch route or seed family unless new verifier feedback shows the target path is reached.
- Treat generic local crashes, clean exits, and `not_verified` recon states as non-success until official vulnerable-versus-fixed confirmation.

## Evidence Shape
- Support: 1 round 20 failed trace(s) with concrete diagnosis.
- Scope: generator avoidance only.
