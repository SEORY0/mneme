---
type: causal-policy
title: No Crash Parser Reached Without Target Crash Negative Memory
description: Negative memory for no_crash with verifier signal parser_reached_without_target_crash.
failure_class: no_crash
verifier_signal: parser_reached_without_target_crash
candidate_family: construct
input_format: any
harness_convention: any
access_scope: generate
success_count: 0
confidence: medium
tags: [no-crash, parser-reached-without-target-crash, negative_memory]
match_keys: [no-crash, parser-reached-without-target-crash, negative_memory]
allowed_scopes: [generate]
forbidden_fields: [raw_poc_bytes, task_id, exact_offset, checksum, submit_metadata]
evidence_level: medium
train_only: true
---
# No Crash Parser Reached Without Target Crash Negative Memory

## Policy
Treat this verifier signal as negative memory for the attempted candidate family. Preserve any parser reachability it proved, but do not keep mutating the same field basin unless the next verification changes the signal.

## Round 4 Reinforcement
- key: `no_crash x parser_reached_without_target_crash`
- outcome: persistent failure basin
- support_count: 1
- candidate_families: construct
- observed_formats: tar-csv-to-shapefile

### Procedure
The parser or executor ran, but the target state was absent. Keep the valid envelope and retarget the semantic selector, state transition, table kind, or option named by the diagnosis.

### Diagnosed Dead Ends
- The active GDAL target is vector-translate, which reads a tar containing command arguments and a CSV source; a direct shapefile member is ignored. CSV inputs that asked the Shapefile driver to write malformed or degenerate polygon WKT executed successfully but did not reach the single-point polygon rewind overflow. The missing gate is an OGR geometry representation accepted from CSV that preserves a one-point polygon into Shapefile output.

### Negative Memory
Do not repeat the same carrier plus broad mutation after this signal. Do not promote this basin into a recovery until a later verifier-confirmed candidate flips the official gate.
