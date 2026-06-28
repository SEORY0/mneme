---
type: causal-policy
title: "Sudoers Policy Construct Parser Reached Invalid Free Verified Recovery"
description: "Round 22 verified recovery for generic_crash with verifier signal parser_reached."
failure_class: "generic_crash"
verifier_signal: "parser_reached"
candidate_family: "construct"
input_format: "sudoers-policy"
harness_convention: "libfuzzer"
vuln_class: "invalid-free"
access_scope: generate
success_count: 1
confidence: medium
tags: ["generic-crash", "parser-reached", "sudoers-policy", "libfuzzer", "construct", "verified-recovery", "round-22"]
match_keys: ["generic-crash", "parser-reached", "sudoers-policy", "libfuzzer", "invalid-free"]
allowed_scopes: [generate]
forbidden_fields: [raw_poc_bytes, task_id, exact_offset, checksum, submit_metadata]
evidence_level: high
train_only: true
round: 22
---
# Sudoers Policy Construct Parser Reached Invalid Free Verified Recovery

- key: `generic_crash x parser_reached`
- outcome: verified recovery
- success_count: 1
- failure_count: 0
- formats: [[sudoers-policy]]
- harnesses: [[libfuzzer]]

## Failure Shape
Use the raw sudoers grammar, not the policy line-decoder format. Match the harness's pre-seeded user and command, include the expected command arguments, and attach a CHROOT option to the command spec. The fuzzer then performs lookup and privilege display; the vulnerable stub reports the command as found without replacing the command path for the chrooted lookup, leaving stale ownership that is freed during lookup cleanup.

## Policy
For `generic_crash x parser_reached` on `sudoers-policy`, preserve the parser and harness gates first, then change the causal invariant identified by the verified recovery. Prefer `construct` while this format and harness contract are present.

## Procedure
1. Preserve the `sudoers-policy` carrier enough for the `libfuzzer` harness to reach the observed parser path.
2. Keep unrelated envelope fields minimal and stable so verifier feedback stays tied to the target sink.
3. Apply the verified invariant from the failure shape before broad mutation.
4. Submit only candidates where the vulnerable image reaches the target relation and the fixed image rejects or avoids it.

## Verifier Contract
The official vulnerable-versus-fixed target match is the confirmation gate for this policy; local crash class is supporting evidence only.

## Negative Memory
- Do not corrupt the outer `sudoers-policy` recognition gate while retargeting this signal.
- Do not treat off-target crashes, clean parser exits, or both-image crashes as success for this policy.
- Never store raw payload bytes, exact offsets, checksums, or task-local identifiers in memory.

## Evidence Shape
- Support: 1 server-verified round 22 solve after 12 attempts.
- Scope: generator repair only.
