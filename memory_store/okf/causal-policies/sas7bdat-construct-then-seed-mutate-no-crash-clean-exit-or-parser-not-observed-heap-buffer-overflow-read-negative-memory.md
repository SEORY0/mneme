---
type: causal-policy
title: "Sas7bdat Construct Then Seed Mutate No Crash Clean Exit Or Parser Not Observed Heap Buffer Overflow Read Negative Memory"
description: "Negative memory for sas7bdat candidates that ended in no_crash with verifier signal clean_exit_or_parser_not_observed."
failure_class: "no_crash"
verifier_signal: "clean_exit_or_parser_not_observed"
candidate_family: "construct_then_seed_mutate"
input_format: "sas7bdat"
harness_convention: "afl"
vuln_class: "heap-buffer-overflow-read"
access_scope: generate
success_count: 0
confidence: medium
tags: ["no-crash", "clean-exit-or-parser-not-observed", "sas7bdat", "afl", "construct-then-seed-mutate", "heap-buffer-overflow-read", "negative-memory", "round-32"]
match_keys: ["no-crash", "clean-exit-or-parser-not-observed", "sas7bdat", "afl", "construct-then-seed-mutate", "heap-buffer-overflow-read", "negative-memory"]
allowed_scopes: [generate]
forbidden_fields: [raw_poc_bytes, task_id, exact_offset, checksum, submit_metadata]
evidence_level: medium
train_only: true
round: 32
---
# Sas7bdat Construct Then Seed Mutate No Crash Clean Exit Or Parser Not Observed Heap Buffer Overflow Read Negative Memory

- key: `no_crash x clean_exit_or_parser_not_observed`
- outcome: persistent diagnosed failure
- success_count: 0
- related format facts: [[sas7bdat]]
- related harness facts: [[afl]]

## Policy
Treat `no_crash x clean_exit_or_parser_not_observed` for `[[sas7bdat]]` under `[[afl]]` as a dead-end basin until new evidence changes the verifier signal. Preserve only parser-recognition facts, then change the missing relation named by the diagnosis.

## Procedure
1. Keep any envelope property that reached the parser or clean execution, but stop repeating the same carrier shape.
2. Avoid the observed dead end: A minimal SAS7BDAT envelope and real generated seeds reached clean execution but did not trigger the target. Overlarge subheader counts in both 32-bit and 64-bit layouts, minimum over-boundary counts, an out-of-page pointer offset, and a 64-bit wrapped length routed through row-compressed handling all exited cleanly. The missing trigger is likely a more exact subheader-pointer state that passes the reader's format gates while reaching the vulnerable pointer-consumption path.
3. Rebuild around `[[sas7bdat]]` and `[[afl]]`, targeting the missing gate or state relation rather than padding, broad corruption, or unrelated seed churn.
4. Submit only after local verification produces a vulnerable-build crash or a plausible parser-branch wrong-sink crash; clean exits under this signal are not submit candidates.

## Format Contract
- SAS7BDAT files start with a fixed magic header that selects endian, 32-bit versus 64-bit layout, encoding, header size, page size, and page count. Pages follow the file header; 32-bit pages use a smaller page header and subheader pointer entries than 64-bit pages. Metadata pages store the page type and subheader count in the page header, then a pointer table. Each pointer gives a subheader offset, length, compression mode, and a data/compressed flag. Subheaders begin with recognized signatures for row size, column size, column text, column names, column attributes, column formats, or related column-list records.

## Harness Contract
- The harness is an AFL-style raw-buffer target. It wraps the entire PoC as an in-memory file, installs ReadStat buffer open/read/seek/update handlers, then calls readstat_parse_sas7bdat with no filename and no FuzzedDataProvider split, mode byte, argv file path, or stdin format wrapper.

## Negative Memory
- Do not store concrete payload bytes, task identifiers, exact positions, checksums, or submit metadata.
- Do not treat parser reachability alone as success without the official target-match signal.
- Do not repeat a clean-exit or both-image-crash basin once the verifier has characterized it.

## Evidence Shape
- Support: one diagnosed Round 32 failed solve attempt.
- Attempts observed: 8.
