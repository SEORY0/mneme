---
type: causal-policy
title: "Ar Archive Construct Parser Reached Official Target Match Heap Buffer Overflow Write Verified Recovery"
description: "Round 12 verified recovery for wrong_sink with verifier signal parser_reached_official_target_match."
failure_class: "wrong_sink"
verifier_signal: "parser_reached_official_target_match"
candidate_family: "construct"
input_format: "ar archive"
harness_convention: "libfuzzer"
vuln_class: "heap-buffer-overflow-write"
access_scope: generate
success_count: 1
confidence: high
tags: ["wrong-sink", "parser-reached-official-target-match", "ar-archive", "verified-recovery", "round-12"]
match_keys: ["wrong_sink", "parser_reached_official_target_match", "ar-archive", "libfuzzer", "heap-buffer-overflow-write", "verified_recovery"]
allowed_scopes: [generate]
forbidden_fields: [raw_poc_bytes, task_id, exact_offset, checksum, submit_metadata]
evidence_level: high
train_only: true
round: 12
---
# Ar Archive Construct Parser Reached Official Target Match Heap Buffer Overflow Write Verified Recovery

- key: `wrong_sink x parser_reached_official_target_match`
- outcome: verified recovery
- confidence: 0.82
- success_count: 1
- failure_count: 0
- formats: [[ar-archive]]
- harnesses: [[libfuzzer]]

## Failure Shape
The verifier-confirmed candidate preserved the `ar-archive` parser envelope under `libfuzzer` and moved the mutation into the relation consumed by the target sink instead of relying on broad corruption.

## Policy
Use this policy when generation reports `wrong_sink` with signal `parser_reached_official_target_match` on `ar-archive` or the same format family. Preserve parser reachability first, then adjust only the smallest format relation named in the procedure until the vulnerable build crashes and the fixed build stays clean.

## Procedure
Build a valid ar-style archive envelope that reaches the special long-name-table member. Keep the member header syntactically acceptable, but make the declared table length invalid so the parser allocates the wrong-sized long-name buffer and then writes the terminator past that allocation.

## Verifier Contract
The official comparison must show target match with a vulnerable-build crash and a clean fixed build. Parser reachability, local-only crashes, off-target crashes, or both-image crashes are not sufficient.

## Format Contract
The ar format begins with a global magic and then a sequence of fixed-width member headers. Member headers contain text fields for name and size and a small trailer marker; member payloads are padded to member alignment. A special long-name-table member is recognized by its reserved name and its size controls allocation of the shared filename table.

## Harness Contract
The libFuzzer harness passes the raw input bytes through a Qt buffer and tries several KArchive readers. KAr is reached only when the raw bytes satisfy the ar magic/header gates.

## Negative Guards
- Do not store raw payload bytes, exact positions, task identifiers, or submit metadata.
- Do not widen mutation after the parser envelope is accepted; shrink back to the single boundary relation when the fixed image also crashes.
- Do not promote this policy to another format unless the same failure key and verifier signal recur under official comparison.
