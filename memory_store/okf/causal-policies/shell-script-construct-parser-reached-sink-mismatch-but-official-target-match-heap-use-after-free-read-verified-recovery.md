---
type: causal-policy
title: "Shell Script Construct Parser Reached Sink Mismatch But Official Target Match Heap Use After Free Read Verified Recovery"
description: "Round 8 verified recovery for wrong_sink with verifier signal parser_reached_sink_mismatch_but_official_target_match."
failure_class: "wrong_sink"
verifier_signal: "parser_reached_sink_mismatch_but_official_target_match"
candidate_family: "construct"
input_format: "shell-script"
harness_convention: "libfuzzer"
vuln_class: "heap-use-after-free-read"
access_scope: generate
success_count: 1
confidence: high
tags: ["wrong-sink", "parser-reached-sink-mismatch-but-official-target-match", "shell-script", "construct", "verified-recovery", "round-8"]
match_keys: ["wrong_sink", "parser_reached_sink_mismatch_but_official_target_match", "shell-script", "libfuzzer", "heap-use-after-free-read", "verified_recovery"]
allowed_scopes: [generate]
forbidden_fields: [raw_poc_bytes, task_id, exact_offset, checksum, submit_metadata]
evidence_level: high
train_only: true
round: 8
---
# Shell Script Construct Parser Reached Sink Mismatch But Official Target Match Heap Use After Free Read Verified Recovery

## Policy
For `wrong_sink x parser_reached_sink_mismatch_but_official_target_match`, preserve the format and harness gates that reached the target path, then apply the verified causal relation below. This is a positive recovery policy because the official vulnerable/fixed verifier recorded a target match.

## Procedure
1. Feed the raw shell parser a heredoc opener with tab-stripping semantics, then make the heredoc body enter nested command/brace parsing and terminate abruptly. This reaches the stale heredoc-initiation bookkeeping path and triggers the use-after-free during parser error or entry formatting; the fixed image keeps the bookkeeping valid.
2. Keep the carrier abstract: preserve the gate/invariant relation, not task-local bytes, offsets, checksums, or submission metadata.
3. If a later candidate changes the verifier signal, re-rank against the new failure key before mutating unrelated fields.

## Format Contract
- The shell input is plain source text. Heredoc redirection syntax creates pending heredoc records, optional tab stripping changes how terminators are recognized, and interpolation inside the heredoc body can re-enter expression and command parsing before the parser finalizes those records.
- Harness: The fuzz target passes the raw input bytes directly as a shell source string to the parser and calls parse once. There is no container format, mode byte, or FuzzedDataProvider field carving.

## Negative Memory
- Do not broaden mutations after the parser/harness gate is proven.
- Do not submit candidates that reproduce on the fixed image or move to an off-target wrapper crash.
- Do not store raw payload bytes, exact offsets, checksums, or task-local identifiers.

## Evidence Shape
- Support: one round-8 worker trace with official target match.
- Scope: generator repair for the same failure-keyed basin.
