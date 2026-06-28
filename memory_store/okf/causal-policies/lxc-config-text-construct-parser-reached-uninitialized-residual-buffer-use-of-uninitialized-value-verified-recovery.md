---
type: causal-policy
title: "Lxc Config Text Construct Parser Reached Uninitialized Residual Buffer Use Of Uninitialized Value Verified Recovery"
description: "Round 25 verified recovery for wrong_sink with verifier signal parser_reached_uninitialized_residual_buffer."
failure_class: "wrong_sink"
verifier_signal: "parser_reached_uninitialized_residual_buffer"
candidate_family: "construct"
input_format: "lxc-config-text"
harness_convention: "libfuzzer-tempfile"
vuln_class: "use-of-uninitialized-value"
access_scope: generate
success_count: 1
confidence: medium
tags: ["wrong-sink", "parser-reached-uninitialized-residual-buffer", "lxc-config-text", "libfuzzer-tempfile", "construct", "verified-recovery", "round-25"]
match_keys: ["wrong_sink", "parser_reached_uninitialized_residual_buffer", "lxc-config-text", "libfuzzer-tempfile", "use-of-uninitialized-value"]
allowed_scopes: [generate]
forbidden_fields: [raw_poc_bytes, task_id, exact_offset, checksum, submit_metadata]
evidence_level: high
train_only: true
round: 25
---
# Lxc Config Text Construct Parser Reached Uninitialized Residual Buffer Use Of Uninitialized Value Verified Recovery

- key: `wrong_sink x parser_reached_uninitialized_residual_buffer`
- outcome: verified recovery
- success_count: 1
- failure_count: 0
- formats: [[lxc-config-text]]
- harnesses: [[libfuzzer-tempfile]]

## Failure Shape
Use a valid LXC config assignment for a time namespace offset with a numeric value followed by a valid short unit suffix. This makes the residual-unit buffer contain a suffix shorter than the stack buffer; the vulnerable build fails to clear the remaining bytes before trimming/comparing the unit, while the fixed build zero-fills it.

## Policy
For `wrong_sink x parser_reached_uninitialized_residual_buffer` on `lxc-config-text`, preserve the format recognition and harness contract before varying the vulnerable invariant. Prefer `construct` only while that carrier and harness contract remain stable.

## Procedure
1. Preserve the `lxc-config-text` carrier and `libfuzzer-tempfile` harness contract until parser reachability is stable.
2. Apply the causal invariant in the failure shape before broad mutation or seed sweeping.
3. Treat local crash class as supporting signal only; keep the candidate only when vulnerable and fixed images diverge on the official target relation.

## Verifier Contract
The official vulnerable-versus-fixed target match is the confirmation gate for this recovery policy; local crash class is supporting evidence only.

## Negative Memory
- Do not corrupt the outer `lxc-config-text` recognition gate while retargeting this signal.
- Do not treat off-target crashes, clean parser exits, fixed-build crashes, or both-image crashes as success for this policy.
- Never store raw payload bytes, exact offsets, checksums, or task-local identifiers in memory.

## Format Contract
LXC config input is line-oriented key/value text. Time namespace offset keys parse a signed integer prefix and a residual unit suffix; accepted unit names include short time units that are later trimmed and compared as strings.

## Harness Contract
The fuzzer writes raw input bytes to a temporary config file, initializes an LXC config object, calls the normal config reader on the temp file, frees the config, and removes the temp file.

## Evidence Shape
- Support: 1 server-verified round 25 solve after 2 attempts.
- Scope: generator repair and retargeting only.
