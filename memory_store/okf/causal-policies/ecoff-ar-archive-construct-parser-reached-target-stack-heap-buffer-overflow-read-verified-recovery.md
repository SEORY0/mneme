---
type: causal-policy
title: "Ecoff Ar Archive Construct Parser Reached Target Stack Heap Buffer Overflow Read Verified Recovery"
description: "Round 27 verified recovery for wrong_sink with verifier signal parser_reached_target_stack."
failure_class: "wrong_sink"
verifier_signal: "parser_reached_target_stack"
candidate_family: "construct"
input_format: "ecoff-ar-archive"
harness_convention: "libfuzzer-bfd-archive"
vuln_class: "heap-buffer-overflow-read"
access_scope: generate
success_count: 1
confidence: high
tags: ["wrong-sink", "parser-reached-target-stack", "ecoff-ar-archive", "libfuzzer-bfd-archive", "construct", "heap-buffer-overflow-read", "verified-recovery", "round-27"]
match_keys: ["wrong_sink", "parser_reached_target_stack", "ecoff-ar-archive", "libfuzzer-bfd-archive", "heap-buffer-overflow-read", "verified_recovery"]
allowed_scopes: [generate]
forbidden_fields: [raw_poc_bytes, task_id, exact_offset, checksum, submit_metadata]
evidence_level: high
train_only: true
round: 27
---
# Ecoff Ar Archive Construct Parser Reached Target Stack Heap Buffer Overflow Read Verified Recovery

## Policy
For `wrong_sink x parser_reached_target_stack`, preserve the format and harness gates that reached the parser or sink, then apply the verified causal relation below. This is a positive recovery policy because the official vulnerable/fixed verifier recorded a target match.

## Procedure
1. Build a syntactically valid archive envelope whose first special member selects the ECOFF archive-map reader, then make the map body shorter than the reader's minimum count-and-table expectation.
2. The vulnerable build reaches the ECOFF armap slurper and reads past the heap allocation while the fixed build rejects the malformed armap before the helper read.
3. Keep the carrier abstract: preserve the gate/invariant relation, not any task-local bytes or offsets.
4. If a later candidate changes the verifier signal, re-rank against the new failure key before mutating unrelated fields.

## Format Contract
- The harness target is the BFD archive detector.
- The outer format uses a SysV ar-style global header followed by fixed-width textual member headers and member bodies.
- ECOFF archive maps are selected by endian-specific special member names; their body is expected to contain a symbol count followed by parallel table/string metadata, so the member name gate is separate from the armap-body size invariant.
- Harness [[libfuzzer-bfd-archive]]:
  - libFuzzer bytes are written unchanged to a temporary file and opened with BFD using automatic target detection.
  - The harness calls the archive format checker directly; there is no FuzzedDataProvider carving, mode byte, checksum wrapper, or file-name-controlled format selection.

## Negative Memory
- Do not broaden mutations after the parser or harness gate is proven.
- Do not submit candidates that reproduce on the fixed image or move to an off-target wrapper crash.
- Do not store payload bytes, exact offsets, checksums, or task-local identifiers.

## Evidence Shape
- Support: one round-27 worker trace with official target match.
- Scope: generator repair for the same failure-keyed basin; pair with [[ecoff-ar-archive]] and [[libfuzzer-bfd-archive]].
