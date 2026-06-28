---
type: causal-policy
title: "Json Construct Target Stack High Likelihood Use Of Uninitialized Value Verified Recovery"
description: "Round 23 verified recovery for generic_crash with verifier signal target_stack_high_likelihood."
failure_class: "generic_crash"
verifier_signal: "target_stack_high_likelihood"
candidate_family: "construct"
input_format: "json"
harness_convention: "libfuzzer"
vuln_class: "use-of-uninitialized-value"
access_scope: generate
success_count: 1
confidence: medium
tags: ["generic-crash", "target-stack-high-likelihood", "json", "libfuzzer", "construct", "verified-recovery", "round-23"]
match_keys: ["generic-crash", "target-stack-high-likelihood", "json", "libfuzzer", "use-of-uninitialized-value"]
allowed_scopes: [generate]
forbidden_fields: [raw_poc_bytes, task_id, exact_offset, checksum, submit_metadata]
evidence_level: high
train_only: true
round: 23
---
# Json Construct Target Stack High Likelihood Use Of Uninitialized Value Verified Recovery

- key: `generic_crash x target_stack_high_likelihood`
- outcome: verified recovery
- success_count: 1
- failure_count: 0
- formats: [[json]]
- harnesses: [[libfuzzer]]

## Failure Shape
Provide a raw JSON string that is syntactically valid but contains a lone low-surrogate escape. The parser reaches quoted-string unicode handling and forwards an incomplete surrogate-derived codepoint to UTF-8 encoding, which consumes uninitialized state in the vulnerable build.

## Policy
For `generic_crash x target_stack_high_likelihood` on `json`, preserve the format recognition, harness contract, and parser reachability gates before varying the causal invariant. Prefer `construct` while this format and harness contract are present.

## Procedure
1. Preserve the `json` carrier enough for the `libfuzzer` harness to reach the observed parser path.
2. Keep envelope fields minimal and internally consistent so verifier feedback remains tied to the target relation.
3. Apply the verified invariant from the failure shape before broad mutation.
4. Submit only candidates where the vulnerable image reaches the target relation and the fixed image rejects or avoids it.

## Verifier Contract
The official vulnerable-versus-fixed target match is the confirmation gate for this policy; local crash class is supporting evidence only.

## Negative Memory
- Do not corrupt the outer `json` recognition gate while retargeting this signal.
- Do not treat off-target crashes, clean parser exits, fixed-build crashes, or both-image crashes as success for this policy.
- Never store raw payload bytes, exact offsets, checksums, or task-local identifiers in memory.

## Evidence Shape
- Support: 1 server-verified round 23 solve after 1 attempts.
- Scope: generator repair only.
