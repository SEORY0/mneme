---
type: causal-policy
title: "Ffmpeg Ipmovie Construct Truncated Header Parser Reached Uninitialized Signature Compare Use Of Uninitialized Value Verified Recovery"
description: "Round 24 verified recovery for wrong_sink with verifier signal parser_reached_uninitialized_signature_compare."
failure_class: "wrong_sink"
verifier_signal: "parser_reached_uninitialized_signature_compare"
candidate_family: "construct_truncated_header"
input_format: "ffmpeg-ipmovie"
harness_convention: "oss-fuzz libfuzzer demuxer"
vuln_class: "use-of-uninitialized-value"
access_scope: generate
success_count: 1
confidence: medium
tags: ["wrong-sink", "parser-reached-uninitialized-signature-compare", "ffmpeg-ipmovie", "oss-fuzz-libfuzzer-demuxer", "construct-truncated-header", "verified-recovery", "round-24"]
match_keys: ["wrong-sink", "parser-reached-uninitialized-signature-compare", "ffmpeg-ipmovie", "oss-fuzz-libfuzzer-demuxer", "use-of-uninitialized-value"]
allowed_scopes: [generate]
forbidden_fields: [raw_poc_bytes, task_id, exact_offset, checksum, submit_metadata]
evidence_level: high
train_only: true
round: 24
---
# Ffmpeg Ipmovie Construct Truncated Header Parser Reached Uninitialized Signature Compare Use Of Uninitialized Value Verified Recovery

- key: `wrong_sink x parser_reached_uninitialized_signature_compare`
- outcome: verified recovery
- success_count: 1
- failure_count: 0
- formats: [[ffmpeg-ipmovie]]
- harnesses: [[oss-fuzz-libfuzzer-demuxer]]

## Failure Shape
Use a short raw input that routes the forced IPMovie demuxer into its signature-read path but ends before the full signature buffer is initialized. The vulnerable build compares partially uninitialized stack data; the fixed build checks the read length first.

## Policy
For `wrong_sink x parser_reached_uninitialized_signature_compare` on `ffmpeg-ipmovie`, preserve the format recognition, harness contract, and parser reachability gates before varying the causal invariant. Prefer `construct_truncated_header` only while this format and harness contract are present.

## Procedure
1. Preserve the `ffmpeg-ipmovie` carrier and `oss-fuzz-libfuzzer-demuxer` harness contract until parser reachability is stable.
2. Apply the causal invariant in the failure shape before broad mutation or seed sweeping.
3. Treat local crash class as supporting signal only; keep the candidate only when vulnerable and fixed images diverge on the official target relation.

## Verifier Contract
The official vulnerable-versus-fixed target match is the confirmation gate for recovery policies; local crash class is supporting evidence only.

## Negative Memory
- Do not corrupt the outer `ffmpeg-ipmovie` recognition gate while retargeting this signal.
- Do not treat off-target crashes, clean parser exits, fixed-build crashes, or both-image crashes as success for this policy.
- Never store raw payload bytes, exact offsets, checksums, or task-local identifiers in memory.

## Evidence Shape
- Support: 1 server-verified round 24 solve after 1 attempts.
- Scope: generator repair and retargeting only.
