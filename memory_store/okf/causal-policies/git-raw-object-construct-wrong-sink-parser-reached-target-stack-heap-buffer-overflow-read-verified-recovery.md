---
type: causal-policy
title: "Git Raw Object Construct Wrong Sink Parser Reached Target Stack Heap Buffer Overflow Read Verified Recovery"
description: "Round 30 verified recovery for wrong_sink with verifier signal parser_reached_target_stack."
failure_class: "wrong_sink"
verifier_signal: "parser_reached_target_stack"
candidate_family: "construct"
input_format: "git-raw-object"
harness_convention: "afl-libfuzzer-raw-bytes"
vuln_class: "heap-buffer-overflow-read"
access_scope: generate
success_count: 1
confidence: medium
tags: ["wrong-sink", "parser-reached-target-stack", "git-raw-object", "afl-libfuzzer-raw-bytes", "construct", "verified-recovery", "round-30"]
match_keys: ["wrong-sink", "parser-reached-target-stack", "git-raw-object", "afl-libfuzzer-raw-bytes", "heap-buffer-overflow-read"]
allowed_scopes: [generate]
forbidden_fields: [raw_poc_bytes, task_id, exact_offset, checksum, submit_metadata]
evidence_level: high
train_only: true
round: 30
---
# Git Raw Object Construct Wrong Sink Parser Reached Target Stack Heap Buffer Overflow Read Verified Recovery

- key: `wrong-sink x parser-reached-target-stack`
- outcome: verified recovery
- success_count: 1
- failure_count: 0
- formats: [[git-raw-object]]
- harnesses: [[afl-libfuzzer-raw-bytes]]

## Failure Shape
Use the raw Git object parser path with a structurally valid commit object. Keep the object headers and first signature valid, then make a later signature timestamp field consist only of whitespace at the physical end of the input so the bounded numeric parser's whitespace skip walks past the supplied buffer length. Do not include trailing message bytes after the terminator.

## Policy
For `wrong-sink x parser-reached-target-stack` on `git-raw-object`, preserve the parser and harness gates first, then mutate only the causal invariant described by the verified trace. Prefer `construct` while this format and harness contract are present.

## Procedure
1. Preserve the `git-raw-object` carrier enough for the `afl-libfuzzer-raw-bytes` harness to reach the parser path.
2. Keep unrelated envelope fields minimal and stable so verifier feedback stays tied to the target sink.
3. Apply the verified invariant from the failure shape rather than random broad mutation.
4. Submit only candidates where the vulnerable image reaches the target relation and the fixed image rejects or avoids it.

## Verifier Contract
The local class may remain coarse. Treat the official vulnerable-versus-fixed target match as the confirmation gate for this policy.

## Negative Memory
- Do not corrupt the outer `git-raw-object` recognition gate while retargeting this signal.
- Do not treat off-target crashes, clean parser reachability, or both-image crashes as success for this policy.
- Never store raw payload bytes, exact offsets, checksums, or task-local identifiers in memory.

## Evidence Shape
- Support: 1 server-verified solve(s), including round 30.
- Scope: generator repair only.
