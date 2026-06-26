---
type: causal-policy
title: "No Crash Parser Reached Clean Transfer Curl Fuzzer Tlv Negative Memory"
description: "Round 8 negative memory for no_crash with verifier signal parser_reached_clean_transfer."
failure_class: "no_crash"
verifier_signal: "parser_reached_clean_transfer"
candidate_family: "construct_and_seed_mutate"
input_format: "curl-fuzzer-tlv"
harness_convention: "afl-file-wrapper"
vuln_class: "buffer-overflow-handling"
access_scope: generate
success_count: 0
confidence: medium
tags: ["no-crash", "parser-reached-clean-transfer", "curl-fuzzer-tlv", "negative_memory", "round-8"]
match_keys: ["no_crash", "parser_reached_clean_transfer", "curl-fuzzer-tlv", "afl-file-wrapper", "negative_memory"]
allowed_scopes: [generate]
forbidden_fields: [raw_poc_bytes, task_id, exact_offset, checksum, submit_metadata]
evidence_level: medium
train_only: true
round: 8
---
# No Crash Parser Reached Clean Transfer Curl Fuzzer Tlv Negative Memory

## Policy
Treat `no_crash x parser_reached_clean_transfer` as a persistent failure basin for `curl-fuzzer-tlv` under `afl-file-wrapper`. Preserve any reachability it proved, but do not keep mutating the same field basin unless the next verification changes the signal.

## Diagnosed Dead End
- URL-only, FTP, POP3, and IMAP TLV streams parsed and executed cleanly. Adding extra complete response lines after terminal ping-pong replies was not enough to trigger the recv-buffer overflow handling path; likely the state machine needs a more exact protocol phase and buffered-data size relationship.

## Format and Harness Gates
- Format: The curl fuzzer input is a sequence of big-endian TLVs. One TLV supplies the URL, response TLVs supply staged server replies, and optional TLVs supply credentials, headers, upload data, or protocol options. Ping-pong protocols consume response slots as simulated socket reads.
- Harness: The AFL-style wrapper passes the whole file to the curl fuzzer, which parses TLVs from the front and configures a mocked socket manager. No FuzzedDataProvider back-loading is used; response ordering and protocol phase determine whether a response slot is consumed.

## Procedure
1. Before retrying this basin, rebuild the carrier around the exact harness contract and confirm parser reachability.
2. Replace the failed mutation family with a more specific invariant that would change the verifier signal.
3. Avoid broad seed mutation, oversized mutation, or off-target crash chasing when this same signal recurs.

## Negative Memory
- Do not promote this basin into a recovery policy until an official vulnerable/fixed verifier target match is observed.
- Do not preserve raw bytes, offsets, checksums, or task-local identifiers.

## Evidence Shape
- Support: one round-8 persistent failure trace.
- Scope: generator avoidance and retargeting for the same failure key.
