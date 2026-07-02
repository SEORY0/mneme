---
type: causal-policy
title: "Flac Construct Seed Metadata Official Vul Crash Fix Clean Use Of Uninitialized Value Verified Recovery"
description: "Round 27 verified recovery for generic_crash with verifier signal official_vul_crash_fix_clean."
failure_class: "generic_crash"
verifier_signal: "official_vul_crash_fix_clean"
candidate_family: "construct_seed_metadata"
input_format: "flac"
harness_convention: "libfuzzer-flac-decoder"
vuln_class: "use-of-uninitialized-value"
access_scope: generate
success_count: 1
confidence: high
tags: ["generic-crash", "official-vul-crash-fix-clean", "flac", "libfuzzer-flac-decoder", "construct-seed-metadata", "use-of-uninitialized-value", "verified-recovery", "round-27"]
match_keys: ["generic_crash", "official_vul_crash_fix_clean", "flac", "libfuzzer-flac-decoder", "use-of-uninitialized-value", "verified_recovery"]
allowed_scopes: [generate]
forbidden_fields: [raw_poc_bytes, task_id, exact_offset, checksum, submit_metadata]
evidence_level: high
train_only: true
round: 27
---
# Flac Construct Seed Metadata Official Vul Crash Fix Clean Use Of Uninitialized Value Verified Recovery

## Policy
For `generic_crash x official_vul_crash_fix_clean`, preserve the format and harness gates that reached the parser or sink, then apply the verified causal relation below. This is a positive recovery policy because the official vulnerable/fixed verifier recorded a target match.

## Procedure
1. Use the harness datasource layout, select native FLAC decoding, enable metadata response for all block types, and run metadata processing.
2. The supplied stream starts with a valid FLAC marker and valid STREAMINFO copied from a real seed, followed by a responded picture metadata block whose declared body is longer than the bytes supplied through the read callback.
3. A small number of final stream chunks are provided before datasource exhaustion, forcing a metadata-read abort state to be overwritten by frame-sync search in the vulnerable build; the fixed build keeps the abort state clean.
4. Keep the carrier abstract: preserve the gate/invariant relation, not any task-local bytes or offsets.
5. If a later candidate changes the verifier signal, re-rank against the new failure key before mutating unrelated fields.

## Format Contract
- A native FLAC stream starts with the FLAC marker, then STREAMINFO must appear first and provide valid stream parameters.
- Metadata block headers carry a last-block flag, a block type, and a body length; responded metadata block types are parsed rather than skipped.
- For this bug, audio frames are not required: the important invariant is that a parsed metadata block advertises more body than the datasource will provide.
- Harness [[libfuzzer-flac-decoder]]:
  - The active target is the FLAC oss-fuzz decoder harness.
  - It uses a custom front-consuming datasource where every scalar or byte vector is encoded as a little-endian length-prefixed chunk.
  - Initial boolean chunks choose native FLAC vs Ogg and decoder options; operation-loop chunks choose calls such as process_until_end_of_metadata.

## Negative Memory
- Do not broaden mutations after the parser or harness gate is proven.
- Do not submit candidates that reproduce on the fixed image or move to an off-target wrapper crash.
- Do not store payload bytes, exact offsets, checksums, or task-local identifiers.

## Evidence Shape
- Support: one round-27 worker trace with official target match.
- Scope: generator repair for the same failure-keyed basin; pair with [[flac]] and [[libfuzzer-flac-decoder]].
