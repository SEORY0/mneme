---
type: causal-policy
title: "No Crash Parser Clean Or Not At Target Sink Rar5 Negative Memory"
description: "Round 8 negative memory for no_crash with verifier signal parser_clean_or_not_at_target_sink."
failure_class: "no_crash"
verifier_signal: "parser_clean_or_not_at_target_sink"
candidate_family: "seed_mutate"
input_format: "rar5"
harness_convention: "afl-file"
vuln_class: "integer-truncation-bounds-check-bypass"
access_scope: generate
success_count: 0
confidence: medium
tags: ["no-crash", "parser-clean-or-not-at-target-sink", "rar5", "negative_memory", "round-8"]
match_keys: ["no_crash", "parser_clean_or_not_at_target_sink", "rar5", "afl-file", "negative_memory"]
allowed_scopes: [generate]
forbidden_fields: [raw_poc_bytes, task_id, exact_offset, checksum, submit_metadata]
evidence_level: medium
train_only: true
round: 8
---
# No Crash Parser Clean Or Not At Target Sink Rar5 Negative Memory

## Policy
Treat `no_crash x parser_clean_or_not_at_target_sink` as a persistent failure basin for `rar5` under `afl-file`. Preserve any reachability it proved, but do not keep mutating the same field basin unless the next verification changes the signal.

## Diagnosed Dead End
- Valid RAR5 samples reached the archive harness but did not exercise the oversized dictionary-window path. Broad mutations of likely archive header fields either remained accepted without reaching the vulnerable read path or did not locate the compressed-file service block that controls the window mask.

## Format and Harness Gates
- Format: RAR5 archives begin with a versioned RAR marker followed by variable-length block headers. File service blocks carry compression metadata, including dictionary/window parameters, and header corruption often causes the libarchive reader to reject or skip an entry before dictionary reads occur.
- Harness: The libarchive AFL wrapper feeds the raw file bytes to an archive reader with all formats and filters enabled, then iterates headers and drains entry data through a fixed-size read buffer. There is no mode byte or FuzzedDataProvider carving.

## Procedure
1. Before retrying this basin, rebuild the carrier around the exact harness contract and confirm parser reachability.
2. Replace the failed mutation family with a more specific invariant that would change the verifier signal.
3. Avoid broad seed mutation, oversized mutation, or off-target crash chasing when this same signal recurs.

## Negative Memory
- Do not promote this basin into a recovery policy until an official vulnerable/fixed verifier target match is observed.
- Do not preserve raw bytes, offsets, checksums, or task-local identifiers.

## Evidence Shape
- Support: one round-8 persistent failure trace.
- Scope: generator avoidance and retargeting for the same failure key.
