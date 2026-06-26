---
type: causal-policy
title: No Crash Dlltool Def And Object Dlltool Harness Clean Or Usage Only Negative Memory
description: Negative memory for no_crash with dlltool_harness_clean_or_usage_only on dlltool-def-and-object inputs.
failure_class: no_crash
verifier_signal: dlltool_harness_clean_or_usage_only
candidate_family: construct
input_format: dlltool-def-and-object
harness_convention: honggfuzz-wrapper
vuln_class: out-of-bounds-read
access_scope: generate
success_count: 0
confidence: medium
tags: [no-crash, dlltool-harness-clean-or-usage-only, dlltool-def-and-object, out-of-bounds-read, construct, negative-memory]
match_keys: [no-crash, dlltool-harness-clean-or-usage-only, dlltool-def-and-object, out-of-bounds-read, negative-memory]
allowed_scopes: [generate]
forbidden_fields: [raw_poc_bytes, task_id, exact_offset, checksum, submit_metadata]
evidence_level: medium
train_only: true
---
# No Crash Dlltool Def And Object Dlltool Harness Clean Or Usage Only Negative Memory

- key: `no_crash x dlltool_harness_clean_or_usage_only`
- outcome: persistent failure / basin to avoid
- success_count: 0
- failure_count: 1

## Failure Shape
The selected dlltool harness splits input into a definition file and object file. Both an
archive-style attempt and a compact COFF-like object stayed clean or usage-only, so the
object half did not reach a symbol table whose empty name is checked against a zero leading
character.

## Policy
Treat `dlltool_harness_clean_or_usage_only` after `no_crash` on `dlltool-def-and-object` as evidence that the candidate preserved or missed
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
