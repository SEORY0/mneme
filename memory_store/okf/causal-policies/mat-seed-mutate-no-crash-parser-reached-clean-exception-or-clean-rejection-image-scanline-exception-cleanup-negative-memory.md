---
type: negative-memory
title: "Mat Seed Mutate No Crash Parser Reached Clean Exception Or Clean Rejection Image Scanline Exception Cleanup Negative Memory"
description: "Round 33 negative memory for no_crash with verifier signal parser_reached_clean_exception_or_clean_rejection."
failure_class: "no_crash"
verifier_signal: "parser_reached_clean_exception_or_clean_rejection"
candidate_family: "seed_mutate"
input_format: "mat"
harness_convention: "libfuzzer"
vuln_class: "image-scanline-exception-cleanup"
access_scope: generate
success_count: 0
failure_count: 1
confidence: medium
tags: ["no-crash", "parser-reached-clean-exception-or-clean-rejection", "mat", "libfuzzer", "seed-mutate", "image-scanline-exception-cleanup", "negative-memory", "round-33"]
match_keys: ["no_crash", "parser_reached_clean_exception_or_clean_rejection", "mat", "libfuzzer", "seed-mutate", "image-scanline-exception-cleanup", "negative_memory"]
allowed_scopes: [generate]
forbidden_fields: [raw_poc_bytes, task_id, exact_offset, checksum, submit_metadata]
evidence_level: medium
train_only: true
round: 33
---
# Mat Seed Mutate No Crash Parser Reached Clean Exception Or Clean Rejection Image Scanline Exception Cleanup Negative Memory

- key: `no_crash x parser_reached_clean_exception_or_clean_rejection`
- outcome: persistent failure / basin to avoid
- success_count: 0
- failure_count: 1
- related format facts: [[mat]]
- related harness facts: [[libfuzzer]]

## Failure Shape
Real MAT seeds were recognized, but mutations for short raster data, degenerate floating-point import ranges, mid-image missing scanlines, maximum accepted dimensions, and explicit dimension-limit exceptions either exited cleanly or produced only a non-reproducible local wrapper crash. The missing trigger appears to be a narrower exception state where scanline population is incomplete yet the image object still survives into vulnerable cleanup or writeback.

## Policy
Treat `no_crash x parser_reached_clean_exception_or_clean_rejection` on `mat` as a basin to avoid unless a new candidate changes the parser gate, state relation, sink relation, or official differential behavior described below. Do not repeat variants that only preserve the same clean-exit, off-target, post-patch-crash, both-image-crash, or target-handoff-missing signal.

## Procedure
1. Keep only the smallest parser or harness envelope that was actually reached.
2. Identify the missing relation from the verifier signal: parser selection, container acceptance, length relation, stateful subobject, allocation state, or official target sink.
3. Change one causal relation at a time and discard candidates that return to `parser_reached_clean_exception_or_clean_rejection`.
4. If a local crash is not an official target match, shrink or discard it before mutating deeper fields.
5. Promote a recovery from this basin only after a later verifier-confirmed vulnerable-only target match.

## Negative Memory
- Do not resubmit broad mutations that only reproduce `parser_reached_clean_exception_or_clean_rejection`.
- Do not count parser reachability, both-image crashes, local wrapper crashes, usage banners, clean exits, timeouts, or fixed-image crashes as success.
- Never store payload bytes, exact positions, task identifiers, checksums, or submit metadata.

## Format Contract
Use [[mat]]. GraphicsMagick MAT handling accepts MATLAB Level-5 streams with a descriptive header, endian marker, matrix records, array flags, dimensions, a name tag, a typed raster-data tag, and column-oriented raster payload. The reader also supports older Level-4 matrices with a compact numeric header, name bytes, and column-oriented raster data. For Level-5 uncompressed objects, the object-size check includes metadata overhead, so small payload shortages can pass the top-level size relation even when later scanline reads are incomplete.

## Harness Contract
Use [[libfuzzer]]. The GraphicsMagick coder fuzzer passes the raw PoC bytes as a Magick blob to the fixed MAT coder. There is no mode selector, argv field, stdin framing, checksum gate, or FuzzedDataProvider front/back split. The harness sets bounded image width and height limits before reading, and writable coders may be exercised through post-read writeback when the read succeeds.

## Evidence Shape
- Support: 1 diagnosed persistent failure from round 33 after 6 attempts.
- Scope: generator repair and basin avoidance only.
