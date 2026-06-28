---
type: causal-policy
title: "No Crash Isce Fuzzer Ran Without Crash Gdal Isce Xml Negative Memory"
description: "Round 24 negative memory for no_crash with verifier signal isce_fuzzer ran without crash."
failure_class: "no_crash"
verifier_signal: "isce_fuzzer ran without crash"
candidate_family: "seed_mutate"
input_format: "gdal-isce-xml"
harness_convention: "libfuzzer GDAL ISCE fuzzer"
vuln_class: "null-pointer-dereference"
access_scope: generate
success_count: 0
confidence: medium
tags: ["no-crash", "isce-fuzzer-ran-without-crash", "gdal-isce-xml", "libfuzzer-gdal-isce-fuzzer", "seed-mutate", "negative-memory", "round-24"]
match_keys: ["no-crash", "isce-fuzzer-ran-without-crash", "gdal-isce-xml", "libfuzzer-gdal-isce-fuzzer", "null-pointer-dereference"]
allowed_scopes: [generate]
forbidden_fields: [raw_poc_bytes, task_id, exact_offset, checksum, submit_metadata]
evidence_level: medium
train_only: true
round: 24
---
# No Crash Isce Fuzzer Ran Without Crash Gdal Isce Xml Negative Memory

- key: `no_crash x isce_fuzzer ran without crash`
- outcome: negative memory
- success_count: 0
- failure_count: 1
- formats: [[gdal-isce-xml]]
- harnesses: [[libfuzzer-gdal-isce-fuzzer]]

## Dead-End Shape
The real ISCE sidecar XML, truncated XML, empty XML, minimal XML, and a metadata mutation all executed cleanly. The missing trigger likely requires a coherent ISCE XML sidecar that references raster component metadata in a partially missing or inconsistent way rather than simply malformed XML.

## Policy
For `no_crash x isce_fuzzer ran without crash` on `gdal-isce-xml`, avoid replaying the observed dead end. This negative memory is co-equal with positive policies and should redirect generation before another official submission. Prefer `seed_mutate` only while this format and harness contract are present.

## Procedure
1. When `no_crash x isce_fuzzer ran without crash` appears for `gdal-isce-xml`, treat this candidate family as a basin-to-avoid rather than evidence of proximity.
2. Preserve any proven format or harness envelope, but change the missing gate, state relation, or sink path before another official submission.
3. Prefer a different construction family if the same verifier signal repeats without new parser-depth evidence.

## Verifier Contract
The official vulnerable-versus-fixed target match is the confirmation gate for recovery policies; local crash class is supporting evidence only.

## Negative Memory
- Do not resubmit candidates that are clean, off-target, rejected before the target path, or crashing both fixed and vulnerable images in this same shape.
- Do not promote this trace as a recovery unless a later verifier run flips the target relation.
- Preserve only descriptive format and harness facts from this failed attempt.

## Evidence Shape
- Support: one diagnosed round 24 persistent failure.
- Scope: generator repair and retargeting only.
