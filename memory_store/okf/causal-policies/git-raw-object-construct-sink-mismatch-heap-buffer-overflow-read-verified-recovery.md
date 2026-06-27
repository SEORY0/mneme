---
type: causal-policy
title: "Git Raw Object Construct Sink Mismatch Heap Buffer Overflow Read Verified Recovery"
description: "Round 12 verified recovery for wrong_sink with verifier signal sink_mismatch."
failure_class: "wrong_sink"
verifier_signal: "sink_mismatch"
candidate_family: "construct"
input_format: "git-raw-object"
harness_convention: "libfuzzer"
vuln_class: "heap-buffer-overflow-read"
access_scope: generate
success_count: 1
confidence: high
tags: ["wrong-sink", "sink-mismatch", "git-raw-object", "verified-recovery", "round-12"]
match_keys: ["wrong_sink", "sink_mismatch", "git-raw-object", "libfuzzer", "heap-buffer-overflow-read", "verified_recovery"]
allowed_scopes: [generate]
forbidden_fields: [raw_poc_bytes, task_id, exact_offset, checksum, submit_metadata]
evidence_level: high
train_only: true
round: 12
---
# Git Raw Object Construct Sink Mismatch Heap Buffer Overflow Read Verified Recovery

- key: `wrong_sink x sink_mismatch`
- outcome: verified recovery
- confidence: 0.82
- success_count: 1
- failure_count: 0
- formats: [[git-raw-object]]
- harnesses: [[libfuzzer]]

## Failure Shape
The verifier-confirmed candidate preserved the `git-raw-object` parser envelope under `libfuzzer` and moved the mutation into the relation consumed by the target sink instead of relying on broad corruption.

## Policy
Use this policy when generation reports `wrong_sink` with signal `sink_mismatch` on `git-raw-object` or the same format family. Preserve parser reachability first, then adjust only the smallest format relation named in the procedure until the vulnerable build crashes and the fixed build stays clean.

## Procedure
Build a raw commit object body that satisfies the commit parser enough to parse an initial tree line and author line, then place a second author marker as the final unterminated field. The duplicate-author scan compares the marker against a non-NUL-terminated buffer end and overreads while checking the prefix terminator.

## Verifier Contract
The official comparison must show target match with a vulnerable-build crash and a clean fixed build. Parser reachability, local-only crashes, off-target crashes, or both-image crashes are not sufficient.

## Format Contract
The objects fuzzer accepts raw object body bytes, not a loose-object zlib envelope. Commit objects are line-oriented records, with header-like fields parsed in order; duplicate author fields are detected by prefix-testing the next line start.

## Harness Contract
The libFuzzer harness feeds the raw input buffer directly to libgit2 object parsing for selected object types. There is no fuzzer-side length prefix or mode byte; the buffer boundary itself is the parser boundary.

## Negative Guards
- Do not store raw payload bytes, exact positions, task identifiers, or submit metadata.
- Do not widen mutation after the parser envelope is accepted; shrink back to the single boundary relation when the fixed image also crashes.
- Do not promote this policy to another format unless the same failure key and verifier signal recur under official comparison.
