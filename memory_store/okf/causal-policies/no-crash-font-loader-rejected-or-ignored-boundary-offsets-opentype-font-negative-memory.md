---
type: causal-policy
title: "No Crash Font Loader Rejected Or Ignored Boundary Offsets Opentype Font Negative Memory"
description: "Round 20 negative memory for no_crash with verifier signal font_loader_rejected_or_ignored_boundary_offsets."
failure_class: "no_crash"
verifier_signal: "font_loader_rejected_or_ignored_boundary_offsets"
candidate_family: "seed_mutate"
input_format: "opentype-font"
harness_convention: "libfuzzer"
vuln_class: "out-of-bounds-read-or-assertion"
access_scope: generate
success_count: 0
confidence: medium
tags: ["no-crash", "font-loader-rejected-or-ignored-boundary-offsets", "opentype-font", "negative-memory", "round-20"]
match_keys: ["no-crash", "font-loader-rejected-or-ignored-boundary-offsets", "opentype-font"]
allowed_scopes: [generate]
forbidden_fields: [raw_poc_bytes, task_id, exact_offset, checksum, submit_metadata]
evidence_level: medium
train_only: true
round: 20
---
# No Crash Font Loader Rejected Or Ignored Boundary Offsets Opentype Font Negative Memory

- key: `no_crash x font_loader_rejected_or_ignored_boundary_offsets`
- outcome: persistent failure basin to avoid
- success_count: 0
- failure_count: 1
- formats: [[opentype-font]]
- harnesses: [[libfuzzer]]

## Dead End
The round 20 attempts for `opentype-font` under `libfuzzer` did not produce a verified target match. Do not promote these attempts into positive recovery without a future server-verified solve.

## Diagnosed Basin
- Mutating a valid font seed so table-directory offsets or selected cmap subtable offsets landed exactly at the file boundary did not crash. Required-table zero-length boundary variants were also rejected or returned cleanly during initial font loading, so the triggering offset likely lives in a later-used substructure or a color/bitmap table not covered by the small TTF seed.

## Negative Policy
When retrieval matches `no_crash x font_loader_rejected_or_ignored_boundary_offsets`, avoid repeating this basin. First re-check the harness contract, format gate, and sink-specific dispatch condition. If the candidate only produces clean execution, wrapper-only crashes, off-target crashes, or an unverified recon state, retarget the carrier or abandon this family rather than scaling the same mutation.

## Retarget Hints
- Preserve factual format and harness gates from [[opentype-font]] and [[libfuzzer]].
- Prefer a different dispatch route or seed family unless new verifier feedback shows the target path is reached.
- Treat generic local crashes, clean exits, and `not_verified` recon states as non-success until official vulnerable-versus-fixed confirmation.

## Evidence Shape
- Support: 1 round 20 failed trace(s) with concrete diagnosis.
- Scope: generator avoidance only.
