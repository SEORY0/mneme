---
type: negative-memory
title: "PDF Seed Mutate Construct Parser Reached But Target Not Triggered Logic Error Empty Rectangle Conversion Negative Memory"
description: "Round 29 negative memory for no_crash with verifier signal parser_reached_but_target_not_triggered."
failure_class: "no_crash"
verifier_signal: "parser_reached_but_target_not_triggered"
candidate_family: "seed_mutate+construct"
input_format: "pdf"
harness_convention: "libfuzzer"
vuln_class: "logic-error-empty-rectangle-conversion"
access_scope: generate
success_count: 0
failure_count: 1
confidence: medium
tags: ["no-crash", "parser-reached-but-target-not-triggered", "pdf", "libfuzzer", "seed-mutate-construct", "logic-error-empty-rectangle-conversion", "negative-memory", "round-29"]
match_keys: ["no_crash", "parser_reached_but_target_not_triggered", "pdf", "libfuzzer", "logic-error-empty-rectangle-conversion", "no-crash", "parser-reached-but-target-not-triggered", "pdf", "libfuzzer", "logic-error-empty-rectangle-conversion", "negative_memory", "seed_mutate+construct", "seed-mutate-construct"]
allowed_scopes: [generate]
forbidden_fields: [raw_poc_bytes, task_id, exact_offset, checksum, submit_metadata]
evidence_level: medium
train_only: true
round: 29
---
# PDF Seed Mutate Construct Parser Reached But Target Not Triggered Logic Error Empty Rectangle Conversion Negative Memory

- key: `no_crash x parser_reached_but_target_not_triggered`
- outcome: persistent failure / basin to avoid
- success_count: 0
- failure_count: 1
- related format facts: [[pdf]]
- related harness facts: [[libfuzzer]]

## Failure Shape
The raw PDF renderer was reached, but every tested path exited cleanly: a real empty-annotation seed, minimal page and crop boxes, annotation rectangles, form bounds, shading bounds, tiling pattern bounds, clipping paths, and tiny or degenerate page units. The likely missing condition is a render route that feeds an attacker-controlled empty rectangle specifically into the vulnerable rounding helper and then makes the coordinate-preservation error observable; the common page-bound route normalizes or sorts empty page boxes before rounding.

## Policy
Treat `no_crash x parser_reached_but_target_not_triggered` on `pdf` for `logic-error-empty-rectangle-conversion` as a basin to avoid unless a new candidate changes the parser gate, state relation, or sink relation described below. Preserve any proven reachability, but reject variants that return to the same clean-exit, off-target-crash, wrong-sink, usage-only, wrapper-mismatch, or both-image-crash basin.

## Procedure
1. Keep only the smallest parser or harness envelope that was actually reached.
2. Identify the missing causal relation from the signal: parser selection, container acceptance, length relation, stateful subobject, allocation state, or official target sink.
3. Change one relation at a time and discard candidates that return to the same `parser_reached_but_target_not_triggered` basin.
4. If a local crash is not an official target match, shrink or discard it before mutating deeper fields.
5. Promote a recovery from this basin only after a later verifier-confirmed target match.

## Negative Memory
- Do not resubmit broad mutations that only reproduce `parser_reached_but_target_not_triggered`.
- Do not count parser reachability, both-image crashes, local wrapper crashes, usage banners, clean exits, or fixed-image crashes as success.
- Never store payload bytes, exact positions, task identifiers, checksums, or submit metadata.

## Format Contract
The PDF parser accepts a normal document tree with catalog, pages, page, media box, optional crop box, resources, annotations, patterns, shadings, forms, and content streams. Empty MediaBox values are replaced by a default page rectangle, empty CropBox values are ignored, and non-overlapping CropBox intersections are sorted back into a non-empty page bound. Very small page bounds are normalized before page transform. The page unit value must be parsed as a real object; plain decimal real values were accepted more reliably than exponent-like spellings in page dictionaries.

## Harness Contract
The libFuzzer harness uses the input bytes as a raw PDF stream, opens it through MuPDF, loads each page, allocates a pixmap from the page bounds using the identity transform and an RGB colorspace, runs page contents plus annotations/widgets through the draw device, and suppresses recoverable MuPDF exceptions. There is no FuzzedDataProvider contract, no leading selector byte, and no secondary file envelope.

## Evidence Shape
- Support: 1 diagnosed persistent failure from round 29 after 19 attempts.
- Scope: generator repair and basin avoidance only.
