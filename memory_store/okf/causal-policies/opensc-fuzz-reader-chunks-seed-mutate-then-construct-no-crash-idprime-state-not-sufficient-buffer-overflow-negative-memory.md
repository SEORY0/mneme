---
type: negative-memory
title: "Opensc Fuzz Reader Chunks Seed Mutate Then Construct No Crash Idprime State Not Sufficient Buffer Overflow Negative Memory"
description: "Round 36 negative memory for no_crash with verifier signal idprime_state_not_sufficient."
failure_class: "no_crash"
verifier_signal: "idprime_state_not_sufficient"
candidate_family: "seed_mutate_then_construct"
input_format: "opensc-fuzz-reader-chunks"
harness_convention: "libfuzzer"
vuln_class: "buffer-overflow"
access_scope: generate
success_count: 0
failure_count: 1
confidence: medium
tags: ["no-crash", "idprime-state-not-sufficient", "opensc-fuzz-reader-chunks", "libfuzzer", "seed-mutate-then-construct", "buffer-overflow", "negative-memory", "round-36"]
match_keys: ["no_crash", "idprime_state_not_sufficient", "opensc-fuzz-reader-chunks", "libfuzzer", "buffer-overflow", "no-crash", "idprime-state-not-sufficient", "negative_memory", "seed_mutate_then_construct", "seed-mutate-then-construct"]
allowed_scopes: [generate]
forbidden_fields: [raw_poc_bytes, task_id, exact_offset, checksum, submit_metadata]
evidence_level: medium
train_only: true
round: 36
---
# Opensc Fuzz Reader Chunks Seed Mutate Then Construct No Crash Idprime State Not Sufficient Buffer Overflow Negative Memory

- key: `no_crash x idprime_state_not_sufficient`
- outcome: persistent failure / basin to avoid
- success_count: 0
- failure_count: 1
- related format facts: [[opensc-fuzz-reader-chunks]]
- related harness facts: [[libfuzzer]]

## Failure Shape
A real corpus transcript with additional operation chunks stayed clean, and constructed idprime transcripts with an exact ATR shape, duplicated select-index phases, generic PKCS#15 failure preludes, synthetic idprime serial reads, indexed certificate records, and oversized private certificate file-size relations also stayed clean. The likely missing condition is a fully coherent idprime PKCS#15 state with a parseable certificate object or a different maximum-length sink than the attempted cache-fill relation.

## Observed Basin
- Failure trajectory classes: no_crash.
- Official confirmation: no server target match for this basin.

## Policy
Treat `no_crash x idprime_state_not_sufficient` on `opensc-fuzz-reader-chunks` under `libfuzzer` as a basin to avoid unless a new candidate changes the parser gate, state relation, or sink relation described above. Preserve any proven reachability, but reject variants that return to the same clean-exit, off-target-crash, wrapper-mismatch, usage-only, or fixed-image-crash behavior.

## Procedure
1. Keep only the smallest parser or harness envelope that was actually reached.
2. Identify the missing relation from the signal: parser selection, container acceptance, length relation, stateful subobject, allocation state, or official target sink.
3. Change one relation at a time and discard candidates that return to the same `idprime_state_not_sufficient` basin.
4. Promote a recovery from this basin only after a later official target match.

## Negative Memory
- Do not resubmit broad mutations that only reproduce `idprime_state_not_sufficient`.
- Do not count parser reachability, both-image crashes, local wrapper crashes, clean exits, or fixed-image crashes as success.
- Do not store payload bytes, exact positions, task identifiers, checksums, or submit metadata.

## Evidence Shape
- Support: 1 diagnosed persistent failure from round 36 after 20 attempts.
- Scope: generator repair and basin avoidance only.
