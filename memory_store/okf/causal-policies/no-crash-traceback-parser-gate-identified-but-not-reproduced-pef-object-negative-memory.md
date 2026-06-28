---
type: causal-policy
title: "No Crash Traceback Parser Gate Identified But Not Reproduced Pef Object Negative Memory"
description: "Round 6 negative memory for no_crash with verifier signal traceback_parser_gate_identified_but_not_reproduced."
failure_class: "no_crash"
verifier_signal: "traceback_parser_gate_identified_but_not_reproduced"
candidate_family: "construct"
input_format: "pef-object"
harness_convention: "afl-file"
vuln_class: "heap-buffer-overflow-read"
access_scope: generate
success_count: 0
confidence: medium
tags: ["no-crash", "traceback-parser-gate-identified-but-not-reproduced", "pef-object", "negative-memory", "round-6"]
match_keys: ["no_crash", "traceback_parser_gate_identified_but_not_reproduced", "pef-object", "afl-file", "negative_memory"]
allowed_scopes: [generate]
forbidden_fields: [raw_poc_bytes, task_id, exact_offset, checksum, submit_metadata]
evidence_level: medium
train_only: true
round: 6
---
# No Crash Traceback Parser Gate Identified But Not Reproduced Pef Object Negative Memory

- key: `no_crash x traceback_parser_gate_identified_but_not_reproduced`
- outcome: persistent failure / basin to avoid
- success_count: 0
- failure_count: 1
- related format facts: [[pef-object]]

## Failure Shape
- A stale verifier run showed the exact traceback-table leading-dot strip crash path, but the local file was absent and could not be submitted. Rebuilding a minimal PEF object with a code section, zero traceback marker, name-present flag, and traceback-offset field produced a valid non-crashing file. The remaining missing condition is likely a symbol-copy path detail or object layout nuance needed for objcopy to canonicalize the generated traceback symbol with the vulnerable allocation shape.

## Policy
Treat `no_crash x traceback_parser_gate_identified_but_not_reproduced` on this format family as negative memory for the attempted carrier. Preserve only verifier-proven reachability, then retarget the missing gate or sink-specific state instead of resubmitting candidates with the same signal.

## Procedure
1. Keep any parser or harness envelope that the verifier proved was reached.
2. Identify the missing causal relation from the signal: parser selection, feature gate, length relation, stateful subobject, or official target sink.
3. Change one relation at a time and reject variants that return to the same clean-exit, off-target-crash, wrong-sink, usage-only, or nonreproducible basin.
4. If a local crash is not an official target match, shrink or discard it before mutating deeper fields.
5. Promote a recovery from this basin only after a later verifier-confirmed target match.

## Negative Memory
- Do not treat local generic crashes, wrapper usage paths, clean parser exits, or wrong-sink labels as success.
- Do not broaden random mutation after reachability is known; move to the smallest missing format contract.
- Do not submit another candidate with this exact failure signal unless the candidate changes the causal gate being tested.
- Do not store raw payload bytes, exact offsets, checksums, or task-local identifiers.

## Evidence Shape
- Support: 1 diagnosed persistent failure(s) from round 6.
- Scope: generator repair and basin avoidance only.
