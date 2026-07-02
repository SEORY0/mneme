---
type: causal-policy
title: "Heif Isobmff Seed Mutate Wrong Sink Official Target Match Heap Buffer Overflow Read Verified Recovery"
description: "Verified recovery distilled from a round trace for wrong_sink / official_target_match."
failure_class: "wrong_sink"
verifier_signal: "official_target_match"
candidate_family: "seed_mutate"
input_format: "heif-isobmff"
harness_convention: "libfuzzer"
vuln_class: "heap-buffer-overflow-read"
access_scope: generate
success_count: 1
confidence: high
tags: ["wrong-sink", "seed-mutate", "heif-isobmff", "heap-buffer-overflow-read", "verified-recovery"]
match_keys: ["wrong-sink", "official-target-match", "heif-isobmff", "libfuzzer", "heap-buffer-overflow-read", "verified-recovery"]
allowed_scopes: [generate]
forbidden_fields: [raw_poc_bytes, task_id, exact_offset, checksum, submit_metadata]
evidence_level: high
train_only: true
provenance: round-35-consolidator
---
# Heif Isobmff Seed Mutate Wrong Sink Official Target Match Heap Buffer Overflow Read Verified Recovery

## Policy
For `wrong_sink` with verifier signal `official_target_match` on `heif-isobmff` under `libfuzzer`, recover by preserving the format and harness gates that reach the target sink, then mutate only the invariant described by the verified recipe. This policy is keyed to the failure signal and is not a byte-level PoC recipe.

## Procedure
1. Start from a valid HEIF file that already has an auxiliary alpha image.
2. Preserve the alpha item, its auxC property, and its auxl relation, but mutate the primary image into a derived overlay-style image whose decoded RGB canvas is larger than the decoded alpha plane.
3. The context then transfers the smaller alpha plane to the larger RGB image, and the fixed file-fuzzer decode target forces color conversion that reads alpha using the canvas dimensions.

## Format Contract
- Input format: [[heif-isobmff]].
- Harness contract: [[libfuzzer]].
- Keep parser reachability and sink selection intact before mutating the vulnerable relation.

## Negative Memory
- Do not broaden this into unrelated `heif-isobmff` failures without the same failure class and verifier signal.
- Do not store task identifiers, raw bytes, exact offsets, checksums, or submit metadata.

## Evidence Shape
- Support: one round 35 verified official target match; vulnerable build reached the target signal and the fixed build did not.
