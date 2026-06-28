---
type: causal-policy
title: "No Crash Local Only Crash Not Official Blosc Chunk Negative Memory"
description: "Round 16 negative memory for no_crash with verifier signal local_only_crash_not_official."
failure_class: "no_crash"
verifier_signal: "local_only_crash_not_official"
candidate_family: "construct"
input_format: "blosc chunk"
harness_convention: "libfuzzer"
vuln_class: "miniz distance-copy uninitialized-value"
access_scope: generate
success_count: 0
confidence: medium
tags: ["no-crash", "local-only-crash-not-official", "blosc-chunk", "negative-memory", "round-16"]
match_keys: ["no_crash", "local_only_crash_not_official", "blosc chunk", "libfuzzer", "negative_memory"]
allowed_scopes: [generate]
forbidden_fields: [raw_poc_bytes, task_id, exact_offset, checksum, submit_metadata]
evidence_level: medium
train_only: true
round: 16
---
# No Crash Local Only Crash Not Official Blosc Chunk Negative Memory

## Policy
For `no_crash x local_only_crash_not_official`, avoid replaying the observed dead end. This negative memory is co-equal with positive policies and should redirect generation before another official submission.

## Procedure
- A self-consistent one-block Blosc chunk with a zlib stream reached local decompression and some malformed deflate streams produced local crashes, but official submit ran the vulnerable image cleanly. The successful condition likely needs a deflate distance-copy sequence that is accepted far enough by miniz under the official build rather than malformed streams that collapse into local wrapper artifacts.
- When `no_crash x local_only_crash_not_official` appears for `blosc chunk`, treat this candidate family as a basin-to-avoid rather than as evidence of proximity to the target.
- Keep any proven parser/harness envelope, but change the missing gate or state relation before submitting again.

## Format Contract
- A compact Blosc chunk starts with version, codec flags, type size, uncompressed size, block size, and total compressed size, followed by block-start entries and per-block stream records. For zlib-backed chunks the high codec flag selects the zlib/miniz format; a no-split flag can reduce a block to one stream. The header compressed size must equal the full input length.
- Harness: The decompression fuzzer consumes raw chunk bytes. It rejects short inputs, rejects a header compressed size different from the file size, rejects zero uncompressed size, validates the compressed buffer, allocates an output buffer, then calls Blosc decompression.

## Negative Memory
- Do not treat this verifier signal as a near miss unless a later candidate changes the missing gate or state relation.
- Do not submit candidates that are clean, parser-mismatched, off-target, or crashing both fixed and vulnerable images in this same shape.
- Preserve only descriptive format facts from the failed attempt; do not promote an unverified causal recovery.

## Evidence Shape
- Support: one diagnosed persistent failure from round 16.
- Scope: generator avoidance for the same failure-keyed basin.
