---
type: "negative-memory"
title: "DXF Text Seed Mutate No Crash Parser Clean Or Target Invariant Not Triggered Heap Buffer Overflow Write Negative Memory"
description: "Round 38 negative memory for no_crash with verifier signal parser_clean_or_target_invariant_not_triggered."
failure_class: "no_crash"
verifier_signal: "parser_clean_or_target_invariant_not_triggered"
candidate_family: "seed_mutate"
input_format: "dxf-text"
harness_convention: "libfuzzer-libredwg-llvmfuzz"
vuln_class: "heap-buffer-overflow-write"
access_scope: "generate"
success_count: 0
failure_count: 1
confidence: "medium"
tags: ["no-crash", "parser-clean-or-target-invariant-not-triggered", "dxf-text", "libfuzzer-libredwg-llvmfuzz", "seed-mutate", "heap-buffer-overflow-write", "negative-memory", "round-38"]
match_keys: ["no_crash", "parser_clean_or_target_invariant_not_triggered", "dxf-text", "libfuzzer-libredwg-llvmfuzz", "heap-buffer-overflow-write", "negative-memory", "seed_mutate"]
allowed_scopes: ["generate"]
forbidden_fields: ["raw_poc_bytes", "task_id", "exact_offset", "checksum", "submit_metadata"]
evidence_level: "medium"
train_only: true
round: 38
---
# DXF Text Seed Mutate No Crash Parser Clean Or Target Invariant Not Triggered Heap Buffer Overflow Write Negative Memory

- key: `no_crash x parser_clean_or_target_invariant_not_triggered`
- outcome: persistent failure / basin to avoid
- success_count: 0
- failure_count: 1
- related format facts: [[dxf-text]]
- related harness facts: [[libfuzzer-libredwg-llvmfuzz]]

## Failure Shape
The accepted DXF seed envelope remained clean after several distinct invariant attempts. Minimal SPATIAL_FILTER construction did not crash; PDFUNDERLAY optional inverted-clip mutation did not advance the parser index as expected; IMAGE clip-count recount mutations, including large repeated coordinate families, stayed clean in both local verification and one official submission. The most likely miss is that the intended stale-index relation needs a different object family or a writer/cleanup path that these seeds did not activate.

## Observed Basin
- Failure trajectory classes: no_crash.
- Official confirmation: no server target match for this basin.

## Policy
Treat `no_crash x parser_clean_or_target_invariant_not_triggered` on `[[dxf-text]]` under `[[libfuzzer-libredwg-llvmfuzz]]` as a basin to avoid unless a new candidate changes the parser gate, state relation, or sink relation described above. Preserve any proven reachability, but reject variants that return to the same clean-exit, off-target-crash, wrapper-mismatch, usage-only, timeout, both-image-crash, or fixed-image-crash behavior.

## Procedure
1. Keep only the smallest parser or harness envelope that was actually reached.
2. Identify the missing relation from the verifier signal: parser selection, container acceptance, length relation, stateful subobject, allocation state, or official target sink.
3. Change one relation at a time and discard candidates that return to the same `parser_clean_or_target_invariant_not_triggered` basin.
4. Promote a recovery from this basin only after a later official target match.

## Negative Memory
- Do not resubmit broad mutations that only reproduce `parser_clean_or_target_invariant_not_triggered`.
- Do not count parser reachability, both-image crashes, local wrapper crashes, clean exits, timeouts, or fixed-image crashes as success.
- Do not store payload bytes, exact positions, task identifiers, checksums, or submit metadata.

## Evidence Shape
- Support: one diagnosed persistent failure from round 38 after 17 attempts.
- Candidate family: seed_mutate.
- Scope: generator repair and basin avoidance only.
