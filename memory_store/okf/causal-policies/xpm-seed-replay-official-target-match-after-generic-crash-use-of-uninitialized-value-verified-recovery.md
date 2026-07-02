---
type: causal-policy
title: "XPM Seed Replay Official Target Match After Generic Crash Use Of Uninitialized Value Verified Recovery"
description: "Round 29 verified recovery for generic_crash with verifier signal official_target_match_after_generic_crash."
failure_class: "generic_crash"
verifier_signal: "official_target_match_after_generic_crash"
candidate_family: "seed_replay"
input_format: "xpm"
harness_convention: "libfuzzer"
vuln_class: "use-of-uninitialized-value"
access_scope: generate
success_count: 1
confidence: high
tags: ["generic-crash", "official-target-match-after-generic-crash", "xpm", "libfuzzer", "seed-replay", "use-of-uninitialized-value", "verified-recovery", "round-29"]
match_keys: ["generic_crash", "official_target_match_after_generic_crash", "xpm", "libfuzzer", "use-of-uninitialized-value", "generic-crash", "official-target-match-after-generic-crash", "xpm", "libfuzzer", "use-of-uninitialized-value", "verified_recovery", "seed_replay", "seed-replay"]
allowed_scopes: [generate]
forbidden_fields: [raw_poc_bytes, task_id, exact_offset, checksum, submit_metadata]
evidence_level: high
train_only: true
round: 29
---
# XPM Seed Replay Official Target Match After Generic Crash Use Of Uninitialized Value Verified Recovery

- key: `generic_crash x official_target_match_after_generic_crash`
- outcome: verified target match / recovery policy
- success_count: 1
- related format facts: [[xpm]]
- related harness facts: [[libfuzzer]]

## Policy
For `generic_crash x official_target_match_after_generic_crash` on `xpm`, keep the parser and harness gates that produced the verifier signal, then vary only the causal relation described below. This is a positive recovery policy because the official vulnerable/fixed verifier recorded a target match.

## Procedure
1. Replay a complete in-repository XPM sample rather than a tiny handcrafted image. The important gates are a recognized XPM magic, a valid quoted header, a complete color table, and enough quoted pixel rows to drive the XPM reader through quote stripping into StringToListMod. The vulnerable behavior depends on the list-conversion algorithm over the reconstructed quoted-line buffer, so preserving the full valid structure reaches the target while the fixed build exits cleanly.
2. Preserve format recognition and the harness input contract while mutating the narrow sink invariant; do not broaden into an off-target crash or a both-image crash.
3. If later verifier output changes the failure key, re-rank against that new key before mutating unrelated fields.

## Format Contract
- Format [[xpm]]: XPM files for this reader start with an identifying comment-style magic and use C-source-like quoted strings. The first quoted record declares image dimensions, color count, and characters per pixel; following quoted records define color keys and then pixel rows. The reader strips unquoted C syntax, turns closing quotes into logical newlines, builds a text-list view over that reconstructed buffer, then parses the color table and pixel rows.
- Harness [[libfuzzer]]: The GraphicsMagick coder harness is a libFuzzer target compiled for the XPM coder. It feeds the entire PoC file as the image blob to Magick++ with the coder fixed by the build; there is no fuzzer-side selector, checksum, or FuzzedDataProvider carving.

## Negative Memory
- Do not corrupt the outer `xpm` recognition gate while retargeting this signal.
- Do not count parser reachability, clean exits, fixed-image crashes, both-image crashes, or local wrong-sink labels as success without official target match.
- Never store payload bytes, exact positions, checksums, submit metadata, or task-local identifiers.

## Evidence Shape
- Support: one round-29 worker trace with official target match.
- Scope: generator repair and retargeting only; pair with [[xpm]] and [[libfuzzer]].
