---
type: causal-policy
title: No Crash Kern Format3 Not Reached Negative Memory
description: Negative memory for no_crash with verifier signal kern_format3_not_reached.
failure_class: no_crash
verifier_signal: kern_format3_not_reached
candidate_family: construct
input_format: any
harness_convention: any
access_scope: generate
success_count: 0
confidence: medium
tags: [no-crash, kern-format3-not-reached, negative_memory]
match_keys: [no-crash, kern-format3-not-reached, negative_memory]
allowed_scopes: [generate]
forbidden_fields: [raw_poc_bytes, task_id, exact_offset, checksum, submit_metadata]
evidence_level: medium
train_only: true
---
# No Crash Kern Format3 Not Reached Negative Memory

## Policy
Treat this verifier signal as negative memory for the attempted candidate family. Preserve any parser reachability it proved, but do not keep mutating the same field basin unless the next verification changes the signal.

## Round 4 Reinforcement
- key: `no_crash x kern_format3_not_reached`
- outcome: persistent failure basin
- support_count: 1
- candidate_families: construct
- observed_formats: opentype-font

### Procedure
Use the signal as a selector map: preserve any reachability it proved, then change the missing protocol/table/module state before changing sizes or payload bytes.

### Diagnosed Dead Ends
- The source-level invariant was identified in the kern Format3 subtable: class-table values can drive an unchecked lookup through the kerning index array. I did not complete a coherent sfnt font with a reachable malformed Format3 kern table and glyph mapping inside the iteration budget.

### Negative Memory
Do not repeat the same carrier plus broad mutation after this signal. Do not promote this basin into a recovery until a later verifier-confirmed candidate flips the official gate.
