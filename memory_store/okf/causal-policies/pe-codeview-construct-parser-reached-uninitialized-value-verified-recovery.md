---
type: causal-policy
title: "Pe Codeview Construct Parser Reached Uninitialized Value Verified Recovery"
description: "Round 25 verified recovery for generic_crash with verifier signal parser_reached."
failure_class: "generic_crash"
verifier_signal: "parser_reached"
candidate_family: "construct"
input_format: "pe-codeview"
harness_convention: "libfuzzer-file-command-wrapper"
vuln_class: "uninitialized-value"
access_scope: generate
success_count: 1
confidence: medium
tags: ["generic-crash", "parser-reached", "pe-codeview", "libfuzzer-file-command-wrapper", "construct", "verified-recovery", "round-25"]
match_keys: ["generic_crash", "parser_reached", "pe-codeview", "libfuzzer-file-command-wrapper", "uninitialized-value"]
allowed_scopes: [generate]
forbidden_fields: [raw_poc_bytes, task_id, exact_offset, checksum, submit_metadata]
evidence_level: high
train_only: true
round: 25
---
# Pe Codeview Construct Parser Reached Uninitialized Value Verified Recovery

- key: `generic_crash x parser_reached`
- outcome: verified recovery
- success_count: 1
- failure_count: 0
- formats: [[pe-codeview]]
- harnesses: [[libfuzzer-file-command-wrapper]]

## Failure Shape
Construct a minimal PE image whose DOS, PE, optional-header, section, and debug-directory gates are valid. Mark the debug entry as CodeView, keep the debug directory mapped, and make the CodeView raw-data pointer refer outside readable file data so the vulnerable helper mishandles the failed read while the fixed build rejects it.

## Policy
For `generic_crash x parser_reached` on `pe-codeview`, preserve the format recognition and harness contract before varying the vulnerable invariant. Prefer `construct` only while that carrier and harness contract remain stable.

## Procedure
1. Preserve the `pe-codeview` carrier and `libfuzzer-file-command-wrapper` harness contract until parser reachability is stable.
2. Apply the causal invariant in the failure shape before broad mutation or seed sweeping.
3. Treat local crash class as supporting signal only; keep the candidate only when vulnerable and fixed images diverge on the official target relation.

## Verifier Contract
The official vulnerable-versus-fixed target match is the confirmation gate for this recovery policy; local crash class is supporting evidence only.

## Negative Memory
- Do not corrupt the outer `pe-codeview` recognition gate while retargeting this signal.
- Do not treat off-target crashes, clean parser exits, fixed-build crashes, or both-image crashes as success for this policy.
- Never store raw payload bytes, exact offsets, checksums, or task-local identifiers in memory.

## Format Contract
A PE CodeView input needs a DOS stub, PE signature, COFF file header, optional header with debug data-directory entry, and a section whose virtual address maps the debug directory. The debug directory entry carries type, data size, data RVA, and raw file pointer for CodeView data.

## Harness Contract
The binutils wrapper writes raw bytes to a temporary file and opens them through BFD. BFD recognizes the PE container and reaches debug-directory handling from the file bytes.

## Evidence Shape
- Support: 1 server-verified round 25 solve after 1 attempt.
- Scope: generator repair and retargeting only.
