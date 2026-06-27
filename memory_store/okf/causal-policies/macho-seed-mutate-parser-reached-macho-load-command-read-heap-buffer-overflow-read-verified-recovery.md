---
type: causal-policy
title: Macho Parser Reached Macho Load Command Read Verified Recovery
description: Server-verified recovery for macho when generic_crash pairs with parser_reached_macho_load_command_read.
failure_class: generic_crash
verifier_signal: parser_reached_macho_load_command_read
candidate_family: seed_mutate
input_format: macho
harness_convention: libfuzzer-yara-macho-module
vuln_class: heap-buffer-overflow-read
access_scope: generate
success_count: 1
confidence: high
tags: [generic-crash, parser-reached-macho-load-command-read, macho, libfuzzer-yara-macho-module, seed-mutate, heap-buffer-overflow-read, verified-recovery]
match_keys: [generic-crash, parser-reached-macho-load-command-read, macho, libfuzzer-yara-macho-module, seed-mutate, heap-buffer-overflow-read, verified-recovery]
allowed_scopes: [generate]
forbidden_fields: [raw_poc_bytes, task_id, exact_offset, checksum, submit_metadata]
evidence_level: high
train_only: true
---
## Policy
When a macho candidate reaches `parser_reached_macho_load_command_read` under `generic_crash`, preserve the accepted carrier and target the single invariant named by the verifier and vulnerability class. This pattern is server-verified for vulnerable-build failure with fixed-build clean behavior, so it outranks generic local sink labels for the same format and harness family.

## Procedure
1. Start from the smallest format-valid carrier that reaches the described parser or decoder path.
2. Preserve harness contract `[[libfuzzer-yara-macho-module]]` and format contract `[[macho]]`; do not switch container families after parser reachability is proven.
3. Apply the causal recovery: Start from a valid tiny Mach-O seed so the YARA Mach-O module reaches normal header parsing. Mutate the relation between the declared load-command count and the actual load-command bytes so an additional command is promised beyond the available command area. The vulnerable parser reads the next command header from beyond the buffer; the fixed build checks the command cursor against the remaining file size.
4. If local verify reports `wrong_sink` or a generic crash inside the same parser branch, submit once and let the official server decide target match.
5. If fixed-build behavior is not clean, shrink the mutation back to the minimal boundary relation before trying a different carrier.

## Negative Memory
- Do not randomize unrelated record families after this signal is reached.
- Do not discard a plausible parser-branch crash solely because local sink labeling is coarse.
- Do not promote this as a byte recipe; it is a format-gate and invariant relation.

## Evidence Shape
- Support: 1 server-verified Round 11 solve.
- Candidate family: seed_mutate.
