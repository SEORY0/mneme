---
type: causal-policy
title: "Uk NTF In GDAL Fuzzer Friendly Archive Construct Parser Reached Target Stack Fixed Clean Heap Buffer Overflow Read Via Negative Size Strncpy Verified Recovery"
description: "Round 26 verified recovery for wrong_sink with verifier signal parser_reached_target_stack_fixed_clean."
failure_class: "wrong_sink"
verifier_signal: "parser_reached_target_stack_fixed_clean"
candidate_family: "construct"
input_format: "uk-ntf-in-gdal-fuzzer-friendly-archive"
harness_convention: "libfuzzer"
vuln_class: "heap-buffer-overflow-read via negative-size strncpy"
access_scope: generate
success_count: 1
confidence: high
tags: ["wrong-sink", "parser-reached-target-stack-fixed-clean", "uk-ntf-in-gdal-fuzzer-friendly-archive", "libfuzzer", "construct", "verified-recovery", "round-26"]
match_keys: ["wrong_sink", "parser_reached_target_stack_fixed_clean", "uk-ntf-in-gdal-fuzzer-friendly-archive", "libfuzzer", "heap-buffer-overflow-read via negative-size strncpy", "verified_recovery"]
allowed_scopes: [generate]
forbidden_fields: [raw_poc_bytes, task_id, exact_offset, checksum, submit_metadata]
evidence_level: high
train_only: true
round: 26
---
# Uk NTF In GDAL Fuzzer Friendly Archive Construct Parser Reached Target Stack Fixed Clean Heap Buffer Overflow Read Via Negative Size Strncpy Verified Recovery

- key: `wrong_sink x parser_reached_target_stack_fixed_clean`
- outcome: verified recovery
- success_count: 1
- failure_count: 0
- formats: [[uk-ntf-in-gdal-fuzzer-friendly-archive]]
- harnesses: [[libfuzzer]]

## Failure Shape
Wrap a minimal UK NTF member in GDAL's fuzzer-friendly archive form. Satisfy the NTF volume, database, and section-header gates, keep the product generic, then create a generic point group whose geometry record is 3D. The section header must violate the invariant that the Z-coordinate field width is nonnegative and consistent with the coordinate record, so 3D geometry extraction asks the shared field copier for an inverted Z range. Attribute-width and real-precision negative-size variants are decoys because they also crash the fixed build.

## Policy
For `wrong_sink x parser_reached_target_stack_fixed_clean` on `uk-ntf-in-gdal-fuzzer-friendly-archive`, preserve the format recognition and harness contract before varying the vulnerable invariant. Prefer `construct` only while that carrier and harness contract remain stable.

## Procedure
1. Preserve the `uk-ntf-in-gdal-fuzzer-friendly-archive` carrier and `libfuzzer` harness contract until parser reachability is stable.
2. Apply the causal invariant in the failure shape before broad mutation or seed sweeping.
3. Treat local crash class as supporting signal only; keep the candidate only when vulnerable and fixed images diverge on the official target relation.

## Verifier Contract
The official vulnerable-versus-fixed target match is the confirmation gate for this recovery policy; local crash class is supporting evidence only.

## Negative Memory
- Do not corrupt the outer `uk-ntf-in-gdal-fuzzer-friendly-archive` recognition gate while retargeting this signal.
- Do not treat off-target crashes, clean parser exits, fixed-build crashes, or both-image crashes as success for this policy.
- Never store raw payload bytes, exact offsets, checksums, or task-local identifiers in memory.

## Format Contract
UK NTF is line-oriented: records begin with a two-digit record type and end with a continuation/final marker plus a percent terminator. A volume header precedes database metadata and a section header; the section header supplies coordinate widths, coordinate scale factors, origins, tile dimensions, and Z-coordinate width. After the section header, feature groups are anchored by feature records such as points or lines and can include geometry or 3D geometry records; a volume-termination record ends the scan.

## Harness Contract
The active GDAL shape fuzzer stores the raw PoC as a virtual tar-like input and opens a fixed member named as a shapefile through GDAL's virtual tar path, then iterates every layer and feature. The accepted archive form starts with GDAL's fuzzer-friendly archive marker and contains a member for the fixed opened filename. There is no FuzzedDataProvider carving; the whole file is the virtual archive.

## Evidence Shape
- Support: 1 server-verified round 26 solve after 10 attempts.
- Scope: generator repair and retargeting only.
