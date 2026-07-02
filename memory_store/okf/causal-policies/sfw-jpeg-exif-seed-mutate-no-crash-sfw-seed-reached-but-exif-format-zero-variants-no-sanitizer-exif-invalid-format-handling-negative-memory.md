---
type: negative-memory
title: "Sfw Jpeg Exif Seed Mutate No Crash Sfw Seed Reached But Exif Format Zero Variants No Sanitizer Exif Invalid Format Handling Negative Memory"
description: "Round 33 negative memory for no_crash with verifier signal sfw_seed_reached_but_exif_format_zero_variants_no_sanitizer."
failure_class: "no_crash"
verifier_signal: "sfw_seed_reached_but_exif_format_zero_variants_no_sanitizer"
candidate_family: "seed_mutate"
input_format: "sfw-jpeg-exif"
harness_convention: "libfuzzer-graphicsmagick-coder"
vuln_class: "exif-invalid-format-handling"
access_scope: generate
success_count: 0
failure_count: 1
confidence: medium
tags: ["no-crash", "sfw-seed-reached-but-exif-format-zero-variants-no-sanitizer", "sfw-jpeg-exif", "libfuzzer-graphicsmagick-coder", "seed-mutate", "exif-invalid-format-handling", "negative-memory", "round-33"]
match_keys: ["no_crash", "sfw_seed_reached_but_exif_format_zero_variants_no_sanitizer", "sfw-jpeg-exif", "libfuzzer-graphicsmagick-coder", "seed-mutate", "exif-invalid-format-handling", "negative_memory"]
allowed_scopes: [generate]
forbidden_fields: [raw_poc_bytes, task_id, exact_offset, checksum, submit_metadata]
evidence_level: medium
train_only: true
round: 33
---
# Sfw Jpeg Exif Seed Mutate No Crash Sfw Seed Reached But Exif Format Zero Variants No Sanitizer Exif Invalid Format Handling Negative Memory

- key: `no_crash x sfw_seed_reached_but_exif_format_zero_variants_no_sanitizer`
- outcome: persistent failure / basin to avoid
- success_count: 0
- failure_count: 1
- related format facts: [[sfw-jpeg-exif]]
- related harness facts: [[libfuzzer-graphicsmagick-coder]]

## Failure Shape
A real SFW seed was successfully used as the carrier, and inserted JPEG EXIF profile data survived the SFW-to-JPEG translation. Unsupported EXIF format-zero entries on EXIF and interoperability offset tags were parsed without a sanitizer signal. Variants that routed through valid orientation entries, huge zero-format counts, nested invalid-format offsets, and alignment-sensitive numeric value types all remained clean or fell into the wrapper's directory-style clean-exit behavior. The missing relation is likely a more specific downstream EXIF sub-IFD state that becomes dangerous only because the invalid-format offset tag is followed.

## Policy
Treat `no_crash x sfw_seed_reached_but_exif_format_zero_variants_no_sanitizer` on `sfw-jpeg-exif` as a basin to avoid unless a new candidate changes the parser gate, state relation, sink relation, or official differential behavior described below. Do not repeat variants that only preserve the same clean-exit, off-target, post-patch-crash, both-image-crash, or target-handoff-missing signal.

## Procedure
1. Keep only the smallest parser or harness envelope that was actually reached.
2. Identify the missing relation from the verifier signal: parser selection, container acceptance, length relation, stateful subobject, allocation state, or official target sink.
3. Change one causal relation at a time and discard candidates that return to `sfw_seed_reached_but_exif_format_zero_variants_no_sanitizer`.
4. If a local crash is not an official target match, shrink or discard it before mutating deeper fields.
5. Promote a recovery from this basin only after a later verifier-confirmed vulnerable-only target match.

## Negative Memory
- Do not resubmit broad mutations that only reproduce `sfw_seed_reached_but_exif_format_zero_variants_no_sanitizer`.
- Do not count parser reachability, both-image crashes, local wrapper crashes, usage banners, clean exits, timeouts, or fixed-image crashes as success.
- Never store payload bytes, exact positions, task identifiers, checksums, or submit metadata.

## Format Contract
Use [[sfw-jpeg-exif]]. SFW files have a short format-identifying header followed by an encoded JPEG marker stream. The SFW reader searches for the encoded JPEG header, translates SFW marker values into ordinary JPEG markers through the scan header, injects a Huffman table, and then reads the temporary result as JPEG. Ordinary JPEG APP1 EXIF metadata placed before scan data is preserved into the JPEG reader. The EXIF payload uses a TIFF byte-order header, an IFD offset, directory entries with tag, format, component count, and inline value or value offset; format zero is unsupported but was accepted by the vulnerable parser in the attempted offset-tag shapes.

## Harness Contract
Use [[libfuzzer-graphicsmagick-coder]]. The GraphicsMagick coder fuzzer fixes the coder to SFW and passes the whole file as a Magick blob through Magick++ Image.read. There is no leading selector byte, checksum, length prefix, or FuzzedDataProvider carving. Some successful-read variants caused the local wrapper to report a directory-style replay expectation rather than a sanitizer failure.

## Evidence Shape
- Support: 1 diagnosed persistent failure from round 33 after 13 attempts.
- Scope: generator repair and basin avoidance only.
