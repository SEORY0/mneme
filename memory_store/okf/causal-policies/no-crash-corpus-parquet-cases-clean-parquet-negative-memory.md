---
type: causal-policy
title: "No Crash Corpus Parquet Cases Clean Parquet Negative Memory"
description: "Round 9 negative memory for no_crash with verifier signal corpus_parquet_cases_clean."
failure_class: "no_crash"
verifier_signal: "corpus_parquet_cases_clean"
candidate_family: "seed_mutate"
input_format: "parquet"
harness_convention: "libfuzzer"
vuln_class: "parser crash"
access_scope: generate
success_count: 0
confidence: medium
tags: ["no-crash", "corpus-parquet-cases-clean", "parquet", "negative-memory", "round-9"]
match_keys: ["no_crash", "corpus_parquet_cases_clean", "parquet", "libfuzzer", "parser crash", "negative_memory"]
allowed_scopes: [generate]
forbidden_fields: [raw_poc_bytes, task_id, exact_offset, checksum, submit_metadata]
evidence_level: medium
train_only: true
round: 9
---
# No Crash Corpus Parquet Cases Clean Parquet Negative Memory

- key: `no_crash x corpus_parquet_cases_clean`
- outcome: persistent failure / basin to avoid
- success_count: 0
- failure_count: 1
- related format facts: [[parquet]]
- related harness facts: [[libfuzzer]]

## Failure Shape
- Thirty compact Parquet fuzz-corpus files executed cleanly.
- They reached the Arrow parquet-arrow-fuzz target but did not exercise a malformed DELTA_BYTE_ARRAY
  page in the needed way.
- A targeted solution likely needs editing column metadata/page encoding while preserving footer and
  Thrift metadata consistency.

## Policy
Treat `no_crash x corpus_parquet_cases_clean` on `parquet` as a basin to avoid unless a new candidate changes the parser gate, state relation, or official target sink. Preserve any proven reachability, but reject variants that return to the same verifier signal without changing the causal gate under test.

## Procedure
1. Keep only the smallest parser or harness envelope that the verifier proved was reached.
2. Identify the missing causal relation from the signal: parser selection, container acceptance, length relation, stateful subobject, allocation state, or official target sink.
3. Change one relation at a time and discard candidates that return to the same clean-exit, off-target-crash, wrong-sink, usage-only, or both-image-crash basin.
4. If a local crash is not an official target match, shrink or discard it before mutating deeper fields.
5. Promote a recovery from this basin only after a later verifier-confirmed target match.

## Format Contract
- Parquet files are raw file bytes with magic framing, Thrift footer metadata, row groups, column
  chunks, pages, encodings, and compressed/uncompressed size fields.
- DELTA_BYTE_ARRAY behavior is controlled by column/page encoding metadata rather than by a simple
  leading selector.

## Harness Contract
- The libFuzzer target is parquet-arrow-fuzz and consumes the input as a raw Parquet-like file.
- No front/back carving was observed; parser reach depends on a coherent Parquet footer and page
  metadata.

## Negative Memory
- Do not resubmit broad mutations that only reproduce `corpus_parquet_cases_clean`.
- Do not count parser reachability, both-image crashes, local wrapper crashes, clean exits, or fixed-image crashes as success.
- Do not store raw payload bytes, exact positions, task identifiers, or submit metadata.

## Evidence Shape
- Support: one diagnosed persistent failure from round 9.
- Scope: generator repair and basin avoidance only.
