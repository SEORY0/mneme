---
type: negative-memory
title: "PDF Seed Mutate Plus Construct No Crash PDF Render Clean Exit Geometry Empty Irect Coordinate Loss Negative Memory"
description: "Round 36 negative memory for no_crash with verifier signal pdf_render_clean_exit."
failure_class: "no_crash"
verifier_signal: "pdf_render_clean_exit"
candidate_family: "seed_mutate+construct"
input_format: "pdf"
harness_convention: "libfuzzer"
vuln_class: "geometry-empty-irect-coordinate-loss"
access_scope: generate
success_count: 0
failure_count: 1
confidence: medium
tags: ["no-crash", "pdf-render-clean-exit", "pdf", "libfuzzer", "seed-mutate-plus-construct", "geometry-empty-irect-coordinate-loss", "negative-memory", "round-36"]
match_keys: ["no_crash", "pdf_render_clean_exit", "pdf", "libfuzzer", "geometry-empty-irect-coordinate-loss", "no-crash", "pdf-render-clean-exit", "negative_memory", "seed_mutate+construct", "seed-mutate-plus-construct"]
allowed_scopes: [generate]
forbidden_fields: [raw_poc_bytes, task_id, exact_offset, checksum, submit_metadata]
evidence_level: medium
train_only: true
round: 36
---
# PDF Seed Mutate Plus Construct No Crash PDF Render Clean Exit Geometry Empty Irect Coordinate Loss Negative Memory

- key: `no_crash x pdf_render_clean_exit`
- outcome: persistent failure / basin to avoid
- success_count: 0
- failure_count: 1
- related format facts: [[pdf]]
- related harness facts: [[libfuzzer]]

## Failure Shape
The vulnerable geometry helper collapses empty floating rectangles to the global empty integer rectangle, but the attempted render surfaces did not consume the lost origin in a crashing way. Tried the existing empty-annotation seed, nonzero degenerate annotation rectangles, empty clipping before image paint, empty transparency forms, empty soft-mask forms, page-level transparency with an empty page box, Type3 glyph bounds, and an explicit annotation appearance with an empty form box. Page boxes are normalized before rendering, and the simple annotation, form, mask, clip, and glyph paths either skip empty integer regions or intersect them away cleanly. The missing relation is likely a more specific downstream consumer that uses the empty rectangle origin after conversion rather than only testing emptiness.

## Observed Basin
- Failure trajectory classes: no_crash.
- Official confirmation: no server target match for this basin.

## Policy
Treat `no_crash x pdf_render_clean_exit` on `pdf` under `libfuzzer` as a basin to avoid unless a new candidate changes the parser gate, state relation, or sink relation described above. Preserve any proven reachability, but reject variants that return to the same clean-exit, off-target-crash, wrapper-mismatch, usage-only, or fixed-image-crash behavior.

## Procedure
1. Keep only the smallest parser or harness envelope that was actually reached.
2. Identify the missing relation from the signal: parser selection, container acceptance, length relation, stateful subobject, allocation state, or official target sink.
3. Change one relation at a time and discard candidates that return to the same `pdf_render_clean_exit` basin.
4. Promote a recovery from this basin only after a later official target match.

## Negative Memory
- Do not resubmit broad mutations that only reproduce `pdf_render_clean_exit`.
- Do not count parser reachability, both-image crashes, local wrapper crashes, clean exits, or fixed-image crashes as success.
- Do not store payload bytes, exact positions, task identifiers, checksums, or submit metadata.

## Evidence Shape
- Support: 1 diagnosed persistent failure from round 36 after 15 attempts.
- Scope: generator repair and basin avoidance only.
