---
type: causal-policy
title: "PDF Postscript Construct Target Match On Submit Verified Recovery"
description: "Round 10 verified recovery for wrong_sink with verifier signal target_match_on_submit."
failure_class: "wrong_sink"
verifier_signal: "target_match_on_submit"
candidate_family: "construct"
input_format: "pdf/postscript"
harness_convention: "libfuzzer"
vuln_class: "memory-corruption"
access_scope: generate
success_count: 1
confidence: high
tags: ["wrong-sink", "target-match-on-submit", "pdf-postscript", "verified-recovery", "round-10"]
match_keys: ["wrong_sink", "target_match_on_submit", "pdf/postscript", "libfuzzer", "memory-corruption", "verified_recovery"]
allowed_scopes: [generate]
forbidden_fields: [raw_poc_bytes, task_id, exact_offset, checksum, submit_metadata]
evidence_level: high
train_only: true
round: 10
---
# PDF Postscript Construct Target Match On Submit Verified Recovery

## Policy
For `wrong_sink x target_match_on_submit`, preserve the format and harness gates that reached the official target path, then apply the verified causal relation below. This is a positive recovery policy because the official vulnerable/fixed verifier recorded a target match.

## Procedure
1. A minimal document envelope was enough to enter Ghostscript through stdin.
2. A content stream with a very large operand sequence pressured the interpreter stack/array movement path and triggered a vulnerable-only memory operation failure that the fixed image rejected cleanly.

## Format Contract
- The harness accepts PostScript or PDF-like data directly on stdin. PDF content streams can carry interpreter operands, and very large operand sequences stress stack extension and movement without needing a fully useful rendered page.
- Harness: The fuzz target launches Ghostscript in-process with a CUPS raster output device and copies raw input bytes to Ghostscript stdin. There is no outer archive; parser selection is by document syntax.

## Negative Memory
- Do not broaden mutations after the parser/harness gate is proven.
- Do not submit candidates that reproduce on the fixed image or move to an off-target wrapper crash.
- Do not store raw payload bytes, exact offsets, checksums, or task-local identifiers.

## Evidence Shape
- Support: one round-10 worker trace with official target match.
- Scope: generator repair for the same failure-keyed basin.
