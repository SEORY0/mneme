---
type: causal-policy
title: "Opentype Sbix Font Seed Mutate No Crash Subset Clean Exit Offset Null Check Missing Negative Memory"
description: "Round 34 negative memory for opentype-sbix-font when no_crash pairs with subset_clean_exit."
failure_class: "no_crash"
verifier_signal: "subset_clean_exit"
candidate_family: "seed_mutate"
input_format: "opentype-sbix-font"
harness_convention: "libfuzzer"
vuln_class: "offset-null-check-missing"
access_scope: generate
success_count: 0
confidence: medium
tags: ["no-crash", "subset-clean-exit", "opentype-sbix-font", "libfuzzer", "seed-mutate", "negative-memory", "round-34"]
match_keys: ["no-crash", "subset-clean-exit", "opentype-sbix-font", "libfuzzer", "seed-mutate", "offset-null-check-missing", "negative-memory"]
allowed_scopes: [generate]
forbidden_fields: [raw_poc_bytes, task_id, exact_offset, checksum, submit_metadata]
evidence_level: medium
train_only: true
round: 34
---
# Opentype Sbix Font Seed Mutate No Crash Subset Clean Exit Offset Null Check Missing Negative Memory

- key: `no_crash x subset_clean_exit`
- outcome: persistent failure / basin to avoid
- success_count: 0
- failure_count: 1
- related format facts: [[opentype-sbix-font]]
- related harness facts: [[libfuzzer]]

## Round 34 Negative Support

- key: `no_crash x subset_clean_exit`
- outcome: persistent failure / basin to avoid
- candidate family: `seed_mutate`
- vulnerability class: `offset-null-check-missing`
- related format facts: [[opentype-sbix-font]]
- related harness facts: [[libfuzzer]]

### Failure Shape
Seed-mutating real sbix fonts reached normal font parsing and subsetting but did not produce a sanitizer signal. Nulling individual strike offsets, using a font with a narrower glyph set, expanding the strike-offset count with null entries, and driving the trailer-controlled second subset pass all completed cleanly. The missing relation is likely a null strike entry whose header-derived glyph offsets form a vulnerable copy or serialization state without being treated as a harmless empty strike.

### Policy
Treat `no_crash x subset_clean_exit` on `opentype-sbix-font` as a basin to avoid unless a new candidate changes the parser gate, state relation, harness contract, or target sink relation described below. Preserve any proven reachability, but reject variants that return to the same signal without changing the causal gate under test.

### Procedure
1. Keep only the smallest parser or harness envelope that was actually reached.
2. Identify the missing causal relation from the signal: parser selection, container acceptance, length relation, stateful subobject, allocation state, or official target sink.
3. Change one relation at a time and discard candidates that return to the same clean-exit, off-target-crash, wrong-sink, usage-only, or both-image-crash basin.
4. Promote a recovery from this basin only after a later verifier-confirmed target match.

### Format Contract
The input is an OpenType font with an SFNT table directory and an sbix table. The sbix table contains a version, flags, a strike count, a strike-offset array, and strike records. Each strike has PPEM/resolution fields followed by a glyph-offset array; glyph data ranges are derived from adjacent offsets and must pass monotonicity and available-length checks during subsetting.

### Harness Contract
The libFuzzer target treats the entire input as a font blob. It always performs one subset with a fixed built-in text set, and if the file is long enough it performs a second subset using a trailing flags byte and a fixed-size native-endian codepoint array read from the end. There is no separate file-format wrapper or leading selector byte.

### Evidence Shape
- Support: one diagnosed persistent round 34 failure.
- Candidate family: `seed_mutate`.
- Verifier key: `no_crash x subset_clean_exit`.
- Vulnerability class: `offset-null-check-missing`.

## Negative Memory
- Do not count parser reachability, both-image crashes, fixed-image crashes, local wrapper crashes, clean exits, or off-target sanitizer crashes as success for this key.
- Do not store concrete payload bytes, exact positions, task identifiers, checksums, or submit metadata.
