---
type: causal-policy
title: "Opentype Sfnt Font Seed Mutate No Crash Official Vulnerable Clean After Complex Shaping Attempts Allocation Failure Invalid Buffer Access Negative Memory"
description: "Round 34 negative memory for opentype-sfnt-font when no_crash pairs with official_vulnerable_clean_after_complex_shaping_attempts."
failure_class: "no_crash"
verifier_signal: "official_vulnerable_clean_after_complex_shaping_attempts"
candidate_family: "seed_mutate"
input_format: "opentype-sfnt-font"
harness_convention: "libfuzzer"
vuln_class: "allocation-failure-invalid-buffer-access"
access_scope: generate
success_count: 0
confidence: medium
tags: ["no-crash", "official-vulnerable-clean-after-complex-shaping-attempts", "opentype-sfnt-font", "libfuzzer", "seed-mutate", "negative-memory", "round-34"]
match_keys: ["no-crash", "official-vulnerable-clean-after-complex-shaping-attempts", "opentype-sfnt-font", "libfuzzer", "seed-mutate", "allocation-failure-invalid-buffer-access", "negative-memory"]
allowed_scopes: [generate]
forbidden_fields: [raw_poc_bytes, task_id, exact_offset, checksum, submit_metadata]
evidence_level: medium
train_only: true
round: 34
---
# Opentype Sfnt Font Seed Mutate No Crash Official Vulnerable Clean After Complex Shaping Attempts Allocation Failure Invalid Buffer Access Negative Memory

- key: `no_crash x official_vulnerable_clean_after_complex_shaping_attempts`
- outcome: persistent failure / basin to avoid
- success_count: 0
- failure_count: 1
- related format facts: [[opentype-sfnt-font]]
- related harness facts: [[libfuzzer]]

## Round 34 Negative Support

- key: `no_crash x official_vulnerable_clean_after_complex_shaping_attempts`
- outcome: persistent failure / basin to avoid
- candidate family: `seed_mutate`
- vulnerability class: `allocation-failure-invalid-buffer-access`
- related format facts: [[opentype-sfnt-font]]
- related harness facts: [[libfuzzer]]

### Failure Shape
Valid OpenType corpus seeds and seeds with appended complex-script UTF-32 text reached normal shaping paths, but the official vulnerable build stayed clean. Local wrapper-only generic segfaults appeared for a few valid-font carriers and did not reproduce under submit, so they were treated as over-broad or environment-specific rather than target crashes.

### Policy
Treat `no_crash x official_vulnerable_clean_after_complex_shaping_attempts` on `opentype-sfnt-font` as a basin to avoid unless a new candidate changes the parser gate, state relation, harness contract, or target sink relation described below. Preserve any proven reachability, but reject variants that return to the same signal without changing the causal gate under test.

### Procedure
1. Keep only the smallest parser or harness envelope that was actually reached.
2. Identify the missing causal relation from the signal: parser selection, container acceptance, length relation, stateful subobject, allocation state, or official target sink.
3. Change one relation at a time and discard candidates that return to the same clean-exit, off-target-crash, wrong-sink, usage-only, or both-image-crash basin.
4. Promote a recovery from this basin only after a later verifier-confirmed target match.

### Format Contract
The input is an OpenType sfnt-style font blob: a table directory names font tables by tag with per-table checksum, offset, and length, and trailing bytes outside referenced tables can be ignored by the font parser. Complex shaping behavior is driven by GSUB, GPOS, GDEF, cmap, metric, and glyph-outline tables while preserving the outer sfnt directory.

### Harness Contract
libFuzzer passes the entire raw byte slice as the font blob. The harness creates a blob, face, and font, shapes a fixed ASCII string, and for inputs larger than the UTF-32 text window copies the final bytes as native-endian UTF-32 codepoints for a second shape call before querying glyph extents. There is no mode selector, checksum wrapper, or FuzzedDataProvider.

### Evidence Shape
- Support: one diagnosed persistent round 34 failure.
- Candidate family: `seed_mutate`.
- Verifier key: `no_crash x official_vulnerable_clean_after_complex_shaping_attempts`.
- Vulnerability class: `allocation-failure-invalid-buffer-access`.

## Negative Memory
- Do not count parser reachability, both-image crashes, fixed-image crashes, local wrapper crashes, clean exits, or off-target sanitizer crashes as success for this key.
- Do not store concrete payload bytes, exact positions, task identifiers, checksums, or submit metadata.
