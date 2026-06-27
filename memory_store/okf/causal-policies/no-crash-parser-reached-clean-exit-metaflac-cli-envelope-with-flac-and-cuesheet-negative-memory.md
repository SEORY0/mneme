---
type: causal-policy
title: "No Crash Parser Reached Clean Exit Metaflac Cli Envelope With Flac And Cuesheet Negative Memory"
description: "Round 15 negative memory for no_crash with verifier signal parser_reached_clean_exit."
failure_class: "no_crash"
verifier_signal: "parser_reached_clean_exit"
candidate_family: "seed_mutate"
input_format: "metaflac-cli-envelope-with-flac-and-cuesheet"
harness_convention: "libfuzzer-cli-envelope"
vuln_class: "heap-use-after-free"
access_scope: generate
success_count: 0
confidence: medium
tags: ["no-crash", "parser-reached-clean-exit", "metaflac-cli-envelope-with-flac-and-cuesheet", "negative-memory", "round-15"]
match_keys: ["no_crash", "parser_reached_clean_exit", "metaflac-cli-envelope-with-flac-and-cuesheet", "libfuzzer-cli-envelope", "heap-use-after-free", "negative_memory"]
allowed_scopes: [generate]
forbidden_fields: [raw_poc_bytes, task_id, exact_offset, checksum, submit_metadata]
evidence_level: medium
train_only: true
round: 15
---
# No Crash Parser Reached Clean Exit Metaflac Cli Envelope With Flac And Cuesheet Negative Memory

- key: `no_crash x parser_reached_clean_exit`
- outcome: persistent failure / basin to avoid
- success_count: 0
- failure_count: 1
- related format facts: [[metaflac-cli-envelope-with-flac-and-cuesheet]]
- related harness facts: [[libfuzzer-cli-envelope]]

## Failure Shape
- Real FLAC seeds and real cuesheet seeds were placed into the metaflac CLI envelope using stdin mode
  and the import-cuesheet option. Variants with only import, import plus automatically generated cued
  seekpoints, and many shorthand operations before or after import all executed cleanly. The likely
  missing trigger is an operation-array growth pattern or FLAC metadata layout that makes the import
  operation handle stale after the automatic add-seekpoint operation is appended.

## Policy
Treat `no_crash x parser_reached_clean_exit` on `metaflac-cli-envelope-with-flac-and-cuesheet` as a basin to avoid unless a new candidate changes the parser gate, state relation, or official target sink. Preserve any proven reachability, but reject variants that return to the same verifier signal without changing the causal gate under test.

## Procedure
1. Keep only the smallest parser or harness envelope that the verifier proved was reached.
2. Identify the missing causal relation from the signal: parser selection, container acceptance, length relation, stateful subobject, allocation state, or official target sink.
3. Change one relation at a time and discard candidates that return to the same clean-exit, off-target-crash, wrong-sink, usage-only, or both-image-crash basin.
4. If a local crash is not an official target match, shrink or discard it before mutating deeper fields.
5. Promote a recovery from this basin only after a later verifier-confirmed target match.

## Format Contract
- The underlying file is a FLAC stream with metadata blocks; the imported side input is a textual
  cuesheet containing CATALOG, FILE, TRACK, and INDEX records. Importing a cuesheet can automatically
  create seekpoint specifications for cue indices unless cued seekpoints are disabled.

## Harness Contract
- The first input byte controls the maximum number of NUL-delimited argv strings and whether stdin
  mode is used. In stdin mode the remaining bytes after argv are split in half: the first half is
  written to the temporary FLAC file and the second half is used as stdin. Without stdin mode the same
  temporary filename is appended twice to argv.

## Negative Memory
- Do not resubmit variants that only reproduce `parser_reached_clean_exit`.
- Do not count parser reachability, both-image crashes, local wrapper crashes, clean exits, or fixed-image crashes as success.
- Do not store raw payload bytes, exact positions, task identifiers, or submit metadata.

## Evidence Shape
- Support: one diagnosed persistent failure from Round 15.
- Scope: generator repair and basin avoidance only.
