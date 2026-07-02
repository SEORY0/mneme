---
type: "negative-memory"
title: "Opentype Font Graphite Seed Mutate No Crash Official Vulnerable Build Clean Exit After Local Wrapper Crashes Use Of Uninitialized Value Negative Memory"
description: "Round 38 negative memory for no_crash with verifier signal official_vulnerable_build_clean_exit_after_local_wrapper_crashes."
failure_class: "no_crash"
verifier_signal: "official_vulnerable_build_clean_exit_after_local_wrapper_crashes"
candidate_family: "seed_mutate"
input_format: "opentype-font-graphite"
harness_convention: "libfuzzer"
vuln_class: "use-of-uninitialized-value"
access_scope: "generate"
success_count: 0
failure_count: 1
confidence: "medium"
tags: ["no-crash", "official-vulnerable-build-clean-exit-after-local-wrapper-crashes", "opentype-font-graphite", "libfuzzer", "seed-mutate", "use-of-uninitialized-value", "negative-memory", "round-38"]
match_keys: ["no_crash", "official_vulnerable_build_clean_exit_after_local_wrapper_crashes", "opentype-font-graphite", "libfuzzer", "use-of-uninitialized-value", "negative-memory", "seed_mutate"]
allowed_scopes: ["generate"]
forbidden_fields: ["raw_poc_bytes", "task_id", "exact_offset", "checksum", "submit_metadata"]
evidence_level: "medium"
train_only: true
round: 38
---
# Opentype Font Graphite Seed Mutate No Crash Official Vulnerable Build Clean Exit After Local Wrapper Crashes Use Of Uninitialized Value Negative Memory

- key: `no_crash x official_vulnerable_build_clean_exit_after_local_wrapper_crashes`
- outcome: persistent failure / basin to avoid
- success_count: 0
- failure_count: 1
- related format facts: [[opentype-font-graphite]]
- related harness facts: [[libfuzzer]]

## Failure Shape
A real Graphite font seed reached OTS and accepted both an uncompressed v3 Glat conversion and a normal LZ4-compressed Glat wrapper. Mutating Silf was the wrong table for this task. Glat LZ4 variants that used short initialized prefixes plus match-copy tails produced local wrapper crashes, but the official vulnerable build clean-exited, so the attempted LZ4 edge did not create a server-reproducible uninitialized-read condition.

## Observed Basin
- Failure trajectory classes: no_crash, generic_crash.
- Official confirmation: no server target match for this basin.

## Policy
Treat `no_crash x official_vulnerable_build_clean_exit_after_local_wrapper_crashes` on `[[opentype-font-graphite]]` under `[[libfuzzer]]` as a basin to avoid unless a new candidate changes the parser gate, state relation, or sink relation described above. Preserve any proven reachability, but reject variants that return to the same clean-exit, off-target-crash, wrapper-mismatch, usage-only, timeout, both-image-crash, or fixed-image-crash behavior.

## Procedure
1. Keep only the smallest parser or harness envelope that was actually reached.
2. Identify the missing relation from the verifier signal: parser selection, container acceptance, length relation, stateful subobject, allocation state, or official target sink.
3. Change one relation at a time and discard candidates that return to the same `official_vulnerable_build_clean_exit_after_local_wrapper_crashes` basin.
4. Promote a recovery from this basin only after a later official target match.

## Negative Memory
- Do not resubmit broad mutations that only reproduce `official_vulnerable_build_clean_exit_after_local_wrapper_crashes`.
- Do not count parser reachability, both-image crashes, local wrapper crashes, clean exits, timeouts, or fixed-image crashes as success.
- Do not store payload bytes, exact positions, task identifiers, checksums, or submit metadata.

## Evidence Shape
- Support: one diagnosed persistent failure from round 38 after 24 attempts.
- Candidate family: seed_mutate.
- Scope: generator repair and basin avoidance only.
