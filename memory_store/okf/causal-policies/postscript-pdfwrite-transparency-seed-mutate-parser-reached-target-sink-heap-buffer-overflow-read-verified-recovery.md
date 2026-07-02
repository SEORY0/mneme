---
type: causal-policy
title: "Postscript Pdfwrite Transparency Seed Mutate Parser Reached Target Sink Heap Buffer Overflow Read Verified Recovery"
description: "Round 27 verified recovery for wrong_sink with verifier signal parser_reached_target_sink."
failure_class: "wrong_sink"
verifier_signal: "parser_reached_target_sink"
candidate_family: "seed_mutate"
input_format: "postscript-pdfwrite-transparency"
harness_convention: "libfuzzer-raw-bytes-to-ghostscript-pdfwrite"
vuln_class: "heap-buffer-overflow-read"
access_scope: generate
success_count: 1
confidence: high
tags: ["wrong-sink", "parser-reached-target-sink", "postscript-pdfwrite-transparency", "libfuzzer-raw-bytes-to-ghostscript-pdfwrite", "seed-mutate", "heap-buffer-overflow-read", "verified-recovery", "round-27"]
match_keys: ["wrong_sink", "parser_reached_target_sink", "postscript-pdfwrite-transparency", "libfuzzer-raw-bytes-to-ghostscript-pdfwrite", "heap-buffer-overflow-read", "verified_recovery"]
allowed_scopes: [generate]
forbidden_fields: [raw_poc_bytes, task_id, exact_offset, checksum, submit_metadata]
evidence_level: high
train_only: true
round: 27
---
# Postscript Pdfwrite Transparency Seed Mutate Parser Reached Target Sink Heap Buffer Overflow Read Verified Recovery

## Policy
For `wrong_sink x parser_reached_target_sink`, preserve the format and harness gates that reached the parser or sink, then apply the verified causal relation below. This is a positive recovery policy because the official vulnerable/fixed verifier recorded a target match.

## Procedure
1. Start from a valid Ghostscript PostScript transparency example, keep the pdfwrite transparency page-device setup, and use direct transparency-group nesting rather than an explicit compositor filter.
2. The nested groups accumulate pdfwrite viewer-state entries up to the stack-growth boundary, then ordinary text is emitted and the document is closed while still inside the nested resource context.
3. The vulnerable text-to-stream transition reads the clipped-text flag just past the tracked viewer-state stack; the fixed build grows or guards the stack before that read.
4. Keep the carrier abstract: preserve the gate/invariant relation, not any task-local bytes or offsets.
5. If a later candidate changes the verifier signal, re-rank against the new failure key before mutating unrelated fields.

## Format Contract
- Ghostscript accepts PostScript programs directly in this harness.
- For pdfwrite, transparency setup can be expressed with a page-device dictionary enabling transparency and compatibility level, followed by transparency-group begin/end operators around drawing or text operations.
- Direct transparency groups are handled as pdfwrite XObject substreams; using an explicit pdf14 device filter can route drawing through the compositor and avoid the high-level pdfwrite text transition.
- Harness [[libfuzzer-raw-bytes-to-ghostscript-pdfwrite]]:
  - The libFuzzer target passes the raw input buffer to Ghostscript as stdin and selects the pdfwrite device with a null output file.
  - There is no FuzzedDataProvider layout, leading mode selector, or external file container; the bytes must be a complete PostScript or PDF program accepted by Ghostscript.

## Negative Memory
- Do not broaden mutations after the parser or harness gate is proven.
- Do not submit candidates that reproduce on the fixed image or move to an off-target wrapper crash.
- Do not store payload bytes, exact offsets, checksums, or task-local identifiers.

## Evidence Shape
- Support: one round-27 worker trace with official target match.
- Scope: generator repair for the same failure-keyed basin; pair with [[postscript-pdfwrite-transparency]] and [[libfuzzer-raw-bytes-to-ghostscript-pdfwrite]].
