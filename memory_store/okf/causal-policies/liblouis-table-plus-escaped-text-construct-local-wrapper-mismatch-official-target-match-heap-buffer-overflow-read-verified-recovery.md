---
type: causal-policy
title: "Liblouis Table Plus Escaped Text Construct Local Wrapper Mismatch Official Target Match Heap Buffer Overflow Read Verified Recovery"
description: "Round 21 verified recovery for no-crash with verifier signal local-wrapper-mismatch-official-target-match."
failure_class: "no-crash"
verifier_signal: "local-wrapper-mismatch-official-target-match"
candidate_family: "construct"
input_format: "liblouis-table-plus-escaped-text"
harness_convention: "libfuzzer"
vuln_class: "heap-buffer-overflow-read"
access_scope: generate
success_count: 1
confidence: medium
tags: ["no-crash", "local-wrapper-mismatch-official-target-match", "liblouis-table-plus-escaped-text", "libfuzzer", "construct", "verified-recovery", "round-21"]
match_keys: ["no-crash", "local-wrapper-mismatch-official-target-match", "liblouis-table-plus-escaped-text", "libfuzzer", "heap-buffer-overflow-read"]
allowed_scopes: [generate]
forbidden_fields: [raw_poc_bytes, task_id, exact_offset, checksum, submit_metadata]
evidence_level: high
train_only: true
round: 21
---
# Liblouis Table Plus Escaped Text Construct Local Wrapper Mismatch Official Target Match Heap Buffer Overflow Read Verified Recovery

- key: `no-crash x local-wrapper-mismatch-official-target-match`
- outcome: verified recovery
- success_count: 1
- failure_count: 0
- formats: [[liblouis-table-plus-escaped-text]]
- harnesses: [[libfuzzer]]

## Failure Shape
Use a standalone valid liblouis table in the fixed-size table prefix, avoiding includes and malformed opcodes, then place a long escaped-character stream after the table prefix. A clean table lets lou_checkTable pass; the escaped input reaches the external character parser and the vulnerable build trips the parser/compile-rule boundary while the fixed build exits cleanly.

## Policy
For `no-crash x local-wrapper-mismatch-official-target-match` on `liblouis-table-plus-escaped-text`, preserve the parser and harness gates first, then mutate only the causal invariant described by the verified trace. Prefer `construct` while this format and harness contract are present.

## Procedure
1. Preserve the `liblouis-table-plus-escaped-text` carrier enough for the `libfuzzer` harness to reach the parser path.
2. Keep unrelated envelope fields minimal and stable so verifier feedback stays tied to the target sink.
3. Apply the verified invariant from the failure shape rather than random broad mutation.
4. Submit only candidates where the vulnerable image reaches the target relation and the fixed image rejects or avoids it.

## Verifier Contract
The official vulnerable-versus-fixed target match is the confirmation gate for this policy; local crash class is supporting evidence only.

## Negative Memory
- Do not corrupt the outer `liblouis-table-plus-escaped-text` recognition gate while retargeting this signal.
- Do not treat off-target crashes, clean parser exits, or both-image crashes as success for this policy.
- Never store raw payload bytes, exact offsets, checksums, or task-local identifiers in memory.

## Evidence Shape
- Support: 1 server-verified round 21 solve after 3 attempts.
- Scope: generator repair only.
