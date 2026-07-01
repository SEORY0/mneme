---
type: "negative-memory"
title: "DXF Text Seed Mutate And Construct No Crash Parser Reached But Fixed Also Crashed On Closest Candidates Heap Buffer Overflow Negative Memory"
description: "Round 38 negative memory for no_crash with verifier signal parser_reached_but_fixed_also_crashed_on_closest_candidates."
failure_class: "no_crash"
verifier_signal: "parser_reached_but_fixed_also_crashed_on_closest_candidates"
candidate_family: "seed_mutate_and_construct"
input_format: "dxf-text"
harness_convention: "libfuzzer"
vuln_class: "heap-buffer-overflow"
access_scope: "generate"
success_count: 0
failure_count: 1
confidence: "medium"
tags: ["no-crash", "parser-reached-but-fixed-also-crashed-on-closest-candidates", "dxf-text", "libfuzzer", "seed-mutate-and-construct", "heap-buffer-overflow", "negative-memory", "round-38"]
match_keys: ["no_crash", "parser_reached_but_fixed_also_crashed_on_closest_candidates", "dxf-text", "libfuzzer", "heap-buffer-overflow", "negative-memory", "seed_mutate_and_construct"]
allowed_scopes: ["generate"]
forbidden_fields: ["raw_poc_bytes", "task_id", "exact_offset", "checksum", "submit_metadata"]
evidence_level: "medium"
train_only: true
round: 38
---
# DXF Text Seed Mutate And Construct No Crash Parser Reached But Fixed Also Crashed On Closest Candidates Heap Buffer Overflow Negative Memory

- key: `no_crash x parser_reached_but_fixed_also_crashed_on_closest_candidates`
- outcome: persistent failure / basin to avoid
- success_count: 0
- failure_count: 1
- related format facts: [[dxf-text]]
- related harness facts: [[libfuzzer]]

## Failure Shape
Real DXF seeds reached WIPEOUT import and constructed OBJECTS-section records reached SPATIAL_FILTER import. Count-only WIPEOUT mutations either stayed clean or produced later writeback overreads that also crashed the fixed build. A SPATIAL_FILTER wrong-code sequence produced an importer heap write but also crashed the fixed build, so it was over-broad. A separate generic point-vector allocation probe stayed clean, likely because the injected object was rejected or not accepted deeply enough.

## Observed Basin
- Failure trajectory classes: no_crash, wrong_sink.
- Official confirmation: no server target match for this basin.

## Policy
Treat `no_crash x parser_reached_but_fixed_also_crashed_on_closest_candidates` on `[[dxf-text]]` under `[[libfuzzer]]` as a basin to avoid unless a new candidate changes the parser gate, state relation, or sink relation described above. Preserve any proven reachability, but reject variants that return to the same clean-exit, off-target-crash, wrapper-mismatch, usage-only, timeout, both-image-crash, or fixed-image-crash behavior.

## Procedure
1. Keep only the smallest parser or harness envelope that was actually reached.
2. Identify the missing relation from the verifier signal: parser selection, container acceptance, length relation, stateful subobject, allocation state, or official target sink.
3. Change one relation at a time and discard candidates that return to the same `parser_reached_but_fixed_also_crashed_on_closest_candidates` basin.
4. Promote a recovery from this basin only after a later official target match.

## Negative Memory
- Do not resubmit broad mutations that only reproduce `parser_reached_but_fixed_also_crashed_on_closest_candidates`.
- Do not count parser reachability, both-image crashes, local wrapper crashes, clean exits, timeouts, or fixed-image crashes as success.
- Do not store payload bytes, exact positions, task identifiers, checksums, or submit metadata.

## Evidence Shape
- Support: one diagnosed persistent failure from round 38 after 8 attempts.
- Candidate family: seed_mutate_and_construct.
- Scope: generator repair and basin avoidance only.
