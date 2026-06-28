---
type: causal-policy
title: "Redis Format String Construct Target Match On Submit Uninitialized Pointer Free Verified Recovery"
description: "Round 21 verified recovery for generic-crash with verifier signal target-match-on-submit."
failure_class: "generic-crash"
verifier_signal: "target-match-on-submit"
candidate_family: "construct"
input_format: "redis-format-string"
harness_convention: "libfuzzer"
vuln_class: "uninitialized-pointer-free"
access_scope: generate
success_count: 1
confidence: medium
tags: ["generic-crash", "target-match-on-submit", "redis-format-string", "libfuzzer", "construct", "verified-recovery", "round-21"]
match_keys: ["generic-crash", "target-match-on-submit", "redis-format-string", "libfuzzer", "uninitialized-pointer-free"]
allowed_scopes: [generate]
forbidden_fields: [raw_poc_bytes, task_id, exact_offset, checksum, submit_metadata]
evidence_level: high
train_only: true
round: 21
---
# Redis Format String Construct Target Match On Submit Uninitialized Pointer Free Verified Recovery

- key: `generic-crash x target-match-on-submit`
- outcome: verified recovery
- success_count: 1
- failure_count: 0
- formats: [[redis-format-string]]
- harnesses: [[libfuzzer]]

## Failure Shape
Use a raw Redis command format string that first builds ordinary command arguments and then hits an invalid printf-style conversion. The format parser returns an error without producing a valid command pointer, and the harness cleanup observes the uninitialized target pointer only in the vulnerable build.

## Policy
For `generic-crash x target-match-on-submit` on `redis-format-string`, preserve the parser and harness gates first, then mutate only the causal invariant described by the verified trace. Prefer `construct` while this format and harness contract are present.

## Procedure
1. Preserve the `redis-format-string` carrier enough for the `libfuzzer` harness to reach the parser path.
2. Keep unrelated envelope fields minimal and stable so verifier feedback stays tied to the target sink.
3. Apply the verified invariant from the failure shape rather than random broad mutation.
4. Submit only candidates where the vulnerable image reaches the target relation and the fixed image rejects or avoids it.

## Verifier Contract
The official vulnerable-versus-fixed target match is the confirmation gate for this policy; local crash class is supporting evidence only.

## Negative Memory
- Do not corrupt the outer `redis-format-string` recognition gate while retargeting this signal.
- Do not treat off-target crashes, clean parser exits, or both-image crashes as success for this policy.
- Never store raw payload bytes, exact offsets, checksums, or task-local identifiers in memory.

## Evidence Shape
- Support: 1 server-verified round 21 solve after 7 attempts.
- Scope: generator repair only.
