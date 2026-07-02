---
type: negative-memory
title: "Postscript Pdfwrite Transparency Seed Mutate Construct No Sanitizer Crash Viewer State Depth Underflow Negative Memory"
description: "Round 29 negative memory for no_crash with verifier signal no_sanitizer_crash."
failure_class: "no_crash"
verifier_signal: "no_sanitizer_crash"
candidate_family: "seed_mutate+construct"
input_format: "postscript-pdfwrite-transparency"
harness_convention: "libfuzzer"
vuln_class: "viewer-state-depth-underflow"
access_scope: generate
success_count: 0
failure_count: 1
confidence: medium
tags: ["no-crash", "no-sanitizer-crash", "postscript-pdfwrite-transparency", "libfuzzer", "seed-mutate-construct", "viewer-state-depth-underflow", "negative-memory", "round-29"]
match_keys: ["no_crash", "no_sanitizer_crash", "postscript-pdfwrite-transparency", "libfuzzer", "viewer-state-depth-underflow", "no-crash", "no-sanitizer-crash", "postscript-pdfwrite-transparency", "libfuzzer", "viewer-state-depth-underflow", "negative_memory", "seed_mutate+construct", "seed-mutate-construct"]
allowed_scopes: [generate]
forbidden_fields: [raw_poc_bytes, task_id, exact_offset, checksum, submit_metadata]
evidence_level: medium
train_only: true
round: 29
---
# Postscript Pdfwrite Transparency Seed Mutate Construct No Sanitizer Crash Viewer State Depth Underflow Negative Memory

- key: `no_crash x no_sanitizer_crash`
- outcome: persistent failure / basin to avoid
- success_count: 0
- failure_count: 1
- related format facts: [[postscript-pdfwrite-transparency]]
- related harness facts: [[libfuzzer]]

## Failure Shape
Multiple parser-accepted carriers executed cleanly: the shipped transparency example, bounded direct-group nesting with and without object-filter page-device flags, PDF transparency form nesting, PDF text clipping and unmatched graphics-state restore, caught PostScript restore attempts, and Type 3 font substream carriers. Direct internal PostScript transparency operators without the example fallback hit a Ghostscript interpreter error under the fixed harness flags, while the fallback seed can reduce those operators to no-ops. The remaining likely gap is the exact externally reachable sequence that both enters pdfwrite's viewer-state restore path at an empty or stale depth and then continues to a later save/text transition rather than being handled by the interpreter.

## Policy
Treat `no_crash x no_sanitizer_crash` on `postscript-pdfwrite-transparency` for `viewer-state-depth-underflow` as a basin to avoid unless a new candidate changes the parser gate, state relation, or sink relation described below. Preserve any proven reachability, but reject variants that return to the same clean-exit, off-target-crash, wrong-sink, usage-only, wrapper-mismatch, or both-image-crash basin.

## Procedure
1. Keep only the smallest parser or harness envelope that was actually reached.
2. Identify the missing causal relation from the signal: parser selection, container acceptance, length relation, stateful subobject, allocation state, or official target sink.
3. Change one relation at a time and discard candidates that return to the same `no_sanitizer_crash` basin.
4. If a local crash is not an official target match, shrink or discard it before mutating deeper fields.
5. Promote a recovery from this basin only after a later verifier-confirmed target match.

## Negative Memory
- Do not resubmit broad mutations that only reproduce `no_sanitizer_crash`.
- Do not count parser reachability, both-image crashes, local wrapper crashes, usage banners, clean exits, or fixed-image crashes as success.
- Never store payload bytes, exact positions, task identifiers, checksums, or submit metadata.

## Format Contract
Ghostscript accepts complete PostScript programs and PDF files as raw stdin for this harness. Pdfwrite transparency setup in PostScript uses a page-device dictionary with transparency-related compatibility settings and transparency group begin/end operations; when the privileged transparency operators are not enabled by startup flags, the shipped example can replace them with no-op fallbacks. PDF transparency can also be expressed with Form XObjects that carry transparency group dictionaries and nested drawing resources. Text clipping can be represented through text rendering modes in PDF or charpath/clip operations in PostScript.

## Harness Contract
libFuzzer supplies the raw buffer directly to Ghostscript stdin and the harness selects the pdfwrite device with a null output file. The fixed argument list includes quiet, safer, no-pause, batch execution and does not use FuzzedDataProvider, a leading mode byte, or an input prefix. The input therefore must be a self-contained PostScript or PDF program; command-line-only Ghostscript switches cannot be supplied through the fuzz bytes.

## Evidence Shape
- Support: 1 diagnosed persistent failure from round 29 after 32 attempts.
- Scope: generator repair and basin avoidance only.
