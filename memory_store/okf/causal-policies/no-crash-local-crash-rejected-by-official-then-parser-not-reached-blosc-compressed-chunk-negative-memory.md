---
type: causal-policy
title: "No Crash Local Crash Rejected By Official Then Parser Not Reached Blosc Compressed Chunk Negative Memory"
description: "Round 16 negative memory for no_crash with verifier signal local_crash_rejected_by_official_then_parser_not_reached."
failure_class: "no_crash"
verifier_signal: "local_crash_rejected_by_official_then_parser_not_reached"
candidate_family: "construct|seed_mutate"
input_format: "blosc-compressed-chunk"
harness_convention: "libfuzzer"
vuln_class: "out-of-bounds-read"
access_scope: generate
success_count: 0
confidence: medium
tags: ["no-crash", "local-crash-rejected-by-official-then-parser-not-reached", "blosc-compressed-chunk", "negative-memory", "round-16"]
match_keys: ["no_crash", "local_crash_rejected_by_official_then_parser_not_reached", "blosc-compressed-chunk", "libfuzzer", "negative_memory"]
allowed_scopes: [generate]
forbidden_fields: [raw_poc_bytes, task_id, exact_offset, checksum, submit_metadata]
evidence_level: medium
train_only: true
round: 16
---
# No Crash Local Crash Rejected By Official Then Parser Not Reached Blosc Compressed Chunk Negative Memory

## Policy
For `no_crash x local_crash_rejected_by_official_then_parser_not_reached`, avoid replaying the observed dead end. This negative memory is co-equal with positive policies and should redirect generation before another official submission.

## Procedure
- A hand-built negative-size chunk produced only a local wrapper crash and was rejected by official submission. Real compatibility chunks and header/table perturbations remained clean, suggesting the candidate family did not satisfy the vulnerable decompression block layout while preserving the official target behavior.
- When `no_crash x local_crash_rejected_by_official_then_parser_not_reached` appears for `blosc-compressed-chunk`, treat this candidate family as a basin-to-avoid rather than as evidence of proximity to the target.
- Keep any proven parser/harness envelope, but change the missing gate or state relation before submitting again.

## Format Contract
- A Blosc chunk has a compact header carrying version/codec flags, type size, uncompressed size, block size and compressed size, followed by block metadata and compressed block data. Header total-size consistency matters; malformed compressed-size markers can crash locally without being an official target match.
- Harness: The harness feeds the raw file bytes directly to the Blosc decompression fuzzer. There is no leading mode byte or datasource envelope; parser reach depends on a self-consistent chunk header and enough block/table data for the decompressor selected by the header.

## Negative Memory
- Do not treat this verifier signal as a near miss unless a later candidate changes the missing gate or state relation.
- Do not submit candidates that are clean, parser-mismatched, off-target, or crashing both fixed and vulnerable images in this same shape.
- Preserve only descriptive format facts from the failed attempt; do not promote an unverified causal recovery.

## Evidence Shape
- Support: one diagnosed persistent failure from round 16.
- Scope: generator avoidance for the same failure-keyed basin.
