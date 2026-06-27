---
type: negative-memory
title: "No Crash Raw Parser Clean Or Not Fp Dng Raw Camera Dng Or Tiff Derived Buffer Negative Memory"
description: "Round 19 negative memory for no_crash with verifier signal raw_parser_clean_or_not_fp_dng."
failure_class: "no_crash"
verifier_signal: "raw_parser_clean_or_not_fp_dng"
candidate_family: "seed_replay_raw_samples_with_config_tail"
input_format: "raw-camera-dng-or-tiff-derived-buffer"
harness_convention: "libfuzzer-with-fuzzed-data-provider-tail"
vuln_class: "out-of-bounds-read"
access_scope: generate
success_count: 0
confidence: medium
tags: ["no-crash", "raw-parser-clean-or-not-fp-dng", "raw-camera-dng-or-tiff-derived-buffer", "libfuzzer-with-fuzzed-data-provider-tail", "seed-replay-raw-samples-with-config-tail", "negative-memory", "round-19"]
match_keys: ["no-crash", "raw-parser-clean-or-not-fp-dng", "raw-camera-dng-or-tiff-derived-buffer", "libfuzzer-with-fuzzed-data-provider-tail", "out-of-bounds-read"]
allowed_scopes: [generate]
forbidden_fields: [raw_poc_bytes, task_id, exact_offset, checksum, submit_metadata]
evidence_level: medium
train_only: true
round: 19
---
# No Crash Raw Parser Clean Or Not Fp Dng Raw Camera Dng Or Tiff Derived Buffer Negative Memory

- key: `no_crash x raw_parser_clean_or_not_fp_dng`
- outcome: persistent failure / basin to avoid
- success_count: 0
- failure_count: 1
- related format facts: [[raw-camera-dng-or-tiff-derived-buffer]]
- harnesses: [[libfuzzer-with-fuzzed-data-provider-tail]]

## Failure Shape
Repository RAW samples with preserved payload prefixes and configuration tails reached LibRaw open/unpack paths or were rejected cleanly, but none selected the FP-DNG decoder with an inconsistent float-data byte-count relation. The missing relation is a TIFF/DNG image-directory setup that marks samples as floating point and provides a data-size field smaller than the decoder later consumes.

## Policy
Treat `no_crash x raw_parser_clean_or_not_fp_dng` on `raw-camera-dng-or-tiff-derived-buffer` as negative memory for the attempted carrier. Preserve only the reachability that was actually observed, then retarget the missing gate or sink-specific state before spending more verification attempts.

## Procedure
1. Keep any parser or harness envelope that the verifier proved was reached.
2. Identify the missing causal relation from the signal: parser selection, feature gate, length relation, stateful subobject, or official target sink.
3. Change one relation at a time and reject variants that return to this same clean-exit, off-target, usage-only, or nonreproducible basin.
4. Promote a recovery from this basin only after a later server-confirmed target match.

## Negative Memory
- Do not resubmit another candidate with this exact failure signal unless it changes the causal gate being tested.
- Do not broaden random mutation after reachability is known; move to the smallest missing format or state contract.
- Do not treat local generic crashes, wrapper usage paths, clean parser exits, or wrong-sink labels as success.
- Never store raw payload bytes, exact offsets, checksums, or task-local identifiers in memory.

## Evidence Shape
- Support: 1 diagnosed persistent failure from round 19.
- Scope: generator repair and basin avoidance only.
