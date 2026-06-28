---
type: causal-policy
title: "No Crash Ghostscript PDF Repair Clean Exit PDF Negative Memory"
description: "Round 16 negative memory for no_crash with verifier signal ghostscript_pdf_repair_clean_exit."
failure_class: "no_crash"
verifier_signal: "ghostscript_pdf_repair_clean_exit"
candidate_family: "construct_pdf_repair_graph"
input_format: "pdf"
harness_convention: "libfuzzer-gstoraster"
vuln_class: "stale-xref-entry-after-repair"
access_scope: generate
success_count: 0
confidence: medium
tags: ["no-crash", "ghostscript-pdf-repair-clean-exit", "pdf", "negative-memory", "round-16"]
match_keys: ["no_crash", "ghostscript_pdf_repair_clean_exit", "pdf", "libfuzzer-gstoraster", "negative_memory"]
allowed_scopes: [generate]
forbidden_fields: [raw_poc_bytes, task_id, exact_offset, checksum, submit_metadata]
evidence_level: medium
train_only: true
round: 16
---
# No Crash Ghostscript PDF Repair Clean Exit PDF Negative Memory

## Policy
For `no_crash x ghostscript_pdf_repair_clean_exit`, avoid replaying the observed dead end. This negative memory is co-equal with positive policies and should redirect generation before another official submission.

## Procedure
- Ghostscript processed valid examples and several broken PDF graphs, including bad startxref repair, indirect font references, object-stream repair probes, duplicate objects, annotation-action references, and short xref-stream metadata. They reached the gstoraster wrapper but did not trigger a stale xref-entry dereference, so the missing gate is the exact repair-while-reading-object sequence that invalidates a currently held xref entry and then reuses it.
- When `no_crash x ghostscript_pdf_repair_clean_exit` appears for `pdf`, treat this candidate family as a basin-to-avoid rather than as evidence of proximity to the target.
- Keep any proven parser/harness envelope, but change the missing gate or state relation before submitting again.

## Format Contract
- PDF repair depends on a recognizable PDF header plus enough object syntax for the repair scanner to rebuild object locations. Page trees, content streams, resources, annotations, object streams, xref tables, and xref streams can all force object dereferences during rendering, but malformed xref data alone is usually repaired or ignored cleanly.
- Harness: The gstoraster fuzzer feeds the raw input as Ghostscript stdin with fixed CUPS raster output arguments. Ghostscript chooses PDF or PostScript from the document syntax. There is no fuzzer-side prefix, sidecar file, or FuzzedDataProvider split.

## Negative Memory
- Do not treat this verifier signal as a near miss unless a later candidate changes the missing gate or state relation.
- Do not submit candidates that are clean, parser-mismatched, off-target, or crashing both fixed and vulnerable images in this same shape.
- Preserve only descriptive format facts from the failed attempt; do not promote an unverified causal recovery.

## Evidence Shape
- Support: one diagnosed persistent failure from round 16.
- Scope: generator avoidance for the same failure-keyed basin.
