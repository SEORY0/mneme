---
type: causal-policy
title: "No Crash Vc1image Elementary Stream Vc1image Decoder Reached Clean Exit Negative Memory"
description: "Negative memory for no_crash with vc1image_decoder_reached_clean_exit on vc1image-elementary-stream inputs."
failure_class: no_crash
verifier_signal: vc1image_decoder_reached_clean_exit
candidate_family: seed_mutate
input_format: vc1image-elementary-stream
harness_convention: libfuzzer-ffmpeg-target-decoder
vuln_class: use-of-uninitialized-value
access_scope: generate
success_count: 0
confidence: medium
tags: [no-crash, vc1image-decoder-reached-clean-exit, vc1image-elementary-stream, use-of-uninitialized-value, negative_memory]
match_keys: [no-crash, vc1image-decoder-reached-clean-exit, vc1image-elementary-stream, use-of-uninitialized-value]
allowed_scopes: [generate]
forbidden_fields: [raw_poc_bytes, task_id, exact_offset, checksum, submit_metadata]
evidence_level: medium
train_only: true
---
# No Crash Vc1image Elementary Stream Vc1image Decoder Reached Clean Exit Negative Memory

- key: `no_crash x vc1image_decoder_reached_clean_exit`
- outcome: persistent failure basin
- success_count: 0
- failure_count: 1
- formats: [[vc1image-elementary-stream]]

## Dead End
Real VC1 and RCV samples reached the VC1IMAGE decoder fuzzer and executed cleanly. The missing condition is likely an image-coded VC1 frame shape that reaches macroblock decoding with skipped or reused block metadata, rather than ordinary video elementary streams.

## Avoid
Do not repeat the same candidate family when the verifier signal matches this key. Treat broad seed mutation, wrapper usage paths, both-image crashes, parser-clean exits, or local-only crashes as evidence that the current surface is not the target differential.

## Recovery Direction
Preserve only independently validated format or harness reachability facts. Re-enter generation by first satisfying the harness contract and the earliest format gate, then use a different target-specific invariant instead of enlarging or randomly mutating the failed family.
