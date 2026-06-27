---
type: causal-policy
title: "No Crash Decoder Reached No Target Crash H264 Annexb Mvc Seed Mutate Heap Buffer Overflow Negative Memory"
description: "Round 14 negative memory for no_crash with verifier signal decoder_reached_no_target_crash."
failure_class: "no_crash"
verifier_signal: "decoder_reached_no_target_crash"
candidate_family: "seed_mutate"
input_format: "h264-annexb-mvc"
harness_convention: "libfuzzer"
vuln_class: "heap-buffer-overflow"
access_scope: generate
success_count: 0
confidence: medium
tags: ["no-crash", "decoder-reached-no-target-crash", "h264-annexb-mvc", "negative-memory", "round-14"]
match_keys: ["no_crash", "decoder_reached_no_target_crash", "h264-annexb-mvc", "libfuzzer", "heap-buffer-overflow", "negative_memory"]
allowed_scopes: [generate]
forbidden_fields: [raw_poc_bytes, task_id, exact_offset, checksum, submit_metadata]
evidence_level: medium
train_only: true
round: 14
---
# No Crash Decoder Reached No Target Crash H264 Annexb Mvc Seed Mutate Heap Buffer Overflow Negative Memory

- key: `no_crash x decoder_reached_no_target_crash`
- outcome: persistent failure / basin to avoid
- success_count: 0
- failure_count: 1
- related format facts: [[h264-annexb-mvc]]
- related harness facts: [[libfuzzer]]

## Failure Shape
Real H.264 corpus streams reached the MVC decoder and executed cleanly. The missing gate is not the Annex-B container or decoder initialization, but a specific MVC-compatible Film Grain Characteristics SEI payload where the bitstream ends before all declared FGC syntax has been semantically decoded.

## Policy
Treat `no_crash x decoder_reached_no_target_crash` on `h264-annexb-mvc` as a basin to avoid unless a new candidate changes the parser gate, state relation, or official target sink. Preserve any proven reachability, but reject variants that return to the same verifier signal without changing the causal gate under test.

## Procedure
1. Keep only the smallest carrier that the verifier proved reaches the parser, decoder, or harness path.
2. Identify the missing causal relation from the signal: parser selection, container acceptance, length relation, stateful subobject, allocation state, or official target sink.
3. Change one relation at a time and discard candidates that return to the same clean-exit, off-target-crash, wrong-sink, usage-only, parser-not-reached, or both-image-crash basin.
4. If a local crash is not an official target match, shrink or discard it before mutating deeper fields.
5. Promote a recovery from this basin only after a later verifier-confirmed target match.

## Negative Memory
- Do not count parser reachability, local crashes, clean exits, fixed-image crashes, usage banners, or sink mismatches as success.
- Do not repeat this candidate family unless the new attempt changes the causal gate named above.
- Do not store concrete payload bytes, task identifiers, exact positions, checksums, or submit metadata.

## Evidence Shape
- Support: one diagnosed persistent failure from Round 14.
- Scope: generator repair and basin avoidance only.
