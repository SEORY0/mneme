---
type: causal-policy
title: "No Crash Harness Usage Banner Pkcs15 Decode Fuzzer Input Seed Mutate Double Free Negative Memory"
description: "Round 14 negative memory for no_crash with verifier signal harness_usage_banner."
failure_class: "no_crash"
verifier_signal: "harness_usage_banner"
candidate_family: "seed_mutate"
input_format: "pkcs15-decode-fuzzer-input"
harness_convention: "honggfuzz-wrapper"
vuln_class: "double-free"
access_scope: generate
success_count: 0
confidence: medium
tags: ["no-crash", "harness-usage-banner", "pkcs15-decode-fuzzer-input", "negative-memory", "round-14"]
match_keys: ["no_crash", "harness_usage_banner", "pkcs15-decode-fuzzer-input", "honggfuzz-wrapper", "double-free", "negative_memory"]
allowed_scopes: [generate]
forbidden_fields: [raw_poc_bytes, task_id, exact_offset, checksum, submit_metadata]
evidence_level: medium
train_only: true
round: 14
---
# No Crash Harness Usage Banner Pkcs15 Decode Fuzzer Input Seed Mutate Double Free Negative Memory

- key: `no_crash x harness_usage_banner`
- outcome: persistent failure / basin to avoid
- success_count: 0
- failure_count: 1
- related format facts: [[pkcs15-decode-fuzzer-input]]
- related harness facts: [[honggfuzz-wrapper]]

## Failure Shape
Corpus inputs from decode, encode, reader, and tool families all produced the selected decode target's honggfuzz usage banner under the verifier rather than a symbolized parser execution. The target contract was identified, but no candidate reached a sanitizer-visible pkcs15-pubkey double-free path in this run.

## Policy
Treat `no_crash x harness_usage_banner` on `pkcs15-decode-fuzzer-input` as a basin to avoid unless a new candidate changes the parser gate, state relation, or official target sink. Preserve any proven reachability, but reject variants that return to the same verifier signal without changing the causal gate under test.

## Procedure
1. Keep only the smallest carrier that the verifier proved reaches the parser, decoder, or harness path.
2. Identify the missing causal relation from the signal: parser selection, container acceptance, length relation, stateful subobject, allocation state, or official target sink.
3. Change one relation at a time and discard candidates that return to the same clean-exit, off-target-crash, wrong-sink, usage-only, parser-not-reached, or both-image-crash basin.
4. If a local crash is not an official target match, shrink or discard it before mutating deeper fields.
5. Promote a recovery from this basin only after a later verifier-confirmed target match.

## Negative Memory
- Do not count parser reachability, local crashes, clean exits, fixed-image crashes, usage banners, or sink mismatches as success.
- Do not repeat this candidate family unless the new attempt changes the causal gate named above.
- Do not store concrete payload bytes, task identifiers, exact positions, checksums, or submit metadata.

## Evidence Shape
- Support: one diagnosed persistent failure from Round 14.
- Scope: generator repair and basin avoidance only.
