---
type: causal-policy
title: "No Crash Ffmpeg Target Decoder Frame Decoder Not Reached Or Clean Decode Negative Memory"
description: "Negative memory for no_crash with decoder_not_reached_or_clean_decode on ffmpeg-target-decoder-frame inputs."
failure_class: no_crash
verifier_signal: decoder_not_reached_or_clean_decode
candidate_family: seed_mutate
input_format: ffmpeg-target-decoder-frame
harness_convention: libfuzzer
vuln_class: use-of-uninitialized-value
access_scope: generate
success_count: 0
confidence: medium
tags: [no-crash, decoder-not-reached-or-clean-decode, ffmpeg-target-decoder-frame, use-of-uninitialized-value, negative_memory]
match_keys: [no-crash, decoder-not-reached-or-clean-decode, ffmpeg-target-decoder-frame, use-of-uninitialized-value]
allowed_scopes: [generate]
forbidden_fields: [raw_poc_bytes, task_id, exact_offset, checksum, submit_metadata]
evidence_level: medium
train_only: true
---
# No Crash Ffmpeg Target Decoder Frame Decoder Not Reached Or Clean Decode Negative Memory

- key: `no_crash x decoder_not_reached_or_clean_decode`
- outcome: persistent failure basin
- success_count: 0
- failure_count: 1
- formats: [[ffmpeg-target-decoder-frame]]

## Dead End
Real WMAVoice ASF samples and synthetic decoder-fuzzer envelopes did not reach the pitch-dependent uninitialized-value path. The likely missing ingredient is extracting valid raw WMAVoice decoder packets and exact codec extradata from the container rather than feeding ASF bytes or guessed context tails.

## Avoid
Do not repeat the same candidate family when the verifier signal matches this key. Treat broad seed mutation, wrapper usage paths, both-image crashes, parser-clean exits, or local-only crashes as evidence that the current surface is not the target differential.

## Recovery Direction
Preserve only independently validated format or harness reachability facts. Re-enter generation by first satisfying the harness contract and the earliest format gate, then use a different target-specific invariant instead of enlarging or randomly mutating the failed family.
