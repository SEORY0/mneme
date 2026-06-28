---
type: causal-policy
title: "No Crash Template Parser Reached No Heap Overflow Lwan Template Negative Memory"
description: "Round 20 negative memory for no_crash with verifier signal template_parser_reached_no_heap_overflow."
failure_class: "no_crash"
verifier_signal: "template_parser_reached_no_heap_overflow"
candidate_family: "seed_mutate"
input_format: "lwan-template"
harness_convention: "libfuzzer"
vuln_class: "heap-buffer-overflow-write"
access_scope: generate
success_count: 0
confidence: medium
tags: ["no-crash", "template-parser-reached-no-heap-overflow", "lwan-template", "negative-memory", "round-20"]
match_keys: ["no-crash", "template-parser-reached-no-heap-overflow", "lwan-template"]
allowed_scopes: [generate]
forbidden_fields: [raw_poc_bytes, task_id, exact_offset, checksum, submit_metadata]
evidence_level: medium
train_only: true
round: 20
---
# No Crash Template Parser Reached No Heap Overflow Lwan Template Negative Memory

- key: `no_crash x template_parser_reached_no_heap_overflow`
- outcome: persistent failure basin to avoid
- success_count: 0
- failure_count: 1
- formats: [[lwan-template]]
- harnesses: [[libfuzzer]]

## Dead End
The round 20 attempts for `lwan-template` under `libfuzzer` did not produce a verified target match. Do not promote these attempts into positive recovery without a future server-verified solve.

## Diagnosed Basin
- Valid corpus templates and malformed mutations reached the template lexer/parser and produced parser diagnostics for unmatched sections, long identifiers, partial includes, negation mismatches, and quote handling, but the compiler rejected them cleanly or compiled/freed them without overflowing.

## Negative Policy
When retrieval matches `no_crash x template_parser_reached_no_heap_overflow`, avoid repeating this basin. First re-check the harness contract, format gate, and sink-specific dispatch condition. If the candidate only produces clean execution, wrapper-only crashes, off-target crashes, or an unverified recon state, retarget the carrier or abandon this family rather than scaling the same mutation.

## Retarget Hints
- Preserve factual format and harness gates from [[lwan-template]] and [[libfuzzer]].
- Prefer a different dispatch route or seed family unless new verifier feedback shows the target path is reached.
- Treat generic local crashes, clean exits, and `not_verified` recon states as non-success until official vulnerable-versus-fixed confirmation.

## Evidence Shape
- Support: 1 round 20 failed trace(s) with concrete diagnosis.
- Scope: generator avoidance only.
