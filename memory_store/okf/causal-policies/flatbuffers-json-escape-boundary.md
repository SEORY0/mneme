---
type: causal-policy
title: FlatBuffers Monster JSON Escape Boundary Recovery
description: Failure-keyed recovery for FlatBuffers Monster JSON parser/generator off-by-one crashes.
failure_class: generic_crash
verifier_signal: sanitizer_crash
candidate_family: construct
input_format: flatbuffers-monster-json
harness_convention: libfuzzer
vuln_class: parser-off-by-one
access_scope: generate
success_count: 1
confidence: medium
tags: [generic_crash, sanitizer_crash, flatbuffers, monster_json, string_escape_boundary]
match_keys: [generic_crash, sanitizer_crash, flatbuffers, monster_json, string_escape_boundary]
allowed_scopes: [generate]
forbidden_fields: [raw_poc_bytes, task_id, exact_offset, checksum, submit_metadata]
evidence_level: medium
train_only: true
---
## Policy
For FlatBuffers Monster JSON tasks, preserve the fuzzer option prefix and a schema-valid minimal Monster object before testing parser boundaries. The causal trigger is a string value ending exactly at an escape boundary that survives parsing and then fails during the parser/generator round trip.

## Procedure
1. Keep the harness option prefix intact so the fixed schema parser is selected.
2. Build the smallest Monster JSON object accepted by the harness.
3. Put the mutation in a string-valued field rather than in object structure.
4. End the string content on an escape boundary that is accepted by the parser but stresses the round-trip generator.
5. Avoid nesting, extra fields, and malformed object syntax until the escape-boundary path is proven clean.

## Negative Memory
- Do not use generic JSON depth bombs for this class; they target a different parser invariant.
- Do not remove the harness prefix while minimizing, because that changes the parser surface.
- Do not corrupt braces or field names; schema rejection hides the string-boundary bug.

## Evidence Shape
- Support: 1 server-verified round observation.
- Scope: generator repair for FlatBuffers Monster JSON string boundary bugs.
