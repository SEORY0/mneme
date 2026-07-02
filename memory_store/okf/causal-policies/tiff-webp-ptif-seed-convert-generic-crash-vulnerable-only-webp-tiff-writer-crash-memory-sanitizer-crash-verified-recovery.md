---
type: causal-policy
title: "Tiff Webp Ptif Seed Convert Generic Crash Vulnerable Only Webp Tiff Writer Crash Memory Sanitizer Crash Verified Recovery"
description: "Verified recovery distilled from a round trace for generic_crash / vulnerable_only_webp_tiff_writer_crash."
failure_class: "generic_crash"
verifier_signal: "vulnerable_only_webp_tiff_writer_crash"
candidate_family: "seed_convert"
input_format: "tiff-webp-ptif"
harness_convention: "libfuzzer-graphicsmagick-coder-write"
vuln_class: "memory-sanitizer-crash"
access_scope: generate
success_count: 1
confidence: high
tags: ["generic-crash", "seed-convert", "tiff-webp-ptif", "memory-sanitizer-crash", "verified-recovery"]
match_keys: ["generic-crash", "vulnerable-only-webp-tiff-writer-crash", "tiff-webp-ptif", "libfuzzer-graphicsmagick-coder-write", "memory-sanitizer-crash", "verified-recovery"]
allowed_scopes: [generate]
forbidden_fields: [raw_poc_bytes, task_id, exact_offset, checksum, submit_metadata]
evidence_level: high
train_only: true
provenance: round-35-consolidator
---
# Tiff Webp Ptif Seed Convert Generic Crash Vulnerable Only Webp Tiff Writer Crash Memory Sanitizer Crash Verified Recovery

## Policy
For `generic_crash` with verifier signal `vulnerable_only_webp_tiff_writer_crash` on `tiff-webp-ptif` under `libfuzzer-graphicsmagick-coder-write`, recover by preserving the format and harness gates that reach the target sink, then mutate only the invariant described by the verified recipe. This policy is keyed to the failure signal and is not a byte-level PoC recipe.

## Procedure
1. Start from a real TIFF image that the PTIF coder accepts, then re-encode it as a valid WebP-compressed TIFF so the reader preserves WebP compression state and the fuzzer's write phase invokes the TIFF WebP encoder.
2. Keep the input decoder-compatible; forcing unsupported bit-depth metadata in the input can make libtiff reject the WebP strip before GraphicsMagick reaches the PTIF writer.
3. The accepted family reaches read, then write, with WebP compression carried through to the vulnerable build while the fixed build exits cleanly.

## Format Contract
- Input format: [[tiff-webp-ptif]].
- Harness contract: [[libfuzzer-graphicsmagick-coder-write]].
- Keep parser reachability and sink selection intact before mutating the vulnerable relation.

## Negative Memory
- Do not broaden this into unrelated `tiff-webp-ptif` failures without the same failure class and verifier signal.
- Do not store task identifiers, raw bytes, exact offsets, checksums, or submit metadata.

## Evidence Shape
- Support: one round 35 verified official target match; vulnerable build reached the target signal and the fixed build did not.

## Diagnosis Notes
Directly changing the input BitsPerSample field to a higher depth caused the WebP-compressed TIFF to fail during the read/decode phase, so the write-side encoder path was never reached. Photometric mutations intended to force fallback RGBA reading also remained blocked before the target writer.
