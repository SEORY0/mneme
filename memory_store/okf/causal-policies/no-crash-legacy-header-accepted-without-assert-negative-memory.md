---
type: causal-policy
title: No Crash Legacy Header Accepted Without Assert Negative Memory
description: Negative memory for no_crash with verifier signal legacy_header_accepted_without_assert.
failure_class: no_crash
verifier_signal: legacy_header_accepted_without_assert
candidate_family: construct
input_format: any
harness_convention: any
access_scope: generate
success_count: 0
confidence: medium
tags: [no-crash, legacy-header-accepted-without-assert, negative_memory]
match_keys: [no-crash, legacy-header-accepted-without-assert, negative_memory]
allowed_scopes: [generate]
forbidden_fields: [raw_poc_bytes, task_id, exact_offset, checksum, submit_metadata]
evidence_level: medium
train_only: true
---
# No Crash Legacy Header Accepted Without Assert Negative Memory

- key: `no_crash x legacy_header_accepted_without_assert`
- outcome: persistent failure basin
- support_count: 1
- candidate_families: construct
- observed_formats: dwg

## Policy
Treat this verifier signal as negative memory for the attempted candidate family. Preserve any parser reachability it proved, but do not keep mutating the same field basin unless the next verification changes the signal.

## Procedure
Use the diagnosis as a selector map: keep the valid base, then change the missing protocol/table/module state rather than increasing file size or randomizing payload bytes.

## Diagnosed Dead Ends
- The sparse legacy DWG header was recognized but still advanced through the fixed header fields cleanly, so it did not violate the expected handoff point into section-locator parsing.

## Negative Memory
Do not repeat the same carrier plus broad mutation after this signal. Do not promote the diagnosis into a recovery until a later verifier-confirmed candidate flips the official gate.
