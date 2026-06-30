---
type: causal-policy
title: "ELF Construct BFD Symbol Table Canonicalization Failed Negative Count Used Negative Symbol Count Memory Operation Verified Recovery"
description: "Round 26 verified recovery for generic_crash with verifier signal bfd_symbol_table_canonicalization_failed_negative_count_used."
failure_class: "generic_crash"
verifier_signal: "bfd_symbol_table_canonicalization_failed_negative_count_used"
candidate_family: "construct"
input_format: "elf"
harness_convention: "libfuzzer/afl objdump file wrapper"
vuln_class: "negative-symbol-count memory operation"
access_scope: generate
success_count: 1
confidence: high
tags: ["generic-crash", "bfd-symbol-table-canonicalization-failed-negative-count-used", "elf", "libfuzzer-afl-objdump-file-wrapper", "construct", "verified-recovery", "round-26"]
match_keys: ["generic_crash", "bfd_symbol_table_canonicalization_failed_negative_count_used", "elf", "libfuzzer/afl objdump file wrapper", "negative-symbol-count memory operation", "verified_recovery"]
allowed_scopes: [generate]
forbidden_fields: [raw_poc_bytes, task_id, exact_offset, checksum, submit_metadata]
evidence_level: high
train_only: true
round: 26
---
# ELF Construct BFD Symbol Table Canonicalization Failed Negative Count Used Negative Symbol Count Memory Operation Verified Recovery

- key: `generic_crash x bfd_symbol_table_canonicalization_failed_negative_count_used`
- outcome: verified recovery
- success_count: 1
- failure_count: 0
- formats: [[elf]]
- harnesses: [[libfuzzer-afl-objdump-file-wrapper]]

## Failure Shape
Construct a small ELF object that BFD recognizes as a valid object with symbols, including coherent ELF identification, section headers, a string table, and a symbol-table section linked to that string table. Keep the symbol table advertised with a small positive size so objdump's upper-bound allocation gate succeeds, but make the symbol-table contents unreadable so canonicalization fails and leaves the global symbol count negative while the symbol pointer remains NULL. When objdump proceeds into disassembly with symbols enabled, the negative count is used as a nonzero symbol count for allocation/copy logic, producing the vulnerable-only crash.

## Policy
For `generic_crash x bfd_symbol_table_canonicalization_failed_negative_count_used` on `elf`, preserve the format recognition and harness contract before varying the vulnerable invariant. Prefer `construct` only while that carrier and harness contract remain stable.

## Procedure
1. Preserve the `elf` carrier and `libfuzzer/afl objdump file wrapper` harness contract until parser reachability is stable.
2. Apply the causal invariant in the failure shape before broad mutation or seed sweeping.
3. Treat local crash class as supporting signal only; keep the candidate only when vulnerable and fixed images diverge on the official target relation.

## Verifier Contract
The official vulnerable-versus-fixed target match is the confirmation gate for this recovery policy; local crash class is supporting evidence only.

## Negative Memory
- Do not corrupt the outer `elf` recognition gate while retargeting this signal.
- Do not treat off-target crashes, clean parser exits, fixed-build crashes, or both-image crashes as success for this policy.
- Never store raw payload bytes, exact offsets, checksums, or task-local identifiers in memory.

## Format Contract
A minimal ELF carrier for this path needs a valid ELF header, section-header table, section-name string table, ordinary string table, executable/content section, and a SHT_SYMTAB entry whose sh_link points at the string table and whose entry size matches the ELF class. The crucial invariant is that the symbol table can be present and sized plausibly for upper-bound computation while its bytes are not actually readable when BFD canonicalizes symbols.

## Harness Contract
The objdump harness writes the raw input bytes to a temporary file and calls the objdump display path on that file. It enables broad objdump modes including section headers, section contents, private headers, DWARF/debug output, relocations, and disassembly. There is no FuzzedDataProvider carving or selector byte; the input must be a complete object file that BFD accepts far enough to reach symbol loading.

## Evidence Shape
- Support: 1 server-verified round 26 solve after 1 attempts.
- Scope: generator repair and retargeting only.
