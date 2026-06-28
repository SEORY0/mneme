---
type: causal-policy
title: "Generic Crash Local Seed Crash Not Confirmed By Submit PDF Negative Memory"
description: "Round 9 negative memory for generic_crash with verifier signal local_seed_crash_not_confirmed_by_submit."
failure_class: "generic_crash"
verifier_signal: "local_seed_crash_not_confirmed_by_submit"
candidate_family: "seed_mutate"
input_format: "pdf"
harness_convention: "libfuzzer"
vuln_class: "logic-bug / parser state misuse"
access_scope: generate
success_count: 0
confidence: medium
tags: ["generic-crash", "local-seed-crash-not-confirmed-by-submit", "pdf", "negative-memory", "round-9"]
match_keys: ["generic_crash", "local_seed_crash_not_confirmed_by_submit", "pdf", "libfuzzer", "logic-bug / parser state misuse", "negative_memory"]
allowed_scopes: [generate]
forbidden_fields: [raw_poc_bytes, task_id, exact_offset, checksum, submit_metadata]
evidence_level: medium
train_only: true
round: 9
---
# Generic Crash Local Seed Crash Not Confirmed By Submit PDF Negative Memory

- key: `generic_crash x local_seed_crash_not_confirmed_by_submit`
- outcome: persistent failure / basin to avoid
- success_count: 0
- failure_count: 1
- related format facts: [[pdf]]
- related harness facts: [[libfuzzer]]

## Failure Shape
- A real PDF corpus seed could make the local wrapper report a segfault, but the official server did
  not reproduce a vulnerable-image crash.
- Other corpus PDFs rendered cleanly.
- I did not isolate the makeStream state-reuse condition inside a PDF stream/object structure.

## Policy
Treat `generic_crash x local_seed_crash_not_confirmed_by_submit` on `pdf` as a basin to avoid unless a new candidate changes the parser gate, state relation, or official target sink. Preserve any proven reachability, but reject variants that return to the same verifier signal without changing the causal gate under test.

## Procedure
1. Keep only the smallest parser or harness envelope that the verifier proved was reached.
2. Identify the missing causal relation from the signal: parser selection, container acceptance, length relation, stateful subobject, allocation state, or official target sink.
3. Change one relation at a time and discard candidates that return to the same clean-exit, off-target-crash, wrong-sink, usage-only, or both-image-crash basin.
4. If a local crash is not an official target match, shrink or discard it before mutating deeper fields.
5. Promote a recovery from this basin only after a later verifier-confirmed target match.

## Format Contract
- PDF inputs for this harness are complete raw documents.
- Useful corpus samples have a normal PDF envelope with indirect objects, content streams, pages,
  fonts, and xref/trailer data; parser reach depends on a loadable document and at least one page
  renderable by Poppler.

## Harness Contract
- The libFuzzer target receives raw file bytes, calls the Poppler raw-data loader, skips locked or
  unloadable documents, then renders every page with page_renderer.
- There is no front/back field carving or mode selector.

## Negative Memory
- Do not resubmit broad mutations that only reproduce `local_seed_crash_not_confirmed_by_submit`.
- Do not count parser reachability, both-image crashes, local wrapper crashes, clean exits, or fixed-image crashes as success.
- Do not store raw payload bytes, exact positions, task identifiers, or submit metadata.

## Evidence Shape
- Support: one diagnosed persistent failure from round 9.
- Scope: generator repair and basin avoidance only.
