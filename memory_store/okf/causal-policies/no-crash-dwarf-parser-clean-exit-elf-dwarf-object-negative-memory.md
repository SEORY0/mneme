---
type: causal-policy
title: "No Crash Dwarf Parser Clean Exit ELF Dwarf Object Negative Memory"
description: "Round 16 negative memory for no_crash with verifier signal dwarf_parser_clean_exit."
failure_class: "no_crash"
verifier_signal: "dwarf_parser_clean_exit"
candidate_family: "construct_elf_debug_addr_section"
input_format: "elf-dwarf-object"
harness_convention: "libfuzzer-libdwarf-debug-addr"
vuln_class: "unsigned-integer-underflow-bounds-check"
access_scope: generate
success_count: 0
confidence: medium
tags: ["no-crash", "dwarf-parser-clean-exit", "elf-dwarf-object", "negative-memory", "round-16"]
match_keys: ["no_crash", "dwarf_parser_clean_exit", "elf-dwarf-object", "libfuzzer-libdwarf-debug-addr", "negative_memory"]
allowed_scopes: [generate]
forbidden_fields: [raw_poc_bytes, task_id, exact_offset, checksum, submit_metadata]
evidence_level: medium
train_only: true
round: 16
---
# No Crash Dwarf Parser Clean Exit ELF Dwarf Object Negative Memory

## Policy
For `no_crash x dwarf_parser_clean_exit`, avoid replaying the observed dead end. This negative memory is co-equal with positive policies and should redirect generation before another official submission.

## Procedure
- ELF carriers with added debug address sections, including short sections, one-entry sections, extended-length variants, and address-size stress cases, were accepted or rejected cleanly. The missing relation is likely not only the .debug_addr byte layout but also CU context state: an address base, address size, and index combination that reaches the extraction helper with a section smaller than the address-size subtraction guard assumes.
- When `no_crash x dwarf_parser_clean_exit` appears for `elf-dwarf-object`, treat this candidate family as a basin-to-avoid rather than as evidence of proximity to the target.
- Keep any proven parser/harness envelope, but change the missing gate or state relation before submitting again.

## Format Contract
- The relevant DWARF carrier is an object file with normal ELF structure plus debug sections. A .debug_addr section alone can be syntactically present, but address extraction also depends on CU context fields such as address size and address base, and on lookup indexes supplied through libdwarf APIs.
- Harness: The libdwarf fuzzer writes the raw input to a temporary object file, opens it with libdwarf, enumerates debug address tables, and queries addresses by index. There is no byte selector or sidecar metadata outside the object file.

## Negative Memory
- Do not treat this verifier signal as a near miss unless a later candidate changes the missing gate or state relation.
- Do not submit candidates that are clean, parser-mismatched, off-target, or crashing both fixed and vulnerable images in this same shape.
- Preserve only descriptive format facts from the failed attempt; do not promote an unverified causal recovery.

## Evidence Shape
- Support: one diagnosed persistent failure from round 16.
- Scope: generator avoidance for the same failure-keyed basin.
