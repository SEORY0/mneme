---
type: "negative-memory"
title: "DWG Drawing Seed Mutate No Crash No Sanitizer Signal Heap Buffer Overflow Negative Memory"
description: "Round 38 negative memory for no_crash with verifier signal no_sanitizer_signal."
failure_class: "no_crash"
verifier_signal: "no_sanitizer_signal"
candidate_family: "seed_mutate"
input_format: "dwg-drawing"
harness_convention: "libfuzzer"
vuln_class: "heap-buffer-overflow"
access_scope: "generate"
success_count: 0
failure_count: 1
confidence: "medium"
tags: ["no-crash", "no-sanitizer-signal", "dwg-drawing", "libfuzzer", "seed-mutate", "heap-buffer-overflow", "negative-memory", "round-38"]
match_keys: ["no_crash", "no_sanitizer_signal", "dwg-drawing", "libfuzzer", "heap-buffer-overflow", "negative-memory", "seed_mutate"]
allowed_scopes: ["generate"]
forbidden_fields: ["raw_poc_bytes", "task_id", "exact_offset", "checksum", "submit_metadata"]
evidence_level: "medium"
train_only: true
round: 38
---
# DWG Drawing Seed Mutate No Crash No Sanitizer Signal Heap Buffer Overflow Negative Memory

- key: `no_crash x no_sanitizer_signal`
- outcome: persistent failure / basin to avoid
- success_count: 0
- failure_count: 1
- related format facts: [[dwg-drawing]]
- related harness facts: [[libfuzzer]]

## Failure Shape
Seed-mutated native drawing inputs reached the DWG decoder and several mutations reached the intended pattern where malformed extended entity data moved the object-local cursor past the valid entity region and generated field decoding continued. The tested carrier entities and output path produced logged bounds errors but no sanitizer-visible crash; malformed EED data was often converted into null decoded entries that the JSON writer and free path tolerated.

## Observed Basin
- Failure trajectory classes: no_crash.
- Official confirmation: no server target match for this basin.

## Policy
Treat `no_crash x no_sanitizer_signal` on `[[dwg-drawing]]` under `[[libfuzzer]]` as a basin to avoid unless a new candidate changes the parser gate, state relation, or sink relation described above. Preserve any proven reachability, but reject variants that return to the same clean-exit, off-target-crash, wrapper-mismatch, usage-only, timeout, both-image-crash, or fixed-image-crash behavior.

## Procedure
1. Keep only the smallest parser or harness envelope that was actually reached.
2. Identify the missing relation from the verifier signal: parser selection, container acceptance, length relation, stateful subobject, allocation state, or official target sink.
3. Change one relation at a time and discard candidates that return to the same `no_sanitizer_signal` basin.
4. Promote a recovery from this basin only after a later official target match.

## Negative Memory
- Do not resubmit broad mutations that only reproduce `no_sanitizer_signal`.
- Do not count parser reachability, both-image crashes, local wrapper crashes, clean exits, timeouts, or fixed-image crashes as success.
- Do not store payload bytes, exact positions, task identifiers, checksums, or submit metadata.

## Evidence Shape
- Support: one diagnosed persistent failure from round 38 after 36 attempts.
- Candidate family: seed_mutate.
- Scope: generator repair and basin avoidance only.
