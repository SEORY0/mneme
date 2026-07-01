---
type: "negative-memory"
title: "Leptonica Spix Seed Mutate Construct No Crash Parser Reached No Target Use Of Uninitialized Value Negative Memory"
description: "Round 38 negative memory for no_crash with verifier signal parser_reached_no_target."
failure_class: "no_crash"
verifier_signal: "parser_reached_no_target"
candidate_family: "seed_mutate|construct"
input_format: "leptonica-spix"
harness_convention: "libfuzzer"
vuln_class: "use-of-uninitialized-value"
access_scope: "generate"
success_count: 0
failure_count: 1
confidence: "medium"
tags: ["no-crash", "parser-reached-no-target", "leptonica-spix", "libfuzzer", "seed-mutate-construct", "use-of-uninitialized-value", "negative-memory", "round-38"]
match_keys: ["no_crash", "parser_reached_no_target", "leptonica-spix", "libfuzzer", "use-of-uninitialized-value", "negative-memory", "seed_mutate|construct"]
allowed_scopes: ["generate"]
forbidden_fields: ["raw_poc_bytes", "task_id", "exact_offset", "checksum", "submit_metadata"]
evidence_level: "medium"
train_only: true
round: 38
---
# Leptonica Spix Seed Mutate Construct No Crash Parser Reached No Target Use Of Uninitialized Value Negative Memory

- key: `no_crash x parser_reached_no_target`
- outcome: persistent failure / basin to avoid
- success_count: 0
- failure_count: 1
- related format facts: [[leptonica-spix]]
- related harness facts: [[libfuzzer]]

## Failure Shape
Valid SPIX inputs reached the find-italic pipeline and debug PDF generation but did not produce the target sanitizer signal. Larger synthetic pages either executed cleanly or produced a broad segmentation fault that the fix oracle rejected, so the remaining gap is the precise intermediate 1-bpp pad-bit state needed by the raster-data compression path.

## Observed Basin
- Failure trajectory classes: generic_crash, no_crash.
- Official confirmation: no server target match for this basin.

## Policy
Treat `no_crash x parser_reached_no_target` on `[[leptonica-spix]]` under `[[libfuzzer]]` as a basin to avoid unless a new candidate changes the parser gate, state relation, or sink relation described above. Preserve any proven reachability, but reject variants that return to the same clean-exit, off-target-crash, wrapper-mismatch, usage-only, timeout, both-image-crash, or fixed-image-crash behavior.

## Procedure
1. Keep only the smallest parser or harness envelope that was actually reached.
2. Identify the missing relation from the verifier signal: parser selection, container acceptance, length relation, stateful subobject, allocation state, or official target sink.
3. Change one relation at a time and discard candidates that return to the same `parser_reached_no_target` basin.
4. Promote a recovery from this basin only after a later official target match.

## Negative Memory
- Do not resubmit broad mutations that only reproduce `parser_reached_no_target`.
- Do not count parser reachability, both-image crashes, local wrapper crashes, clean exits, timeouts, or fixed-image crashes as success.
- Do not store payload bytes, exact positions, task identifiers, checksums, or submit metadata.

## Evidence Shape
- Support: one diagnosed persistent failure from round 38 after 10 attempts.
- Candidate family: seed_mutate|construct.
- Scope: generator repair and basin avoidance only.
