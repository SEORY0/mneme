---
type: causal-policy
title: "ELF MIPS Relocatable Construct MIPS ELF Relocation Parser Reached Binutils MIPS ELF Micromips Relocation Misapplication Verified Recovery"
description: "Round 19 verified recovery for generic_crash with verifier signal parser_reached_binutils_mips_elf."
failure_class: "generic_crash"
verifier_signal: "parser_reached_binutils_mips_elf"
candidate_family: "construct_mips_elf_relocation"
input_format: "elf-mips-relocatable"
harness_convention: "afl-libfuzzer-binutils-nm"
vuln_class: "microMIPS-relocation-misapplication"
access_scope: generate
success_count: 1
confidence: medium
tags: ["generic-crash", "parser-reached-binutils-mips-elf", "elf-mips-relocatable", "afl-libfuzzer-binutils-nm", "construct-mips-elf-relocation", "verified-recovery", "round-19"]
match_keys: ["generic-crash", "parser-reached-binutils-mips-elf", "elf-mips-relocatable", "afl-libfuzzer-binutils-nm", "micromips-relocation-misapplication"]
allowed_scopes: [generate]
forbidden_fields: [raw_poc_bytes, task_id, exact_offset, checksum, submit_metadata]
evidence_level: high
train_only: true
round: 19
---
# ELF MIPS Relocatable Construct MIPS ELF Relocation Parser Reached Binutils MIPS ELF Micromips Relocation Misapplication Verified Recovery

- key: `generic_crash x parser_reached_binutils_mips_elf`
- outcome: verified recovery
- success_count: 1
- failure_count: 0
- formats: [[elf-mips-relocatable]]
- harnesses: [[afl-libfuzzer-binutils-nm]]

## Failure Shape
Build a compact MIPS relocatable ELF that is accepted by BFD, contains a small executable section with a microMIPS GP-relative load-like instruction, a minimal symbol table, and a relocation section applying the problematic microMIPS GP-relative relocation to that section. The vulnerable build mishandles the relocation transformation during binutils processing, while the fixed build rejects or handles the relation cleanly.

## Policy
For `generic_crash x parser_reached_binutils_mips_elf` on `elf-mips-relocatable`, preserve the parser and harness gates first, then mutate only the causal invariant described by the verified trace. Prefer `construct_mips_elf_relocation` while this format and harness contract are present.

## Procedure
1. Preserve the `elf-mips-relocatable` carrier enough for the `afl-libfuzzer-binutils-nm` harness to reach the parser path.
2. Keep unrelated envelope fields minimal and stable so verifier feedback stays tied to the target sink.
3. Apply the verified invariant from the failure shape rather than random broad mutation.
4. Submit only candidates where the vulnerable image reaches the target relation and the fixed image rejects or avoids it.

## Verifier Contract
The local class may remain coarse. Treat the official vulnerable-versus-fixed target match as the confirmation gate for this policy.

## Negative Memory
- Do not corrupt the outer `elf-mips-relocatable` recognition gate while retargeting this signal.
- Do not treat off-target crashes or both-image crashes as success for this policy.
- Never store raw payload bytes, exact offsets, checksums, or task-local identifiers in memory.

## Evidence Shape
- Support: 1 server-verified round 19 solve.
- Scope: generator repair only.
