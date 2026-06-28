---
type: causal-policy
title: "No Crash Decoder Clean Exit Wrong Packet Contract Ffmpeg Rv60 Elementary Packet Stream Negative Memory"
description: "Round 20 negative memory for no_crash with verifier signal decoder_clean_exit_wrong_packet_contract."
failure_class: "no_crash"
verifier_signal: "decoder_clean_exit_wrong_packet_contract"
candidate_family: "seed_probe-realmedia-and-packet-stream"
input_format: "ffmpeg-rv60-elementary-packet-stream"
harness_convention: "libfuzzer-ffmpeg-target-decoder"
vuln_class: "out-of-bounds-read"
access_scope: generate
success_count: 0
confidence: medium
tags: ["no-crash", "decoder-clean-exit-wrong-packet-contract", "ffmpeg-rv60-elementary-packet-stream", "negative-memory", "round-20"]
match_keys: ["no-crash", "decoder-clean-exit-wrong-packet-contract", "ffmpeg-rv60-elementary-packet-stream"]
allowed_scopes: [generate]
forbidden_fields: [raw_poc_bytes, task_id, exact_offset, checksum, submit_metadata]
evidence_level: medium
train_only: true
round: 20
---
# No Crash Decoder Clean Exit Wrong Packet Contract Ffmpeg Rv60 Elementary Packet Stream Negative Memory

- key: `no_crash x decoder_clean_exit_wrong_packet_contract`
- outcome: persistent failure basin to avoid
- success_count: 0
- failure_count: 1
- formats: [[ffmpeg-rv60-elementary-packet-stream]]
- harnesses: [[libfuzzer-ffmpeg-target-decoder]]

## Dead End
The round 20 attempts for `ffmpeg-rv60-elementary-packet-stream` under `libfuzzer-ffmpeg-target-decoder` did not produce a verified target match. Do not promote these attempts into positive recovery without a future server-verified solve.

## Diagnosed Basin
- RealMedia/RV-family sample bytes, split-packet variants, and decoder-tail variants all exited cleanly. The likely missing contract is RV60 elementary frame syntax: container bytes or unrelated RealMedia samples do not necessarily provide a valid RV60 frame header, slice table, and slice payload layout needed to reach slice bitreader initialization.

## Negative Policy
When retrieval matches `no_crash x decoder_clean_exit_wrong_packet_contract`, avoid repeating this basin. First re-check the harness contract, format gate, and sink-specific dispatch condition. If the candidate only produces clean execution, wrapper-only crashes, off-target crashes, or an unverified recon state, retarget the carrier or abandon this family rather than scaling the same mutation.

## Retarget Hints
- Preserve factual format and harness gates from [[ffmpeg-rv60-elementary-packet-stream]] and [[libfuzzer-ffmpeg-target-decoder]].
- Prefer a different dispatch route or seed family unless new verifier feedback shows the target path is reached.
- Treat generic local crashes, clean exits, and `not_verified` recon states as non-success until official vulnerable-versus-fixed confirmation.

## Evidence Shape
- Support: 1 round 20 failed trace(s) with concrete diagnosis.
- Scope: generator avoidance only.
