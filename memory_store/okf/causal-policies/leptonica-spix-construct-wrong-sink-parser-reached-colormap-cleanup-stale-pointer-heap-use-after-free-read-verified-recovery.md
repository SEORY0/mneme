---
type: causal-policy
title: "Leptonica Spix Construct Wrong Sink Parser Reached Colormap Cleanup Stale Pointer Heap Use After Free Read Verified Recovery"
description: "Verified recovery distilled from a round trace for wrong_sink / parser_reached_colormap_cleanup_stale_pointer."
failure_class: "wrong_sink"
verifier_signal: "parser_reached_colormap_cleanup_stale_pointer"
candidate_family: "construct"
input_format: "leptonica-spix"
harness_convention: "libfuzzer"
vuln_class: "heap-use-after-free-read"
access_scope: generate
success_count: 1
confidence: high
tags: ["wrong-sink", "construct", "leptonica-spix", "heap-use-after-free-read", "verified-recovery"]
match_keys: ["wrong-sink", "parser-reached-colormap-cleanup-stale-pointer", "leptonica-spix", "libfuzzer", "heap-use-after-free-read", "verified-recovery"]
allowed_scopes: [generate]
forbidden_fields: [raw_poc_bytes, task_id, exact_offset, checksum, submit_metadata]
evidence_level: high
train_only: true
provenance: round-35-consolidator
---
# Leptonica Spix Construct Wrong Sink Parser Reached Colormap Cleanup Stale Pointer Heap Use After Free Read Verified Recovery

## Policy
For `wrong_sink` with verifier signal `parser_reached_colormap_cleanup_stale_pointer` on `leptonica-spix` under `libfuzzer`, recover by preserving the format and harness gates that reach the target sink, then mutate only the invariant described by the verified recipe. This policy is keyed to the failure signal and is not a byte-level PoC recipe.

## Procedure
1. Use Leptonica serialized PIX rather than a general image encoding, because the selected color-quantization fuzzer reads SPix directly.
2. Build a minimal accepted grayscale PIX with coherent dimensions, depth, raster size, and optional color table so thresholding creates a colormapped result.
3. The harness keeps a borrowed colormap pointer from that result, destroys the owning PIX, and then destroys the stale colormap pointer; keeping the image tiny avoids unrelated quantization behavior while the fixed build exits cleanly.

## Format Contract
- Input format: [[leptonica-spix]].
- Harness contract: [[libfuzzer]].
- Keep parser reachability and sink selection intact before mutating the vulnerable relation.

## Negative Memory
- Do not broaden this into unrelated `leptonica-spix` failures without the same failure class and verifier signal.
- Do not store task identifiers, raw bytes, exact offsets, checksums, or submit metadata.

## Evidence Shape
- Support: one round 35 verified official target match; vulnerable build reached the target signal and the fixed build did not.

## Diagnosis Notes
Generic image containers exited cleanly because they did not match the selected SPix-only harness. A minimal serialized PIX reached the thresholding and cleanup path immediately, and the sanitizer report arose during colormap destruction after the owning image had already freed the same object.
