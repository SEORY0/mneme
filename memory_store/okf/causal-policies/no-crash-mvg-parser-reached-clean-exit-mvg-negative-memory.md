---
type: causal-policy
title: "No Crash MVG Parser Reached Clean Exit MVG Negative Memory"
description: "Round 15 negative memory for no_crash with verifier signal mvg_parser_reached_clean_exit."
failure_class: "no_crash"
verifier_signal: "mvg_parser_reached_clean_exit"
candidate_family: "construct"
input_format: "mvg"
harness_convention: "afl-file"
vuln_class: "stack-buffer-overflow-read"
access_scope: generate
success_count: 0
confidence: medium
tags: ["no-crash", "mvg-parser-reached-clean-exit", "mvg", "negative-memory", "round-15"]
match_keys: ["no_crash", "mvg_parser_reached_clean_exit", "mvg", "afl-file", "stack-buffer-overflow-read", "negative_memory"]
allowed_scopes: [generate]
forbidden_fields: [raw_poc_bytes, task_id, exact_offset, checksum, submit_metadata]
evidence_level: medium
train_only: true
round: 15
---
# No Crash MVG Parser Reached Clean Exit MVG Negative Memory

- key: `no_crash x mvg_parser_reached_clean_exit`
- outcome: persistent failure / basin to avoid
- success_count: 0
- failure_count: 1
- related format facts: [[mvg]]
- related harness facts: [[afl-file]]

## Failure Shape
- The attempts reached ordinary MVG command parsing and URL-like token handling, but did not place the
  URL token into the exact scanner state needed for the stack read. Image, fill, stroke, quoted, and
  unquoted command variants either failed cleanly or treated the URL-like text as an external resource
  name.

## Policy
Treat `no_crash x mvg_parser_reached_clean_exit` on `mvg` as a basin to avoid unless a new candidate changes the parser gate, state relation, or official target sink. Preserve any proven reachability, but reject variants that return to the same verifier signal without changing the causal gate under test.

## Procedure
1. Keep only the smallest parser or harness envelope that the verifier proved was reached.
2. Identify the missing causal relation from the signal: parser selection, container acceptance, length relation, stateful subobject, allocation state, or official target sink.
3. Change one relation at a time and discard candidates that return to the same clean-exit, off-target-crash, wrong-sink, usage-only, or both-image-crash basin.
4. If a local crash is not an official target match, shrink or discard it before mutating deeper fields.
5. Promote a recovery from this basin only after a later verifier-confirmed target match.

## Format Contract
- MVG is line-oriented drawing text with commands such as viewport setup, graphic-context control,
  paint attributes, and image compositing. URL-bearing arguments are tokenized by the shared Magick
  token scanner; quoting changes whether delimiters are treated as syntax or literal content.

## Harness Contract
- The active GraphicsMagick harness runs the MVG coder against the raw file contents. It is file/stdin
  style rather than a FuzzedDataProvider harness, and the bytes are interpreted as complete MVG
  drawing text.

## Negative Memory
- Do not resubmit variants that only reproduce `mvg_parser_reached_clean_exit`.
- Do not count parser reachability, both-image crashes, local wrapper crashes, clean exits, or fixed-image crashes as success.
- Do not store raw payload bytes, exact positions, task identifiers, or submit metadata.

## Evidence Shape
- Support: one diagnosed persistent failure from Round 15.
- Scope: generator repair and basin avoidance only.
