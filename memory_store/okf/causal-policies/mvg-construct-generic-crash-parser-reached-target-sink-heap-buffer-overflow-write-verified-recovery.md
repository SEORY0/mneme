---
type: causal-policy
title: "MVG Construct Generic Crash Parser Reached Target Sink Heap Buffer Overflow Write Verified Recovery"
description: "Round 32 server-verified recovery for mvg keyed by generic_crash x parser_reached_target_sink."
failure_class: "generic_crash"
verifier_signal: "parser_reached_target_sink"
candidate_family: "construct"
input_format: "mvg"
harness_convention: "afl-libfuzzer-raw-graphicsmagick-mvg-coder"
vuln_class: "heap-buffer-overflow-write"
access_scope: generate
success_count: 1
confidence: high
tags: ["generic-crash", "parser-reached-target-sink", "mvg", "afl-libfuzzer-raw-graphicsmagick-mvg-coder", "construct", "heap-buffer-overflow-write", "verified-recovery", "round-32"]
match_keys: ["generic-crash", "parser-reached-target-sink", "mvg", "afl-libfuzzer-raw-graphicsmagick-mvg-coder", "construct", "heap-buffer-overflow-write", "verified-recovery"]
allowed_scopes: [generate]
forbidden_fields: [raw_poc_bytes, task_id, exact_offset, checksum, submit_metadata]
evidence_level: high
train_only: true
round: 32
---
# MVG Construct Generic Crash Parser Reached Target Sink Heap Buffer Overflow Write Verified Recovery

- key: `generic_crash x parser_reached_target_sink`
- outcome: server-verified target match
- success_count: 1
- related format facts: [[mvg]]
- related harness facts: [[afl-libfuzzer-raw-graphicsmagick-mvg-coder]]

## Policy
When `mvg` under `[[afl-libfuzzer-raw-graphicsmagick-mvg-coder]]` produces `parser_reached_target_sink` from `generic_crash`, keep the parser-reaching envelope and retarget the causal invariant that the official verifier accepted. Local sink labels are advisory once the vulnerable image fails and the fixed image stays clean or the server reports target match.

## Procedure
1. Preserve the harness and format contract that reached the parser: `[[mvg]]` through `[[afl-libfuzzer-raw-graphicsmagick-mvg-coder]]`.
2. Apply the verified recovery: Use a minimal MVG drawing with a valid canvas declaration and a single path primitive. Make the path begin with a small open subpath that has enough points to reach polygon conversion, then add several additional open one-point subpaths. The parser accepts the drawing, but conversion to PathInfo appends ghost closure records for each open subpath and the vulnerable allocation underestimates that expansion; the fixed build avoids the overflow.
3. Keep mutations narrow around the gate/invariant relation rather than rebuilding unrelated carriers or adding broad random noise.
4. If local labels report a non-target sink while the parser branch is reached, submit one minimized candidate before discarding it.
5. Reject both-image crashes, fixed-image crashes, parser rejection, and clean exits as non-success even when they look close locally.

## Format Contract
- MVG is line-oriented drawing text. A valid carrier can start with a canvas/view declaration followed by drawing directives and primitive geometry. A path primitive contains SVG-like move and line commands inside quoted path data; open subpaths are preserved as separate primitive runs and later converted into PathInfo records with virtual closure points.

## Harness Contract
- The GraphicsMagick coder harness fixes the coder to MVG and passes the entire PoC as a Magick blob. There is no mode selector, length prefix, checksum, or FuzzedDataProvider split; the raw bytes must be accepted as a complete MVG drawing.

## Negative Memory
- Do not store concrete payload bytes, task identifiers, exact positions, checksums, or submit metadata.
- Do not treat parser reachability alone as success without the official target-match signal.
- Do not repeat a clean-exit or both-image-crash basin once the verifier has characterized it.

## Evidence Shape
- Support: one server-verified Round 32 solve.
- Candidate family: construct.
