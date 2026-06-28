---
type: causal-policy
title: "Cil Seed Mutate Target Sink Match Heap Buffer Overflow Read Verified Recovery"
description: "Round 23 verified recovery for generic_crash with verifier signal target_sink_match."
failure_class: "generic_crash"
verifier_signal: "target_sink_match"
candidate_family: "seed_mutate"
input_format: "cil"
harness_convention: "libfuzzer"
vuln_class: "heap-buffer-overflow-read"
access_scope: generate
success_count: 1
confidence: medium
tags: ["generic-crash", "target-sink-match", "cil", "libfuzzer", "seed-mutate", "verified-recovery", "round-23"]
match_keys: ["generic-crash", "target-sink-match", "cil", "libfuzzer", "heap-buffer-overflow-read"]
allowed_scopes: [generate]
forbidden_fields: [raw_poc_bytes, task_id, exact_offset, checksum, submit_metadata]
evidence_level: high
train_only: true
round: 23
---
# Cil Seed Mutate Target Sink Match Heap Buffer Overflow Read Verified Recovery

- key: `generic_crash x target_sink_match`
- outcome: verified recovery
- success_count: 1
- failure_count: 0
- formats: [[cil]]
- harnesses: [[libfuzzer]]

## Failure Shape
Start from a valid CIL policy seed so policy compilation reaches post-processing. Mutate a file context path pattern so it ends with an escape character; the post file-context path handling advances past the string boundary while normalizing or sorting file contexts.

## Policy
For `generic_crash x target_sink_match` on `cil`, preserve the format recognition, harness contract, and parser reachability gates before varying the causal invariant. Prefer `seed_mutate` while this format and harness contract are present.

## Procedure
1. Preserve the `cil` carrier enough for the `libfuzzer` harness to reach the observed parser path.
2. Keep envelope fields minimal and internally consistent so verifier feedback remains tied to the target relation.
3. Apply the verified invariant from the failure shape before broad mutation.
4. Submit only candidates where the vulnerable image reaches the target relation and the fixed image rejects or avoids it.

## Verifier Contract
The official vulnerable-versus-fixed target match is the confirmation gate for this policy; local crash class is supporting evidence only.

## Negative Memory
- Do not corrupt the outer `cil` recognition gate while retargeting this signal.
- Do not treat off-target crashes, clean parser exits, fixed-build crashes, or both-image crashes as success for this policy.
- Never store raw payload bytes, exact offsets, checksums, or task-local identifiers in memory.

## Evidence Shape
- Support: 1 server-verified round 23 solve after 1 attempts.
- Scope: generator repair only.
