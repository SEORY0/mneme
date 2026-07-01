---
type: causal-policy
title: "TIFF Seed Mutate Generic Crash Official Target Match Fixed Clean Unsupported Cielog Alpha Crash Verified Recovery"
description: "Round 32 server-verified recovery for tiff keyed by generic_crash x official_target_match_fixed_clean."
failure_class: "generic_crash"
verifier_signal: "official_target_match_fixed_clean"
candidate_family: "seed_mutate"
input_format: "tiff"
harness_convention: "libfuzzer"
vuln_class: "unsupported-cielog-alpha-crash"
access_scope: generate
success_count: 1
confidence: high
tags: ["generic-crash", "official-target-match-fixed-clean", "tiff", "libfuzzer", "seed-mutate", "unsupported-cielog-alpha-crash", "verified-recovery", "round-32"]
match_keys: ["generic-crash", "official-target-match-fixed-clean", "tiff", "libfuzzer", "seed-mutate", "unsupported-cielog-alpha-crash", "verified-recovery"]
allowed_scopes: [generate]
forbidden_fields: [raw_poc_bytes, task_id, exact_offset, checksum, submit_metadata]
evidence_level: high
train_only: true
round: 32
---
# TIFF Seed Mutate Generic Crash Official Target Match Fixed Clean Unsupported Cielog Alpha Crash Verified Recovery

- key: `generic_crash x official_target_match_fixed_clean`
- outcome: server-verified target match
- success_count: 1
- related format facts: [[tiff]]
- related harness facts: [[libfuzzer]]

## Policy
When `tiff` under `[[libfuzzer]]` produces `official_target_match_fixed_clean` from `generic_crash`, keep the parser-reaching envelope and retarget the causal invariant that the official verifier accepted. Local sink labels are advisory once the vulnerable image fails and the fixed image stays clean or the server reports target match.

## Procedure
1. Preserve the harness and format contract that reached the parser: `[[tiff]]` through `[[libfuzzer]]`.
2. Apply the verified recovery: Start from a real CIE Log TIFF seed that already satisfies the TIFF signature, IFD, Log compression, and raster-data gates. Preserve the compressed image carrier and mutate only the channel metadata so the image is interpreted as CIE Log with alpha/extra samples. Broad rebuilt TIFFs crashed both images; the minimal seed mutation isolated the unsupported CIE Log alpha path so the vulnerable build crashed and the fixed build rejected it cleanly.
3. Keep mutations narrow around the gate/invariant relation rather than rebuilding unrelated carriers or adding broad random noise.
4. If local labels report a non-target sink while the parser branch is reached, submit one minimized candidate before discarding it.
5. Reject both-image crashes, fixed-image crashes, parser rejection, and clean exits as non-success even when they look close locally.

## Format Contract
- TIFF parsing is gated by byte order, magic, an IFD, and tag value storage rules. CIE Log selection is controlled by photometric interpretation and SGILog compression tags, while alpha is driven by samples-per-pixel plus extra-samples metadata. Small SHORT arrays may be stored inline in the IFD entry; larger arrays use out-of-line storage, so preserving correct tag storage form matters for parser reachability.

## Harness Contract
- The GraphicsMagick TIFF coder fuzzer feeds raw file bytes as an image blob with the TIFF coder selected by the harness. It reads the image and then exercises TIFF write-back when the read succeeds. There is no mode byte or FuzzedDataProvider framing; candidate files must also be readable by the Docker-copied target file user.

## Negative Memory
- Do not store concrete payload bytes, task identifiers, exact positions, checksums, or submit metadata.
- Do not treat parser reachability alone as success without the official target-match signal.
- Do not repeat a clean-exit or both-image-crash basin once the verifier has characterized it.

## Evidence Shape
- Support: one server-verified Round 32 solve.
- Candidate family: seed_mutate.
