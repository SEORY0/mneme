---
type: causal-policy
title: "Git Raw Object Construct Parser Reached Target Strstr Overread Heap Buffer Overflow Read Verified Recovery"
description: "Round 19 verified recovery for wrong_sink with verifier signal parser_reached_target_strstr_overread."
failure_class: "wrong_sink"
verifier_signal: "parser_reached_target_strstr_overread"
candidate_family: "construct"
input_format: "git-raw-object"
harness_convention: "libfuzzer"
vuln_class: "heap-buffer-overflow-read"
access_scope: generate
success_count: 1
confidence: medium
tags: ["wrong-sink", "parser-reached-target-strstr-overread", "git-raw-object", "libfuzzer", "construct", "verified-recovery", "round-19"]
match_keys: ["wrong-sink", "parser-reached-target-strstr-overread", "git-raw-object", "libfuzzer", "heap-buffer-overflow-read"]
allowed_scopes: [generate]
forbidden_fields: [raw_poc_bytes, task_id, exact_offset, checksum, submit_metadata]
evidence_level: high
train_only: true
round: 19
---
# Git Raw Object Construct Parser Reached Target Strstr Overread Heap Buffer Overflow Read Verified Recovery

- key: `wrong_sink x parser_reached_target_strstr_overread`
- outcome: verified recovery
- success_count: 1
- failure_count: 0
- formats: [[git-raw-object]]
- harnesses: [[libfuzzer]]

## Failure Shape
Use the raw object-body fuzzer envelope for libgit2 tag parsing. Provide a structurally valid tag header through object, type, tag, and tagger fields, then leave a further non-message header fragment without the blank-line separator so the tag parser searches past the libFuzzer buffer boundary with an unbounded substring search.

## Policy
For `wrong_sink x parser_reached_target_strstr_overread` on `git-raw-object`, preserve the parser and harness gates first, then mutate only the causal invariant described by the verified trace. Prefer `construct` while this format and harness contract are present.

## Procedure
1. Preserve the `git-raw-object` carrier enough for the `libfuzzer` harness to reach the parser path.
2. Keep unrelated envelope fields minimal and stable so verifier feedback stays tied to the target sink.
3. Apply the verified invariant from the failure shape rather than random broad mutation.
4. Submit only candidates where the vulnerable image reaches the target relation and the fixed image rejects or avoids it.

## Verifier Contract
The local class may remain coarse. Treat the official vulnerable-versus-fixed target match as the confirmation gate for this policy.

## Negative Memory
- Do not corrupt the outer `git-raw-object` recognition gate while retargeting this signal.
- Do not treat off-target crashes or both-image crashes as success for this policy.
- Never store raw payload bytes, exact offsets, checksums, or task-local identifiers in memory.

## Evidence Shape
- Support: 1 server-verified round 19 solve.
- Scope: generator repair only.
