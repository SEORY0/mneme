---
type: causal-policy
title: "No Crash Parser Reached Clean Exit Wpg Heap Buffer Overflow Negative Memory"
description: "Negative memory for persistent no_crash / parser_reached_clean_exit basin."
failure_class: "no_crash"
verifier_signal: "parser_reached_clean_exit"
candidate_family: "construct+seed_mutate+bounded_sweep"
input_format: "wpg"
harness_convention: "libfuzzer"
vuln_class: "heap-buffer-overflow"
access_scope: generate
success_count: 0
confidence: medium
tags: ["no-crash", "construct-seed-mutate-bounded-sweep", "wpg", "heap-buffer-overflow", "negative-memory"]
match_keys: ["no-crash", "parser-reached-clean-exit", "wpg", "libfuzzer", "heap-buffer-overflow", "negative-memory"]
allowed_scopes: [generate]
forbidden_fields: [raw_poc_bytes, task_id, exact_offset, checksum, submit_metadata]
evidence_level: medium
train_only: true
provenance: round-35-consolidator
---
# No Crash Parser Reached Clean Exit Wpg Heap Buffer Overflow Negative Memory

## Policy
For `no_crash` with verifier signal `parser_reached_clean_exit` on `wpg` under `libfuzzer`, treat the recorded family as a basin to avoid until a later verifier-confirmed candidate flips the gate. Preserve the descriptive format/harness facts, but do not promote this into a recovery policy.

## Avoided Basin
- The WPG parser was reached, but the tested hypotheses all exited cleanly in the vulnerable build.
- Distinct attempts covered a corrected WPG header/data-offset contract, WPG1 bitmap records with degenerate depth and empty or truncated raster data, WPG1 palette/count variants, WPG1 type-2 seed mutations with enabled rotation and stressed geometry, WPG2 compressed bitmap row over-expansion past the declared height, and a bounded parameter sweep over level-1 bitmap dimensions, bit depths, and RLE token families.
- The likely missing condition is a narrower row-import failure that leaves the RLE decoder continuing after InsertRow reports failure, but the attempted over-expansion and EOF paths did not reproduce the sanitizer failure.

## Recovery Direction
- Keep the parser/harness reachability facts in [[wpg]] and [[libfuzzer]].
- Retarget away from the failed relation named by `parser_reached_clean_exit`; require vulnerable-only official confirmation before promoting any replacement.

## Evidence Shape
- Support: one round 35 persistent failure with concrete diagnosis and no official target match.
