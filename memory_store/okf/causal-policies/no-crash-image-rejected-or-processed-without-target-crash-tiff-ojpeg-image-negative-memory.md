---
type: causal-policy
title: "No Crash Image Rejected Or Processed Without Target Crash Tiff Ojpeg Image Negative Memory"
description: "Round 8 negative memory for no_crash with verifier signal image_rejected_or_processed_without_target_crash."
failure_class: "no_crash"
verifier_signal: "image_rejected_or_processed_without_target_crash"
candidate_family: "seed_mutate"
input_format: "tiff/ojpeg image"
harness_convention: "libfuzzer"
vuln_class: "double-free-or-invalid-free"
access_scope: generate
success_count: 0
confidence: medium
tags: ["no-crash", "image-rejected-or-processed-without-target-crash", "tiff-ojpeg-image", "negative_memory", "round-8"]
match_keys: ["no_crash", "image_rejected_or_processed_without_target_crash", "tiff/ojpeg image", "libfuzzer", "negative_memory"]
allowed_scopes: [generate]
forbidden_fields: [raw_poc_bytes, task_id, exact_offset, checksum, submit_metadata]
evidence_level: medium
train_only: true
round: 8
---
# No Crash Image Rejected Or Processed Without Target Crash Tiff Ojpeg Image Negative Memory

## Policy
Treat `no_crash x image_rejected_or_processed_without_target_crash` as a persistent failure basin for `tiff/ojpeg image` under `libfuzzer`. Preserve any reachability it proved, but do not keep mutating the same field basin unless the next verification changes the signal.

## Diagnosed Dead End
- Real TIFF seeds with the harness transform prefix and old-JPEG compression mutations either failed image read cleanly or processed without the target free failure. The unresolved piece is a coherent old-JPEG TIFF directory with the legacy JPEG tags expected by the libtiff path.

## Format and Harness Gates
- Format: The image payload is a TIFF-like file; changing only the compression indicator is insufficient if companion strip/JPEG offset and byte-count metadata are not internally consistent. Non-PNM image formats are accepted by the harness image reader.
- Harness: The fuzzer carves the first three little-endian signed 16-bit fields as rotation/shear parameters and passes the remaining bytes to the image reader. PoCs must prepend those parameter bytes before the actual image container.

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
