---
type: causal-policy
title: No Crash Sql Parser Reached Without Crash Negative Memory
description: Negative memory for no_crash with verifier signal sql_parser_reached_without_crash.
failure_class: no_crash
verifier_signal: sql_parser_reached_without_crash
candidate_family: construct
input_format: any
harness_convention: any
access_scope: generate
success_count: 0
confidence: medium
tags: [no-crash, sql-parser-reached-without-crash, negative_memory]
match_keys: [no-crash, sql-parser-reached-without-crash, negative_memory]
allowed_scopes: [generate]
forbidden_fields: [raw_poc_bytes, task_id, exact_offset, checksum, submit_metadata]
evidence_level: medium
train_only: true
---
# No Crash Sql Parser Reached Without Crash Negative Memory

- key: `no_crash x sql_parser_reached_without_crash`
- outcome: persistent failure basin
- support_count: 1
- candidate_families: construct
- observed_formats: sql

## Policy
Treat this verifier signal as negative memory for the attempted candidate family. Preserve any parser reachability it proved, but do not keep mutating the same field basin unless the next verification changes the signal.

## Procedure
Use the diagnosis as a selector map: keep the valid base, then change the missing protocol/table/module state rather than increasing file size or randomizing payload bytes.

## Diagnosed Dead Ends
- Malformed insert values containing parenthesized SELECT and EXISTS expressions were accepted or converted into parser errors without crashing. The fuzzer only calls the statement parser, so the trigger likely requires a more specific malformed exists-expression shape that leaves the insert value parser in an inconsistent state rather than simply producing an ErrorExpression.

## Negative Memory
Do not repeat the same carrier plus broad mutation after this signal. Do not promote the diagnosis into a recovery until a later verifier-confirmed candidate flips the official gate.
