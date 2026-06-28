---
type: causal-policy
title: "Generic Crash Both Images Crashed Officially Pdf Negative Memory"
description: "Round 7 negative memory for generic_crash with verifier signal both_images_crashed_officially."
failure_class: "generic_crash"
verifier_signal: "both_images_crashed_officially"
candidate_family: "construct"
input_format: "pdf"
harness_convention: "libfuzzer"
vuln_class: "null-or-uninitialized-font-state"
access_scope: generate
success_count: 0
confidence: medium
tags: ["generic-crash", "both-images-crashed-officially", "pdf", "negative-memory", "round-7"]
match_keys: ["generic_crash", "both_images_crashed_officially", "pdf", "libfuzzer", "null-or-uninitialized-font-state", "negative_memory"]
allowed_scopes: [generate]
forbidden_fields: [raw_poc_bytes, task_id, exact_offset, checksum, submit_metadata]
evidence_level: medium
train_only: true
round: 7
---
# Generic Crash Both Images Crashed Officially Pdf Negative Memory

- key: `generic_crash x both_images_crashed_officially`
- outcome: persistent failure / basin to avoid
- success_count: 0
- failure_count: 1
- related format facts: [[pdf]]
- related harness facts: [[libfuzzer]]

## Failure Shape
A minimal PDF with a base font, stroked text, and a degenerate text matrix reached the PDF renderer
locally without a target crash. Official submission crashed both images, indicating a non-target
PDF/rendering failure rather than the fixed textScale condition.

## Policy
Treat `generic_crash x both_images_crashed_officially` on `pdf` as a basin to avoid unless a new candidate changes the specific parser gate, state relation, or sink relation described below. Preserve any proven reachability, but reject variants that return the same verifier signal without changing the causal gate under test.

## Procedure
1. Keep only the smallest parser or harness envelope that the verifier proved was reached.
2. Identify the missing causal relation from the signal: parser selection, container acceptance, length relation, stateful subobject, allocation state, or official target sink.
3. Change one relation at a time and discard candidates that return to the same clean-exit, off-target-crash, wrong-sink, usage-only, or both-image-crash basin.
4. If a local crash is not an official target match, shrink or discard it before mutating deeper fields.
5. Promote a recovery from this basin only after a later verifier-confirmed target match.

## Negative Memory
- Do not resubmit broad mutations that only reproduce `both_images_crashed_officially`.
- Do not count parser reachability, both-image crashes, local wrapper crashes, or clean exits as success.
- Do not store raw payload bytes, exact positions, task identifiers, or submit metadata.

## Format Contract
PDF reachability requires a catalog, pages tree, page object, resources with a font, and a content
stream. Poppler only asks SplashFTFont for a glyph path for stroked or clipped text rendering modes;
ordinary filled text does not use this path. A degenerate text matrix can drive a zero text scale in
the FreeType font wrapper.

## Harness Contract
The harness loads raw bytes as a PDF document and renders every page with poppler::page_renderer.
The input must be a parseable PDF; rendering operations in the content stream determine whether the
Splash font path code is reached.

## Evidence Shape
- Support: 1 diagnosed persistent failure from round 7.
- Scope: generator repair and basin avoidance only.
