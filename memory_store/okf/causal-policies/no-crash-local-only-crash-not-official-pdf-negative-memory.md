---
type: causal-policy
title: "No Crash Local Only Crash Not Official PDF Negative Memory"
description: "Round 16 negative memory for no_crash with verifier signal local_only_crash_not_official."
failure_class: "no_crash"
verifier_signal: "local_only_crash_not_official"
candidate_family: "construct"
input_format: "pdf"
harness_convention: "libfuzzer"
vuln_class: "MuPDF empty image paint rectangle underflow"
access_scope: generate
success_count: 0
confidence: medium
tags: ["no-crash", "local-only-crash-not-official", "pdf", "negative-memory", "round-16"]
match_keys: ["no_crash", "local_only_crash_not_official", "pdf", "libfuzzer", "negative_memory"]
allowed_scopes: [generate]
forbidden_fields: [raw_poc_bytes, task_id, exact_offset, checksum, submit_metadata]
evidence_level: medium
train_only: true
round: 16
---
# No Crash Local Only Crash Not Official PDF Negative Memory

## Policy
For `no_crash x local_only_crash_not_official`, avoid replaying the observed dead end. This negative memory is co-equal with positive policies and should redirect generation before another official submission.

## Procedure
- Minimal PDFs with degenerate page boxes and image XObjects exercised the document renderer, and one local run reported a crash, but confirmation and official submit were clean. The missing condition is likely a specific image transform and clipping state that makes both the page scissor and image bbox become the library's empty-rectangle sentinels inside the image painter.
- When `no_crash x local_only_crash_not_official` appears for `pdf`, treat this candidate family as a basin-to-avoid rather than as evidence of proximity to the target.
- Keep any proven parser/harness envelope, but change the missing gate or state relation before submitting again.

## Format Contract
- A minimal PDF needs a catalog, pages tree, page object, content stream, resources, and an image XObject. Page boxes and content-stream graphics state commands can make image painting degenerate by combining page geometry, transforms, and image draw operations.
- Harness: The MuPDF fuzzer opens the raw bytes as a PDF stream, counts pages, and renders every page to an RGB pixmap with the identity transform. It does not use a prefix, mode selector, or FuzzedDataProvider layout.

## Negative Memory
- Do not treat this verifier signal as a near miss unless a later candidate changes the missing gate or state relation.
- Do not submit candidates that are clean, parser-mismatched, off-target, or crashing both fixed and vulnerable images in this same shape.
- Preserve only descriptive format facts from the failed attempt; do not promote an unverified causal recovery.

## Evidence Shape
- Support: one diagnosed persistent failure from round 16.
- Scope: generator avoidance for the same failure-keyed basin.
