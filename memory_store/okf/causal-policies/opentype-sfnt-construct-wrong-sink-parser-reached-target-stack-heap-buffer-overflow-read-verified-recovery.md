---
type: causal-policy
title: "Opentype Sfnt Construct Wrong Sink Parser Reached Target Stack Heap Buffer Overflow Read Verified Recovery"
description: "Round 30 verified recovery for wrong_sink with verifier signal parser_reached_target_stack."
failure_class: "wrong_sink"
verifier_signal: "parser_reached_target_stack"
candidate_family: "construct"
input_format: "opentype-sfnt"
harness_convention: "libfuzzer"
vuln_class: "heap-buffer-overflow-read"
access_scope: generate
success_count: 1
confidence: medium
tags: ["wrong-sink", "parser-reached-target-stack", "opentype-sfnt", "libfuzzer", "construct", "verified-recovery", "round-30"]
match_keys: ["wrong-sink", "parser-reached-target-stack", "opentype-sfnt", "libfuzzer", "heap-buffer-overflow-read"]
allowed_scopes: [generate]
forbidden_fields: [raw_poc_bytes, task_id, exact_offset, checksum, submit_metadata]
evidence_level: high
train_only: true
round: 30
---
# Opentype Sfnt Construct Wrong Sink Parser Reached Target Stack Heap Buffer Overflow Read Verified Recovery

- key: `wrong-sink x parser-reached-target-stack`
- outcome: verified recovery
- success_count: 1
- failure_count: 0
- formats: [[opentype-sfnt]]
- harnesses: [[libfuzzer]]

## Failure Shape
Build a minimal but coherent SFNT/OpenType font so the loader accepts the required table directory and reaches cmap parsing. Keep the mandatory font tables structurally consistent, then place a cmap table whose encoding record starts a multi-byte subtable-offset field close enough to the table boundary that the first byte is in range but the full word read crosses the allocation boundary.

## Policy
For `wrong-sink x parser-reached-target-stack` on `opentype-sfnt`, preserve the parser and harness gates first, then mutate only the causal invariant described by the verified trace. Prefer `construct` while this format and harness contract are present.

## Procedure
1. Preserve the `opentype-sfnt` carrier enough for the `libfuzzer` harness to reach the parser path.
2. Keep unrelated envelope fields minimal and stable so verifier feedback stays tied to the target sink.
3. Apply the verified invariant from the failure shape rather than random broad mutation.
4. Submit only candidates where the vulnerable image reaches the target relation and the fixed image rejects or avoids it.

## Verifier Contract
The local class may remain coarse. Treat the official vulnerable-versus-fixed target match as the confirmation gate for this policy.

## Negative Memory
- Do not corrupt the outer `opentype-sfnt` recognition gate while retargeting this signal.
- Do not treat off-target crashes, clean parser reachability, or both-image crashes as success for this policy.
- Never store raw payload bytes, exact offsets, checksums, or task-local identifiers in memory.

## Evidence Shape
- Support: 1 server-verified solve(s), including round 30.
- Scope: generator repair only.
