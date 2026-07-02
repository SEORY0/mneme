---
type: causal-policy
title: "Mapserver Mapfile Minimal Mapfile Target Sink Crash Double Free Verified Recovery"
description: "Round 28 verified recovery for generic_crash with verifier signal target_sink_crash."
failure_class: "generic_crash"
verifier_signal: "target_sink_crash"
candidate_family: "minimal_mapfile"
input_format: "mapserver-mapfile"
harness_convention: "libfuzzer"
vuln_class: "double-free"
access_scope: generate
success_count: 1
confidence: high
tags: ["generic-crash", "target-sink-crash", "mapserver-mapfile", "libfuzzer", "minimal-mapfile", "double-free", "verified-recovery", "round-28"]
match_keys: ["generic_crash", "target_sink_crash", "mapserver-mapfile", "libfuzzer", "double-free", "verified_recovery", "other", "double-free"]
allowed_scopes: [generate]
forbidden_fields: [raw_poc_bytes, task_id, exact_offset, checksum, submit_metadata]
evidence_level: high
train_only: true
round: 28
---
# Mapserver Mapfile Minimal Mapfile Target Sink Crash Double Free Verified Recovery

## Policy
For `generic_crash x target_sink_crash`, preserve the format and harness gates that reached the parser or sink, then apply the verified causal relation below. This is a positive recovery policy because the official vulnerable/fixed verifier recorded a target match.

## Procedure
1. Use a syntactically recognizable MapServer mapfile that reaches the top-level map parser, then enter an embedded legend label block. Allocate one label-owned string field and end the file before the label block closes. The EOF error path frees the embedded label's internals inside label loading, and the later map cleanup frees the same embedded label internals again.
2. Keep the carrier abstract: preserve the gate, invariant, and sink relation rather than task-local bytes, exact offsets, checksums, or identifiers.
3. If the verifier signal changes, re-rank against the new failure key before mutating unrelated fields.

## Format Contract
- Format [[mapserver-mapfile]]: MapServer mapfiles are keyword block files beginning with a top-level map block and closed by matching end tokens. Top-level blocks can include legend and scalebar sections, and those sections contain embedded label objects. Label fields such as font-like string properties allocate label-owned memory during parsing. EOF inside a nested block is treated as a parse failure while already-initialized map members are still cleaned up.
- Harness [[libfuzzer]]: The libFuzzer harness accepts raw PoC bytes within a bounded size range, writes them unchanged to a temporary file with a mapfile extension, calls msLoadMap on that file, then immediately calls msFreeMap on the returned pointer and clears the MapServer error list.

## Negative Memory
- Do not broaden mutations after parser or harness reachability is proven.
- Do not submit candidates that reproduce on the fixed image, crash both images, or move to an off-target wrapper crash.
- Do not store payload bytes, exact offsets, checksums, or task-local identifiers.

## Evidence Shape
- Support: one round-28 worker trace with official target match.
- Scope: generator repair for the same failure-keyed basin; pair with [[mapserver-mapfile]] and [[libfuzzer]].
