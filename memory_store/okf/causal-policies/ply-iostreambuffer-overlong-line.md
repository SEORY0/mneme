---
type: causal-policy
title: "Ply Iostreambuffer Overlong Line"
description: "Round 6 verified recovery for wrong_sink with verifier signal parser_reached_sink_mismatch_label_but_stack_matches_iostreambuffer."
failure_class: "wrong_sink"
verifier_signal: "parser_reached_sink_mismatch_label_but_stack_matches_iostreambuffer"
candidate_family: "construct_long_line"
input_format: "ply"
harness_convention: "libfuzzer raw importer buffer"
vuln_class: "heap-buffer-overflow-write"
access_scope: generate
success_count: 1
confidence: high
tags: ["wrong-sink", "parser-reached-sink-mismatch-label-but-stack-matches-iostreambuffer", "ply", "construct-long-line", "verified-recovery", "round-6"]
match_keys: ["wrong_sink", "parser_reached_sink_mismatch_label_but_stack_matches_iostreambuffer", "ply", "libfuzzer raw importer buffer", "heap-buffer-overflow-write", "verified_recovery"]
allowed_scopes: [generate]
forbidden_fields: [raw_poc_bytes, task_id, exact_offset, checksum, submit_metadata]
evidence_level: high
train_only: true
round: 6
---
# Ply Iostreambuffer Overlong Line

## Policy
For `wrong_sink x parser_reached_sink_mismatch_label_but_stack_matches_iostreambuffer`, preserve the format and harness gates that reached the parser/sink, then apply the verified causal relation below. This is a positive recovery policy because the official vulnerable/fixed verifier recorded a target match.

## Procedure
1. Build an ASCII PLY envelope with a valid header prefix and place one header/comment line longer than the importer line buffer. Keep the rest of the PLY structure minimal so the PLY importer is selected and the oversized line is copied by IOStreamBuffer line reading.
2. Keep the carrier abstract: preserve the gate/invariant relation, not any task-local bytes or offsets.
3. If a later candidate changes the verifier signal, re-rank against the new failure key before mutating unrelated fields.

## Format Contract
- PLY text begins with a magic line, an ASCII format declaration, optional header fields such as comments and element declarations, and an end-header marker. The Assimp importer selects the PLY parser from this prefix before reading header lines through IOStreamBuffer.
- Harness: The Assimp fuzzer passes the entire input buffer to Importer.ReadFileFromMemory without a custom extension. Format selection is content-based, so the raw bytes must begin with a recognized format skeleton.

## Negative Memory
- Do not broaden mutations after the parser/harness gate is proven.
- Do not submit candidates that reproduce on the fixed image or move to an off-target wrapper crash.
- Do not store raw payload bytes, exact offsets, checksums, or task-local identifiers.

## Evidence Shape
- Support: one round-6 worker trace with official target match.
- Scope: generator repair for the same failure-keyed basin.
