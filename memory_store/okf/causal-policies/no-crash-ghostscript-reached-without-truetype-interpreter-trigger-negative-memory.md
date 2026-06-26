---
type: causal-policy
title: No Crash Ghostscript Reached Without Truetype Interpreter Trigger Negative Memory
description: Negative memory for no_crash with verifier signal ghostscript_reached_without_truetype_interpreter_trigger.
failure_class: no_crash
verifier_signal: ghostscript_reached_without_truetype_interpreter_trigger
candidate_family: construct
input_format: any
harness_convention: any
access_scope: generate
success_count: 0
confidence: medium
tags: [no-crash, ghostscript-reached-without-truetype-interpreter-trigger, negative_memory]
match_keys: [no-crash, ghostscript-reached-without-truetype-interpreter-trigger, negative_memory]
allowed_scopes: [generate]
forbidden_fields: [raw_poc_bytes, task_id, exact_offset, checksum, submit_metadata]
evidence_level: medium
train_only: true
---
# No Crash Ghostscript Reached Without Truetype Interpreter Trigger Negative Memory

- key: `no_crash x ghostscript_reached_without_truetype_interpreter_trigger`
- outcome: persistent failure basin
- support_count: 1
- candidate_families: construct
- observed_formats: pdf-or-truetype

## Policy
Treat this verifier signal as negative memory for the attempted candidate family. Preserve any parser reachability it proved, but do not keep mutating the same field basin unless the next verification changes the signal.

## Procedure
Use the diagnosis as a selector map: keep the valid base, then change the missing protocol/table/module state rather than increasing file size or randomizing payload bytes.

## Diagnosed Dead Ends
- The attempted PDF did not reach the TrueType ISECT instruction path. Source inspection showed the sink in the embedded TrueType bytecode interpreter, so a useful next candidate should embed or directly provide a font program whose glyph instructions execute ISECT with an available-point index that is not validated before touching the target zone.

## Negative Memory
Do not repeat the same carrier plus broad mutation after this signal. Do not promote the diagnosis into a recovery until a later verifier-confirmed candidate flips the official gate.
