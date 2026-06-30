---
type: causal-policy
title: "Ldif Construct Text Parser Reached Target Stack Null Dereference Write Verified Recovery"
description: "Round 28 verified recovery for generic_crash with verifier signal parser_reached_target_stack."
failure_class: "generic_crash"
verifier_signal: "parser_reached_target_stack"
candidate_family: "construct_text"
input_format: "ldif"
harness_convention: "libfuzzer-raw-file"
vuln_class: "null-dereference-write"
access_scope: generate
success_count: 1
confidence: high
tags: ["generic-crash", "parser-reached-target-stack", "ldif", "libfuzzer-raw-file", "construct-text", "null-dereference-write", "verified-recovery", "round-28"]
match_keys: ["generic_crash", "parser_reached_target_stack", "ldif", "libfuzzer-raw-file", "null-dereference-write", "verified_recovery", "construct", "null-pointer-dereference"]
allowed_scopes: [generate]
forbidden_fields: [raw_poc_bytes, task_id, exact_offset, checksum, submit_metadata]
evidence_level: high
train_only: true
round: 28
---
# Ldif Construct Text Parser Reached Target Stack Null Dereference Write Verified Recovery

## Policy
For `generic_crash x parser_reached_target_stack`, preserve the format and harness gates that reached the parser or sink, then apply the verified causal relation below. This is a positive recovery policy because the official vulnerable/fixed verifier recorded a target match.

## Procedure
1. Use a syntactically valid LDIF text entry that reaches EOF without completing any non-default sudoRole. The parser initializes its role caches and then calls the role conversion routine with an empty role list; the vulnerable conversion path dereferences the missing role array entry, while the fixed build skips conversion when there are no roles.
2. Keep the carrier abstract: preserve the gate, invariant, and sink relation rather than task-local bytes, exact offsets, checksums, or identifiers.
3. If the verifier signal changes, re-rank against the new failure key before mutating unrelated fields.

## Format Contract
- Format [[ldif]]: The harness accepts raw text as an LDIF file. LDIF lines are parsed as alphabetic attribute names followed by a colon and an optional value, with blank lines or EOF terminating an entry. A completed sudoRole requires the sudoRole object class and the required user, host, and command attributes; entries without that object class or without the required role attributes do not become completed roles.
- Harness [[libfuzzer-raw-file]]: libFuzzer bytes are written unchanged to a temporary file. The harness only requires a small minimum size, opens the file as binary input, initializes the sudoers parser, and calls the LDIF parser directly. There is no FuzzedDataProvider layout, checksum, command-line argument, or additional envelope.

## Negative Memory
- Do not broaden mutations after parser or harness reachability is proven.
- Do not submit candidates that reproduce on the fixed image, crash both images, or move to an off-target wrapper crash.
- Do not store payload bytes, exact offsets, checksums, or task-local identifiers.

## Evidence Shape
- Support: one round-28 worker trace with official target match.
- Scope: generator repair for the same failure-keyed basin; pair with [[ldif]] and [[libfuzzer-raw-file]].
