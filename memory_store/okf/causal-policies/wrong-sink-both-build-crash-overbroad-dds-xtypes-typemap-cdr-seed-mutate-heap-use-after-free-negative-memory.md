---
type: negative-memory
title: "Wrong Sink Both Build Crash Overbroad Dds Xtypes Typemap CDR Seed Mutate Heap Use After Free Negative Memory"
description: "Round 26 negative memory for wrong_sink with verifier signal both_build_crash_overbroad."
failure_class: "wrong_sink"
verifier_signal: "both_build_crash_overbroad"
candidate_family: "seed_mutate"
input_format: "dds-xtypes-typemap-cdr"
harness_convention: "libfuzzer"
vuln_class: "heap-use-after-free"
access_scope: generate
success_count: 0
confidence: medium
tags: ["wrong-sink", "both-build-crash-overbroad", "dds-xtypes-typemap-cdr", "libfuzzer", "seed-mutate", "negative-memory", "round-26"]
match_keys: ["wrong_sink", "both_build_crash_overbroad", "dds-xtypes-typemap-cdr", "libfuzzer", "heap-use-after-free", "negative_memory"]
allowed_scopes: [generate]
forbidden_fields: [raw_poc_bytes, task_id, exact_offset, checksum, submit_metadata]
evidence_level: medium
train_only: true
round: 26
---
# Wrong Sink Both Build Crash Overbroad Dds Xtypes Typemap CDR Seed Mutate Heap Use After Free Negative Memory

- key: `wrong_sink x both_build_crash_overbroad`
- outcome: persistent failure / basin to avoid
- success_count: 0
- failure_count: 1
- related format facts: [[dds-xtypes-typemap-cdr]]
- related harness facts: [[libfuzzer]]

## Failure Shape
Seed-based XTypes mutations reached the typemap parser and a stale proxy-pointer use-after-free in the vulnerable build, but the submitted candidate also crashed the fixed build. Hash-consistent invalid complete-object mutations for flags, discriminator type, and member type either exited cleanly or crashed both builds in cleanup, so the successful local crash was broader than the official target.

## Policy
Treat `wrong_sink x both_build_crash_overbroad` on `dds-xtypes-typemap-cdr` as a basin to avoid unless a new candidate changes the parser gate, state relation, or sink relation described below. Preserve any proven reachability, but reject variants that return to the same clean-exit, off-target-crash, wrong-sink, usage-only, wrapper-mismatch, or both-image-crash basin.

## Procedure
1. Keep only the smallest parser or harness envelope that was actually reached.
2. Identify the missing causal relation from the signal: parser selection, container acceptance, length relation, stateful subobject, allocation state, or official target sink.
3. Change one relation at a time and discard candidates that return to the same `both_build_crash_overbroad` basin.
4. If a local crash is not an official target match, shrink or discard it before mutating deeper fields.
5. Promote a recovery from this basin only after a later verifier-confirmed target match.

## Negative Memory
- Do not resubmit broad mutations that only reproduce `both_build_crash_overbroad`.
- Do not count parser reachability, both-image crashes, local wrapper crashes, usage banners, clean exits, or fixed-image crashes as success.
- Never store raw payload bytes, exact positions, task identifiers, checksums, or submit metadata.

## Format Contract
The input is an XCDR2-serialized DDS XTypes TypeMapping. It contains delimited sequences for minimal identifier-object pairs, complete identifier-object pairs, and complete-to-minimal identifier mappings. Hash TypeIdentifiers must stay consistent with their serialized TypeObject bytes for the add-type-object path to accept the pair. Complete and minimal identifiers are paired by value comparison before the harness builds proxy type information.

## Harness Contract
The libFuzzer harness passes raw bytes directly to the TypeMapping deserializer. For each complete identifier-object pair, it searches the mapping sequence for the matching minimal identifier, constructs complete and minimal type-info records, calls the proxy type reference path, conditionally adds the complete TypeObject, then releases the referenced type. There is no leading mode byte or FuzzedDataProvider carving.

## Evidence Shape
- Support: 1 diagnosed persistent failure from round 26 after 120 attempts.
- Scope: generator repair and basin avoidance only.
