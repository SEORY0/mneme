---
type: causal-policy
title: "PDF Construct Target Match Confirmed By Submit Use Of Uninitialized Value Verified Recovery"
description: "Round 29 verified recovery for generic_crash with verifier signal target_match_confirmed_by_submit."
failure_class: "generic_crash"
verifier_signal: "target_match_confirmed_by_submit"
candidate_family: "construct"
input_format: "pdf"
harness_convention: "libfuzzer"
vuln_class: "use-of-uninitialized-value"
access_scope: generate
success_count: 1
confidence: high
tags: ["generic-crash", "target-match-confirmed-by-submit", "pdf", "libfuzzer", "construct", "use-of-uninitialized-value", "verified-recovery", "round-29"]
match_keys: ["generic_crash", "target_match_confirmed_by_submit", "pdf", "libfuzzer", "use-of-uninitialized-value", "generic-crash", "target-match-confirmed-by-submit", "pdf", "libfuzzer", "use-of-uninitialized-value", "verified_recovery", "construct", "construct"]
allowed_scopes: [generate]
forbidden_fields: [raw_poc_bytes, task_id, exact_offset, checksum, submit_metadata]
evidence_level: high
train_only: true
round: 29
---
# PDF Construct Target Match Confirmed By Submit Use Of Uninitialized Value Verified Recovery

- key: `generic_crash x target_match_confirmed_by_submit`
- outcome: verified target match / recovery policy
- success_count: 1
- related format facts: [[pdf]]
- related harness facts: [[libfuzzer]]

## Policy
For `generic_crash x target_match_confirmed_by_submit` on `pdf`, keep the parser and harness gates that produced the verifier signal, then vary only the causal relation described below. This is a positive recovery policy because the official vulnerable/fixed verifier recorded a target match.

## Procedure
1. Build a minimal renderable PDF whose page content invokes a type 4 mesh shading resource. Satisfy the document tree, page resource, content-stream, shading dictionary, bit-width, and decode-array gates. In the mesh sample stream, make the first edge-flag value fall outside the independent-triangle and continuation cases, then follow it with a continuation flag so the renderer consumes prior triangle state before a valid independent triangle initialized it.
2. Preserve format recognition and the harness input contract while mutating the narrow sink invariant; do not broaden into an off-target crash or a both-image crash.
3. If later verifier output changes the failure key, re-rank against that new key before mutating unrelated fields.

## Format Contract
- Format [[pdf]]: A PDF render path needs a catalog, pages tree, page object, media box, content stream, and resources dictionary. Shading resources are referenced from page content with the shading operator. A type 4 mesh shading stream is controlled by flag, coordinate, and component bit-width entries plus a decode array; mesh samples are packed bit fields read most-significant-bit first.
- Harness [[libfuzzer]]: The libFuzzer harness passes the raw input bytes directly to MuPDF as a PDF stream, opens it with the PDF handler, counts pages, renders each page with the identity transform into an RGB pixmap, and drops the pixmap. There is no input carving, mode byte, or FuzzedDataProvider layout.

## Negative Memory
- Do not corrupt the outer `pdf` recognition gate while retargeting this signal.
- Do not count parser reachability, clean exits, fixed-image crashes, both-image crashes, or local wrong-sink labels as success without official target match.
- Never store payload bytes, exact positions, checksums, submit metadata, or task-local identifiers.

## Evidence Shape
- Support: one round-29 worker trace with official target match.
- Scope: generator repair and retargeting only; pair with [[pdf]] and [[libfuzzer]].
