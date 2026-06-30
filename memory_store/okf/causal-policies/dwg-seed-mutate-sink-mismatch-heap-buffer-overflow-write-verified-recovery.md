---
type: causal-policy
title: "Dwg Seed Mutate Sink Mismatch Heap Buffer Overflow Write Verified Recovery"
description: "Round 29 verified recovery for wrong_sink with verifier signal sink_mismatch."
failure_class: "wrong_sink"
verifier_signal: "sink_mismatch"
candidate_family: "seed_mutate"
input_format: "dwg"
harness_convention: "libfuzzer"
vuln_class: "heap-buffer-overflow-write"
access_scope: generate
success_count: 1
confidence: high
tags: ["wrong-sink", "sink-mismatch", "dwg", "libfuzzer", "seed-mutate", "heap-buffer-overflow-write", "verified-recovery", "round-29"]
match_keys: ["wrong_sink", "sink_mismatch", "dwg", "libfuzzer", "heap-buffer-overflow-write", "wrong-sink", "sink-mismatch", "dwg", "libfuzzer", "heap-buffer-overflow-write", "verified_recovery", "seed_mutate", "seed-mutate"]
allowed_scopes: [generate]
forbidden_fields: [raw_poc_bytes, task_id, exact_offset, checksum, submit_metadata]
evidence_level: high
train_only: true
round: 29
---
# Dwg Seed Mutate Sink Mismatch Heap Buffer Overflow Write Verified Recovery

- key: `wrong_sink x sink_mismatch`
- outcome: verified target match / recovery policy
- success_count: 1
- related format facts: [[dwg]]
- related harness facts: [[libfuzzer]]

## Policy
For `wrong_sink x sink_mismatch` on `dwg`, keep the parser and harness gates that produced the verifier signal, then vary only the causal relation described below. This is a positive recovery policy because the official vulnerable/fixed verifier recorded a target match.

## Procedure
1. Start from a valid legacy DWG seed so the decoder populates the bit-chain codepage used by output writers. Preserve the binary layout and string lengths, and mutate one retained text/name field to same-length high-bit legacy-codepage characters that expand during UTF-8 conversion. When the JSON output path quotes that field, the destination estimate is too small and the vulnerable conversion writes past the allocation; the fixed build rejects or resizes safely.
2. Preserve format recognition and the harness input contract while mutating the narrow sink invariant; do not broaden into an off-target crash or a both-image crash.
3. If later verifier output changes the failure key, re-rank against that new key before mutating unrelated fields.

## Format Contract
- Format [[dwg]]: The harness accepts DWG, JSON, or DXF based on the first bytes: DWG begins with the standard ASCII release marker, JSON begins with an object marker, and other inputs are treated as DXF. DXF header codepage parsing updates the DWG header, but the JSON writer's conversion uses the bit-chain codepage copied from the input chain. Native DWG decoding carries the legacy codepage into that chain, so DWG is the reliable family for this sink. Legacy TV strings are byte strings interpreted through the drawing codepage, then quoted as UTF-8 for JSON output.
- Harness [[libfuzzer]]: The harness is libFuzzer over raw bytes with no FuzzedDataProvider carving. It null-terminates copied text inputs when needed, decodes the buffer as DWG, JSON, or DXF, then writes one randomly selected output format to a sink file. The JSON writer is one reachable output path and converts retained legacy TV strings through the vulnerable converter.

## Negative Memory
- Do not corrupt the outer `dwg` recognition gate while retargeting this signal.
- Do not count parser reachability, clean exits, fixed-image crashes, both-image crashes, or local wrong-sink labels as success without official target match.
- Never store payload bytes, exact positions, checksums, submit metadata, or task-local identifiers.

## Evidence Shape
- Support: one round-29 worker trace with official target match.
- Scope: generator repair and retargeting only; pair with [[dwg]] and [[libfuzzer]].
