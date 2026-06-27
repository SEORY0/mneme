---
type: causal-policy
title: "No Crash Parser Not Reached Or Subset Path Not Triggered Opentype Font Negative Memory"
description: "Round 20 negative memory for no_crash with verifier signal parser_not_reached_or_subset_path_not_triggered."
failure_class: "no_crash"
verifier_signal: "parser_not_reached_or_subset_path_not_triggered"
candidate_family: "construct"
input_format: "opentype-font"
harness_convention: "libfuzzer-harfbuzz-subset"
vuln_class: "stack-use-after-return"
access_scope: generate
success_count: 0
confidence: medium
tags: ["no-crash", "parser-not-reached-or-subset-path-not-triggered", "opentype-font", "negative-memory", "round-20"]
match_keys: ["no-crash", "parser-not-reached-or-subset-path-not-triggered", "opentype-font"]
allowed_scopes: [generate]
forbidden_fields: [raw_poc_bytes, task_id, exact_offset, checksum, submit_metadata]
evidence_level: medium
train_only: true
round: 20
---
# No Crash Parser Not Reached Or Subset Path Not Triggered Opentype Font Negative Memory

- key: `no_crash x parser_not_reached_or_subset_path_not_triggered`
- outcome: persistent failure basin to avoid
- success_count: 0
- failure_count: 1
- formats: [[opentype-font]]
- harnesses: [[libfuzzer-harfbuzz-subset]]

## Dead End
The round 20 attempts for `opentype-font` under `libfuzzer-harfbuzz-subset` did not produce a verified target match. Do not promote these attempts into positive recovery without a future server-verified solve.

## Diagnosed Basin
- The harness accepted raw font bytes and reached the subset fuzzer, but minimal SFNT carriers with sparse GSUB data did not form a valid substitution table that exercises SingleSubstFormat1 serialization. The useful path likely needs a well-formed font with a valid coverage table and glyph mapping that survives subsetting.

## Negative Policy
When retrieval matches `no_crash x parser_not_reached_or_subset_path_not_triggered`, avoid repeating this basin. First re-check the harness contract, format gate, and sink-specific dispatch condition. If the candidate only produces clean execution, wrapper-only crashes, off-target crashes, or an unverified recon state, retarget the carrier or abandon this family rather than scaling the same mutation.

## Retarget Hints
- Preserve factual format and harness gates from [[opentype-font]] and [[libfuzzer-harfbuzz-subset]].
- Prefer a different dispatch route or seed family unless new verifier feedback shows the target path is reached.
- Treat generic local crashes, clean exits, and `not_verified` recon states as non-success until official vulnerable-versus-fixed confirmation.

## Evidence Shape
- Support: 1 round 20 failed trace(s) with concrete diagnosis.
- Scope: generator avoidance only.
