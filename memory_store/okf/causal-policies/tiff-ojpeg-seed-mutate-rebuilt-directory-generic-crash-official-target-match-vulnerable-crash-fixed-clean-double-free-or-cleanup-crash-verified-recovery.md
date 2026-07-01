---
type: causal-policy
title: "Tiff Ojpeg Seed Mutate Rebuilt Directory Generic Crash Official Target Match Vulnerable Crash Fixed Clean Double Free Or Cleanup Crash Verified Recovery"
description: "Verified recovery distilled from a round trace for generic_crash / official_target_match_vulnerable_crash_fixed_clean."
failure_class: "generic_crash"
verifier_signal: "official_target_match_vulnerable_crash_fixed_clean"
candidate_family: "seed_mutate_rebuilt_directory"
input_format: "tiff-ojpeg"
harness_convention: "libfuzzer"
vuln_class: "double-free-or-cleanup-crash"
access_scope: generate
success_count: 1
confidence: high
tags: ["generic-crash", "seed-mutate-rebuilt-directory", "tiff-ojpeg", "double-free-or-cleanup-crash", "verified-recovery"]
match_keys: ["generic-crash", "official-target-match-vulnerable-crash-fixed-clean", "tiff-ojpeg", "libfuzzer", "double-free-or-cleanup-crash", "verified-recovery"]
allowed_scopes: [generate]
forbidden_fields: [raw_poc_bytes, task_id, exact_offset, checksum, submit_metadata]
evidence_level: high
train_only: true
provenance: round-35-consolidator
---
# Tiff Ojpeg Seed Mutate Rebuilt Directory Generic Crash Official Target Match Vulnerable Crash Fixed Clean Double Free Or Cleanup Crash Verified Recovery

## Policy
For `generic_crash` with verifier signal `official_target_match_vulnerable_crash_fixed_clean` on `tiff-ojpeg` under `libfuzzer`, recover by preserving the format and harness gates that reach the target sink, then mutate only the invariant described by the verified recipe. This policy is keyed to the failure signal and is not a byte-level PoC recipe.

## Procedure
1. Start from a valid single-sample JPEG-compressed TIFF seed that already reaches Leptonica image import after the harness prefix.
2. Rebuild the TIFF directory as old-JPEG rather than only flipping the compression tag: preserve baseline geometry, strip offsets and byte counts, and add the legacy JPEG interchange tags while removing the newer JPEG-tables carrier.
3. The vulnerable build enters old-JPEG cleanup through TIFFCleanup, while the fixed build rejects or cleans up the legacy state without crashing.

## Format Contract
- Input format: [[tiff-ojpeg]].
- Harness contract: [[libfuzzer]].
- Keep parser reachability and sink selection intact before mutating the vulnerable relation.

## Negative Memory
- Do not broaden this into unrelated `tiff-ojpeg` failures without the same failure class and verifier signal.
- Do not store task identifiers, raw bytes, exact offsets, checksums, or submit metadata.

## Evidence Shape
- Support: one round 35 verified official target match; vulnerable build reached the target signal and the fixed build did not.

## Diagnosis Notes
Compression-only old-JPEG mutations were over-broad and crashed both images. Unsupported bit-depth and frame-precision variants either failed to reproduce officially or were rejected before the target cleanup path. A valid legacy-directory relation was required.
