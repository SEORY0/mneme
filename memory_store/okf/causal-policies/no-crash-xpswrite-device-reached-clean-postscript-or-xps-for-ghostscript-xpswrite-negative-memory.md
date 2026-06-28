---
type: causal-policy
title: "No Crash Xpswrite Device Reached Clean Postscript Or XPS For Ghostscript Xpswrite Negative Memory"
description: "Round 9 negative memory for no_crash with verifier signal xpswrite_device_reached_clean."
failure_class: "no_crash"
verifier_signal: "xpswrite_device_reached_clean"
candidate_family: "seed_mutate-and-construct-postscript"
input_format: "postscript-or-xps-for-ghostscript-xpswrite"
harness_convention: "libfuzzer"
vuln_class: "heap-buffer-overflow-write"
access_scope: generate
success_count: 0
confidence: medium
tags: ["no-crash", "xpswrite-device-reached-clean", "postscript-or-xps-for-ghostscript-xpswrite", "negative-memory", "round-9"]
match_keys: ["no_crash", "xpswrite_device_reached_clean", "postscript-or-xps-for-ghostscript-xpswrite", "libfuzzer", "heap-buffer-overflow-write", "negative_memory"]
allowed_scopes: [generate]
forbidden_fields: [raw_poc_bytes, task_id, exact_offset, checksum, submit_metadata]
evidence_level: medium
train_only: true
round: 9
---
# No Crash Xpswrite Device Reached Clean Postscript Or XPS For Ghostscript Xpswrite Negative Memory

- key: `no_crash x xpswrite_device_reached_clean`
- outcome: persistent failure / basin to avoid
- success_count: 0
- failure_count: 1
- related format facts: [[postscript-or-xps-for-ghostscript-xpswrite]]
- related harness facts: [[libfuzzer]]

## Failure Shape
- A valid xpswrite seed and a narrow one-bit image program executed cleanly.
- The unresolved gate is creating a small bitmap that just satisfies the clist allocation
  calculation while still causing the copy routine to copy padded scanlines.

## Policy
Treat `no_crash x xpswrite_device_reached_clean` on `postscript-or-xps-for-ghostscript-xpswrite` as a basin to avoid unless a new candidate changes the parser gate, state relation, or official target sink. Preserve any proven reachability, but reject variants that return to the same verifier signal without changing the causal gate under test.

## Procedure
1. Keep only the smallest parser or harness envelope that the verifier proved was reached.
2. Identify the missing causal relation from the signal: parser selection, container acceptance, length relation, stateful subobject, allocation state, or official target sink.
3. Change one relation at a time and discard candidates that return to the same clean-exit, off-target-crash, wrong-sink, usage-only, or both-image-crash basin.
4. If a local crash is not an official target match, shrink or discard it before mutating deeper fields.
5. Promote a recovery from this basin only after a later verifier-confirmed target match.

## Format Contract
- The relevant bitmap relation is width bytes versus padded raster bytes across multiple scanlines:
  a non-byte-aligned or otherwise padded small bitmap can have an allocation computed from unpadded
  final-line width while the copier uses full raster lines.
- Ghostscript can reach bitmap output through XPS/PDF/PostScript rendering depending on the device
  wrapper.

## Harness Contract
- The wrapper is fixed to the Ghostscript xpswrite device fuzzer.
- It consumes raw document bytes with no front selector.
- The active device is not the generic raster fuzzer, so candidates must render through xpswrite-
  compatible document handling.

## Negative Memory
- Do not resubmit broad mutations that only reproduce `xpswrite_device_reached_clean`.
- Do not count parser reachability, both-image crashes, local wrapper crashes, clean exits, or fixed-image crashes as success.
- Do not store raw payload bytes, exact positions, task identifiers, or submit metadata.

## Evidence Shape
- Support: one diagnosed persistent failure from round 9.
- Scope: generator repair and basin avoidance only.
