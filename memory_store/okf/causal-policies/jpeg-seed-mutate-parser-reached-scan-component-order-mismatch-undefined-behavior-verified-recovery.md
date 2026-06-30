---
type: causal-policy
title: "Jpeg Seed Mutate Parser Reached Scan Component Order Mismatch Undefined Behavior Verified Recovery"
description: "Round 28 verified recovery for wrong_sink with verifier signal parser_reached_scan_component_order_mismatch."
failure_class: "wrong_sink"
verifier_signal: "parser_reached_scan_component_order_mismatch"
candidate_family: "seed_mutate"
input_format: "jpeg"
harness_convention: "libfuzzer"
vuln_class: "undefined-behavior"
access_scope: generate
success_count: 1
confidence: high
tags: ["wrong-sink", "parser-reached-scan-component-order-mismatch", "jpeg", "libfuzzer", "seed-mutate", "undefined-behavior", "verified-recovery", "round-28"]
match_keys: ["wrong_sink", "parser_reached_scan_component_order_mismatch", "jpeg", "libfuzzer", "undefined-behavior", "verified_recovery", "seed-mutate", "undefined-behavior"]
allowed_scopes: [generate]
forbidden_fields: [raw_poc_bytes, task_id, exact_offset, checksum, submit_metadata]
evidence_level: high
train_only: true
round: 28
---
# Jpeg Seed Mutate Parser Reached Scan Component Order Mismatch Undefined Behavior Verified Recovery

## Policy
For `wrong_sink x parser_reached_scan_component_order_mismatch`, preserve the format and harness gates that reached the parser or sink, then apply the verified causal relation below. This is a positive recovery policy because the official vulnerable/fixed verifier recorded a target match.

## Procedure
1. Start from a valid baseline JPEG seed that already passes SOI, table, frame, scan, and entropy-data gates. Preserve the frame header, quantization tables, Huffman tables, and entropy payload. Mutate only the start-of-scan component descriptor order so the scan still lists all frame components, but a later component appears before an earlier frame-header component. This reaches the scan parser's component-order validation path and the vulnerable build trips sanitizer instrumentation there; the fixed build exits cleanly.
2. Keep the carrier abstract: preserve the gate, invariant, and sink relation rather than task-local bytes, exact offsets, checksums, or identifiers.
3. If the verifier signal changes, re-rank against the new failure key before mutating unrelated fields.

## Format Contract
- Format [[jpeg]]: JPEG inputs require SOI marker framing, length-delimited metadata/table segments, a start-of-frame marker with precision, dimensions, and component descriptors, a start-of-scan marker with a scan component count, per-scan component selectors and table ids, spectral-selection bytes, and entropy-coded data ending at a marker. Multi-component baseline scans must use scan component descriptors consistent with the frame header order.
- Harness [[libfuzzer]]: The libFuzzer harness passes raw input bytes directly to LibGfx's JPEG image decoder plugin, initializes it, and requests the first frame. There is no filename wrapper, leading mode byte, sidecar metadata, checksum layer, or FuzzedDataProvider front/back split.

## Negative Memory
- Do not broaden mutations after parser or harness reachability is proven.
- Do not submit candidates that reproduce on the fixed image, crash both images, or move to an off-target wrapper crash.
- Do not store payload bytes, exact offsets, checksums, or task-local identifiers.

## Evidence Shape
- Support: one round-28 worker trace with official target match.
- Scope: generator repair for the same failure-keyed basin; pair with [[jpeg]] and [[libfuzzer]].
