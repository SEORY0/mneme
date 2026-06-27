---
type: causal-policy
title: "No Crash PDF Render Clean Exit PDF Negative Memory"
description: "Round 10 negative memory for no_crash with verifier signal pdf_render_clean_exit."
failure_class: "no_crash"
verifier_signal: "pdf_render_clean_exit"
candidate_family: "seed_mutate"
input_format: "pdf"
harness_convention: "libfuzzer"
vuln_class: "use-of-uninitialized-value"
access_scope: generate
success_count: 0
confidence: medium
tags: ["no-crash", "pdf-render-clean-exit", "negative-memory", "round-10"]
match_keys: ["no_crash", "pdf_render_clean_exit", "pdf", "libfuzzer", "negative_memory"]
allowed_scopes: [generate]
forbidden_fields: [raw_poc_bytes, task_id, exact_offset, checksum, submit_metadata]
evidence_level: medium
train_only: true
round: 10
---
# No Crash PDF Render Clean Exit PDF Negative Memory

## Policy
For `no_crash x pdf_render_clean_exit`, avoid replaying the observed dead end. This negative memory is co-equal with positive policies and should redirect generation before another official submission.

## Procedure
1. A supplied Poppler PDF seed loaded and rendered cleanly.
2. When `no_crash x pdf_render_clean_exit` appears for `pdf`, treat this candidate family as a basin-to-avoid rather than as evidence of proximity to the target.
3. Keep any proven parser/harness envelope, but change the missing gate or state relation before submitting again.

## Format Contract
- The input must be a loadable PDF document with enough catalog, page, xref/trailer, and page resources for Poppler to create pages and render them. Broken-file reachability depends on preserving document repair gates while corrupting a narrow object/resource relation.
- Harness: The libFuzzer target passes the entire raw byte string to poppler::document::load_from_raw_data, skips locked or unloaded documents, creates each page, and renders each page with poppler::page_renderer. There is no FuzzedDataProvider carving.

## Negative Memory
- Do not treat this verifier signal as a near miss unless a later candidate changes the missing gate or state relation.
- Do not submit candidates that are clean, parser-mismatched, off-target, or crashing both fixed and vulnerable images in this same shape.
- Preserve only descriptive format facts from the failed attempt; do not promote an unverified causal recovery.

## Evidence Shape
- Support: one diagnosed round-10 persistent failure.
- Scope: generator avoidance for the same failure-keyed basin.
