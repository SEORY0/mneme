---
type: causal-policy
title: "Gas Assembly Source Minimal Raw Text Parser Reached Target Sink Use Of Uninitialized Value Verified Recovery"
description: "Round 27 verified recovery for wrong_sink with verifier signal parser_reached_target_sink."
failure_class: "wrong_sink"
verifier_signal: "parser_reached_target_sink"
candidate_family: "minimal_raw_text"
input_format: "gas-assembly-source"
harness_convention: "libfuzzer-raw-file-to-gas"
vuln_class: "use-of-uninitialized-value"
access_scope: generate
success_count: 1
confidence: high
tags: ["wrong-sink", "parser-reached-target-sink", "gas-assembly-source", "libfuzzer-raw-file-to-gas", "minimal-raw-text", "use-of-uninitialized-value", "verified-recovery", "round-27"]
match_keys: ["wrong_sink", "parser_reached_target_sink", "gas-assembly-source", "libfuzzer-raw-file-to-gas", "use-of-uninitialized-value", "verified_recovery"]
allowed_scopes: [generate]
forbidden_fields: [raw_poc_bytes, task_id, exact_offset, checksum, submit_metadata]
evidence_level: high
train_only: true
round: 27
---
# Gas Assembly Source Minimal Raw Text Parser Reached Target Sink Use Of Uninitialized Value Verified Recovery

## Policy
For `wrong_sink x parser_reached_target_sink`, preserve the format and harness gates that reached the parser or sink, then apply the verified causal relation below. This is a positive recovery policy because the official vulnerable/fixed verifier recorded a target match.

## Procedure
1. Provide a minimal raw assembler source that starts an assembler preprocessor line marker and then ends immediately, before the directive's following line can be read.
2. This satisfies the assembler source path but forces EOF at the vulnerable read, leaving the local buffer without a fresh line and triggering the uninitialized newline scan only in the vulnerable build.
3. Keep the carrier abstract: preserve the gate/invariant relation, not any task-local bytes or offsets.
4. If a later candidate changes the verifier signal, re-rank against the new failure key before mutating unrelated fields.

## Format Contract
- The input is plain assembler text as consumed by GNU as.
- A leading preprocessor line-control directive changes the input-file reader's path: the reader consumes the marker, expects a following source-name line, and scans that line for a newline terminator.
- EOF at that point is a semantic violation rather than a binary container failure.
- Harness [[libfuzzer-raw-file-to-gas]]:
  - libFuzzer bytes are written unchanged to a temporary assembly file and the assembler is invoked on that file.
  - The harness does not carve fields from the input and does not use FuzzedDataProvider; every byte is interpreted as assembler source text.

## Negative Memory
- Do not broaden mutations after the parser or harness gate is proven.
- Do not submit candidates that reproduce on the fixed image or move to an off-target wrapper crash.
- Do not store payload bytes, exact offsets, checksums, or task-local identifiers.

## Evidence Shape
- Support: one round-27 worker trace with official target match.
- Scope: generator repair for the same failure-keyed basin; pair with [[gas-assembly-source]] and [[libfuzzer-raw-file-to-gas]].
