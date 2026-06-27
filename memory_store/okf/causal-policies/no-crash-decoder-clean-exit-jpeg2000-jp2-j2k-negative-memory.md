---
type: causal-policy
title: "No Crash Decoder Clean Exit Jpeg2000 Jp2 J2k Negative Memory"
description: "Round 16 negative memory for no_crash with verifier signal decoder_clean_exit."
failure_class: "no_crash"
verifier_signal: "decoder_clean_exit"
candidate_family: "seed_sweep"
input_format: "jpeg2000-jp2-j2k"
harness_convention: "afl-file-openjpeg-decompress"
vuln_class: "integer-overflow-to-out-of-bounds-read"
access_scope: generate
success_count: 0
confidence: medium
tags: ["no-crash", "decoder-clean-exit", "jpeg2000-jp2-j2k", "negative-memory", "round-16"]
match_keys: ["no_crash", "decoder_clean_exit", "jpeg2000-jp2-j2k", "afl-file-openjpeg-decompress", "negative_memory"]
allowed_scopes: [generate]
forbidden_fields: [raw_poc_bytes, task_id, exact_offset, checksum, submit_metadata]
evidence_level: medium
train_only: true
round: 16
---
# No Crash Decoder Clean Exit Jpeg2000 Jp2 J2k Negative Memory

## Policy
For `no_crash x decoder_clean_exit`, avoid replaying the observed dead end. This negative memory is co-equal with positive policies and should redirect generation before another official submission.

## Procedure
- Repository nonregression JP2/J2K seeds reached the decompression wrapper and were accepted or rejected cleanly. The missing relation is the precise progression-order/tile-packet state that drives the packet-iterator arithmetic near overflow before tier-two packet decoding.
- When `no_crash x decoder_clean_exit` appears for `jpeg2000-jp2-j2k`, treat this candidate family as a basin-to-avoid rather than as evidence of proximity to the target.
- Keep any proven parser/harness envelope, but change the missing gate or state relation before submitting again.

## Format Contract
- The wrapper accepts raw JPEG 2000 codestreams and JP2 containers. J2K codestreams are selected by their codestream marker prefix, while JP2 files are selected by their signature box layout. Tile, progression-order-change, coding-style, and packet header marker segments control the iterator state that later packet decoding consumes.
- Harness: The OpenJPEG decompression fuzzer consumes the entire file as one input. It chooses JP2 versus raw codestream from magic bytes, bounds the decode area internally, and then invokes the normal decompressor without a leading mode byte or sidecar metadata.

## Negative Memory
- Do not treat this verifier signal as a near miss unless a later candidate changes the missing gate or state relation.
- Do not submit candidates that are clean, parser-mismatched, off-target, or crashing both fixed and vulnerable images in this same shape.
- Preserve only descriptive format facts from the failed attempt; do not promote an unverified causal recovery.

## Evidence Shape
- Support: one diagnosed persistent failure from round 16.
- Scope: generator avoidance for the same failure-keyed basin.
