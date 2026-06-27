---
type: causal-policy
title: "Mapserver Mapfile Construct Parser Reached Target Crash Heap Buffer Overflow Read Verified Recovery"
description: "Round 9 verified recovery for wrong_sink with verifier signal parser_reached_target_crash."
failure_class: "wrong_sink"
verifier_signal: "parser_reached_target_crash"
candidate_family: "construct"
input_format: "mapserver-mapfile"
harness_convention: "afl-file"
vuln_class: "heap-buffer-overflow-read"
access_scope: generate
success_count: 1
confidence: high
tags: ["wrong-sink", "parser-reached-target-crash", "mapserver-mapfile", "construct", "verified-recovery", "round-9"]
match_keys: ["wrong_sink", "parser_reached_target_crash", "mapserver-mapfile", "afl-file", "heap-buffer-overflow-read", "verified_recovery"]
allowed_scopes: [generate]
forbidden_fields: [raw_poc_bytes, task_id, exact_offset, checksum, submit_metadata]
evidence_level: high
train_only: true
round: 9
---
# Mapserver Mapfile Construct Parser Reached Target Crash Heap Buffer Overflow Read Verified Recovery

## Policy
For `wrong_sink x parser_reached_target_crash`, preserve the format and harness gates that reached the target path, then apply the verified causal relation below. This is a positive recovery policy because the official vulnerable/fixed verifier recorded a target match.

## Procedure
1. Build a syntactically recognizable MapServer mapfile that enters the top-level map block, then
  start a quoted string value and end the file while the lexer is still in the quoted-string state.
1. The lexer has accumulated string content but has not written the closing terminator; the mapfile
  parser later formats an error using that shared buffer and reads past the allocation.

## Format Contract
- MapServer mapfiles are line-oriented text files whose first significant token must be the MAP
  keyword and whose top-level block normally ends with END.
- Keywords such as NAME consume string tokens.
- Quoted strings are accumulated by a lexer state machine into a shared buffer; normal closing
  quotes store a terminator, while EOF inside that state can leave the buffer unterminated.

## Harness Contract
- The AFL-style file harness rejects very small and very large files, writes the fuzz input as a
  mapfile, and calls the normal mapfile loader.
- The input is not carved; bytes are interpreted directly by the MapServer lexer/parser.

## Related Knowledge
- Format facts: [[mapserver-mapfile]]
- Harness facts: [[afl-file]]

## Negative Memory
- Do not broaden mutations after the parser/harness gate is proven.
- Do not submit candidates that reproduce on the fixed image, move to an off-target wrapper crash, or only preserve a local-only crash signal.
- Do not store raw payload bytes, exact offsets, checksums, or task-local identifiers.

## Evidence Shape
- Support: one round-9 worker trace with official target match.
- Scope: generator repair for the same failure-keyed basin.
