---
type: negative-memory
title: "Native Vips Image Construct Seed Replay No Crash Parser Reached Clean Exit Behavioral Truncation Or Parser Target Mismatch Negative Memory"
description: "Round 37 negative memory for no_crash with verifier signal parser_reached_clean_exit."
failure_class: "no_crash"
verifier_signal: "parser_reached_clean_exit"
candidate_family: "construct|seed_replay"
input_format: "native-vips-image"
harness_convention: "libfuzzer-jpegsave-file"
vuln_class: "behavioral-truncation-or-parser-target-mismatch"
access_scope: generate
success_count: 0
failure_count: 1
confidence: medium
tags: ["no-crash", "parser-reached-clean-exit", "native-vips-image", "libfuzzer-jpegsave-file", "construct-seed-replay", "behavioral-truncation-or-parser-target-mismatch", "negative-memory", "round-37"]
match_keys: ["no_crash", "parser_reached_clean_exit", "native-vips-image", "libfuzzer-jpegsave-file", "behavioral-truncation-or-parser-target-mismatch", "negative-memory", "construct|seed_replay"]
allowed_scopes: [generate]
forbidden_fields: [raw_poc_bytes, task_id, exact_offset, checksum, submit_metadata]
evidence_level: medium
train_only: true
round: 37
---
# Native Vips Image Construct Seed Replay No Crash Parser Reached Clean Exit Behavioral Truncation Or Parser Target Mismatch Negative Memory

- key: `no_crash x parser_reached_clean_exit`
- outcome: persistent failure / basin to avoid
- success_count: 0
- failure_count: 1
- related format facts: [[native-vips-image]]
- related harness facts: [[libfuzzer-jpegsave-file]]

## Failure Shape
The active container entrypoint exercised a libvips JPEG-save fuzz target rather than the CLI option-formatting path named in the task card. Constructed native VIPS images reached image loading and color conversion, and replayed corpus images reached accepted parser paths, but both vulnerable and confirmed fixed builds exited cleanly without a sanitizer-visible split.

## Observed Basin
- Failure trajectory classes: no_crash, no_crash, no_crash, no_crash, no_crash, no_crash.
- Official confirmation: no server target match for this basin.

## Policy
Treat `no_crash x parser_reached_clean_exit` on `native-vips-image` under `libfuzzer-jpegsave-file` as a basin to avoid unless a new candidate changes the parser gate, state relation, or sink relation described above. Preserve any proven reachability, but reject variants that return to the same clean-exit, off-target-crash, wrapper-mismatch, usage-only, timeout, or fixed-image-crash behavior.

## Procedure
1. Keep only the smallest parser or harness envelope that was actually reached.
2. Identify the missing relation from the signal: parser selection, container acceptance, length relation, stateful subobject, allocation state, or official target sink.
3. Change one relation at a time and discard candidates that return to the same `parser_reached_clean_exit` basin.
4. Promote a recovery from this basin only after a later official target match.

## Negative Memory
- Do not resubmit broad mutations that only reproduce `parser_reached_clean_exit`.
- Do not count parser reachability, both-image crashes, local wrapper crashes, clean exits, timeouts, or fixed-image crashes as success.
- Do not store payload bytes, exact positions, task identifiers, checksums, or submit metadata.

## Evidence Shape
- Support: one diagnosed persistent failure from round 37 after 6 attempts.
- Candidate family: construct|seed_replay.
- Scope: generator repair and basin avoidance only.
