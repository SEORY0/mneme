---
type: causal-policy
title: "Cyclonedds Xtypes Typemap Xcdr2 Seed Mutate Sink Mismatch Heap Buffer Overflow Read Verified Recovery"
description: "Round 29 verified recovery for wrong_sink with verifier signal sink_mismatch."
failure_class: "wrong_sink"
verifier_signal: "sink_mismatch"
candidate_family: "seed_mutate"
input_format: "cyclonedds-xtypes-typemap-xcdr2"
harness_convention: "libfuzzer"
vuln_class: "heap-buffer-overflow-read"
access_scope: generate
success_count: 1
confidence: high
tags: ["wrong-sink", "sink-mismatch", "cyclonedds-xtypes-typemap-xcdr2", "libfuzzer", "seed-mutate", "heap-buffer-overflow-read", "verified-recovery", "round-29"]
match_keys: ["wrong_sink", "sink_mismatch", "cyclonedds-xtypes-typemap-xcdr2", "libfuzzer", "heap-buffer-overflow-read", "wrong-sink", "sink-mismatch", "cyclonedds-xtypes-typemap-xcdr2", "libfuzzer", "heap-buffer-overflow-read", "verified_recovery", "seed_mutate", "seed-mutate"]
allowed_scopes: [generate]
forbidden_fields: [raw_poc_bytes, task_id, exact_offset, checksum, submit_metadata]
evidence_level: high
train_only: true
round: 29
---
# Cyclonedds Xtypes Typemap Xcdr2 Seed Mutate Sink Mismatch Heap Buffer Overflow Read Verified Recovery

- key: `wrong_sink x sink_mismatch`
- outcome: verified target match / recovery policy
- success_count: 1
- related format facts: [[cyclonedds-xtypes-typemap-xcdr2]]
- related harness facts: [[libfuzzer]]

## Policy
For `wrong_sink x sink_mismatch` on `cyclonedds-xtypes-typemap-xcdr2`, keep the parser and harness gates that produced the verifier signal, then vary only the causal relation described below. This is a positive recovery policy because the official vulnerable/fixed verifier recorded a target match.

## Procedure
1. Start from a valid XTypes TypeMapping corpus entry that already contains a complete enumerated type object, its minimal counterpart, and a complete-to-minimal mapping. Preserve the top-level sequence structure, replace only the complete enum literal sequence with an empty sequence, shrink the enclosing length fields consistently, and recompute the affected complete type hash references so the harness accepts the object and reaches enum validation. The vulnerable invariant is that enum validation assumes at least one literal before comparing adjacent sorted values.
2. Preserve format recognition and the harness input contract while mutating the narrow sink invariant; do not broaden into an off-target crash or a both-image crash.
3. If later verifier output changes the failure key, re-rank against that new key before mutating unrelated fields.

## Format Contract
- Format [[cyclonedds-xtypes-typemap-xcdr2]]: CycloneDDS TypeMapping fuzz inputs are XCDR2-serialized maps with three top-level length-delimited sequences: minimal type-object pairs, complete type-object pairs, and complete-to-minimal identifier pairs. Hash-style type identifiers are stored separately from the length-delimited TypeObject payloads, and the hash for a TypeObject is computed over its serialized TypeObject envelope including its own length delimiter. Complete enumerated type objects contain enum flags, an enumerated header with bit-bound and type detail, then a length-delimited literal sequence whose count may be made zero if enclosing lengths and identifiers are kept consistent.
- Harness [[libfuzzer]]: The libFuzzer harness passes the raw input bytes directly to the CycloneDDS TypeMapping deserializer. It iterates complete type-object pairs, finds a matching minimal id through the complete-to-minimal sequence, constructs complete/minimal type information, references the complete type, and then adds the complete type object, which invokes XTypes validation.

## Negative Memory
- Do not corrupt the outer `cyclonedds-xtypes-typemap-xcdr2` recognition gate while retargeting this signal.
- Do not count parser reachability, clean exits, fixed-image crashes, both-image crashes, or local wrong-sink labels as success without official target match.
- Never store payload bytes, exact positions, checksums, submit metadata, or task-local identifiers.

## Evidence Shape
- Support: one round-29 worker trace with official target match.
- Scope: generator repair and retargeting only; pair with [[cyclonedds-xtypes-typemap-xcdr2]] and [[libfuzzer]].
