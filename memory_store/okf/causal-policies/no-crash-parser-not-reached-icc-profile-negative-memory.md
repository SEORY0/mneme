---
type: causal-policy
title: "No Crash Parser Not Reached ICC Profile Negative Memory"
description: "Round 16 negative memory for no_crash with verifier signal parser_not_reached."
failure_class: "no_crash"
verifier_signal: "parser_not_reached"
candidate_family: "seed_mutate"
input_format: "icc-profile"
harness_convention: "libfuzzer"
vuln_class: "memory-corruption"
access_scope: generate
success_count: 0
confidence: medium
tags: ["no-crash", "parser-not-reached", "icc-profile", "negative-memory", "round-16"]
match_keys: ["no_crash", "parser_not_reached", "icc-profile", "libfuzzer", "negative_memory"]
allowed_scopes: [generate]
forbidden_fields: [raw_poc_bytes, task_id, exact_offset, checksum, submit_metadata]
evidence_level: medium
train_only: true
round: 16
---
# No Crash Parser Not Reached ICC Profile Negative Memory

## Policy
For `no_crash x parser_not_reached`, avoid replaying the observed dead end. This negative memory is co-equal with positive policies and should redirect generation before another official submission.

## Procedure
- Profile seeds opened through LittleCMS but did not create the tolerant-read/strict-write mismatch needed for the crafted pipeline/tag corruption. Simple profile-class and tag-table mutations remained in normal parse or clean rejection paths.
- When `no_crash x parser_not_reached` appears for `icc-profile`, treat this candidate family as a basin-to-avoid rather than as evidence of proximity to the target.
- Keep any proven parser/harness envelope, but change the missing gate or state relation before submitting again.

## Format Contract
- ICC profiles have a fixed header, profile class/color-space signatures, a tag count, and tag directory entries that point to typed tag payloads. LittleCMS tolerates some malformed tag payloads while later serialization or transform construction can enforce stricter structure.
- Harness: The lcms harness consumes raw profile bytes from memory and exercises profile opening plus color-management operations. There is no wrapper; the profile header and tag table must remain coherent enough for profile creation before malformed tag internals matter.

## Negative Memory
- Do not treat this verifier signal as a near miss unless a later candidate changes the missing gate or state relation.
- Do not submit candidates that are clean, parser-mismatched, off-target, or crashing both fixed and vulnerable images in this same shape.
- Preserve only descriptive format facts from the failed attempt; do not promote an unverified causal recovery.

## Evidence Shape
- Support: one diagnosed persistent failure from round 16.
- Scope: generator avoidance for the same failure-keyed basin.
