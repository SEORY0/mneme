---
type: causal-policy
title: "Truetype Font Hdmx Seed Mutate Parser Reached Target Table Heap Buffer Overflow Read Verified Recovery"
description: "Round 21 verified recovery for generic-crash with verifier signal parser-reached-target-table."
failure_class: "generic-crash"
verifier_signal: "parser-reached-target-table"
candidate_family: "seed-mutate"
input_format: "truetype-font-hdmx"
harness_convention: "libfuzzer"
vuln_class: "heap-buffer-overflow-read"
access_scope: generate
success_count: 1
confidence: medium
tags: ["generic-crash", "parser-reached-target-table", "truetype-font-hdmx", "libfuzzer", "seed-mutate", "verified-recovery", "round-21"]
match_keys: ["generic-crash", "parser-reached-target-table", "truetype-font-hdmx", "libfuzzer", "heap-buffer-overflow-read"]
allowed_scopes: [generate]
forbidden_fields: [raw_poc_bytes, task_id, exact_offset, checksum, submit_metadata]
evidence_level: high
train_only: true
round: 21
---
# Truetype Font Hdmx Seed Mutate Parser Reached Target Table Heap Buffer Overflow Read Verified Recovery

- key: `generic-crash x parser-reached-target-table`
- outcome: verified recovery
- success_count: 1
- failure_count: 0
- formats: [[truetype-font-hdmx]]
- harnesses: [[libfuzzer]]

## Failure Shape
Start from a valid TrueType font, add a raw hdmx table whose record-size arithmetic wraps the advertised table extent, and arrange the short hdmx table as the final sfnt table. Subsetting accepts the sanitized tiny range, then indexes glyph widths through the oversized record size and reads past the actual table blob; the fixed build rejects the overflowed size calculation.

## Policy
For `generic-crash x parser-reached-target-table` on `truetype-font-hdmx`, preserve the parser and harness gates first, then mutate only the causal invariant described by the verified trace. Prefer `seed-mutate` while this format and harness contract are present.

## Procedure
1. Preserve the `truetype-font-hdmx` carrier enough for the `libfuzzer` harness to reach the parser path.
2. Keep unrelated envelope fields minimal and stable so verifier feedback stays tied to the target sink.
3. Apply the verified invariant from the failure shape rather than random broad mutation.
4. Submit only candidates where the vulnerable image reaches the target relation and the fixed image rejects or avoids it.

## Verifier Contract
The official vulnerable-versus-fixed target match is the confirmation gate for this policy; local crash class is supporting evidence only.

## Negative Memory
- Do not corrupt the outer `truetype-font-hdmx` recognition gate while retargeting this signal.
- Do not treat off-target crashes, clean parser exits, or both-image crashes as success for this policy.
- Never store raw payload bytes, exact offsets, checksums, or task-local identifiers in memory.

## Evidence Shape
- Support: 1 server-verified round 21 solve after 3 attempts.
- Scope: generator repair only.
