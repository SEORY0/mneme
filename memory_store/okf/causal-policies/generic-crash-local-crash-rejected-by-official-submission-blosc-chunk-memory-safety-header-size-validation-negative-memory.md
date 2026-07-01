---
type: causal-policy
title: "Generic Crash Local Crash Rejected By Official Submission Blosc Chunk Memory Safety Header Size Validation Negative Memory"
description: "Negative memory for persistent generic_crash / local_crash_rejected_by_official_submission basin."
failure_class: "generic_crash"
verifier_signal: "local_crash_rejected_by_official_submission"
candidate_family: "construct_and_seed_mutate"
input_format: "blosc-chunk"
harness_convention: "libfuzzer"
vuln_class: "memory-safety-header-size-validation"
access_scope: generate
success_count: 0
confidence: medium
tags: ["generic-crash", "construct-and-seed-mutate", "blosc-chunk", "memory-safety-header-size-validation", "negative-memory"]
match_keys: ["generic-crash", "local-crash-rejected-by-official-submission", "blosc-chunk", "libfuzzer", "memory-safety-header-size-validation", "negative-memory"]
allowed_scopes: [generate]
forbidden_fields: [raw_poc_bytes, task_id, exact_offset, checksum, submit_metadata]
evidence_level: medium
train_only: true
provenance: round-35-consolidator
---
# Generic Crash Local Crash Rejected By Official Submission Blosc Chunk Memory Safety Header Size Validation Negative Memory

## Policy
For `generic_crash` with verifier signal `local_crash_rejected_by_official_submission` on `blosc-chunk` under `libfuzzer`, treat the recorded family as a basin to avoid until a later verifier-confirmed candidate flips the gate. Preserve the descriptive format/harness facts, but do not promote this into a recovery policy.

## Avoided Basin
- The raw chunk gates were satisfied in several ways, but the explored malformed header-size relations either returned cleanly, produced low-likelihood raw decoder crashes, or also crashed the fixed build.
- Distinct attempts included compact constructed chunks, signed block-start values before chunk data, block-start-table extent stress, split-stream negative compressed-size markers, shifted negative stream markers after a valid split, seed-mutated valid corpus chunks, and legacy-to-extended header-layout flips.
- I did not find a sanitizer-visible vulnerable-only relation for this shard.

## Recovery Direction
- Keep the parser/harness reachability facts in [[blosc-chunk]] and [[libfuzzer]].
- Retarget away from the failed relation named by `local_crash_rejected_by_official_submission`; require vulnerable-only official confirmation before promoting any replacement.

## Evidence Shape
- Support: one round 35 persistent failure with concrete diagnosis and no official target match.
