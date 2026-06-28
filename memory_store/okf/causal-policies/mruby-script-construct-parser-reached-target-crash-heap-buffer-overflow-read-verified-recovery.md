---
type: causal-policy
title: "Mruby Script Construct Parser Reached Target Crash Heap Buffer Overflow Read Verified Recovery"
description: "Round 9 verified recovery for wrong_sink with verifier signal parser_reached_target_crash."
failure_class: "wrong_sink"
verifier_signal: "parser_reached_target_crash"
candidate_family: "construct"
input_format: "mruby-script"
harness_convention: "honggfuzz-file"
vuln_class: "heap-buffer-overflow-read"
access_scope: generate
success_count: 1
confidence: high
tags: ["wrong-sink", "parser-reached-target-crash", "mruby-script", "construct", "verified-recovery", "round-9"]
match_keys: ["wrong_sink", "parser_reached_target_crash", "mruby-script", "honggfuzz-file", "heap-buffer-overflow-read", "verified_recovery"]
allowed_scopes: [generate]
forbidden_fields: [raw_poc_bytes, task_id, exact_offset, checksum, submit_metadata]
evidence_level: high
train_only: true
round: 9
---
# Mruby Script Construct Parser Reached Target Crash Heap Buffer Overflow Read Verified Recovery

## Policy
For `wrong_sink x parser_reached_target_crash`, preserve the format and harness gates that reached the target path, then apply the verified causal relation below. This is a positive recovery policy because the official vulnerable/fixed verifier recorded a target match.

## Procedure
1. Feed raw Ruby source that creates a normal Array, calls Array#shift with a negative count, keeps
  the returned value live, and forces garbage collection.
1. The negative count is accepted as a copy length and corrupts array/shared-array metadata; GC then
  walks the malformed array state and reads outside the valid allocation.

## Format Contract
- The input is plain mruby source text.
- Array literals/ranges are enough to reach the core Array implementation; calling shift with an
  explicit integer argument uses the multi-shift path rather than the one-element shift helper.

## Harness Contract
- The honggfuzz-style target copies the raw input into a NUL-terminated buffer, opens a fresh mruby
  VM, calls mrb_load_string on the buffer, closes the VM, and frees the buffer.
- There is no leading mode byte or secondary file format.

## Related Knowledge
- Format facts: [[mruby-script]]
- Harness facts: [[honggfuzz-file]]

## Negative Memory
- Do not broaden mutations after the parser/harness gate is proven.
- Do not submit candidates that reproduce on the fixed image, move to an off-target wrapper crash, or only preserve a local-only crash signal.
- Do not store raw payload bytes, exact offsets, checksums, or task-local identifiers.

## Evidence Shape
- Support: one round-9 worker trace with official target match.
- Scope: generator repair for the same failure-keyed basin.
