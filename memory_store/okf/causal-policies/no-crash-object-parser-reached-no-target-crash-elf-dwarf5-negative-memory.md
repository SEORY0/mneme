---
type: causal-policy
title: "No Crash Object Parser Reached No Target Crash ELF Dwarf5 Negative Memory"
description: "Round 13 negative memory for no_crash with verifier signal object_parser_reached_no_target_crash."
failure_class: "no_crash"
verifier_signal: "object_parser_reached_no_target_crash"
candidate_family: "seed_mutate"
input_format: "elf-dwarf5"
harness_convention: "libfuzzer-libdwarf-macro-dwarf5"
vuln_class: "out-of-bounds-read"
access_scope: generate
success_count: 0
confidence: medium
tags: ["no-crash", "object-parser-reached-no-target-crash", "elf-dwarf5", "negative-memory", "round-13"]
match_keys: ["no_crash", "object_parser_reached_no_target_crash", "elf-dwarf5", "libfuzzer-libdwarf-macro-dwarf5", "out-of-bounds-read", "negative_memory"]
allowed_scopes: [generate]
forbidden_fields: [raw_poc_bytes, task_id, exact_offset, checksum, submit_metadata]
evidence_level: medium
train_only: true
round: 13
---
# No Crash Object Parser Reached No Target Crash ELF Dwarf5 Negative Memory

- key: `no_crash x object_parser_reached_no_target_crash`
- outcome: persistent failure / basin to avoid
- success_count: 0
- failure_count: 1
- related format facts: [[elf-dwarf5]]
- related harness facts: [[libfuzzer-libdwarf-macro-dwarf5]]

## Failure Shape
Existing ELF/DWARF seeds and a locally generated DWARF5 macro object reached the selected macro fuzzer without sanitizer findings. Mutations that shortened the debug-info section, enlarged or shrank the CU unit length, moved the debug-info section boundary, and invalidated the abbreviation reference were rejected or handled cleanly. The missing gate is likely a more precise DIE/abbreviation shape where a child or sibling traversal crosses the compilation-unit boundary only after macro context discovery succeeds.

## Policy
Treat `no_crash x object_parser_reached_no_target_crash` on `elf-dwarf5` as a basin to avoid unless a new candidate changes the specific parser gate, state relation, or sink relation described below. Preserve any proven reachability, but reject variants that return to the same clean-exit, off-target-crash, wrong-sink, usage-only, or both-image-crash basin.

## Procedure
1. Keep only the smallest parser or harness envelope that the verifier proved was reached.
2. Identify the missing causal relation from the signal: parser selection, container acceptance, length relation, stateful subobject, allocation state, or official target sink.
3. Change one relation at a time and discard candidates that return to the same clean-exit, off-target-crash, wrong-sink, usage-only, or both-image-crash basin.
4. If a local crash is not an official target match, shrink or discard it before mutating deeper fields.
5. Promote a recovery from this basin only after a later verifier-confirmed target match.

## Negative Memory
- Do not resubmit broad mutations that only reproduce `object_parser_reached_no_target_crash`.
- Do not count parser reachability, both-image crashes, local wrapper crashes, or clean exits as success.
- Do not store raw payload bytes, exact positions, task identifiers, checksums, or submit metadata.

## Format Contract
The useful inputs are object files with ELF section headers and DWARF sections such as debug_info, debug_abbrev, debug_str, debug_line, and debug_macro. DWARF5 macro traversal depends on a valid CU DIE, a macro-related attribute or offset, and a debug_macro unit containing well-formed macro operations.

## Harness Contract
The selected libdwarf harness writes the raw input to a temporary file, initializes libdwarf from that file, reads the first CU header, obtains the CU DIE with sibling traversal, then asks for DWARF5 macro context and iterates macro operations. The verifier selected the DWARF5 macro fuzzer, not a plain die-CU-only harness.

## Evidence Shape
- Support: 1 diagnosed persistent failure from round 13.
- Scope: generator repair and basin avoidance only.
## Round 13 Failure Reinforcement

- key: `no_crash x object_parser_reached_no_target_crash`
- related format facts: [[elf-dwarf5]]
- related harness facts: [[libfuzzer-libdwarf-macro-dwarf5]]

### Failure Shape Delta
Existing ELF/DWARF seeds and a locally generated DWARF5 macro object reached the selected macro fuzzer without sanitizer findings. Mutations that shortened the debug-info section, enlarged or shrank the CU unit length, moved the debug-info section boundary, and invalidated the abbreviation reference were rejected or handled cleanly. The missing gate is likely a more precise DIE/abbreviation shape where a child or sibling traversal crosses the compilation-unit boundary only after macro context discovery succeeds.

### Format Contract Delta
The useful inputs are object files with ELF section headers and DWARF sections such as debug_info, debug_abbrev, debug_str, debug_line, and debug_macro. DWARF5 macro traversal depends on a valid CU DIE, a macro-related attribute or offset, and a debug_macro unit containing well-formed macro operations.

### Harness Contract Delta
The selected libdwarf harness writes the raw input to a temporary file, initializes libdwarf from that file, reads the first CU header, obtains the CU DIE with sibling traversal, then asks for DWARF5 macro context and iterates macro operations. The verifier selected the DWARF5 macro fuzzer, not a plain die-CU-only harness.

### Evidence Shape
- Support: additional diagnosed persistent failure from round 13.
- Scope: generator repair and basin avoidance only.
