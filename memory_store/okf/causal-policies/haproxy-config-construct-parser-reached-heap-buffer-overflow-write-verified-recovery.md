---
type: causal-policy
title: "Haproxy Config Construct Parser Reached Heap Buffer Overflow Write Verified Recovery"
description: "Round 22 verified recovery for generic_crash with verifier signal parser_reached."
failure_class: "generic_crash"
verifier_signal: "parser_reached"
candidate_family: "construct"
input_format: "haproxy-config"
harness_convention: "libfuzzer"
vuln_class: "heap-buffer-overflow-write"
access_scope: generate
success_count: 1
confidence: medium
tags: ["generic-crash", "parser-reached", "haproxy-config", "libfuzzer", "construct", "verified-recovery", "round-22"]
match_keys: ["generic-crash", "parser-reached", "haproxy-config", "libfuzzer", "heap-buffer-overflow-write"]
allowed_scopes: [generate]
forbidden_fields: [raw_poc_bytes, task_id, exact_offset, checksum, submit_metadata]
evidence_level: high
train_only: true
round: 22
---
# Haproxy Config Construct Parser Reached Heap Buffer Overflow Write Verified Recovery

- key: `generic_crash x parser_reached`
- outcome: verified recovery
- success_count: 1
- failure_count: 0
- formats: [[haproxy-config]]
- harnesses: [[libfuzzer]]

## Failure Shape
Satisfy the harness minimum-size gate, then feed the config parser a physical line that reaches the line-buffer continuation path while its C-string logical length is empty. This decouples the read length from the parser's newline-trimming pointer arithmetic and makes the trailing-line terminator write before the allocated line buffer.

## Policy
For `generic_crash x parser_reached` on `haproxy-config`, preserve the parser and harness gates first, then change the causal invariant identified by the verified recovery. Prefer `construct` while this format and harness contract are present.

## Procedure
1. Preserve the `haproxy-config` carrier enough for the `libfuzzer` harness to reach the observed parser path.
2. Keep unrelated envelope fields minimal and stable so verifier feedback stays tied to the target sink.
3. Apply the verified invariant from the failure shape before broad mutation.
4. Submit only candidates where the vulnerable image reaches the target relation and the fixed image rejects or avoids it.

## Verifier Contract
The official vulnerable-versus-fixed target match is the confirmation gate for this policy; local crash class is supporting evidence only.

## Negative Memory
- Do not corrupt the outer `haproxy-config` recognition gate while retargeting this signal.
- Do not treat off-target crashes, clean parser exits, or both-image crashes as success for this policy.
- Never store raw payload bytes, exact offsets, checksums, or task-local identifiers in memory.

## Evidence Shape
- Support: 1 server-verified round 22 solve after 8 attempts.
- Scope: generator repair only.
