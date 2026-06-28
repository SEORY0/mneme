---
type: causal-policy
title: "Rollei Raw Text Header Construct Parser Reached Stack Buffer Overflow Read Verified Recovery"
description: "Round 22 verified recovery for generic_crash with verifier signal parser_reached."
failure_class: "generic_crash"
verifier_signal: "parser_reached"
candidate_family: "construct"
input_format: "rollei-raw-text-header"
harness_convention: "libfuzzer"
vuln_class: "stack-buffer-overflow-read"
access_scope: generate
success_count: 1
confidence: medium
tags: ["generic-crash", "parser-reached", "rollei-raw-text-header", "libfuzzer", "construct", "verified-recovery", "round-22"]
match_keys: ["generic-crash", "parser-reached", "rollei-raw-text-header", "libfuzzer", "stack-buffer-overflow-read"]
allowed_scopes: [generate]
forbidden_fields: [raw_poc_bytes, task_id, exact_offset, checksum, submit_metadata]
evidence_level: high
train_only: true
round: 22
---
# Rollei Raw Text Header Construct Parser Reached Stack Buffer Overflow Read Verified Recovery

- key: `generic_crash x parser_reached`
- outcome: verified recovery
- success_count: 1
- failure_count: 0
- formats: [[rollei-raw-text-header]]
- harnesses: [[libfuzzer]]

## Failure Shape
Select the Rollei parser with the expected text signature, then provide a boundary-sized header line that is not terminated before the parser scans it. The vulnerable parser searches past the local line buffer, while the fixed build handles the line boundary cleanly.

## Policy
For `generic_crash x parser_reached` on `rollei-raw-text-header`, preserve the parser and harness gates first, then change the causal invariant identified by the verified recovery. Prefer `construct` while this format and harness contract are present.

## Procedure
1. Preserve the `rollei-raw-text-header` carrier enough for the `libfuzzer` harness to reach the observed parser path.
2. Keep unrelated envelope fields minimal and stable so verifier feedback stays tied to the target sink.
3. Apply the verified invariant from the failure shape before broad mutation.
4. Submit only candidates where the vulnerable image reaches the target relation and the fixed image rejects or avoids it.

## Verifier Contract
The official vulnerable-versus-fixed target match is the confirmation gate for this policy; local crash class is supporting evidence only.

## Negative Memory
- Do not corrupt the outer `rollei-raw-text-header` recognition gate while retargeting this signal.
- Do not treat off-target crashes, clean parser exits, or both-image crashes as success for this policy.
- Never store raw payload bytes, exact offsets, checksums, or task-local identifiers in memory.

## Evidence Shape
- Support: 1 server-verified round 22 solve after 2 attempts.
- Scope: generator repair only.
