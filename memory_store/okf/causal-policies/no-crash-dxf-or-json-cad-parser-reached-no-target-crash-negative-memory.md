---
type: causal-policy
title: "No Crash Dxf Or Json Cad Parser Reached No Target Crash Negative Memory"
description: "Negative memory for no_crash with parser_reached_no_target_crash on dxf-or-json-cad inputs."
failure_class: no_crash
verifier_signal: parser_reached_no_target_crash
candidate_family: seed_mutate
input_format: dxf-or-json-cad
harness_convention: libfuzzer-libredwg-llvmfuzz
vuln_class: double-free
access_scope: generate
success_count: 0
confidence: medium
tags: [no-crash, parser-reached-no-target-crash, dxf-or-json-cad, double-free, negative_memory]
match_keys: [no-crash, parser-reached-no-target-crash, dxf-or-json-cad, double-free]
allowed_scopes: [generate]
forbidden_fields: [raw_poc_bytes, task_id, exact_offset, checksum, submit_metadata]
evidence_level: medium
train_only: true
---
# No Crash Dxf Or Json Cad Parser Reached No Target Crash Negative Memory

- key: `no_crash x parser_reached_no_target_crash`
- outcome: persistent failure basin
- success_count: 0
- failure_count: 1
- formats: [[dxf-or-json-cad]]

## Dead End
Bundled DXF seeds and constructed inputs with custom class names, unknown entity names, dimension subclass rewrites, duplicate class/object names, and JSON dxfname fields all parsed and cleaned up without a sanitizer finding. The missing gate is likely a more precise DXF import state where ownership of the same dxfname allocation is transferred to an object or class and then also freed on an error or export cleanup path.

## Avoid
Do not repeat the same candidate family when the verifier signal matches this key. Treat broad seed mutation, wrapper usage paths, both-image crashes, parser-clean exits, or local-only crashes as evidence that the current surface is not the target differential.

## Recovery Direction
Preserve only independently validated format or harness reachability facts. Re-enter generation by first satisfying the harness contract and the earliest format gate, then use a different target-specific invariant instead of enlarging or randomly mutating the failed family.
