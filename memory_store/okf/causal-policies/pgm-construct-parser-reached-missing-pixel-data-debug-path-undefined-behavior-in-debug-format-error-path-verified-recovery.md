---
type: causal-policy
title: "PGM Construct Parser Reached Missing Pixel Data Debug Path Undefined Behavior In Debug Format Error Path Verified Recovery"
description: "Round 24 verified recovery for wrong_sink with verifier signal parser_reached_missing_pixel_data_debug_path."
failure_class: "wrong_sink"
verifier_signal: "parser_reached_missing_pixel_data_debug_path"
candidate_family: "construct"
input_format: "pgm"
harness_convention: "libfuzzer raw bytes"
vuln_class: "undefined-behavior-in-debug-format-error-path"
access_scope: generate
success_count: 1
confidence: medium
tags: ["wrong-sink", "parser-reached-missing-pixel-data-debug-path", "pgm", "libfuzzer-raw-bytes", "construct", "verified-recovery", "round-24"]
match_keys: ["wrong-sink", "parser-reached-missing-pixel-data-debug-path", "pgm", "libfuzzer-raw-bytes", "undefined-behavior-in-debug-format-error-path"]
allowed_scopes: [generate]
forbidden_fields: [raw_poc_bytes, task_id, exact_offset, checksum, submit_metadata]
evidence_level: high
train_only: true
round: 24
---
# PGM Construct Parser Reached Missing Pixel Data Debug Path Undefined Behavior In Debug Format Error Path Verified Recovery

- key: `wrong_sink x parser_reached_missing_pixel_data_debug_path`
- outcome: verified recovery
- success_count: 1
- failure_count: 0
- formats: [[pgm]]
- harnesses: [[libfuzzer-raw-bytes]]

## Failure Shape
Build a syntactically valid portable graymap header that stays within the loader dimension comfort gates, then provide too little pixel data. The vulnerable loader reaches the missing-color-data error/debug path and triggers UB; the fixed image avoids that crash.

## Policy
For `wrong_sink x parser_reached_missing_pixel_data_debug_path` on `pgm`, preserve the format recognition, harness contract, and parser reachability gates before varying the causal invariant. Prefer `construct` only while this format and harness contract are present.

## Procedure
1. Preserve the `pgm` carrier and `libfuzzer-raw-bytes` harness contract until parser reachability is stable.
2. Apply the causal invariant in the failure shape before broad mutation or seed sweeping.
3. Treat local crash class as supporting signal only; keep the candidate only when vulnerable and fixed images diverge on the official target relation.

## Verifier Contract
The official vulnerable-versus-fixed target match is the confirmation gate for recovery policies; local crash class is supporting evidence only.

## Negative Memory
- Do not corrupt the outer `pgm` recognition gate while retargeting this signal.
- Do not treat off-target crashes, clean parser exits, fixed-build crashes, or both-image crashes as success for this policy.
- Never store raw payload bytes, exact offsets, checksums, or task-local identifiers in memory.

## Evidence Shape
- Support: 1 server-verified round 24 solve after 2 attempts.
- Scope: generator repair and retargeting only.
