---
type: causal-policy
title: "Lwan Template Construct Boundary Wrong Sink Parser Reached Harness Boundary Overflow Global Buffer Overflow Write Verified Recovery"
description: "Round 34 verified recovery for lwan-template when wrong_sink pairs with parser_reached_harness_boundary_overflow."
failure_class: "wrong_sink"
verifier_signal: "parser_reached_harness_boundary_overflow"
candidate_family: "construct-boundary"
input_format: "lwan-template"
harness_convention: "libfuzzer"
vuln_class: "global-buffer-overflow-write"
access_scope: generate
success_count: 1
confidence: high
tags: ["wrong-sink", "parser-reached-harness-boundary-overflow", "lwan-template", "libfuzzer", "construct-boundary", "verified-recovery", "round-34"]
match_keys: ["wrong-sink", "parser-reached-harness-boundary-overflow", "lwan-template", "libfuzzer", "construct-boundary", "global-buffer-overflow-write", "verified-recovery"]
allowed_scopes: [generate]
forbidden_fields: [raw_poc_bytes, task_id, exact_offset, checksum, submit_metadata]
evidence_level: high
train_only: true
round: 34
---
# Lwan Template Construct Boundary Wrong Sink Parser Reached Harness Boundary Overflow Global Buffer Overflow Write Verified Recovery

- key: `wrong_sink x parser_reached_harness_boundary_overflow`
- outcome: server-verified vulnerable/fixed split
- success_count: 1
- related format facts: [[lwan-template]]
- related harness facts: [[libfuzzer]]

## Round 34 Verified Support

- key: `wrong_sink x parser_reached_harness_boundary_overflow`
- outcome: server-verified vulnerable/fixed split
- candidate family: `construct-boundary`
- vulnerability class: `global-buffer-overflow-write`
- related format facts: [[lwan-template]]
- related harness facts: [[libfuzzer]]

### Policy
When `wrong_sink x parser_reached_harness_boundary_overflow` appears for `lwan-template`, preserve the accepted parser and harness gates, then target the specific state relation that the verifier proved. Treat the official vulnerable-only target match as the success gate; local crash class alone is not enough.

### Procedure
1. Use the [[libfuzzer]] harness contract and the [[lwan-template]] format contract before changing sink fields.
2. Recreate the verified causal relation: Reachability did not require a semantically rich template. The raw libFuzzer input had to sit exactly on the harness copy-buffer boundary: the copy itself remains accepted, then the harness appends its terminator past the fixed global buffer before ordinary template parsing matters.
3. Keep selectors, lengths, state setup, and container invariants coherent until the target parser state is reached.
4. Submit only when the candidate is expected to preserve the vulnerable/fixed split rather than a generic both-build crash.

### Format Contract
Lwan templates use Mustache-like markers for variables, unescaped variables, sections, inverted sections, comments, and partials. Parser-visible identifiers are matched against a descriptor table, and malformed or unknown tags can be rejected cleanly. For this task the decisive invariant was the harness pre-parser copy and terminator behavior, not a template grammar invariant.

### Harness Contract
The libFuzzer harness consumes raw file bytes with no mode byte and no FuzzedDataProvider splitting. It copies the input into a fixed global character buffer, appends a NUL terminator, then calls the template compiler with a fixed descriptor table.

### Evidence Shape
- Support: one server-verified round 34 solve.
- Candidate family: `construct-boundary`.
- Verifier key: `wrong_sink x parser_reached_harness_boundary_overflow`.
- Vulnerability class: `global-buffer-overflow-write`.

## Negative Memory
- Do not count parser reachability, both-image crashes, fixed-image crashes, local wrapper crashes, clean exits, or off-target sanitizer crashes as success for this key.
- Do not store concrete payload bytes, exact positions, task identifiers, checksums, or submit metadata.
