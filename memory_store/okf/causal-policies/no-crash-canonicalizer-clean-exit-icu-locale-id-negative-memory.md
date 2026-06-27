---
type: causal-policy
title: "No Crash Canonicalizer Clean Exit Icu Locale Id Negative Memory"
description: "Round 15 negative memory for no_crash with verifier signal canonicalizer_clean_exit."
failure_class: "no_crash"
verifier_signal: "canonicalizer_clean_exit"
candidate_family: "seed_mutate"
input_format: "icu-locale-id"
harness_convention: "libfuzzer"
vuln_class: "stack-use-after-scope"
access_scope: generate
success_count: 0
confidence: medium
tags: ["no-crash", "canonicalizer-clean-exit", "icu-locale-id", "negative-memory", "round-15"]
match_keys: ["no_crash", "canonicalizer_clean_exit", "icu-locale-id", "libfuzzer", "stack-use-after-scope", "negative_memory"]
allowed_scopes: [generate]
forbidden_fields: [raw_poc_bytes, task_id, exact_offset, checksum, submit_metadata]
evidence_level: medium
train_only: true
round: 15
---
# No Crash Canonicalizer Clean Exit Icu Locale Id Negative Memory

- key: `no_crash x canonicalizer_clean_exit`
- outcome: persistent failure / basin to avoid
- success_count: 0
- failure_count: 1
- related format facts: [[icu-locale-id]]
- related harness facts: [[libfuzzer]]

## Failure Shape
- Seed-derived locale IDs with repeated Unicode extension keys, private-use sections, invalid
  punctuation, long region-like fields, and mixed canonicalization features did not trigger the
  lifetime bug. The missing gate appears to be a canonicalization alias or likely-subtags path that
  returns or reuses temporary stack storage.

## Policy
Treat `no_crash x canonicalizer_clean_exit` on `icu-locale-id` as a basin to avoid unless a new candidate changes the parser gate, state relation, or official target sink. Preserve any proven reachability, but reject variants that return to the same verifier signal without changing the causal gate under test.

## Procedure
1. Keep only the smallest parser or harness envelope that the verifier proved was reached.
2. Identify the missing causal relation from the signal: parser selection, container acceptance, length relation, stateful subobject, allocation state, or official target sink.
3. Change one relation at a time and discard candidates that return to the same clean-exit, off-target-crash, wrong-sink, usage-only, or both-image-crash basin.
4. If a local crash is not an official target match, shrink or discard it before mutating deeper fields.
5. Promote a recovery from this basin only after a later verifier-confirmed target match.

## Format Contract
- ICU locale IDs include language, script, region, variants, Unicode extension key/type pairs,
  transformed extension data, and private-use subtags. The canonicalizer normalizes separators,
  aliases, and extension ordering into a fixed-size destination buffer.

## Harness Contract
- The libFuzzer target converts the raw input to a zero-terminated string and calls uloc_canonicalize
  with a fixed-capacity output buffer. There is no length prefix, mode selector, or FuzzedDataProvider
  consumption.

## Negative Memory
- Do not resubmit variants that only reproduce `canonicalizer_clean_exit`.
- Do not count parser reachability, both-image crashes, local wrapper crashes, clean exits, or fixed-image crashes as success.
- Do not store raw payload bytes, exact positions, task identifiers, or submit metadata.

## Evidence Shape
- Support: one diagnosed persistent failure from Round 15.
- Scope: generator repair and basin avoidance only.
