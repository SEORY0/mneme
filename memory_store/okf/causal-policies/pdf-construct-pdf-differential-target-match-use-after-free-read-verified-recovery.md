---
type: causal-policy
title: "Pdf Construct Pdf Differential Target Match Use After Free Read Verified Recovery"
description: "Round 28 verified recovery for generic_crash with verifier signal differential_target_match."
failure_class: "generic_crash"
verifier_signal: "differential_target_match"
candidate_family: "construct_pdf"
input_format: "pdf"
harness_convention: "libfuzzer-raw-memory"
vuln_class: "use-after-free-read"
access_scope: generate
success_count: 1
confidence: high
tags: ["generic-crash", "differential-target-match", "pdf", "libfuzzer-raw-memory", "construct-pdf", "use-after-free-read", "verified-recovery", "round-28"]
match_keys: ["generic_crash", "differential_target_match", "pdf", "libfuzzer-raw-memory", "use-after-free-read", "verified_recovery", "construct", "use-after-free-read"]
allowed_scopes: [generate]
forbidden_fields: [raw_poc_bytes, task_id, exact_offset, checksum, submit_metadata]
evidence_level: high
train_only: true
round: 28
---
# Pdf Construct Pdf Differential Target Match Use After Free Read Verified Recovery

## Policy
For `generic_crash x differential_target_match`, preserve the format and harness gates that reached the parser or sink, then apply the verified causal relation below. This is a positive recovery policy because the official vulnerable/fixed verifier recorded a target match.

## Procedure
1. Build a structurally valid single-page PDF with a correct object table, content stream length, xref, and trailer. In the page content stream, repeatedly apply clipping path operations without unwinding the draw device stack, enough to force the draw stack past its inline storage and through a heap relocation. The vulnerable clipping code keeps a pointer to the old current scissor across a stack push, so the relocation makes the next scissor intersection read stale memory; the fixed build refreshes the scissor after the push.
2. Keep the carrier abstract: preserve the gate, invariant, and sink relation rather than task-local bytes, exact offsets, checksums, or identifiers.
3. If the verifier signal changes, re-rank against the new failure key before mutating unrelated fields.

## Format Contract
- Format [[pdf]]: A minimal PDF that renders through this harness needs a catalog, pages tree, page dictionary with media box/resources, a contents stream with a self-consistent length, and a valid xref/trailer. Page content graphics operators can create a rectangle path, apply it as the clipping path, and clear the path; repeated clipping intersects the current clipping region and pushes nested draw-device state.
- Harness [[libfuzzer-raw-memory]]: The libFuzzer input is used directly as an in-memory PDF stream. The harness registers MuPDF document handlers, opens the stream explicitly as a PDF, renders every page to an RGB pixmap with an identity transform, drops the pixmap, and suppresses MuPDF exceptions. There is no mode byte, stdin/file-path contract, or FuzzedDataProvider front/back split.

## Negative Memory
- Do not broaden mutations after parser or harness reachability is proven.
- Do not submit candidates that reproduce on the fixed image, crash both images, or move to an off-target wrapper crash.
- Do not store payload bytes, exact offsets, checksums, or task-local identifiers.

## Evidence Shape
- Support: one round-28 worker trace with official target match.
- Scope: generator repair for the same failure-keyed basin; pair with [[pdf]] and [[libfuzzer-raw-memory]].
