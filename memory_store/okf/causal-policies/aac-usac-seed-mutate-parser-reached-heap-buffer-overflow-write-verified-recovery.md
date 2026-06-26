---
type: causal-policy
title: "AAC USAC Seed Mutate Parser Reached Heap Buffer Overflow Write Verified Recovery"
description: "Round 8 verified recovery for generic_crash with verifier signal parser_reached."
failure_class: "generic_crash"
verifier_signal: "parser_reached"
candidate_family: "seed_mutate"
input_format: "aac-usac"
harness_convention: "libfuzzer"
vuln_class: "heap-buffer-overflow-write"
access_scope: generate
success_count: 1
confidence: high
tags: ["generic-crash", "parser-reached", "aac-usac", "seed-mutate", "verified-recovery", "round-8"]
match_keys: ["generic_crash", "parser_reached", "aac-usac", "libfuzzer", "heap-buffer-overflow-write", "verified_recovery"]
allowed_scopes: [generate]
forbidden_fields: [raw_poc_bytes, task_id, exact_offset, checksum, submit_metadata]
evidence_level: high
train_only: true
round: 8
---
# AAC USAC Seed Mutate Parser Reached Heap Buffer Overflow Write Verified Recovery

## Policy
For `generic_crash x parser_reached`, preserve the format and harness gates that reached the target path, then apply the verified causal relation below. This is a positive recovery policy because the official vulnerable/fixed verifier recorded a target match.

## Procedure
1. Use a compact AAC/USAC decoder input that is recognized by the XAAC fuzzer as an ADTS-like stream and configures USAC with SBR enabled. The key invariant is an unsupported output channel configuration flowing into SBR initialization: the decoder allocates SBR persistent/header/channel state for the supported shape, then ixheaacd_init_sbr iterates using the parsed channel count and writes an additional SBR header/channel entry beyond the heap allocation. The fixed build rejects or handles that unsupported USAC channel configuration before the write.
2. Keep the carrier abstract: preserve the gate/invariant relation, not task-local bytes, offsets, checksums, or submission metadata.
3. If a later candidate changes the verifier signal, re-rank against the new failure key before mutating unrelated fields.

## Format Contract
- The accepted input is a raw AAC/USAC decoder stream, not an outer length-prefixed harness format. The XAAC decoder fuzzer decides ADTS mode from the first bytes, initializes the decoder, configures it with the same input buffer, then repeatedly decodes frames. Reaching this bug requires a USAC configuration with SBR ratio enabled and a parsed channel count that reaches decoder-create and SBR initialization.
- Harness: The libFuzzer target feeds the entire buffer directly to the XAAC decoder wrapper. It checks only for an ADTS-like sync prefix to choose ADTS versus MP4-style mode, then calls init, config, and decode in sequence while advancing by consumed bytes. There is no external selector byte or FuzzedDataProvider layout.

## Negative Memory
- Do not broaden mutations after the parser/harness gate is proven.
- Do not submit candidates that reproduce on the fixed image or move to an off-target wrapper crash.
- Do not store raw payload bytes, exact offsets, checksums, or task-local identifiers.

## Evidence Shape
- Support: one round-8 worker trace with official target match.
- Scope: generator repair for the same failure-keyed basin.
