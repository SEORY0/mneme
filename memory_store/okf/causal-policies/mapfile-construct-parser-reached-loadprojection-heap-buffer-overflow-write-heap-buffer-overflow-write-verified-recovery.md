---
type: causal-policy
title: "Mapfile Construct Parser Reached Loadprojection Heap Buffer Overflow Write Heap Buffer Overflow Write Verified Recovery"
description: "Round 21 verified recovery for generic-crash with verifier signal parser-reached-loadprojection-heap-buffer-overflow-write."
failure_class: "generic-crash"
verifier_signal: "parser-reached-loadprojection-heap-buffer-overflow-write"
candidate_family: "construct"
input_format: "mapfile"
harness_convention: "libfuzzer-tempfile-mapserver-mapfuzzer"
vuln_class: "heap-buffer-overflow-write"
access_scope: generate
success_count: 1
confidence: medium
tags: ["generic-crash", "parser-reached-loadprojection-heap-buffer-overflow-write", "mapfile", "libfuzzer-tempfile-mapserver-mapfuzzer", "construct", "verified-recovery", "round-21"]
match_keys: ["generic-crash", "parser-reached-loadprojection-heap-buffer-overflow-write", "mapfile", "libfuzzer-tempfile-mapserver-mapfuzzer", "heap-buffer-overflow-write"]
allowed_scopes: [generate]
forbidden_fields: [raw_poc_bytes, task_id, exact_offset, checksum, submit_metadata]
evidence_level: high
train_only: true
round: 21
---
# Mapfile Construct Parser Reached Loadprojection Heap Buffer Overflow Write Heap Buffer Overflow Write Verified Recovery

- key: `generic-crash x parser-reached-loadprojection-heap-buffer-overflow-write`
- outcome: verified recovery
- success_count: 1
- failure_count: 0
- formats: [[mapfile]]
- harnesses: [[libfuzzer-tempfile-mapserver-mapfuzzer]]

## Failure Shape
Construct a minimal MapServer mapfile that fully parses as a MAP with a required layer and a top-level PROJECTION block. Put more separate quoted projection arguments in the block than the projection argument vector can hold. Keeping the surrounding map syntax valid reaches projection loading, where the vulnerable build appends past the fixed-size argument storage and the fixed build bounds or rejects it.

## Policy
For `generic-crash x parser-reached-loadprojection-heap-buffer-overflow-write` on `mapfile`, preserve the parser and harness gates first, then mutate only the causal invariant described by the verified trace. Prefer `construct` while this format and harness contract are present.

## Procedure
1. Preserve the `mapfile` carrier enough for the `libfuzzer-tempfile-mapserver-mapfuzzer` harness to reach the parser path.
2. Keep unrelated envelope fields minimal and stable so verifier feedback stays tied to the target sink.
3. Apply the verified invariant from the failure shape rather than random broad mutation.
4. Submit only candidates where the vulnerable image reaches the target relation and the fixed image rejects or avoids it.

## Verifier Contract
The official vulnerable-versus-fixed target match is the confirmation gate for this policy; local crash class is supporting evidence only.

## Negative Memory
- Do not corrupt the outer `mapfile` recognition gate while retargeting this signal.
- Do not treat off-target crashes, clean parser exits, or both-image crashes as success for this policy.
- Never store raw payload bytes, exact offsets, checksums, or task-local identifiers in memory.

## Evidence Shape
- Support: 1 server-verified round 21 solve after 5 attempts.
- Scope: generator repair only.
