---
type: causal-policy
title: "No Crash Parser Not Reached Or Clean Image Spix Negative Memory"
description: "Round 8 negative memory for no_crash with verifier signal parser_not_reached_or_clean_image."
failure_class: "no_crash"
verifier_signal: "parser_not_reached_or_clean_image"
candidate_family: "construct_and_seed_mutate"
input_format: "spix"
harness_convention: "libfuzzer"
vuln_class: "uninitialized-value"
access_scope: generate
success_count: 0
confidence: medium
tags: ["no-crash", "parser-not-reached-or-clean-image", "spix", "negative_memory", "round-8"]
match_keys: ["no_crash", "parser_not_reached_or_clean_image", "spix", "libfuzzer", "negative_memory"]
allowed_scopes: [generate]
forbidden_fields: [raw_poc_bytes, task_id, exact_offset, checksum, submit_metadata]
evidence_level: medium
train_only: true
round: 8
---
# No Crash Parser Not Reached Or Clean Image Spix Negative Memory

## Policy
Treat `no_crash x parser_not_reached_or_clean_image` as a persistent failure basin for `spix` under `libfuzzer`. Preserve any reachability it proved, but do not keep mutating the same field basin unless the next verification changes the signal.

## Diagnosed Dead End
- JPEG/PNG samples and partial SPIX-shaped envelopes did not pass the serialized PIX gate. Without a valid SPIX serialization for a dewarpable page image, the debug-output path containing the improper directory argument was not reached.

## Format and Harness Gates
- Format: SPIX is Leptonica serialized PIX data with a recognizable file-type header followed by serialized image metadata and raster data. Common image formats such as JPEG are not accepted by pixReadMemSpix in this harness even though Leptonica can read them elsewhere.
- Harness: The libFuzzer target requires the raw input itself to be a valid SPIX buffer, then calls dewarpSinglePage with debug output enabled and also tries to read the same bytes as a compressed PIXA. No bytes are carved before the image parser.

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
