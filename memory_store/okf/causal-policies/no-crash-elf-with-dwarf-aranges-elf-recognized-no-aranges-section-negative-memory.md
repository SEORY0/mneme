---
type: causal-policy
title: No Crash ELF With Dwarf Aranges ELF Recognized No Aranges Section Negative Memory
description: Negative memory for no_crash with elf_recognized_no_aranges_section on elf with dwarf aranges inputs.
failure_class: no_crash
verifier_signal: elf_recognized_no_aranges_section
candidate_family: construct
input_format: elf with dwarf aranges
harness_convention: libfuzzer
vuln_class: bounds-check-assertion
access_scope: generate
success_count: 0
confidence: medium
tags: [no-crash, elf-recognized-no-aranges-section, elf-with-dwarf-aranges, bounds-check-assertion, construct, negative-memory]
match_keys: [no-crash, elf-recognized-no-aranges-section, elf-with-dwarf-aranges, bounds-check-assertion, negative-memory]
allowed_scopes: [generate]
forbidden_fields: [raw_poc_bytes, task_id, exact_offset, checksum, submit_metadata]
evidence_level: medium
train_only: true
---
# No Crash ELF With Dwarf Aranges ELF Recognized No Aranges Section Negative Memory

- key: `no_crash x elf_recognized_no_aranges_section`
- outcome: persistent failure / basin to avoid
- success_count: 0
- failure_count: 1

## Failure Shape
The candidate reached ELF recognition but did not include the debug-aranges section shape
needed to enter the target range loop. The unresolved trigger is a malformed aranges block
whose rounded pointer relation violates the intended bounds invariant.

## Policy
Treat `elf_recognized_no_aranges_section` after `no_crash` on `elf with dwarf aranges` as evidence that the candidate preserved or missed
the wrong invariant. The next generator should keep any proven reachability gate, then retarget to
the smallest missing format contract or sink-specific state instead of repeating the same carrier.

## Procedure
1. Preserve only the envelope features that the verifier proved reached parsing or harness execution.
2. Identify the missing target condition named by the verifier signal: parser reachability, sink selection, structural subobject, length relation, checksum gate, or protocol classification.
3. Change one causal relation at a time and reject variants that move backward to bad format, usage-only wrapper output, or the same clean-exit basin.
4. If the signal says parser or sink was not reached, prefer a more faithful seed or format-specific carrier before mutating bug-trigger fields.
5. If the signal says parser reached cleanly, stop broad fuzzing and violate the exact boundary named by the vulnerability class.

## Negative Memory
- Do not resubmit this failure shape without a new verifier signal.
- Do not widen mutations after reachability is established.
- Do not confuse local wrapper crashes, usage paths, or clean parser exits with official target matches.
- Do not store raw payload bytes, exact offsets, checksums, or task-local identifiers.

## Evidence Shape
- Support: 1 diagnosed persistent failure.
- Scope: generator repair and basin avoidance only.
