---
type: causal-policy
title: "Leptonica Pixa Pa With Embedded PNG Seed Mutate Parser Reached Official Target Match Heap Buffer Overflow Read Verified Recovery"
description: "Round 27 verified recovery for wrong_sink with verifier signal parser_reached_official_target_match."
failure_class: "wrong_sink"
verifier_signal: "parser_reached_official_target_match"
candidate_family: "seed_mutate"
input_format: "leptonica-pixa-pa-with-embedded-png"
harness_convention: "libfuzzer-file-backed"
vuln_class: "heap-buffer-overflow-read"
access_scope: generate
success_count: 1
confidence: high
tags: ["wrong-sink", "parser-reached-official-target-match", "leptonica-pixa-pa-with-embedded-png", "libfuzzer-file-backed", "seed-mutate", "heap-buffer-overflow-read", "verified-recovery", "round-27"]
match_keys: ["wrong_sink", "parser_reached_official_target_match", "leptonica-pixa-pa-with-embedded-png", "libfuzzer-file-backed", "heap-buffer-overflow-read", "verified_recovery"]
allowed_scopes: [generate]
forbidden_fields: [raw_poc_bytes, task_id, exact_offset, checksum, submit_metadata]
evidence_level: high
train_only: true
round: 27
---
# Leptonica Pixa Pa With Embedded PNG Seed Mutate Parser Reached Official Target Match Heap Buffer Overflow Read Verified Recovery

## Policy
For `wrong_sink x parser_reached_official_target_match`, preserve the format and harness gates that reached the parser or sink, then apply the verified causal relation below. This is a positive recovery policy because the official vulnerable/fixed verifier recorded a target match.

## Procedure
1. Start from a real pixa_recog_fuzzer seed so the serialized PIXA and embedded PNG images remain structurally valid.
2. Preserve the embedded PNG integrity checks while changing the per-image text labels into valid short UTF-8 labels that retain enough class variety for recognizer training but include high-bit bytes.
3. The outlier-display path copies those labels into rendered text; bitmap-font rendering then uses each label byte as an index into ASCII-sized font and baseline tables, causing a vulnerable-only out-of-bounds table read.
4. Keep the carrier abstract: preserve the gate/invariant relation, not any task-local bytes or offsets.
5. If a later candidate changes the verifier signal, re-rank against the new failure key before mutating unrelated fields.

## Format Contract
- The input is a text PIXA serialization that contains a header with a pix count followed by embedded PNG images.
- Each embedded PNG can carry a text label used as the PIX text field; changing label chunks requires preserving the PNG chunk structure and recomputing chunk integrity fields.
- The recognizer accepts short labels and keeps the label text for later display, so label mutations must stay within the recognizer's small per-class text limit and retain enough class diversity to avoid early rejection.
- Harness [[libfuzzer-file-backed]]:
  - The libFuzzer harness writes the raw input bytes to a temporary .pa file and calls pixaRead on that file.
  - It creates recognizers from the loaded PIXA, runs boot training, removes outliers with debug images requested, and then calls recognition on the removed-outlier display image.
  - There is no FuzzedDataProvider split; reachability depends on the raw file being a readable Leptonica PIXA with embedded image labels.

## Negative Memory
- Do not broaden mutations after the parser or harness gate is proven.
- Do not submit candidates that reproduce on the fixed image or move to an off-target wrapper crash.
- Do not store payload bytes, exact offsets, checksums, or task-local identifiers.

## Evidence Shape
- Support: one round-27 worker trace with official target match.
- Scope: generator repair for the same failure-keyed basin; pair with [[leptonica-pixa-pa-with-embedded-png]] and [[libfuzzer-file-backed]].
