---
type: causal-policy
title: "No Crash Parser Not Reached Fuji Raf Raw Negative Memory"
description: "Round 16 negative memory for no_crash with verifier signal parser_not_reached."
failure_class: "no_crash"
verifier_signal: "parser_not_reached"
candidate_family: "seed_mutate"
input_format: "fuji-raf-raw"
harness_convention: "libfuzzer"
vuln_class: "out-of-bounds-read"
access_scope: generate
success_count: 0
confidence: medium
tags: ["no-crash", "parser-not-reached", "fuji-raf-raw", "negative-memory", "round-16"]
match_keys: ["no_crash", "parser_not_reached", "fuji-raf-raw", "libfuzzer", "negative_memory"]
allowed_scopes: [generate]
forbidden_fields: [raw_poc_bytes, task_id, exact_offset, checksum, submit_metadata]
evidence_level: medium
train_only: true
round: 16
---
# No Crash Parser Not Reached Fuji Raf Raw Negative Memory

## Policy
For `no_crash x parser_not_reached`, avoid replaying the observed dead end. This negative memory is co-equal with positive policies and should redirect generation before another official submission.

## Procedure
- Real RAF corpus files and coarse header-preserving truncation/extension mutations stayed clean. The attempts preserved enough camera file structure for LibRaw to process but did not locate or corrupt the Adobe RAF maker-note size relation needed by the vulnerable parser.
- When `no_crash x parser_not_reached` appears for `fuji-raf-raw`, treat this candidate family as a basin-to-avoid rather than as evidence of proximity to the target.
- Keep any proven parser/harness envelope, but change the missing gate or state relation before submitting again.

## Format Contract
- Fuji RAF inputs are complete camera RAW files with a recognizable RAF header, camera metadata and large image/makernote regions. LibRaw expects a whole file buffer rather than an isolated maker-note record; preserving global RAW structure is important for open/unpack reachability.
- Harness: The LibRaw fuzzer feeds the raw input buffer to `open_buffer`, then attempts unpacking and processing modes. There is no extra envelope. Inputs above the harness size limit are ignored; valid seed-mutation is preferable to constructing a RAW file from scratch.

## Negative Memory
- Do not treat this verifier signal as a near miss unless a later candidate changes the missing gate or state relation.
- Do not submit candidates that are clean, parser-mismatched, off-target, or crashing both fixed and vulnerable images in this same shape.
- Preserve only descriptive format facts from the failed attempt; do not promote an unverified causal recovery.

## Evidence Shape
- Support: one diagnosed persistent failure from round 16.
- Scope: generator avoidance for the same failure-keyed basin.
