---
type: causal-policy
title: "Elf Construct Parser Reached Use Of Uninitialized Value Verified Recovery"
description: "Round 12 verified recovery for generic_crash with verifier signal parser_reached."
failure_class: "generic_crash"
verifier_signal: "parser_reached"
candidate_family: "construct"
input_format: "elf"
harness_convention: "file-parser"
vuln_class: "use-of-uninitialized-value"
access_scope: generate
success_count: 1
confidence: high
tags: ["generic-crash", "parser-reached", "elf", "verified-recovery", "round-12"]
match_keys: ["generic_crash", "parser_reached", "elf", "file-parser", "use-of-uninitialized-value", "verified_recovery"]
allowed_scopes: [generate]
forbidden_fields: [raw_poc_bytes, task_id, exact_offset, checksum, submit_metadata]
evidence_level: high
train_only: true
round: 12
---
# Elf Construct Parser Reached Use Of Uninitialized Value Verified Recovery

- key: `generic_crash x parser_reached`
- outcome: verified recovery
- confidence: 0.82
- success_count: 1
- failure_count: 0
- formats: [[elf]]
- harnesses: [[file-parser]]

## Failure Shape
The verifier-confirmed candidate preserved the `elf` parser envelope under `file-parser` and moved the mutation into the relation consumed by the target sink instead of relying on broad corruption.

## Policy
Use this policy when generation reports `generic_crash` with signal `parser_reached` on `elf` or the same format family. Preserve parser reachability first, then adjust only the smallest format relation named in the procedure until the vulnerable build crashes and the fixed build stays clean.

## Procedure
Build a compact ELF file with a valid ELF header and program-header table but no section-header table. Arrange dynamic metadata so dynamic-symbol reconstruction runs before all loadable program headers needed for address translation have been populated, causing the dynamic-symbol path to use uninitialized program-header state.

## Verifier Contract
The official comparison must show target match with a vulnerable-build crash and a clean fixed build. Parser reachability, local-only crashes, off-target crashes, or both-image crashes are not sufficient.

## Format Contract
ELF parsing uses the file header to locate program headers and section headers. Dynamic symbol recovery may use dynamic-segment tags and virtual-address-to-file-offset translation through loadable program headers when section headers are absent.

## Harness Contract
The binutils-style harness consumes the raw bytes as an ELF file through BFD/ELF parser entry points. There is no fuzzer prefix; the file header determines class, endianness, program headers, and section-header absence.

## Negative Guards
- Do not store raw payload bytes, exact positions, task identifiers, or submit metadata.
- Do not widen mutation after the parser envelope is accepted; shrink back to the single boundary relation when the fixed image also crashes.
- Do not promote this policy to another format unless the same failure key and verifier signal recur under official comparison.
