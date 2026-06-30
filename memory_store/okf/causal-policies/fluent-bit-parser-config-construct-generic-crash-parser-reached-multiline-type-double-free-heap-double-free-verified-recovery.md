---
type: causal-policy
title: "Fluent Bit Parser Config Construct Generic Crash Parser Reached Multiline Type Double Free Heap Double Free Verified Recovery"
description: "Round 30 verified recovery for generic_crash with verifier signal parser_reached_multiline_type_double_free."
failure_class: "generic_crash"
verifier_signal: "parser_reached_multiline_type_double_free"
candidate_family: "construct"
input_format: "fluent-bit-parser-config"
harness_convention: "libfuzzer-config-random"
vuln_class: "heap-double-free"
access_scope: generate
success_count: 1
confidence: medium
tags: ["generic-crash", "parser-reached-multiline-type-double-free", "fluent-bit-parser-config", "libfuzzer-config-random", "construct", "verified-recovery", "round-30"]
match_keys: ["generic-crash", "parser-reached-multiline-type-double-free", "fluent-bit-parser-config", "libfuzzer-config-random", "heap-double-free"]
allowed_scopes: [generate]
forbidden_fields: [raw_poc_bytes, task_id, exact_offset, checksum, submit_metadata]
evidence_level: high
train_only: true
round: 30
---
# Fluent Bit Parser Config Construct Generic Crash Parser Reached Multiline Type Double Free Heap Double Free Verified Recovery

- key: `generic-crash x parser-reached-multiline-type-double-free`
- outcome: verified recovery
- success_count: 1
- failure_count: 0
- formats: [[fluent-bit-parser-config]]
- harnesses: [[libfuzzer-config-random]]

## Failure Shape
Use the config-random parser harness contract: the file bytes are a Fluent Bit parser configuration. Build a syntactically valid multiline parser section with the required name and type keys, but set the type key to an unsupported token. This reaches the type-validation error path after the temporary value is allocated; the vulnerable cleanup destroys that same temporary value before and inside the shared error label, while the fixed build avoids the duplicate free.

## Policy
For `generic-crash x parser-reached-multiline-type-double-free` on `fluent-bit-parser-config`, preserve the parser and harness gates first, then mutate only the causal invariant described by the verified trace. Prefer `construct` while this format and harness contract are present.

## Procedure
1. Preserve the `fluent-bit-parser-config` carrier enough for the `libfuzzer-config-random` harness to reach the parser path.
2. Keep unrelated envelope fields minimal and stable so verifier feedback stays tied to the target sink.
3. Apply the verified invariant from the failure shape rather than random broad mutation.
4. Submit only candidates where the vulnerable image reaches the target relation and the fixed image rejects or avoids it.

## Verifier Contract
The local class may remain coarse. Treat the official vulnerable-versus-fixed target match as the confirmation gate for this policy.

## Negative Memory
- Do not corrupt the outer `fluent-bit-parser-config` recognition gate while retargeting this signal.
- Do not treat off-target crashes, clean parser reachability, or both-image crashes as success for this policy.
- Never store raw payload bytes, exact offsets, checksums, or task-local identifiers in memory.

## Evidence Shape
- Support: 1 server-verified solve(s), including round 30.
- Scope: generator repair only.
