---
type: causal-policy
title: "Fio Ini Construct Target Stack Overflow Verified Recovery"
description: "Round 7 verified recovery for wrong_sink with verifier signal target_stack_overflow."
failure_class: "wrong_sink"
verifier_signal: "target_stack_overflow"
candidate_family: "construct"
input_format: "fio-ini"
harness_convention: "afl-file"
vuln_class: "stack-buffer-overflow-write"
access_scope: generate
success_count: 1
confidence: high
tags: ["wrong-sink", "target-stack-overflow", "construct", "fio-ini", "verified-recovery", "round-7"]
match_keys: ["wrong_sink", "target_stack_overflow", "fio-ini", "afl-file", "stack-buffer-overflow-write", "verified_recovery"]
allowed_scopes: [generate]
forbidden_fields: [raw_poc_bytes, task_id, exact_offset, checksum, submit_metadata]
evidence_level: high
train_only: true
round: 7
---
# Fio Ini Construct Target Stack Overflow Verified Recovery

- key: `wrong_sink x target_stack_overflow`
- outcome: verified recovery
- confidence: 0.82
- success_count: 1
- failure_count: 0
- formats: [[fio-ini]]
- harnesses: [[afl-file]]

## Failure Shape
The verifier-confirmed candidate preserved the `fio-ini` parser envelope under `afl-file` and moved the mutation into the relation consumed by the target sink instead of relying on broad corruption.

## Policy
Use this policy when generation reports `wrong_sink` with signal `target_stack_overflow` on `fio-ini` or the same format family. Preserve parser reachability first, then adjust only the smallest format relation named in the procedure until the vulnerable build crashes and the fixed build stays clean.

## Procedure
Build a syntactically valid fio job file with a normal global section and one job section. Set the
filename option to a path string longer than the fixed path buffer while keeping the rest of the job
minimal and valid, and keep the harness parse-mode byte at the end so the buffer is parsed as an ini
job.

## Verifier Contract
The official comparison must show target match with a vulnerable-build crash and a clean fixed build. Parser reachability, local-only crashes, off-target crashes, or both-image crashes are not sufficient.

## Format Contract
fio job input is line-oriented ini text with section headers and key-value options. The filename
option is split into path entries and each entry is passed to file setup, where a fixed path-sized
stack buffer is populated from the option value.

## Harness Contract
The AFL-style harness reads the whole file, copies all but the last byte into a NUL-terminated ini
buffer, and uses the final byte as the client/type argument to parse_jobs_ini. It initializes fio
options once, then parses the buffer in parse-only mode.

## Negative Guards
- Do not store raw payload bytes, exact positions, task identifiers, or submit metadata.
- Do not widen mutation after the parser envelope is accepted; shrink back to the single boundary relation when the fixed image also crashes.
- Do not promote this policy to another format unless the same failure key and verifier signal recur under official comparison.
