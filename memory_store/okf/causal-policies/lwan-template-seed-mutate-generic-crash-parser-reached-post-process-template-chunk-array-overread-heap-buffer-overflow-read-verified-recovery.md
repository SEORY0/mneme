---
type: causal-policy
title: "Lwan Template Seed Mutate Generic Crash Parser Reached Post Process Template Chunk Array Overread Heap Buffer Overflow Read Verified Recovery"
description: "Round 34 verified recovery for lwan-template when generic_crash pairs with parser_reached_post_process_template_chunk_array_overread."
failure_class: "generic_crash"
verifier_signal: "parser_reached_post_process_template_chunk_array_overread"
candidate_family: "seed_mutate"
input_format: "lwan-template"
harness_convention: "libfuzzer"
vuln_class: "heap-buffer-overflow-read"
access_scope: generate
success_count: 1
confidence: high
tags: ["generic-crash", "parser-reached-post-process-template-chunk-array-overread", "lwan-template", "libfuzzer", "seed-mutate", "verified-recovery", "round-34"]
match_keys: ["generic-crash", "parser-reached-post-process-template-chunk-array-overread", "lwan-template", "libfuzzer", "seed-mutate", "heap-buffer-overflow-read", "verified-recovery"]
allowed_scopes: [generate]
forbidden_fields: [raw_poc_bytes, task_id, exact_offset, checksum, submit_metadata]
evidence_level: high
train_only: true
round: 34
---
# Lwan Template Seed Mutate Generic Crash Parser Reached Post Process Template Chunk Array Overread Heap Buffer Overflow Read Verified Recovery

- key: `generic_crash x parser_reached_post_process_template_chunk_array_overread`
- outcome: server-verified vulnerable/fixed split
- success_count: 1
- related format facts: [[lwan-template]]
- related harness facts: [[libfuzzer]]

## Round 34 Verified Support

- key: `generic_crash x parser_reached_post_process_template_chunk_array_overread`
- outcome: server-verified vulnerable/fixed split
- candidate family: `seed_mutate`
- vulnerability class: `heap-buffer-overflow-read`
- related format facts: [[lwan-template]]
- related harness facts: [[libfuzzer]]

### Policy
When `generic_crash x parser_reached_post_process_template_chunk_array_overread` appears for `lwan-template`, preserve the accepted parser and harness gates, then target the specific state relation that the verifier proved. Treat the official vulnerable-only target match as the success gate; local crash class alone is not enough.

### Procedure
1. Use the [[libfuzzer]] harness contract and the [[lwan-template]] format contract before changing sink fields.
2. Recreate the verified causal relation: Start from a valid Lwan directory-list template seed so known descriptor names, conditionals, and the file-list section all parse. Mutate section delimiters so parsing accepts a start chunk whose matching terminator is absent or misclassified, while enough later text chunks force the chunk array onto heap storage. During post-processing, the vulnerable compiler scans forward looking for an end marker that is not present before the heap allocation boundary; the fixed build stops the scan cleanly.
3. Keep selectors, lengths, state setup, and container invariants coherent until the target parser state is reached.
4. Submit only when the candidate is expected to preserve the vulnerable/fixed split rather than a generic both-build crash.

### Format Contract
Lwan templates are Mustache-like text. Actions use double braces; variables must match the harness descriptor table. Conditional sections use a question suffix and close with the same name plus the question suffix. Sequence sections use a hash marker and close by name. Inverted sections use a caret before a variable or before a hash section. Partials use a greater-than marker followed by an identifier-like path. Parser errors are common for unknown variables, unmatched sections, malformed close markers, and invalid triple-brace escaping.

### Harness Contract
The libFuzzer harness passes the raw file bytes as a NUL-terminated template string capped to a fixed internal copy buffer, compiles it with a descriptor exposing path strings and a file-list sequence, then frees the compiled template. There is no mode byte, length prefix, checksum, or FuzzedDataProvider tail layout.

### Evidence Shape
- Support: one server-verified round 34 solve.
- Candidate family: `seed_mutate`.
- Verifier key: `generic_crash x parser_reached_post_process_template_chunk_array_overread`.
- Vulnerability class: `heap-buffer-overflow-read`.

## Negative Memory
- Do not count parser reachability, both-image crashes, fixed-image crashes, local wrapper crashes, clean exits, or off-target sanitizer crashes as success for this key.
- Do not store concrete payload bytes, exact positions, task identifiers, checksums, or submit metadata.
