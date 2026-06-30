---
type: negative-memory
title: "No Crash Parser Reached Clean Or Usage Only Opentype Font Seed Mutate Lookup Sanitizer Invalid Access Negative Memory"
description: "Round 26 negative memory for no_crash with verifier signal parser_reached_clean_or_usage_only."
failure_class: "no_crash"
verifier_signal: "parser_reached_clean_or_usage_only"
candidate_family: "seed_mutate"
input_format: "opentype-font"
harness_convention: "honggfuzz-compatible one-input HarfBuzz shape fuzzer"
vuln_class: "lookup-sanitizer-invalid-access"
access_scope: generate
success_count: 0
confidence: medium
tags: ["no-crash", "parser-reached-clean-or-usage-only", "opentype-font", "honggfuzz-compatible-one-input-harfbuzz-shape-fuzzer", "seed-mutate", "negative-memory", "round-26"]
match_keys: ["no_crash", "parser_reached_clean_or_usage_only", "opentype-font", "honggfuzz-compatible one-input HarfBuzz shape fuzzer", "lookup-sanitizer-invalid-access", "negative_memory"]
allowed_scopes: [generate]
forbidden_fields: [raw_poc_bytes, task_id, exact_offset, checksum, submit_metadata]
evidence_level: medium
train_only: true
round: 26
---
# No Crash Parser Reached Clean Or Usage Only Opentype Font Seed Mutate Lookup Sanitizer Invalid Access Negative Memory

- key: `no_crash x parser_reached_clean_or_usage_only`
- outcome: persistent failure / basin to avoid
- success_count: 0
- failure_count: 1
- related format facts: [[opentype-font]]
- related harness facts: [[honggfuzz-compatible-one-input-harfbuzz-shape-fuzzer]]

## Failure Shape
Real OpenType Extension-lookup seeds and synthetic appended layout tables preserved the sfnt envelope and targeted zero-count, null-offset, and absent-subtable variants. In this build those mutations exited cleanly; the zero-length array access appears to fall into HarfBuzz null-object handling rather than producing a sanitizer-visible invalid access under the shape harness.

## Policy
Treat `no_crash x parser_reached_clean_or_usage_only` on `opentype-font` as a basin to avoid unless a new candidate changes the parser gate, state relation, or sink relation described below. Preserve any proven reachability, but reject variants that return to the same clean-exit, off-target-crash, wrong-sink, usage-only, wrapper-mismatch, or both-image-crash basin.

## Procedure
1. Keep only the smallest parser or harness envelope that was actually reached.
2. Identify the missing causal relation from the signal: parser selection, container acceptance, length relation, stateful subobject, allocation state, or official target sink.
3. Change one relation at a time and discard candidates that return to the same `parser_reached_clean_or_usage_only` basin.
4. If a local crash is not an official target match, shrink or discard it before mutating deeper fields.
5. Promote a recovery from this basin only after a later verifier-confirmed target match.

## Negative Memory
- Do not resubmit broad mutations that only reproduce `parser_reached_clean_or_usage_only`.
- Do not count parser reachability, both-image crashes, local wrapper crashes, usage banners, clean exits, or fixed-image crashes as success.
- Never store raw payload bytes, exact positions, task identifiers, checksums, or submit metadata.

## Format Contract
The input is a complete sfnt/OpenType font. The sfnt directory maps table tags to checksummed table records with offsets and lengths. GSUB/GPOS layout tables contain ScriptList, FeatureList, and LookupList offsets; a lookup record has a lookup type, lookup flags, a subtable-count field, and an array of relative subtable offsets. Extension lookup types are used in GSUB and GPOS to wrap an extension subtable whose own body names the underlying lookup type and an offset to the target subtable.

## Harness Contract
The wrapper runs the HarfBuzz shape fuzzer on the PoC path. The fuzzer creates an hb_face and hb_font from the whole input, shapes fixed ASCII and UTF-32 text, and uses trailing bytes as variation/text controls when enough data is present. There is no leading mode selector or FuzzedDataProvider layout; the primary gate is a valid OpenType font blob.

## Evidence Shape
- Support: 1 diagnosed persistent failure from round 26 after 5 attempts.
- Scope: generator repair and basin avoidance only.
