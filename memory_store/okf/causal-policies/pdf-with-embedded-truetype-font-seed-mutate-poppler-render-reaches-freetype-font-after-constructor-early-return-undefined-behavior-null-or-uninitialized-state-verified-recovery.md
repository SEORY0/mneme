---
type: causal-policy
title: "Pdf With Embedded Truetype Font Seed Mutate Poppler Render Reaches Freetype Font After Constructor Early Return Undefined Behavior Null Or Uninitialized State Verified Recovery"
description: "Round 28 verified recovery for generic_crash with verifier signal poppler_render_reaches_freetype_font_after_constructor_early_return."
failure_class: "generic_crash"
verifier_signal: "poppler_render_reaches_freetype_font_after_constructor_early_return"
candidate_family: "seed_mutate"
input_format: "pdf-with-embedded-truetype-font"
harness_convention: "libfuzzer"
vuln_class: "undefined-behavior-null-or-uninitialized-state"
access_scope: generate
success_count: 1
confidence: high
tags: ["generic-crash", "poppler-render-reaches-freetype-font-after-constructor-early-return", "pdf-with-embedded-truetype-font", "libfuzzer", "seed-mutate", "undefined-behavior-null-or-uninitialized-state", "verified-recovery", "round-28"]
match_keys: ["generic_crash", "poppler_render_reaches_freetype_font_after_constructor_early_return", "pdf-with-embedded-truetype-font", "libfuzzer", "undefined-behavior-null-or-uninitialized-state", "verified_recovery", "seed-mutate", "use-of-uninitialized-value"]
allowed_scopes: [generate]
forbidden_fields: [raw_poc_bytes, task_id, exact_offset, checksum, submit_metadata]
evidence_level: high
train_only: true
round: 28
---
# Pdf With Embedded Truetype Font Seed Mutate Poppler Render Reaches Freetype Font After Constructor Early Return Undefined Behavior Null Or Uninitialized State Verified Recovery

## Policy
For `generic_crash x poppler_render_reaches_freetype_font_after_constructor_early_return`, preserve the format and harness gates that reached the parser or sink, then apply the verified causal relation below. This is a positive recovery policy because the official vulnerable/fixed verifier recorded a target match.

## Procedure
1. Start from a real embedded TrueType font seed, but rebuild a minimal PDF around it so the document structure is simple and the font stream can be left uncompressed. Include the normal catalog, page tree, page resources, a TrueType font object, a FontDescriptor that references the embedded FontFile2 stream, and a content stream that selects the font and draws a glyph. Mutate the TrueType header so the FreeType face loads but reports an invalid font units value; Poppler's FreeType font wrapper constructor then returns before fully initializing glyph-rendering state, while the page renderer still calls makeGlyph for the drawn text. The fixed build bails out cleanly, while the vulnerable build crashes during rendering.
2. Keep the carrier abstract: preserve the gate, invariant, and sink relation rather than task-local bytes, exact offsets, checksums, or identifiers.
3. If the verifier signal changes, re-rank against the new failure key before mutating unrelated fields.

## Format Contract
- Format [[pdf-with-embedded-truetype-font]]: A compact PDF can reach this path with ordinary raw PDF objects: Catalog to Pages to Page, a Resources font dictionary, a TrueType font dictionary with widths and WinAnsi encoding, a FontDescriptor with a FontFile2 stream, and a page content stream containing BT/Tf/Td/Tj text drawing operators. The embedded TrueType stream uses the standard sfnt table directory; its head table carries the units-per-em value that Poppler later observes through FreeType. Keeping the font stream unfiltered avoids compressed length repair when mutating font-internal fields.
- Harness [[libfuzzer]]: The libFuzzer harness passes the input bytes directly to poppler::document::load_from_raw_data. There is no prefix, selector byte, or FuzzedDataProvider carving. If the document loads and is not locked, the harness creates a page renderer and renders every page, so page content that selects an embedded font and draws text reaches SplashOutputDev and SplashFTFont::makeGlyph.

## Negative Memory
- Do not broaden mutations after parser or harness reachability is proven.
- Do not submit candidates that reproduce on the fixed image, crash both images, or move to an off-target wrapper crash.
- Do not store payload bytes, exact offsets, checksums, or task-local identifiers.

## Evidence Shape
- Support: one round-28 worker trace with official target match.
- Scope: generator repair for the same failure-keyed basin; pair with [[pdf-with-embedded-truetype-font]] and [[libfuzzer]].
