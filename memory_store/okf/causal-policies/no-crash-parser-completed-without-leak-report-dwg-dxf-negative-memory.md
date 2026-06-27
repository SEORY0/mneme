---
type: causal-policy
title: "No Crash Parser Completed Without Leak Report Dwg DXF Negative Memory"
description: "Round 9 negative memory for no_crash with verifier signal parser_completed_without_leak_report."
failure_class: "no_crash"
verifier_signal: "parser_completed_without_leak_report"
candidate_family: "seed_mutate"
input_format: "dwg/dxf"
harness_convention: "libfuzzer"
vuln_class: "memory-leak on parser error"
access_scope: generate
success_count: 0
confidence: medium
tags: ["no-crash", "parser-completed-without-leak-report", "dwg-dxf", "negative-memory", "round-9"]
match_keys: ["no_crash", "parser_completed_without_leak_report", "dwg/dxf", "libfuzzer", "memory-leak on parser error", "negative_memory"]
allowed_scopes: [generate]
forbidden_fields: [raw_poc_bytes, task_id, exact_offset, checksum, submit_metadata]
evidence_level: medium
train_only: true
round: 9
---
# No Crash Parser Completed Without Leak Report Dwg DXF Negative Memory

- key: `no_crash x parser_completed_without_leak_report`
- outcome: persistent failure / basin to avoid
- success_count: 0
- failure_count: 1
- related format facts: [[dwg-dxf]]
- related harness facts: [[libfuzzer]]

## Failure Shape
- Minimal DXF and real DWG/DXF samples executed without a leak or crash report under the local
  verifier.
- The remaining gap is a DXF error path in in_dxf that allocates before failing; the tested valid
  and lightly malformed inputs did not hit that leak-reporting path.

## Policy
Treat `no_crash x parser_completed_without_leak_report` on `dwg/dxf` as a basin to avoid unless a new candidate changes the parser gate, state relation, or official target sink. Preserve any proven reachability, but reject variants that return to the same verifier signal without changing the causal gate under test.

## Procedure
1. Keep only the smallest parser or harness envelope that the verifier proved was reached.
2. Identify the missing causal relation from the signal: parser selection, container acceptance, length relation, stateful subobject, allocation state, or official target sink.
3. Change one relation at a time and discard candidates that return to the same clean-exit, off-target-crash, wrong-sink, usage-only, or both-image-crash basin.
4. If a local crash is not an official target match, shrink or discard it before mutating deeper fields.
5. Promote a recovery from this basin only after a later verifier-confirmed target match.

## Format Contract
- DXF is line-oriented group-code/value text with sections ending in EOF; DWG is binary and
  versioned.
- The libredwg corpus includes both valid CAD drawings and known-error examples, but valid samples
  tend to complete normally.

## Harness Contract
- The fuzz target receives raw file bytes and lets libredwg auto-parse DWG/DXF-style content.
- There is no explicit mode byte or FuzzedDataProvider layout observed in the harness.

## Negative Memory
- Do not resubmit broad mutations that only reproduce `parser_completed_without_leak_report`.
- Do not count parser reachability, both-image crashes, local wrapper crashes, clean exits, or fixed-image crashes as success.
- Do not store raw payload bytes, exact positions, task identifiers, or submit metadata.

## Evidence Shape
- Support: one diagnosed persistent failure from round 9.
- Scope: generator repair and basin avoidance only.
