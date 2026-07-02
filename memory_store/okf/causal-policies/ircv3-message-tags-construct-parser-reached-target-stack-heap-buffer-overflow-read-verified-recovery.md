---
type: causal-policy
title: "Ircv3 Message Tags Construct Parser Reached Target Stack Heap Buffer Overflow Read Verified Recovery"
description: "Round 27 verified recovery for wrong_sink with verifier signal parser_reached_target_stack."
failure_class: "wrong_sink"
verifier_signal: "parser_reached_target_stack"
candidate_family: "construct"
input_format: "ircv3-message-tags"
harness_convention: "libfuzzer"
vuln_class: "heap-buffer-overflow-read"
access_scope: generate
success_count: 1
confidence: high
tags: ["wrong-sink", "parser-reached-target-stack", "ircv3-message-tags", "libfuzzer", "construct", "heap-buffer-overflow-read", "verified-recovery", "round-27"]
match_keys: ["wrong_sink", "parser_reached_target_stack", "ircv3-message-tags", "libfuzzer", "heap-buffer-overflow-read", "verified_recovery"]
allowed_scopes: [generate]
forbidden_fields: [raw_poc_bytes, task_id, exact_offset, checksum, submit_metadata]
evidence_level: high
train_only: true
round: 27
---
# Ircv3 Message Tags Construct Parser Reached Target Stack Heap Buffer Overflow Read Verified Recovery

## Policy
For `wrong_sink x parser_reached_target_stack`, preserve the format and harness gates that reached the parser or sink, then apply the verified causal relation below. This is a positive recovery policy because the official vulnerable/fixed verifier recorded a target match.

## Procedure
1. The harness mode selector had to leave the incoming IRC text unprefixed so the line began with a message-tag section.
2. A syntactically valid tagged IRC line then used a tag value ending in a lone escape before the command separator, reaching tag-value unescaping and causing the parser to read beyond the tag value terminator.
3. Keep the carrier abstract: preserve the gate/invariant relation, not any task-local bytes or offsets.
4. If a later candidate changes the verifier signal, re-rank against the new failure key before mutating unrelated fields.

## Format Contract
- IRCv3 message tags are accepted only at the start of an incoming line.
- The tag section begins with a marker, contains semicolon-separated key/value pairs, and ends at the command separator.
- Tag values support backslash escapes for separators and control characters, so a trailing escape is interpreted by the tag unescape routine rather than by the main command parser.
- Harness [[libfuzzer]]:
  - The libFuzzer input is raw text with a leading mode selector.
  - After the selector is consumed, the remaining bytes are split into line records on IRC line separators and emitted to Irssi's server incoming path.
  - In one mode the harness prepends a source prefix to each line, which prevents the message-tag parser from seeing tags at the beginning.

## Negative Memory
- Do not broaden mutations after the parser or harness gate is proven.
- Do not submit candidates that reproduce on the fixed image or move to an off-target wrapper crash.
- Do not store payload bytes, exact offsets, checksums, or task-local identifiers.

## Evidence Shape
- Support: one round-27 worker trace with official target match.
- Scope: generator repair for the same failure-keyed basin; pair with [[ircv3-message-tags]] and [[libfuzzer]].
