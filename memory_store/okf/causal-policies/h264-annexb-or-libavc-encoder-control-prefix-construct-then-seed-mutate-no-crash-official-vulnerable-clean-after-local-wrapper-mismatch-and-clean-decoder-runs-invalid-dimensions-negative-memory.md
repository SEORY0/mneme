---
type: negative-memory
title: "H264 Annexb Or Libavc Encoder Control Prefix Construct Then Seed Mutate No Crash Official Vulnerable Clean After Local Wrapper Mismatch And Clean Decoder Runs Invalid Dimensions Negative Memory"
description: "Round 37 negative memory for no_crash with verifier signal official_vulnerable_clean_after_local_wrapper_mismatch_and_clean_decoder_runs."
failure_class: "no_crash"
verifier_signal: "official_vulnerable_clean_after_local_wrapper_mismatch_and_clean_decoder_runs"
candidate_family: "construct_then_seed_mutate"
input_format: "h264-annexb-or-libavc-encoder-control-prefix"
harness_convention: "libfuzzer"
vuln_class: "invalid-dimensions"
access_scope: generate
success_count: 0
failure_count: 1
confidence: medium
tags: ["no-crash", "official-vulnerable-clean-after-local-wrapper-mismatch-and-clean-decoder-runs", "h264-annexb-or-libavc-encoder-control-prefix", "libfuzzer", "construct-then-seed-mutate", "invalid-dimensions", "negative-memory", "round-37"]
match_keys: ["no_crash", "official_vulnerable_clean_after_local_wrapper_mismatch_and_clean_decoder_runs", "h264-annexb-or-libavc-encoder-control-prefix", "libfuzzer", "invalid-dimensions", "negative-memory", "construct_then_seed_mutate"]
allowed_scopes: [generate]
forbidden_fields: [raw_poc_bytes, task_id, exact_offset, checksum, submit_metadata]
evidence_level: medium
train_only: true
round: 37
---
# H264 Annexb Or Libavc Encoder Control Prefix Construct Then Seed Mutate No Crash Official Vulnerable Clean After Local Wrapper Mismatch And Clean Decoder Runs Invalid Dimensions Negative Memory

- key: `no_crash x official_vulnerable_clean_after_local_wrapper_mismatch_and_clean_decoder_runs`
- outcome: persistent failure / basin to avoid
- success_count: 0
- failure_count: 1
- related format facts: [[h264-annexb-or-libavc-encoder-control-prefix]]
- related harness facts: [[libfuzzer]]

## Failure Shape
The description-driven encoder-control construction reached the official server but exited cleanly on the vulnerable image. The generated docker image's observable wrapper executed a decoder fuzzer rather than the encoder control harness, so additional H.264 Annex-B seed truncation, SPS dimension/cropping mutation, and early IDR residual perturbation families were tried; those locally executed without sanitizer findings before the attempt budget was capped.

## Observed Basin
- Failure trajectory classes: no_crash, no_crash, no_crash, no_crash, no_crash.
- Official confirmation: no server target match for this basin.

## Policy
Treat `no_crash x official_vulnerable_clean_after_local_wrapper_mismatch_and_clean_decoder_runs` on `h264-annexb-or-libavc-encoder-control-prefix` under `libfuzzer` as a basin to avoid unless a new candidate changes the parser gate, state relation, or sink relation described above. Preserve any proven reachability, but reject variants that return to the same clean-exit, off-target-crash, wrapper-mismatch, usage-only, timeout, or fixed-image-crash behavior.

## Procedure
1. Keep only the smallest parser or harness envelope that was actually reached.
2. Identify the missing relation from the signal: parser selection, container acceptance, length relation, stateful subobject, allocation state, or official target sink.
3. Change one relation at a time and discard candidates that return to the same `official_vulnerable_clean_after_local_wrapper_mismatch_and_clean_decoder_runs` basin.
4. Promote a recovery from this basin only after a later official target match.

## Negative Memory
- Do not resubmit broad mutations that only reproduce `official_vulnerable_clean_after_local_wrapper_mismatch_and_clean_decoder_runs`.
- Do not count parser reachability, both-image crashes, local wrapper crashes, clean exits, timeouts, or fixed-image crashes as success.
- Do not store payload bytes, exact positions, task identifiers, checksums, or submit metadata.

## Evidence Shape
- Support: one diagnosed persistent failure from round 37 after 5 attempts.
- Candidate family: construct_then_seed_mutate.
- Scope: generator repair and basin avoidance only.
