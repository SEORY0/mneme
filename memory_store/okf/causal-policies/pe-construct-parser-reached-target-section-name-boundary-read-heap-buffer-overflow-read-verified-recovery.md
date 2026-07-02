---
type: causal-policy
title: "PE Construct Parser Reached Target Section Name Boundary Read Heap Buffer Overflow Read Verified Recovery"
description: "Round 29 verified recovery for wrong_sink with verifier signal parser_reached_target_section_name_boundary_read."
failure_class: "wrong_sink"
verifier_signal: "parser_reached_target_section_name_boundary_read"
candidate_family: "construct"
input_format: "pe"
harness_convention: "libfuzzer"
vuln_class: "heap-buffer-overflow-read"
access_scope: generate
success_count: 1
confidence: high
tags: ["wrong-sink", "parser-reached-target-section-name-boundary-read", "pe", "libfuzzer", "construct", "heap-buffer-overflow-read", "verified-recovery", "round-29"]
match_keys: ["wrong_sink", "parser_reached_target_section_name_boundary_read", "pe", "libfuzzer", "heap-buffer-overflow-read", "wrong-sink", "parser-reached-target-section-name-boundary-read", "pe", "libfuzzer", "heap-buffer-overflow-read", "verified_recovery", "construct", "construct"]
allowed_scopes: [generate]
forbidden_fields: [raw_poc_bytes, task_id, exact_offset, checksum, submit_metadata]
evidence_level: high
train_only: true
round: 29
---
# PE Construct Parser Reached Target Section Name Boundary Read Heap Buffer Overflow Read Verified Recovery

- key: `wrong_sink x parser_reached_target_section_name_boundary_read`
- outcome: verified target match / recovery policy
- success_count: 1
- related format facts: [[pe]]
- related harness facts: [[libfuzzer]]

## Policy
For `wrong_sink x parser_reached_target_section_name_boundary_read` on `pe`, keep the parser and harness gates that produced the verifier signal, then vary only the causal relation described below. This is a positive recovery policy because the official vulnerable/fixed verifier recorded a target match.

## Procedure
1. Construct a minimal PE that satisfies the harness rule for translating a section RVA to its raw offset, then make the section name use the COFF long-name lookup path. Arrange the long-name string pointer at the end of the mapped input so the precedence-bugged bounds macro accepts a one-byte read past the buffer when the name loop asks for the next byte.
2. Preserve format recognition and the harness input contract while mutating the narrow sink invariant; do not broaden into an off-target crash or a both-image crash.
3. If later verifier output changes the failure key, re-rank against that new key before mutating unrelated fields.

## Format Contract
- Format [[pe]]: A PE input needs an MZ header, a PE signature reached through the DOS header pointer, a COFF header, an optional header, and a section table. YARA resolves slash-prefixed section names through the COFF symbol/string-table convention, while section address translation depends on the section virtual address, raw-data offset, and size fields being mutually consistent.
- Harness [[libfuzzer]]: The libFuzzer harness scans the raw input bytes with a fixed YARA rule that imports the PE module and reads section metadata. There is no FuzzedDataProvider splitting for this target; parser reachability depends on making the raw buffer look enough like a PE for the module to expose the first section.

## Negative Memory
- Do not corrupt the outer `pe` recognition gate while retargeting this signal.
- Do not count parser reachability, clean exits, fixed-image crashes, both-image crashes, or local wrong-sink labels as success without official target match.
- Never store payload bytes, exact positions, checksums, submit metadata, or task-local identifiers.

## Evidence Shape
- Support: one round-29 worker trace with official target match.
- Scope: generator repair and retargeting only; pair with [[pe]] and [[libfuzzer]].
