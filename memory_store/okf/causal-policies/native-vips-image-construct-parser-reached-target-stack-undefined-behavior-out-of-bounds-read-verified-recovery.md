---
type: causal-policy
title: "Native Vips Image Construct Parser Reached Target Stack Undefined Behavior Out Of Bounds Read Verified Recovery"
description: "Round 29 verified recovery for wrong_sink with verifier signal parser_reached_target_stack."
failure_class: "wrong_sink"
verifier_signal: "parser_reached_target_stack"
candidate_family: "construct"
input_format: "native-vips-image"
harness_convention: "libfuzzer-jpegsave-file"
vuln_class: "undefined-behavior-out-of-bounds-read"
access_scope: generate
success_count: 1
confidence: high
tags: ["wrong-sink", "parser-reached-target-stack", "native-vips-image", "libfuzzer-jpegsave-file", "construct", "undefined-behavior-out-of-bounds-read", "verified-recovery", "round-29"]
match_keys: ["wrong_sink", "parser_reached_target_stack", "native-vips-image", "libfuzzer-jpegsave-file", "undefined-behavior-out-of-bounds-read", "wrong-sink", "parser-reached-target-stack", "native-vips-image", "libfuzzer-jpegsave-file", "undefined-behavior-out-of-bounds-read", "verified_recovery", "construct", "construct"]
allowed_scopes: [generate]
forbidden_fields: [raw_poc_bytes, task_id, exact_offset, checksum, submit_metadata]
evidence_level: high
train_only: true
round: 29
---
# Native Vips Image Construct Parser Reached Target Stack Undefined Behavior Out Of Bounds Read Verified Recovery

- key: `wrong_sink x parser_reached_target_stack`
- outcome: verified target match / recovery policy
- success_count: 1
- related format facts: [[native-vips-image]]
- related harness facts: [[libfuzzer-jpegsave-file]]

## Policy
For `wrong_sink x parser_reached_target_stack` on `native-vips-image`, keep the parser and harness gates that produced the verifier signal, then vary only the causal relation described below. This is a positive recovery policy because the official vulnerable/fixed verifier recorded a target match.

## Procedure
1. Build a structurally valid tiny native VIPS image whose interpretation metadata marks the pixels as CMC and whose bands and numeric format are acceptable to the JPEG save path. The file-based libFuzzer target writes the raw input to a temporary file, opens it through the native VIPS reader, and then saving to JPEG asks libvips to convert the CMC image to a saveable color space. That conversion instantiates the CMC-to-LCh operation, which builds the UCS/CMC inverse hue table and triggers the vulnerable out-of-bounds table read in the unpatched build.
2. Preserve format recognition and the harness input contract while mutating the narrow sink invariant; do not broaden into an off-target crash or a both-image crash.
3. If later verifier output changes the failure key, re-rank against that new key before mutating unrelated fields.

## Format Contract
- Format [[native-vips-image]]: Native VIPS files begin with a fixed binary header containing image dimensions, band count, band format, coding, interpretation, resolution, and origin fields, followed directly by raw pixel samples. The header can encode a CMC interpretation directly, which is useful when ordinary image carriers would lose or normalize color-space metadata. Small dimensions and a normal uncoded numeric pixel format keep the loader and saver on the intended color-conversion path.
- Harness [[libfuzzer-jpegsave-file]]: The observed active target is the file-based JPEG save libFuzzer harness. It receives raw input bytes, writes them unchanged to a temporary file, loads that file with sequential access, rejects oversized images or excessive band counts, and then calls JPEG save-to-buffer. There is no FuzzedDataProvider carving; the entire PoC is the file image consumed by the loader.

## Negative Memory
- Do not corrupt the outer `native-vips-image` recognition gate while retargeting this signal.
- Do not count parser reachability, clean exits, fixed-image crashes, both-image crashes, or local wrong-sink labels as success without official target match.
- Never store payload bytes, exact positions, checksums, submit metadata, or task-local identifiers.

## Evidence Shape
- Support: one round-29 worker trace with official target match.
- Scope: generator repair and retargeting only; pair with [[native-vips-image]] and [[libfuzzer-jpegsave-file]].
