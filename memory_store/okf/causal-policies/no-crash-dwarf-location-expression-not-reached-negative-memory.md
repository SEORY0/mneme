---
type: causal-policy
title: No Crash Dwarf Location Expression Not Reached Negative Memory
description: Negative memory for no_crash with verifier signal dwarf_location_expression_not_reached.
failure_class: no_crash
verifier_signal: dwarf_location_expression_not_reached
candidate_family: construct
input_format: any
harness_convention: any
access_scope: generate
success_count: 0
confidence: medium
tags: [no-crash, dwarf-location-expression-not-reached, negative_memory]
match_keys: [no-crash, dwarf-location-expression-not-reached, negative_memory]
allowed_scopes: [generate]
forbidden_fields: [raw_poc_bytes, task_id, exact_offset, checksum, submit_metadata]
evidence_level: medium
train_only: true
---
# No Crash Dwarf Location Expression Not Reached Negative Memory

## Policy
Treat this verifier signal as negative memory for the attempted candidate family. Preserve any parser reachability it proved, but do not keep mutating the same field basin unless the next verification changes the signal.

## Round 4 Reinforcement
- key: `no_crash x dwarf_location_expression_not_reached`
- outcome: persistent failure basin
- support_count: 1
- candidate_families: construct
- observed_formats: elf-object-with-dwarf-frame-location-data

### Procedure
Use the signal as a selector map: preserve any reachability it proved, then change the missing protocol/table/module state before changing sizes or payload bytes.

### Diagnosed Dead Ends
- The libdwarf location-op invariant was identified: a pointer-encoding location opcode at the end of a frame-related section causes the operand reader to fetch one byte past the section. I did not complete a minimal object whose DWARF frame metadata drives initialization into that exact location-expression reader.

### Negative Memory
Do not repeat the same carrier plus broad mutation after this signal. Do not promote this basin into a recovery until a later verifier-confirmed candidate flips the official gate.
