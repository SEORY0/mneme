---
type: causal-policy
title: "Rawspeed Panasonic Fuzzer Record Construct Parser Reached Target Function Heap Buffer Overflow Write Verified Recovery"
description: "Round 21 verified recovery for wrong-sink with verifier signal parser-reached-target-function."
failure_class: "wrong-sink"
verifier_signal: "parser-reached-target-function"
candidate_family: "construct"
input_format: "rawspeed-panasonic-fuzzer-record"
harness_convention: "afl-libfuzzer-compatible"
vuln_class: "heap-buffer-overflow-write"
access_scope: generate
success_count: 1
confidence: medium
tags: ["wrong-sink", "parser-reached-target-function", "rawspeed-panasonic-fuzzer-record", "afl-libfuzzer-compatible", "construct", "verified-recovery", "round-21"]
match_keys: ["wrong-sink", "parser-reached-target-function", "rawspeed-panasonic-fuzzer-record", "afl-libfuzzer-compatible", "heap-buffer-overflow-write"]
allowed_scopes: [generate]
forbidden_fields: [raw_poc_bytes, task_id, exact_offset, checksum, submit_metadata]
evidence_level: high
train_only: true
round: 21
---
# Rawspeed Panasonic Fuzzer Record Construct Parser Reached Target Function Heap Buffer Overflow Write Verified Recovery

- key: `wrong-sink x parser-reached-target-function`
- outcome: verified recovery
- success_count: 1
- failure_count: 0
- formats: [[rawspeed-panasonic-fuzzer-record]]
- harnesses: [[afl-libfuzzer-compatible]]

## Failure Shape
Build the harness record with valid raw-image metadata for a single-component ushort image, then set the Panasonic load-flags value larger than the bitpump scratch buffer while still supplying enough remaining compressed data to pass the input-length gate. The vulnerable bitpump uses that unsanitized value as both an offset and a subtraction term before copying into the scratch buffer.

## Policy
For `wrong-sink x parser-reached-target-function` on `rawspeed-panasonic-fuzzer-record`, preserve the parser and harness gates first, then mutate only the causal invariant described by the verified trace. Prefer `construct` while this format and harness contract are present.

## Procedure
1. Preserve the `rawspeed-panasonic-fuzzer-record` carrier enough for the `afl-libfuzzer-compatible` harness to reach the parser path.
2. Keep unrelated envelope fields minimal and stable so verifier feedback stays tied to the target sink.
3. Apply the verified invariant from the failure shape rather than random broad mutation.
4. Submit only candidates where the vulnerable image reaches the target relation and the fixed image rejects or avoids it.

## Verifier Contract
The official vulnerable-versus-fixed target match is the confirmation gate for this policy; local crash class is supporting evidence only.

## Negative Memory
- Do not corrupt the outer `rawspeed-panasonic-fuzzer-record` recognition gate while retargeting this signal.
- Do not treat off-target crashes, clean parser exits, or both-image crashes as success for this policy.
- Never store raw payload bytes, exact offsets, checksums, or task-local identifiers in memory.

## Evidence Shape
- Support: 1 server-verified round 21 solve after 2 attempts.
- Scope: generator repair only.
