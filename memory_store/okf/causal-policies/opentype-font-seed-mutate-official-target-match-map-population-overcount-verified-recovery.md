---
type: causal-policy
title: "Opentype Font Seed Mutate Official Target Match Map Population Overcount Verified Recovery"
description: "Round 29 verified recovery for generic_crash with verifier signal official_target_match."
failure_class: "generic_crash"
verifier_signal: "official_target_match"
candidate_family: "seed_mutate"
input_format: "opentype-font"
harness_convention: "libfuzzer"
vuln_class: "map-population-overcount"
access_scope: generate
success_count: 1
confidence: high
tags: ["generic-crash", "official-target-match", "opentype-font", "libfuzzer", "seed-mutate", "map-population-overcount", "verified-recovery", "round-29"]
match_keys: ["generic_crash", "official_target_match", "opentype-font", "libfuzzer", "map-population-overcount", "generic-crash", "official-target-match", "opentype-font", "libfuzzer", "map-population-overcount", "verified_recovery", "seed_mutate", "seed-mutate"]
allowed_scopes: [generate]
forbidden_fields: [raw_poc_bytes, task_id, exact_offset, checksum, submit_metadata]
evidence_level: high
train_only: true
round: 29
---
# Opentype Font Seed Mutate Official Target Match Map Population Overcount Verified Recovery

- key: `generic_crash x official_target_match`
- outcome: verified target match / recovery policy
- success_count: 1
- related format facts: [[opentype-font]]
- related harness facts: [[libfuzzer]]

## Policy
For `generic_crash x official_target_match` on `opentype-font`, keep the parser and harness gates that produced the verifier signal, then vary only the causal relation described below. This is a positive recovery policy because the official vulnerable/fixed verifier recorded a target match.

## Procedure
1. Use a small structurally valid hb-subset-fuzzer corpus font seed that reaches subset face construction. Preserve the font carrier rather than corrupting table gates; the harness size-dependent allocation schedule and subset map construction expose the duplicate-key population invariant, while the fixed build exits cleanly.
2. Preserve format recognition and the harness input contract while mutating the narrow sink invariant; do not broaden into an off-target crash or a both-image crash.
3. If later verifier output changes the failure key, re-rank against that new key before mutating unrelated fields.

## Format Contract
- Format [[opentype-font]]: The input is a complete sfnt/OpenType font blob. HarfBuzz needs a coherent table directory and enough cmap/layout/outline structure for subset planning and output face construction; isolated table bytes or non-font instruction streams do not satisfy this harness.
- Harness [[libfuzzer]]: The active binary is hb-subset-fuzzer. It consumes the whole file as an hb_blob font, runs one subset with built-in text, and for larger inputs may also read trailing subset flags and UTF-32 codepoints from the end of the same byte string. The harness also derives allocation-failure state from total input size.

## Negative Memory
- Do not corrupt the outer `opentype-font` recognition gate while retargeting this signal.
- Do not count parser reachability, clean exits, fixed-image crashes, both-image crashes, or local wrong-sink labels as success without official target match.
- Never store payload bytes, exact positions, checksums, submit metadata, or task-local identifiers.

## Evidence Shape
- Support: one round-29 worker trace with official target match.
- Scope: generator repair and retargeting only; pair with [[opentype-font]] and [[libfuzzer]].
