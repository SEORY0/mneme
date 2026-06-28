---
type: negative-memory
title: "No Crash Pdf Type0 Cmap Clean Pdf Postscript Cmap Negative Memory"
description: "Round 19 negative memory for no_crash with verifier signal pdf_type0_cmap_clean."
failure_class: "no_crash"
verifier_signal: "pdf_type0_cmap_clean"
candidate_family: "construct"
input_format: "pdf-postscript-cmap"
harness_convention: "libfuzzer-ghostscript-stdin"
vuln_class: "path-or-name-length-validation"
access_scope: generate
success_count: 0
confidence: medium
tags: ["no-crash", "pdf-type0-cmap-clean", "pdf-postscript-cmap", "libfuzzer-ghostscript-stdin", "construct", "negative-memory", "round-19"]
match_keys: ["no-crash", "pdf-type0-cmap-clean", "pdf-postscript-cmap", "libfuzzer-ghostscript-stdin", "path-or-name-length-validation"]
allowed_scopes: [generate]
forbidden_fields: [raw_poc_bytes, task_id, exact_offset, checksum, submit_metadata]
evidence_level: medium
train_only: true
round: 19
---
# No Crash Pdf Type0 Cmap Clean Pdf Postscript Cmap Negative Memory

- key: `no_crash x pdf_type0_cmap_clean`
- outcome: persistent failure / basin to avoid
- success_count: 0
- failure_count: 1
- related format facts: [[pdf-postscript-cmap]]
- harnesses: [[libfuzzer-ghostscript-stdin]]

## Failure Shape
A minimal PDF with a Type0 font and oversized embedded CMap name executed cleanly. The missing gate is likely the external CMap resource-file open path where a name is converted to a resource filename, rather than only an embedded stream name.

## Policy
Treat `no_crash x pdf_type0_cmap_clean` on `pdf-postscript-cmap` as negative memory for the attempted carrier. Preserve only the reachability that was actually observed, then retarget the missing gate or sink-specific state before spending more verification attempts.

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
