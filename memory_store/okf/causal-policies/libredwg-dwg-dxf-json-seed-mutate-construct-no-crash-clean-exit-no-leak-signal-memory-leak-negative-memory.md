---
type: "negative-memory"
title: "Libredwg DWG DXF JSON Seed Mutate Construct No Crash Clean Exit No Leak Signal Memory Leak Negative Memory"
description: "Round 38 negative memory for no_crash with verifier signal clean_exit_no_leak_signal."
failure_class: "no_crash"
verifier_signal: "clean_exit_no_leak_signal"
candidate_family: "seed_mutate+construct"
input_format: "libredwg-dwg-dxf-json"
harness_convention: "libfuzzer"
vuln_class: "memory-leak"
access_scope: "generate"
success_count: 0
failure_count: 1
confidence: "medium"
tags: ["no-crash", "clean-exit-no-leak-signal", "libredwg-dwg-dxf-json", "libfuzzer", "seed-mutate-construct", "memory-leak", "negative-memory", "round-38"]
match_keys: ["no_crash", "clean_exit_no_leak_signal", "libredwg-dwg-dxf-json", "libfuzzer", "memory-leak", "negative-memory", "seed_mutate+construct"]
allowed_scopes: ["generate"]
forbidden_fields: ["raw_poc_bytes", "task_id", "exact_offset", "checksum", "submit_metadata"]
evidence_level: "medium"
train_only: true
round: 38
---
# Libredwg DWG DXF JSON Seed Mutate Construct No Crash Clean Exit No Leak Signal Memory Leak Negative Memory

- key: `no_crash x clean_exit_no_leak_signal`
- outcome: persistent failure / basin to avoid
- success_count: 0
- failure_count: 1
- related format facts: [[libredwg-dwg-dxf-json]]
- related harness facts: [[libfuzzer]]

## Failure Shape
The local harness executed each candidate cleanly and the official differential kept the vulnerable image at a clean exit. Attempts covered seed-truncated DXF, structured DXF parser errors after section/object allocation, a syntactically valid JSON critical-schema error after parser-state allocation, and a seed-truncated DWG decode error. The task description suggests a leak-only target, but this libFuzzer-style verifier did not surface a leak signal for these input-error families.

## Observed Basin
- Failure trajectory classes: no_crash.
- Official confirmation: no server target match for this basin.

## Policy
Treat `no_crash x clean_exit_no_leak_signal` on `[[libredwg-dwg-dxf-json]]` under `[[libfuzzer]]` as a basin to avoid unless a new candidate changes the parser gate, state relation, or sink relation described above. Preserve any proven reachability, but reject variants that return to the same clean-exit, off-target-crash, wrapper-mismatch, usage-only, timeout, both-image-crash, or fixed-image-crash behavior.

## Procedure
1. Keep only the smallest parser or harness envelope that was actually reached.
2. Identify the missing relation from the verifier signal: parser selection, container acceptance, length relation, stateful subobject, allocation state, or official target sink.
3. Change one relation at a time and discard candidates that return to the same `clean_exit_no_leak_signal` basin.
4. Promote a recovery from this basin only after a later official target match.

## Negative Memory
- Do not resubmit broad mutations that only reproduce `clean_exit_no_leak_signal`.
- Do not count parser reachability, both-image crashes, local wrapper crashes, clean exits, timeouts, or fixed-image crashes as success.
- Do not store payload bytes, exact positions, task identifiers, checksums, or submit metadata.

## Evidence Shape
- Support: one diagnosed persistent failure from round 38 after 6 attempts.
- Candidate family: seed_mutate+construct.
- Scope: generator repair and basin avoidance only.
