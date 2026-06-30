---
type: causal-policy
title: "ELF Construct Parser Reached Sink Mismatch But Official Target Match Heap Buffer Overflow Write Verified Recovery"
description: "Round 27 verified recovery for wrong_sink with verifier signal parser_reached_sink_mismatch_but_official_target_match."
failure_class: "wrong_sink"
verifier_signal: "parser_reached_sink_mismatch_but_official_target_match"
candidate_family: "construct"
input_format: "elf"
harness_convention: "libfuzzer"
vuln_class: "heap-buffer-overflow-write"
access_scope: generate
success_count: 1
confidence: high
tags: ["wrong-sink", "parser-reached-sink-mismatch-but-official-target-match", "elf", "libfuzzer", "construct", "heap-buffer-overflow-write", "verified-recovery", "round-27"]
match_keys: ["wrong_sink", "parser_reached_sink_mismatch_but_official_target_match", "elf", "libfuzzer", "heap-buffer-overflow-write", "verified_recovery"]
allowed_scopes: [generate]
forbidden_fields: [raw_poc_bytes, task_id, exact_offset, checksum, submit_metadata]
evidence_level: high
train_only: true
round: 27
---
# ELF Construct Parser Reached Sink Mismatch But Official Target Match Heap Buffer Overflow Write Verified Recovery

## Policy
For `wrong_sink x parser_reached_sink_mismatch_but_official_target_match`, preserve the format and harness gates that reached the parser or sink, then apply the verified causal relation below. This is a positive recovery policy because the official vulnerable/fixed verifier recorded a target match.

## Procedure
1. Build a minimal loadable ELF whose dynamic relocation table is coherent enough for the loader to enumerate it, then make the relocation entry-size metadata invalid while leaving a positive relocation byte count and a file-backed relocation record.
2. The vulnerable loop uses the inconsistent entry-size and total-size relation and writes relocation records beyond the allocated array; the fixed build rejects or guards the invalid relocation entry size.
3. Keep the carrier abstract: preserve the gate/invariant relation, not any task-local bytes or offsets.
4. If a later candidate changes the verifier signal, re-rank against the new failure key before mutating unrelated fields.

## Format Contract
- ELF parsing requires a coherent file header and program headers; a dynamic segment should be file-backed through a loadable segment.
- Dynamic relocation tags drive the relocation table pointer, total byte size, and per-entry stride.
- A single relocation record can be enough once the dynamic metadata reaches the relocation population path.
- Harness [[libfuzzer]]:
  - The target consumes raw file bytes as the tested binary input; there is no fuzzer-side prefix, selector byte, or FuzzedDataProvider layout.
  - The radare2 analysis harness opens the file and drives the ELF loader and analysis path.

## Negative Memory
- Do not broaden mutations after the parser or harness gate is proven.
- Do not submit candidates that reproduce on the fixed image or move to an off-target wrapper crash.
- Do not store payload bytes, exact offsets, checksums, or task-local identifiers.

## Evidence Shape
- Support: one round-27 worker trace with official target match.
- Scope: generator repair for the same failure-keyed basin; pair with [[elf]] and [[libfuzzer]].
