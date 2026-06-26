---
type: causal-policy
title: "No Crash Valid Font Exercised Without Target Crash Opentype CFF Font Negative Memory"
description: "Round 8 negative memory for no_crash with verifier signal valid_font_exercised_without_target_crash."
failure_class: "no_crash"
verifier_signal: "valid_font_exercised_without_target_crash"
candidate_family: "seed_mutate"
input_format: "OpenType/CFF font"
harness_convention: "libfuzzer"
vuln_class: "heap-buffer-overflow-read"
access_scope: generate
success_count: 0
confidence: medium
tags: ["no-crash", "valid-font-exercised-without-target-crash", "opentype-cff-font", "negative_memory", "round-8"]
match_keys: ["no_crash", "valid_font_exercised_without_target_crash", "OpenType/CFF font", "libfuzzer", "negative_memory"]
allowed_scopes: [generate]
forbidden_fields: [raw_poc_bytes, task_id, exact_offset, checksum, submit_metadata]
evidence_level: medium
train_only: true
round: 8
---
# No Crash Valid Font Exercised Without Target Crash Opentype CFF Font Negative Memory

## Policy
Treat `no_crash x valid_font_exercised_without_target_crash` as a persistent failure basin for `OpenType/CFF font` under `libfuzzer`. Preserve any reachability it proved, but do not keep mutating the same field basin unless the next verification changes the signal.

## Diagnosed Dead End
- Valid TrueType and CFF OpenType seeds were accepted by the shaping harness, and simple CFF-family seed changes and truncation did not reach the charset overrun condition. The missing trigger is likely a coherent CFF charset/cardinality inconsistency rather than an envelope or magic gate.

## Format and Harness Gates
- Format: The harness consumes a complete font file. OpenType/CFF inputs must preserve the sfnt directory and CFF table structure well enough for HarfBuzz to instantiate a face before charset handling is reached; arbitrary truncation is filtered before the target code.
- Harness: libFuzzer passes the raw file bytes directly to the HarfBuzz shape fuzzer. There is no leading mode byte or FuzzedDataProvider carving in this selected harness.

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
