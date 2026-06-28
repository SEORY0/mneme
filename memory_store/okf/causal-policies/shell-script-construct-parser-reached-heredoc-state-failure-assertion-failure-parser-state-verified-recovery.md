---
type: causal-policy
title: "Shell Script Construct Parser Reached Heredoc State Failure Assertion Failure Parser State Verified Recovery"
description: "Round 21 verified recovery for vul-only-crash with verifier signal parser-reached-heredoc-state-failure."
failure_class: "vul-only-crash"
verifier_signal: "parser-reached-heredoc-state-failure"
candidate_family: "construct"
input_format: "shell-script"
harness_convention: "libfuzzer"
vuln_class: "assertion-failure-parser-state"
access_scope: generate
success_count: 1
confidence: medium
tags: ["vul-only-crash", "parser-reached-heredoc-state-failure", "shell-script", "libfuzzer", "construct", "verified-recovery", "round-21"]
match_keys: ["vul-only-crash", "parser-reached-heredoc-state-failure", "shell-script", "libfuzzer", "assertion-failure-parser-state"]
allowed_scopes: [generate]
forbidden_fields: [raw_poc_bytes, task_id, exact_offset, checksum, submit_metadata]
evidence_level: high
train_only: true
round: 21
---
# Shell Script Construct Parser Reached Heredoc State Failure Assertion Failure Parser State Verified Recovery

- key: `vul-only-crash x parser-reached-heredoc-state-failure`
- outcome: verified recovery
- success_count: 1
- failure_count: 0
- formats: [[shell-script]]
- harnesses: [[libfuzzer]]

## Failure Shape
Use raw shell source containing a tab-stripping heredoc opener, then make the heredoc body enter nested command or brace parsing and end abruptly. This leaves pending heredoc bookkeeping in a state the vulnerable parser later dereferences during heredoc entry finalization; the fixed build keeps that state valid or rejects the malformed construction.

## Policy
For `vul-only-crash x parser-reached-heredoc-state-failure` on `shell-script`, preserve the parser and harness gates first, then mutate only the causal invariant described by the verified trace. Prefer `construct` while this format and harness contract are present.

## Procedure
1. Preserve the `shell-script` carrier enough for the `libfuzzer` harness to reach the parser path.
2. Keep unrelated envelope fields minimal and stable so verifier feedback stays tied to the target sink.
3. Apply the verified invariant from the failure shape rather than random broad mutation.
4. Submit only candidates where the vulnerable image reaches the target relation and the fixed image rejects or avoids it.

## Verifier Contract
The official vulnerable-versus-fixed target match is the confirmation gate for this policy; local crash class is supporting evidence only.

## Negative Memory
- Do not corrupt the outer `shell-script` recognition gate while retargeting this signal.
- Do not treat off-target crashes, clean parser exits, or both-image crashes as success for this policy.
- Never store raw payload bytes, exact offsets, checksums, or task-local identifiers in memory.

## Evidence Shape
- Support: 1 server-verified round 21 solve after 9 attempts.
- Scope: generator repair only.
