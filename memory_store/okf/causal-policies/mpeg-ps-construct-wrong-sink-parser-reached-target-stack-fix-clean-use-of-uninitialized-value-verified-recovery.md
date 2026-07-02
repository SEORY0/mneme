---
type: causal-policy
title: "Mpeg Ps Construct Wrong Sink Parser Reached Target Stack Fix Clean Use Of Uninitialized Value Verified Recovery"
description: "Round 30 verified recovery for wrong_sink with verifier signal parser_reached_target_stack_fix_clean."
failure_class: "wrong_sink"
verifier_signal: "parser_reached_target_stack_fix_clean"
candidate_family: "construct"
input_format: "mpeg-ps"
harness_convention: "libfuzzer-ffmpeg-demuxer"
vuln_class: "use-of-uninitialized-value"
access_scope: generate
success_count: 1
confidence: medium
tags: ["wrong-sink", "parser-reached-target-stack-fix-clean", "mpeg-ps", "libfuzzer-ffmpeg-demuxer", "construct", "verified-recovery", "round-30"]
match_keys: ["wrong-sink", "parser-reached-target-stack-fix-clean", "mpeg-ps", "libfuzzer-ffmpeg-demuxer", "use-of-uninitialized-value"]
allowed_scopes: [generate]
forbidden_fields: [raw_poc_bytes, task_id, exact_offset, checksum, submit_metadata]
evidence_level: high
train_only: true
round: 30
---
# Mpeg Ps Construct Wrong Sink Parser Reached Target Stack Fix Clean Use Of Uninitialized Value Verified Recovery

- key: `wrong-sink x parser-reached-target-stack-fix-clean`
- outcome: verified recovery
- success_count: 1
- failure_count: 0
- formats: [[mpeg-ps]]
- harnesses: [[libfuzzer-ffmpeg-demuxer]]

## Failure Shape
Build a minimal MPEG program-stream video PES packet that passes the PES header parser and leaves only a short video payload for stream sniffing. Make the available payload prefix satisfy the AVS sequence-header comparison, but declare/provide fewer payload bytes than the demuxer's fixed-size sniff read expects, so the vulnerable build evaluates uninitialized bytes from the local sniff buffer. The fixed build checks the short read and exits cleanly.

## Policy
For `wrong-sink x parser-reached-target-stack-fix-clean` on `mpeg-ps`, preserve the parser and harness gates first, then mutate only the causal invariant described by the verified trace. Prefer `construct` while this format and harness contract are present.

## Procedure
1. Preserve the `mpeg-ps` carrier enough for the `libfuzzer-ffmpeg-demuxer` harness to reach the parser path.
2. Keep unrelated envelope fields minimal and stable so verifier feedback stays tied to the target sink.
3. Apply the verified invariant from the failure shape rather than random broad mutation.
4. Submit only candidates where the vulnerable image reaches the target relation and the fixed image rejects or avoids it.

## Verifier Contract
The local class may remain coarse. Treat the official vulnerable-versus-fixed target match as the confirmation gate for this policy.

## Negative Memory
- Do not corrupt the outer `mpeg-ps` recognition gate while retargeting this signal.
- Do not treat off-target crashes, clean parser reachability, or both-image crashes as success for this policy.
- Never store raw payload bytes, exact offsets, checksums, or task-local identifiers in memory.

## Evidence Shape
- Support: 1 server-verified solve(s), including round 30.
- Scope: generator repair only.
