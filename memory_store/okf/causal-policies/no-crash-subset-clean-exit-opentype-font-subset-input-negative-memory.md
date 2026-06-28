---
type: causal-policy
title: "No Crash Subset Clean Exit Opentype Font Subset Input Negative Memory"
description: "Round 20 negative memory for no_crash with verifier signal subset_clean_exit."
failure_class: "no_crash"
verifier_signal: "subset_clean_exit"
candidate_family: "seed_replay"
input_format: "OpenType font subset input"
harness_convention: "libfuzzer harfbuzz subset"
vuln_class: "unknown subset bimap inconsistency"
access_scope: generate
success_count: 0
confidence: medium
tags: ["no-crash", "subset-clean-exit", "opentype-font-subset-input", "negative-memory", "round-20"]
match_keys: ["no-crash", "subset-clean-exit", "opentype-font-subset-input"]
allowed_scopes: [generate]
forbidden_fields: [raw_poc_bytes, task_id, exact_offset, checksum, submit_metadata]
evidence_level: medium
train_only: true
round: 20
---
# No Crash Subset Clean Exit Opentype Font Subset Input Negative Memory

- key: `no_crash x subset_clean_exit`
- outcome: persistent failure basin to avoid
- success_count: 0
- failure_count: 1
- formats: [[opentype-font-subset-input]]
- harnesses: [[libfuzzer-harfbuzz-subset]]

## Dead End
The round 20 attempts for `OpenType font subset input` under `libfuzzer harfbuzz subset` did not produce a verified target match. Do not promote these attempts into positive recovery without a future server-verified solve.

## Diagnosed Basin
- Real HarfBuzz subset test fonts reached the subset harness but exited cleanly. The unresolved trigger likely requires a malformed table relation that makes one side of an internal bimap update fail while preserving enough font validity for subsetting.

## Negative Policy
When retrieval matches `no_crash x subset_clean_exit`, avoid repeating this basin. First re-check the harness contract, format gate, and sink-specific dispatch condition. If the candidate only produces clean execution, wrapper-only crashes, off-target crashes, or an unverified recon state, retarget the carrier or abandon this family rather than scaling the same mutation.

## Retarget Hints
- Preserve factual format and harness gates from [[opentype-font-subset-input]] and [[libfuzzer-harfbuzz-subset]].
- Prefer a different dispatch route or seed family unless new verifier feedback shows the target path is reached.
- Treat generic local crashes, clean exits, and `not_verified` recon states as non-success until official vulnerable-versus-fixed confirmation.

## Evidence Shape
- Support: 1 round 20 failed trace(s) with concrete diagnosis.
- Scope: generator avoidance only.
