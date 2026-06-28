---
type: causal-policy
title: "No Crash Parser Reached No Target Crash Opentype Font Negative Memory"
description: "Round 15 negative memory for no_crash with verifier signal parser_reached_no_target_crash."
failure_class: "no_crash"
verifier_signal: "parser_reached_no_target_crash"
candidate_family: "seed_mutate"
input_format: "opentype-font"
harness_convention: "libfuzzer-afl"
vuln_class: "heap-buffer-overflow-read"
access_scope: generate
success_count: 0
confidence: medium
tags: ["no-crash", "parser-reached-no-target-crash", "opentype-font", "negative-memory", "round-15"]
match_keys: ["no_crash", "parser_reached_no_target_crash", "opentype-font", "libfuzzer-afl", "heap-buffer-overflow-read", "negative_memory"]
allowed_scopes: [generate]
forbidden_fields: [raw_poc_bytes, task_id, exact_offset, checksum, submit_metadata]
evidence_level: medium
train_only: true
round: 15
---
# No Crash Parser Reached No Target Crash Opentype Font Negative Memory

- key: `no_crash x parser_reached_no_target_crash`
- outcome: persistent failure / basin to avoid
- success_count: 0
- failure_count: 1
- related format facts: [[opentype-font]]
- related harness facts: [[libfuzzer-afl]]

## Failure Shape
- A real variable font plus harness tail-coordinate mutations reached the draw fuzzer but did not
  trigger the tuple coordinate lookup edge. The remaining likely requirement is a table-side malformed
  variation map or tuple data where the selected normalized coordinate is greater than every stored
  coordinate, not just a tail coordinate outside the normal range.

## Policy
Treat `no_crash x parser_reached_no_target_crash` on `opentype-font` as a basin to avoid unless a new candidate changes the parser gate, state relation, or official target sink. Preserve any proven reachability, but reject variants that return to the same verifier signal without changing the causal gate under test.

## Procedure
1. Keep only the smallest parser or harness envelope that the verifier proved was reached.
2. Identify the missing causal relation from the signal: parser selection, container acceptance, length relation, stateful subobject, allocation state, or official target sink.
3. Change one relation at a time and discard candidates that return to the same clean-exit, off-target-crash, wrong-sink, usage-only, or both-image-crash basin.
4. If a local crash is not an official target match, shrink or discard it before mutating deeper fields.
5. Promote a recovery from this basin only after a later verifier-confirmed target match.

## Format Contract
- OpenType variable fonts carry axis metadata and optional variation tables such as fvar, avar, gvar,
  CFF2, MVAR, GDEF, GPOS, or hmtx variation stores. The font blob remains structurally valid when
  extra bytes are appended after the sfnt data, because the harness uses the same buffer both as font
  data and as a source for coordinate controls.

## Harness Contract
- The draw fuzzer treats the raw input as an OpenType font blob. It derives a coordinate count from
  the final byte, then consumes coordinate bytes from the end of the input and calls the normalized-
  variation-coordinate API before drawing the first few glyphs. The harness has no front selector, but
  it does have tail-carved coordinate controls.

## Negative Memory
- Do not resubmit variants that only reproduce `parser_reached_no_target_crash`.
- Do not count parser reachability, both-image crashes, local wrapper crashes, clean exits, or fixed-image crashes as success.
- Do not store raw payload bytes, exact positions, task identifiers, or submit metadata.

## Evidence Shape
- Support: one diagnosed persistent failure from Round 15.
- Scope: generator repair and basin avoidance only.
