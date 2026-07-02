---
type: causal-policy
title: "LXC Config Text Construct Parser Reached Idmap Option Copy Heap Buffer Overflow Write Verified Recovery"
description: "Round 26 verified recovery for wrong_sink with verifier signal parser_reached_idmap_option_copy."
failure_class: "wrong_sink"
verifier_signal: "parser_reached_idmap_option_copy"
candidate_family: "construct"
input_format: "lxc-config-text"
harness_convention: "libfuzzer"
vuln_class: "heap-buffer-overflow-write"
access_scope: generate
success_count: 1
confidence: high
tags: ["wrong-sink", "parser-reached-idmap-option-copy", "lxc-config-text", "libfuzzer", "construct", "verified-recovery", "round-26"]
match_keys: ["wrong_sink", "parser_reached_idmap_option_copy", "lxc-config-text", "libfuzzer", "heap-buffer-overflow-write", "verified_recovery"]
allowed_scopes: [generate]
forbidden_fields: [raw_poc_bytes, task_id, exact_offset, checksum, submit_metadata]
evidence_level: high
train_only: true
round: 26
---
# LXC Config Text Construct Parser Reached Idmap Option Copy Heap Buffer Overflow Write Verified Recovery

- key: `wrong_sink x parser_reached_idmap_option_copy`
- outcome: verified recovery
- success_count: 1
- failure_count: 0
- formats: [[lxc-config-text]]
- harnesses: [[libfuzzer]]

## Failure Shape
Use a single valid LXC configuration assignment that routes through rootfs mount option parsing, keep the outer key/value syntax intact, and make only the idmapped-mount option value exceed the fixed destination path buffer. The vulnerable build copies using an input-derived bound before it can reject the value, while the fixed build bounds the copy by the destination capacity.

## Policy
For `wrong_sink x parser_reached_idmap_option_copy` on `lxc-config-text`, preserve the format recognition and harness contract before varying the vulnerable invariant. Prefer `construct` only while that carrier and harness contract remain stable.

## Procedure
1. Preserve the `lxc-config-text` carrier and `libfuzzer` harness contract until parser reachability is stable.
2. Apply the causal invariant in the failure shape before broad mutation or seed sweeping.
3. Treat local crash class as supporting signal only; keep the candidate only when vulnerable and fixed images diverge on the official target relation.

## Verifier Contract
The official vulnerable-versus-fixed target match is the confirmation gate for this recovery policy; local crash class is supporting evidence only.

## Negative Memory
- Do not corrupt the outer `lxc-config-text` recognition gate while retargeting this signal.
- Do not treat off-target crashes, clean parser exits, fixed-build crashes, or both-image crashes as success for this policy.
- Never store raw payload bytes, exact offsets, checksums, or task-local identifiers in memory.

## Format Contract
LXC config is line-oriented key/value text. Rootfs options are parsed as a comma-separated mount-option string; LXC-specific options such as idmapped mount paths are recognized inside that value before generic mount-option parsing continues.

## Harness Contract
The exercised libFuzzer target copies the raw input into a NUL-terminated string, interprets it as a config define assignment, loads it through the container config setter, and then reads the configured item back. There is no FuzzedDataProvider layout or binary prefix; the first text key controls the parser route.

## Evidence Shape
- Support: 1 server-verified round 26 solve after 1 attempts.
- Scope: generator repair and retargeting only.
