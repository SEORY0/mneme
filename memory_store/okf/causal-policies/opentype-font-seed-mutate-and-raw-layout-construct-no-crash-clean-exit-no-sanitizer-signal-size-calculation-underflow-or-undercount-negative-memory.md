---
type: causal-policy
title: "Opentype Font Seed Mutate And Raw Layout Construct No Crash Clean Exit No Sanitizer Signal Size Calculation Underflow Or Undercount Negative Memory"
description: "Negative memory for opentype-font candidates that ended in no_crash with verifier signal clean_exit_no_sanitizer_signal."
failure_class: "no_crash"
verifier_signal: "clean_exit_no_sanitizer_signal"
candidate_family: "seed_mutate_and_raw_layout_construct"
input_format: "opentype-font"
harness_convention: "afl-compatible-libfuzzer-harfbuzz-subset"
vuln_class: "size-calculation-underflow-or-undercount"
access_scope: generate
success_count: 0
confidence: medium
tags: ["no-crash", "clean-exit-no-sanitizer-signal", "opentype-font", "afl-compatible-libfuzzer-harfbuzz-subset", "seed-mutate-and-raw-layout-construct", "size-calculation-underflow-or-undercount", "negative-memory", "round-32"]
match_keys: ["no-crash", "clean-exit-no-sanitizer-signal", "opentype-font", "afl-compatible-libfuzzer-harfbuzz-subset", "seed-mutate-and-raw-layout-construct", "size-calculation-underflow-or-undercount", "negative-memory"]
allowed_scopes: [generate]
forbidden_fields: [raw_poc_bytes, task_id, exact_offset, checksum, submit_metadata]
evidence_level: medium
train_only: true
round: 32
---
# Opentype Font Seed Mutate And Raw Layout Construct No Crash Clean Exit No Sanitizer Signal Size Calculation Underflow Or Undercount Negative Memory

- key: `no_crash x clean_exit_no_sanitizer_signal`
- outcome: persistent diagnosed failure
- success_count: 0
- related format facts: [[opentype-font]]
- related harness facts: [[afl-compatible-libfuzzer-harfbuzz-subset]]

## Policy
Treat `no_crash x clean_exit_no_sanitizer_signal` for `[[opentype-font]]` under `[[afl-compatible-libfuzzer-harfbuzz-subset]]` as a dead-end basin until new evidence changes the verifier signal. Preserve only parser-recognition facts, then change the missing relation named by the diagnosis.

## Procedure
1. Keep any envelope property that reached the parser or clean execution, but stop repeating the same carrier shape.
2. Avoid the observed dead end: The full-font parser and subset harness accepted ordinary OpenType seeds and packaged subset-corpus fixtures, but no sanitizer signal appeared. Mutations that preserved the SFNT envelope and targeted OpenType layout array sizing in ScriptList/Script structures stayed clean, including high-level font-writer variants and a raw GSUB table replacement. The likely missing condition is a narrower serializer state or downstream use of the undercounted serialized layout object, not a simple parser gate, font checksum, or script-record count mutation.
3. Rebuild around `[[opentype-font]]` and `[[afl-compatible-libfuzzer-harfbuzz-subset]]`, targeting the missing gate or state relation rather than padding, broad corruption, or unrelated seed churn.
4. Submit only after local verification produces a vulnerable-build crash or a plausible parser-branch wrong-sink crash; clean exits under this signal are not submit candidates.

## Format Contract
- The input is a complete SFNT/OpenType font blob with a table directory and tagged table records. The relevant layout tables are GSUB and GPOS; their top-level headers point to ScriptList, FeatureList, and LookupList subtables. ScriptList contains records with script tags and relative offsets to Script subtables; Script subtables contain an optional default LangSys and a LangSysRecord array. The vulnerable macro candidates in this source family include structures where a trailing array is wider than its count field, so the computed serialized size can undercount the true fixed prefix plus records. A valid outer SFNT directory and coherent layout-table offsets are necessary; isolated GSUB bytes are not sufficient.

## Harness Contract
- The active target is the HarfBuzz subset fuzzer. It reads the PoC as raw font bytes through an AFL-compatible libFuzzer-style wrapper; there is no leading mode selector and no FuzzedDataProvider split. The harness creates an hb_blob and hb_face from the entire input, then runs subsetting over fixed codepoints and, for sufficiently large inputs, also over trailing UTF-32 codepoints copied from the end of the same buffer. The same bytes are still treated as the font blob, so any trailer must not destroy the font envelope.

## Negative Memory
- Do not store concrete payload bytes, task identifiers, exact positions, checksums, or submit metadata.
- Do not treat parser reachability alone as success without the official target-match signal.
- Do not repeat a clean-exit or both-image-crash basin once the verifier has characterized it.

## Evidence Shape
- Support: one diagnosed Round 32 failed solve attempt.
- Attempts observed: 13.
