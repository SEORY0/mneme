---
type: causal-policy
title: "Tiff Ojpeg Image Seed Mutate Generic Crash Official Target Match After Local Generic Crash Invalid Free Or Double Free Verified Recovery"
description: "Verified recovery distilled from a round trace for generic_crash / official_target_match_after_local_generic_crash."
failure_class: "generic_crash"
verifier_signal: "official_target_match_after_local_generic_crash"
candidate_family: "seed_mutate"
input_format: "tiff-ojpeg-image"
harness_convention: "libfuzzer"
vuln_class: "invalid-free-or-double-free"
access_scope: generate
success_count: 1
confidence: high
tags: ["generic-crash", "seed-mutate", "tiff-ojpeg-image", "invalid-free-or-double-free", "verified-recovery"]
match_keys: ["generic-crash", "official-target-match-after-local-generic-crash", "tiff-ojpeg-image", "libfuzzer", "invalid-free-or-double-free", "verified-recovery"]
allowed_scopes: [generate]
forbidden_fields: [raw_poc_bytes, task_id, exact_offset, checksum, submit_metadata]
evidence_level: high
train_only: true
provenance: round-35-consolidator
---
# Tiff Ojpeg Image Seed Mutate Generic Crash Official Target Match After Local Generic Crash Invalid Free Or Double Free Verified Recovery

## Policy
For `generic_crash` with verifier signal `official_target_match_after_local_generic_crash` on `tiff-ojpeg-image` under `libfuzzer`, recover by preserving the format and harness gates that reach the target sink, then mutate only the invariant described by the verified recipe. This policy is keyed to the failure signal and is not a byte-level PoC recipe.

## Procedure
1. Start from a genuine strip-based legacy OJPEG TIFF so that the JPEG interchange data, strip storage, and legacy table references remain coherent, then prepend the harness parameter prefix.
2. A compression-only mutation of an ordinary TIFF is not enough.
3. Preserve the old-JPEG directory family and mutate only the advertised sample layout so Leptonica's scanline-size gate accepts the image and dispatches through the old-JPEG RGBA reader.
4. That inconsistent but parser-valid OJPEG state reaches libtiff's OJPEG header/read/cleanup path and produces a vulnerable-only free crash.

## Format Contract
- Input format: [[tiff-ojpeg-image]].
- Harness contract: [[libfuzzer]].
- Keep parser reachability and sink selection intact before mutating the vulnerable relation.

## Negative Memory
- Do not broaden this into unrelated `tiff-ojpeg-image` failures without the same failure class and verifier signal.
- Do not store task identifiers, raw bytes, exact offsets, checksums, or submit metadata.

## Evidence Shape
- Support: one round 35 verified official target match; vulnerable build reached the target signal and the fixed build did not.
