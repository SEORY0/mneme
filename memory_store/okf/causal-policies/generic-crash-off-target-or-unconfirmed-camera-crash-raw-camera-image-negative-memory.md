---
type: causal-policy
title: "Generic Crash Off Target Or Unconfirmed Camera Crash Raw Camera Image Negative Memory"
description: "Round 8 negative memory for generic_crash with verifier signal off_target_or_unconfirmed_camera_crash."
failure_class: "generic_crash"
verifier_signal: "off_target_or_unconfirmed_camera_crash"
candidate_family: "seed_mutate"
input_format: "raw camera image"
harness_convention: "libfuzzer"
vuln_class: "use-of-uninitialized-value"
access_scope: generate
success_count: 0
confidence: medium
tags: ["generic-crash", "off-target-or-unconfirmed-camera-crash", "raw-camera-image", "negative_memory", "round-8"]
match_keys: ["generic_crash", "off_target_or_unconfirmed_camera_crash", "raw camera image", "libfuzzer", "negative_memory"]
allowed_scopes: [generate]
forbidden_fields: [raw_poc_bytes, task_id, exact_offset, checksum, submit_metadata]
evidence_level: medium
train_only: true
round: 8
---
# Generic Crash Off Target Or Unconfirmed Camera Crash Raw Camera Image Negative Memory

## Policy
Treat `generic_crash x off_target_or_unconfirmed_camera_crash` as a persistent failure basin for `raw camera image` under `libfuzzer`. Preserve any reachability it proved, but do not keep mutating the same field basin unless the next verification changes the signal.

## Diagnosed Dead End
- Camera corpus seeds and EOF truncations did not confirm the phase-one flat-field/read-shorts target. One large raw-camera seed was too large for official submission and a smaller truncation was rejected as off-target, so this remains unresolved.

## Format and Harness Gates
- Format: The LibRaw harness needs a recognizable raw camera container such as RAF, CR2, or NEF so open_buffer and unpack reach decoder-specific code. EOF truncation can create generic failures, but the target requires reaching phase-one correction and flat-field handling specifically.
- Harness: The fuzzer passes raw file bytes to LibRaw open_buffer, then calls unpack and processing routines. There is no explicit selector; the file signature chooses the camera decoder.

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
