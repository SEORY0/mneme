---
type: causal-policy
title: "Mxf Seed Mutate Wrong Sink Parser Reached Msan Uninitialized Stack Key Use Of Uninitialized Value Verified Recovery"
description: "Round 30 verified recovery for wrong_sink with verifier signal parser_reached-msan-uninitialized-stack-key."
failure_class: "wrong_sink"
verifier_signal: "parser_reached-msan-uninitialized-stack-key"
candidate_family: "seed_mutate"
input_format: "mxf"
harness_convention: "libfuzzer-ffmpeg-dem-mxf"
vuln_class: "use-of-uninitialized-value"
access_scope: generate
success_count: 1
confidence: medium
tags: ["wrong-sink", "parser-reached-msan-uninitialized-stack-key", "mxf", "libfuzzer-ffmpeg-dem-mxf", "seed-mutate", "verified-recovery", "round-30"]
match_keys: ["wrong-sink", "parser-reached-msan-uninitialized-stack-key", "mxf", "libfuzzer-ffmpeg-dem-mxf", "use-of-uninitialized-value"]
allowed_scopes: [generate]
forbidden_fields: [raw_poc_bytes, task_id, exact_offset, checksum, submit_metadata]
evidence_level: high
train_only: true
round: 30
---
# Mxf Seed Mutate Wrong Sink Parser Reached Msan Uninitialized Stack Key Use Of Uninitialized Value Verified Recovery

- key: `wrong-sink x parser-reached-msan-uninitialized-stack-key`
- outcome: verified recovery
- success_count: 1
- failure_count: 0
- formats: [[mxf]]
- harnesses: [[libfuzzer-ffmpeg-dem-mxf]]

## Failure Shape
Preserve a real MXF header partition pack so the demuxer accepts the stream, then append a metadata KLV for a TaggedValue local set. Inside that local set, use the indirect-value tag with a declared payload large enough to require a fixed-width type key, but end the input before the full type key is available. The vulnerable parser performs the short read into a fresh stack key buffer and immediately compares it; the repaired build rejects the short read cleanly.

## Policy
For `wrong-sink x parser-reached-msan-uninitialized-stack-key` on `mxf`, preserve the parser and harness gates first, then mutate only the causal invariant described by the verified trace. Prefer `seed-mutate` while this format and harness contract are present.

## Procedure
1. Preserve the `mxf` carrier enough for the `libfuzzer-ffmpeg-dem-mxf` harness to reach the parser path.
2. Keep unrelated envelope fields minimal and stable so verifier feedback stays tied to the target sink.
3. Apply the verified invariant from the failure shape rather than random broad mutation.
4. Submit only candidates where the vulnerable image reaches the target relation and the fixed image rejects or avoids it.

## Verifier Contract
The local class may remain coarse. Treat the official vulnerable-versus-fixed target match as the confirmation gate for this policy.

## Negative Memory
- Do not corrupt the outer `mxf` recognition gate while retargeting this signal.
- Do not treat off-target crashes, clean parser reachability, or both-image crashes as success for this policy.
- Never store raw payload bytes, exact offsets, checksums, or task-local identifiers in memory.

## Evidence Shape
- Support: 1 server-verified solve(s), including round 30.
- Scope: generator repair only.
