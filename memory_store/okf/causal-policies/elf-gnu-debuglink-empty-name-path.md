---
type: causal-policy
title: ELF GNU Debuglink Empty Name Path Recovery
description: Verified recovery for wrong_sink with sanitizer_crash on elf-gnu-debuglink inputs.
failure_class: wrong_sink
verifier_signal: sanitizer_crash
candidate_family: construct
input_format: elf-gnu-debuglink
harness_convention: libfuzzer
vuln_class: global-buffer-overflow-read
access_scope: generate
success_count: 1
confidence: medium
tags: [wrong-sink, sanitizer-crash, construct, elf-gnu-debuglink, global-buffer-overflow-read, verified-recovery]
match_keys: [wrong-sink, sanitizer-crash, elf-gnu-debuglink, global-buffer-overflow-read]
allowed_scopes: [generate]
forbidden_fields: [raw_poc_bytes, task_id, exact_offset, checksum, submit_metadata]
evidence_level: high
train_only: true
---
# ELF GNU Debuglink Empty Name Path Recovery

- key: `wrong_sink x sanitizer_crash`
- outcome: verified recovery
- success_count: 1
- failure_count: 0
- formats: [[elf-gnu-debuglink]]

## Failure Shape
Start from a valid ELF carrier that already has GNU debuglink metadata, then replace the
debuglink section with a format-valid but empty link-name record. This passes the section
parser and then violates the path-join invariant that path fragments have enough characters
for full-path probing.

## Policy
For `wrong_sink x sanitizer_crash` on `elf-gnu-debuglink`, preserve the parser and harness gate first, then mutate
only the causal invariant described by the verified trace. Prefer the candidate family `construct`
when the carrier is available because this shape was server-confirmed against vulnerable and fixed
builds.

## Procedure
1. Start from a valid ELF carrier that already reaches section parsing.
2. Keep GNU debuglink metadata recognizable while making the link-name field empty or too short
for path probing assumptions.
3. Preserve section headers and string-table relationships so the debuglink reader, not the ELF
loader, owns the failure.
4. When earlier candidates exit cleanly, retarget from general ELF validity to the path-join
invariant.

## Verifier Contract
The local signal may remain coarse. Keep candidates that reach the named parser or sink and
use the official vulnerable-versus-fixed comparison as the target-match gate.

## Negative Memory
- Do not remove section-table reachability while editing debuglink metadata.
- Do not rely on invalid ELF magic, missing string tables, or arbitrary appended names.
- Never store raw payload bytes, exact offsets, checksums, or task-local identifiers in memory.

## Evidence Shape
- Support: 1 server-verified solve.
- Scope: generator repair only.
