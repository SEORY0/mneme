---
type: causal-policy
title: "Ar Archive Construct Parser Reached Sink Match Verified Recovery"
description: "Round 7 verified recovery for generic_crash with verifier signal parser_reached_sink_match."
failure_class: "generic_crash"
verifier_signal: "parser_reached_sink_match"
candidate_family: "construct"
input_format: "ar-archive"
harness_convention: "file-fuzzer-karchive-multi-archive"
vuln_class: "heap-buffer-overflow-write"
access_scope: generate
success_count: 1
confidence: high
tags: ["generic-crash", "parser-reached-sink-match", "construct", "ar-archive", "verified-recovery", "round-7"]
match_keys: ["generic_crash", "parser_reached_sink_match", "ar-archive", "file-fuzzer-karchive-multi-archive", "heap-buffer-overflow-write", "verified_recovery"]
allowed_scopes: [generate]
forbidden_fields: [raw_poc_bytes, task_id, exact_offset, checksum, submit_metadata]
evidence_level: high
train_only: true
round: 7
---
# Ar Archive Construct Parser Reached Sink Match Verified Recovery

- key: `generic_crash x parser_reached_sink_match`
- outcome: verified recovery
- confidence: 0.82
- success_count: 1
- failure_count: 0
- formats: [[ar-archive]]
- harnesses: [[file-fuzzer-karchive-multi-archive]]

## Failure Shape
The verifier-confirmed candidate preserved the `ar-archive` parser envelope under `file-fuzzer-karchive-multi-archive` and moved the mutation into the relation consumed by the target sink instead of relying on broad corruption.

## Policy
Use this policy when generation reports `generic_crash` with signal `parser_reached_sink_match` on `ar-archive` or the same format family. Preserve parser reachability first, then adjust only the smallest format relation named in the procedure until the vulnerable build crashes and the fixed build stays clean.

## Procedure
Use a syntactically valid ar archive envelope so KArchive reaches the ar handler, then choose the
special long-filename table member rather than an ordinary file member. Put a negative decimal
member size in that header so the long-name allocation and terminator write use the signed value
before payload reading.

## Verifier Contract
The official comparison must show target match with a vulnerable-build crash and a clean fixed build. Parser reachability, local-only crashes, off-target crashes, or both-image crashes are not sufficient.

## Format Contract
An ar archive starts with a fixed global magic followed by fixed-width member headers. The KAr
parser has a special path for the long filename table member; that path parses the member size as
signed decimal text and immediately allocates and writes a terminator based on it.

## Harness Contract
The harness feeds the raw file bytes through several KArchive handlers. No mode byte or
FuzzedDataProvider layout is carved from the input; parser reachability depends on the archive magic
and member header fields.

## Negative Guards
- Do not store raw payload bytes, exact positions, task identifiers, or submit metadata.
- Do not widen mutation after the parser envelope is accepted; shrink back to the single boundary relation when the fixed image also crashes.
- Do not promote this policy to another format unless the same failure key and verifier signal recur under official comparison.
