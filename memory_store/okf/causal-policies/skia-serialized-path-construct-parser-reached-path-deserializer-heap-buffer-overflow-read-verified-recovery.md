---
type: causal-policy
title: "Skia Serialized Path Construct Parser Reached Path Deserializer Heap Buffer Overflow Read Verified Recovery"
description: "Round 23 verified recovery for wrong_sink with verifier signal parser_reached_path_deserializer."
failure_class: "wrong_sink"
verifier_signal: "parser_reached_path_deserializer"
candidate_family: "construct"
input_format: "skia-serialized-path"
harness_convention: "libfuzzer"
vuln_class: "heap-buffer-overflow-read"
access_scope: generate
success_count: 1
confidence: medium
tags: ["wrong-sink", "parser-reached-path-deserializer", "skia-serialized-path", "libfuzzer", "construct", "verified-recovery", "round-23"]
match_keys: ["wrong-sink", "parser-reached-path-deserializer", "skia-serialized-path", "libfuzzer", "heap-buffer-overflow-read"]
allowed_scopes: [generate]
forbidden_fields: [raw_poc_bytes, task_id, exact_offset, checksum, submit_metadata]
evidence_level: high
train_only: true
round: 23
---
# Skia Serialized Path Construct Parser Reached Path Deserializer Heap Buffer Overflow Read Verified Recovery

- key: `wrong_sink x parser_reached_path_deserializer`
- outcome: verified recovery
- success_count: 1
- failure_count: 0
- formats: [[skia-serialized-path]]
- harnesses: [[libfuzzer]]

## Failure Shape
Use the public SkPath serialization layout with a valid current-version general-path header and byte counts that satisfy buffer validation, but make the verb stream require more points than the serialized point count provides. The deserializer reconstructs the path by verb semantics and reads past the available point array.

## Policy
For `wrong_sink x parser_reached_path_deserializer` on `skia-serialized-path`, preserve the format recognition, harness contract, and parser reachability gates before varying the causal invariant. Prefer `construct` while this format and harness contract are present.

## Procedure
1. Preserve the `skia-serialized-path` carrier enough for the `libfuzzer` harness to reach the observed parser path.
2. Keep envelope fields minimal and internally consistent so verifier feedback remains tied to the target relation.
3. Apply the verified invariant from the failure shape before broad mutation.
4. Submit only candidates where the vulnerable image reaches the target relation and the fixed image rejects or avoids it.

## Verifier Contract
The official vulnerable-versus-fixed target match is the confirmation gate for this policy; local crash class is supporting evidence only.

## Negative Memory
- Do not corrupt the outer `skia-serialized-path` recognition gate while retargeting this signal.
- Do not treat off-target crashes, clean parser exits, fixed-build crashes, or both-image crashes as success for this policy.
- Never store raw payload bytes, exact offsets, checksums, or task-local identifiers in memory.

## Evidence Shape
- Support: 1 server-verified round 23 solve after 1 attempts.
- Scope: generator repair only.
