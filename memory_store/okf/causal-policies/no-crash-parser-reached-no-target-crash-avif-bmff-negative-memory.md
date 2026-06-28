---
type: causal-policy
title: "No Crash Parser Reached No Target Crash Avif Bmff Negative Memory"
description: "Round 12 negative memory for no_crash with verifier signal parser_reached_no_target_crash."
failure_class: "no_crash"
verifier_signal: "parser_reached_no_target_crash"
candidate_family: "seed_mutate_and_construct"
input_format: "avif-bmff"
harness_convention: "libfuzzer"
vuln_class: "container-uniqueness-logic-error"
access_scope: generate
success_count: 0
confidence: medium
tags: ["no-crash", "parser-reached-no-target-crash", "avif-bmff", "negative-memory", "round-12"]
match_keys: ["no_crash", "parser_reached_no_target_crash", "avif-bmff", "libfuzzer", "container-uniqueness-logic-error", "negative_memory"]
allowed_scopes: [generate]
forbidden_fields: [raw_poc_bytes, task_id, exact_offset, checksum, submit_metadata]
evidence_level: medium
train_only: true
round: 12
---
# No Crash Parser Reached No Target Crash Avif Bmff Negative Memory

- key: `no_crash x parser_reached_no_target_crash`
- outcome: persistent failure / basin to avoid
- success_count: 0
- failure_count: 1
- related format facts: [[avif-bmff]]
- related harness facts: [[libfuzzer]]

## Failure Shape
Valid AVIF seed mutation and constructed duplicate top-level box layouts were accepted or rejected without a crash. Duplicating top-level file-type, metadata, and movie-style boxes did not by itself trigger the described error-flow invariant.

## Policy
Treat `no_crash x parser_reached_no_target_crash` on `avif-bmff` as a basin to avoid unless a new candidate changes the parser gate, state relation, or official target sink. Preserve any proven reachability, but reject variants that return to the same verifier signal without changing the causal gate under test.

## Procedure
1. Keep only the smallest parser or harness envelope that the verifier proved was reached.
2. Identify the missing causal relation from the signal: parser selection, container acceptance, length relation, stateful subobject, allocation state, or official target sink.
3. Change one relation at a time and discard candidates that return to the same clean-exit, off-target-crash, wrong-sink, usage-only, or both-image-crash basin.
4. If a local crash is not an official target match, shrink or discard it before mutating deeper fields.
5. Promote a recovery from this basin only after a later verifier-confirmed target match.

## Format Contract
AVIF uses BMFF boxes with a size, type, and payload. A minimal decoded seed carried a file-type box followed by metadata and media-data boxes. Metadata boxes contain nested item/property structures with their own uniqueness checks, while the described invariant concerns top-level uniqueness and error flow.

## Harness Contract
The decoder fuzzer passes raw input bytes directly to avifDecoderSetIOMemory and then parses or decodes through libavif. There is no prefix selector or footer; the candidate must be a BMFF-like byte stream.

## Negative Memory
- Do not resubmit broad mutations that only reproduce `parser_reached_no_target_crash`.
- Do not count parser reachability, both-image crashes, local wrapper crashes, clean exits, or fixed-image crashes as success.
- Do not store raw payload bytes, exact positions, task identifiers, or submit metadata.

## Evidence Shape
- Support: one diagnosed persistent failure from round 12.
- Scope: generator repair and basin avoidance only.
