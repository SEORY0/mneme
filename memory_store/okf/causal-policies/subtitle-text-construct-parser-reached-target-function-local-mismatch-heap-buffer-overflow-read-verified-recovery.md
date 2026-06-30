---
type: causal-policy
title: "Subtitle Text Construct Parser Reached Target Function Local Mismatch Heap Buffer Overflow Read Verified Recovery"
description: "Round 26 verified recovery for wrong_sink with verifier signal parser_reached_target_function_local_mismatch."
failure_class: "wrong_sink"
verifier_signal: "parser_reached_target_function_local_mismatch"
candidate_family: "construct"
input_format: "subtitle-text"
harness_convention: "libfuzzer-typefind"
vuln_class: "heap-buffer-overflow-read"
access_scope: generate
success_count: 1
confidence: high
tags: ["wrong-sink", "parser-reached-target-function-local-mismatch", "subtitle-text", "libfuzzer-typefind", "construct", "verified-recovery", "round-26"]
match_keys: ["wrong_sink", "parser_reached_target_function_local_mismatch", "subtitle-text", "libfuzzer-typefind", "heap-buffer-overflow-read", "verified_recovery"]
allowed_scopes: [generate]
forbidden_fields: [raw_poc_bytes, task_id, exact_offset, checksum, submit_metadata]
evidence_level: high
train_only: true
round: 26
---
# Subtitle Text Construct Parser Reached Target Function Local Mismatch Heap Buffer Overflow Read Verified Recovery

- key: `wrong_sink x parser_reached_target_function_local_mismatch`
- outcome: verified recovery
- success_count: 1
- failure_count: 0
- formats: [[subtitle-text]]
- harnesses: [[libfuzzer-typefind]]

## Failure Shape
Feed raw subtitle text through the typefind harness. Satisfy the LRC autodetect gate with a leading bracketed timestamp-like line, then place an empty non-final line in the newline-split stream so the parser checks the previous character of a zero-length line.

## Policy
For `wrong_sink x parser_reached_target_function_local_mismatch` on `subtitle-text`, preserve the format recognition and harness contract before varying the vulnerable invariant. Prefer `construct` only while that carrier and harness contract remain stable.

## Procedure
1. Preserve the `subtitle-text` carrier and `libfuzzer-typefind` harness contract until parser reachability is stable.
2. Apply the causal invariant in the failure shape before broad mutation or seed sweeping.
3. Treat local crash class as supporting signal only; keep the candidate only when vulnerable and fixed images diverge on the official target relation.

## Verifier Contract
The official vulnerable-versus-fixed target match is the confirmation gate for this recovery policy; local crash class is supporting evidence only.

## Negative Memory
- Do not corrupt the outer `subtitle-text` recognition gate while retargeting this signal.
- Do not treat off-target crashes, clean parser exits, fixed-build crashes, or both-image crashes as success for this policy.
- Never store raw payload bytes, exact offsets, checksums, or task-local identifiers in memory.

## Format Contract
The relevant subtitle carrier is line-oriented text. LRC autodetection is entered by a leading bracketed line and then walks newline-separated entries looking for bracket and colon structure; a blank line before another line becomes a zero-length split entry.

## Harness Contract
The fuzz target feeds the file bytes directly to GStreamer typefinding through an appsrc-style path. There is no mode selector or FuzzedDataProvider carving; the typefinder peeks an initial text window and passes NUL-terminated text to subtitle autodetection.

## Evidence Shape
- Support: 1 server-verified round 26 solve after 1 attempts.
- Scope: generator repair and retargeting only.
