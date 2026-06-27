---
type: causal-policy
title: "No Crash Parser Not Observed By Verifier Opentype Font Negative Memory"
description: "Round 9 negative memory for no_crash with verifier signal parser_not_observed_by_verifier."
failure_class: "no_crash"
verifier_signal: "parser_not_observed_by_verifier"
candidate_family: "seed_mutate"
input_format: "opentype-font"
harness_convention: "libfuzzer"
vuln_class: "invalid-buffer-access"
access_scope: generate
success_count: 0
confidence: medium
tags: ["no-crash", "parser-not-observed-by-verifier", "opentype-font", "negative-memory", "round-9"]
match_keys: ["no_crash", "parser_not_observed_by_verifier", "opentype-font", "libfuzzer", "invalid-buffer-access", "negative_memory"]
allowed_scopes: [generate]
forbidden_fields: [raw_poc_bytes, task_id, exact_offset, checksum, submit_metadata]
evidence_level: medium
train_only: true
round: 9
---
# No Crash Parser Not Observed By Verifier Opentype Font Negative Memory

- key: `no_crash x parser_not_observed_by_verifier`
- outcome: persistent failure / basin to avoid
- success_count: 0
- failure_count: 1
- related format facts: [[opentype-font]]
- related harness facts: [[libfuzzer]]

## Failure Shape
- Real HarfBuzz shaping-font seeds parsed and shaped successfully but did not reach the OOM-only
  invalid-buffer-access condition.
- No reliable table mutation was identified that both preserves enough OpenType structure for
  shaping and forces the intended allocation-failure path.

## Policy
Treat `no_crash x parser_not_observed_by_verifier` on `opentype-font` as a basin to avoid unless a new candidate changes the parser gate, state relation, or official target sink. Preserve any proven reachability, but reject variants that return to the same verifier signal without changing the causal gate under test.

## Procedure
1. Keep only the smallest parser or harness envelope that the verifier proved was reached.
2. Identify the missing causal relation from the signal: parser selection, container acceptance, length relation, stateful subobject, allocation state, or official target sink.
3. Change one relation at a time and discard candidates that return to the same clean-exit, off-target-crash, wrong-sink, usage-only, or both-image-crash basin.
4. If a local crash is not an official target match, shrink or discard it before mutating deeper fields.
5. Promote a recovery from this basin only after a later verifier-confirmed target match.

## Format Contract
- The target accepts raw OpenType/TrueType font bytes.
- Valid fonts need a normal sfnt table directory and shaping-relevant tables such as cmap/glyf or
  CFF plus metrics/layout tables; corrupting table offsets or lengths too broadly tends to be
  sanitized away before shaping.

## Harness Contract
- The harness wraps all input bytes in an hb_blob, creates an hb_face and hb_font, installs OpenType
  font functions, shapes a fixed ASCII string, then if the input is large enough treats the last
  bytes as UTF-32 text, shapes that buffer too, and queries glyph extents for each shaped glyph.
- There is no input carving other than the final UTF-32 text reuse.

## Negative Memory
- Do not resubmit broad mutations that only reproduce `parser_not_observed_by_verifier`.
- Do not count parser reachability, both-image crashes, local wrapper crashes, clean exits, or fixed-image crashes as success.
- Do not store raw payload bytes, exact positions, task identifiers, or submit metadata.

## Evidence Shape
- Support: one diagnosed persistent failure from round 9.
- Scope: generator repair and basin avoidance only.
