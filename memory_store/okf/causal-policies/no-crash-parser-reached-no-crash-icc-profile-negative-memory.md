---
type: causal-policy
title: "No Crash Parser Reached No Crash Icc Profile Negative Memory"
description: "Round 12 negative memory for no_crash with verifier signal parser_reached_no_crash."
failure_class: "no_crash"
verifier_signal: "parser_reached_no_crash"
candidate_family: "seed_mutate"
input_format: "icc-profile"
harness_convention: "libfuzzer"
vuln_class: "forged-profile-validation"
access_scope: generate
success_count: 0
confidence: medium
tags: ["no-crash", "parser-reached-no-crash", "icc-profile", "negative-memory", "round-12"]
match_keys: ["no_crash", "parser_reached_no_crash", "icc-profile", "libfuzzer", "forged-profile-validation", "negative_memory"]
allowed_scopes: [generate]
forbidden_fields: [raw_poc_bytes, task_id, exact_offset, checksum, submit_metadata]
evidence_level: medium
train_only: true
round: 12
---
# No Crash Parser Reached No Crash Icc Profile Negative Memory

- key: `no_crash x parser_reached_no_crash`
- outcome: persistent failure / basin to avoid
- success_count: 0
- failure_count: 1
- related format facts: [[icc-profile]]
- related harness facts: [[libfuzzer]]

## Failure Shape
Mutating real ICC profile seeds across profile class, input colorspace, profile connection space, and high-channel colorspace signatures did not reach the forged-profile transform bug. The likely missing gate is a coherent transform tag or pipeline whose channel counts disagree with the forged header while still passing lcms profile validation.

## Policy
Treat `no_crash x parser_reached_no_crash` on `icc-profile` as a basin to avoid unless a new candidate changes the parser gate, state relation, or official target sink. Preserve any proven reachability, but reject variants that return to the same verifier signal without changing the causal gate under test.

## Procedure
1. Keep only the smallest parser or harness envelope that the verifier proved was reached.
2. Identify the missing causal relation from the signal: parser selection, container acceptance, length relation, stateful subobject, allocation state, or official target sink.
3. Change one relation at a time and discard candidates that return to the same clean-exit, off-target-crash, wrong-sink, usage-only, or both-image-crash basin.
4. If a local crash is not an official target match, shrink or discard it before mutating deeper fields.
5. Promote a recovery from this basin only after a later verifier-confirmed target match.

## Format Contract
ICC profiles have a fixed header describing profile class, data colorspace, profile connection space, and a tag table. lcms opens the profile from memory, derives input channel count from the header colorspace, then creates a transform to an sRGB destination using profile tags and pipeline stages.

## Harness Contract
The lcms fuzzer passes the raw input directly to profile-open-from-memory. If a source profile opens, it creates an sRGB destination profile, derives a source pixel format from the source colorspace, creates a transform, and executes one transform sample.

## Negative Memory
- Do not resubmit broad mutations that only reproduce `parser_reached_no_crash`.
- Do not count parser reachability, both-image crashes, local wrapper crashes, clean exits, or fixed-image crashes as success.
- Do not store raw payload bytes, exact positions, task identifiers, or submit metadata.

## Evidence Shape
- Support: one diagnosed persistent failure from round 12.
- Scope: generator repair and basin avoidance only.
