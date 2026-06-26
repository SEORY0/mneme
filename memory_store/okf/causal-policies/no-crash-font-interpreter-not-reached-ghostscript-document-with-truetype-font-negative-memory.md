---
type: causal-policy
title: "No Crash Font Interpreter Not Reached Ghostscript Document With Truetype Font Negative Memory"
description: "Round 8 negative memory for no_crash with verifier signal font_interpreter_not_reached."
failure_class: "no_crash"
verifier_signal: "font_interpreter_not_reached"
candidate_family: "seed_mutate"
input_format: "ghostscript-document-with-truetype-font"
harness_convention: "libfuzzer"
vuln_class: "bounds-check-missing-read"
access_scope: generate
success_count: 0
confidence: medium
tags: ["no-crash", "font-interpreter-not-reached", "ghostscript-document-with-truetype-font", "negative_memory", "round-8"]
match_keys: ["no_crash", "font_interpreter_not_reached", "ghostscript-document-with-truetype-font", "libfuzzer", "negative_memory"]
allowed_scopes: [generate]
forbidden_fields: [raw_poc_bytes, task_id, exact_offset, checksum, submit_metadata]
evidence_level: medium
train_only: true
round: 8
---
# No Crash Font Interpreter Not Reached Ghostscript Document With Truetype Font Negative Memory

## Policy
Treat `no_crash x font_interpreter_not_reached` as a persistent failure basin for `ghostscript-document-with-truetype-font` under `libfuzzer`. Preserve any reachability it proved, but do not keep mutating the same field basin unless the next verification changes the signal.

## Diagnosed Dead End
- A standalone TrueType font seed was rejected by the selected Ghostscript device fuzzer before reaching the TrueType instruction interpreter. The missing envelope is likely a PostScript or PDF document that embeds and renders a crafted TrueType font so the glyph program reaches the MSIRP instruction path.

## Format and Harness Gates
- Format: The vulnerable logic is in the TrueType bytecode interpreter for glyph programs. Reaching it requires a document-level container that loads a TrueType font, selects glyphs, and renders them through Ghostscript so the font instructions execute.
- Harness: The selected Ghostscript fuzzer treats the raw input as a document for a pdfwrite/device pipeline rather than as a bare font file. Inputs must satisfy the Ghostscript document parser before embedded font programs can run.

## Procedure
1. Before retrying this basin, rebuild the carrier around the exact harness contract and confirm parser reachability.
2. Replace the failed mutation family with a more specific invariant that would change the verifier signal.
3. Avoid broad seed mutation, oversized mutation, or off-target crash chasing when this same signal recurs.

## Negative Memory
- Do not promote this basin into a recovery policy until an official vulnerable/fixed verifier target match is observed.
- Do not preserve raw bytes, offsets, checksums, or task-local identifiers.

## Evidence Shape
- Support: one round-8 persistent failure trace.
- Scope: generator avoidance and retargeting for the same failure key.
