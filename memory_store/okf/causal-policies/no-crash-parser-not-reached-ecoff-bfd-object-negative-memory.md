---
type: causal-policy
title: "No Crash Parser Not Reached Ecoff BFD Object Negative Memory"
description: "Round 16 negative memory for no_crash with verifier signal parser_not_reached."
failure_class: "no_crash"
verifier_signal: "parser_not_reached"
candidate_family: "seed_mutate+construct"
input_format: "ecoff-bfd-object"
harness_convention: "afl-file"
vuln_class: "out-of-bounds-pointer-use"
access_scope: generate
success_count: 0
confidence: medium
tags: ["no-crash", "parser-not-reached", "ecoff-bfd-object", "negative-memory", "round-16"]
match_keys: ["no_crash", "parser_not_reached", "ecoff-bfd-object", "afl-file", "negative_memory"]
allowed_scopes: [generate]
forbidden_fields: [raw_poc_bytes, task_id, exact_offset, checksum, submit_metadata]
evidence_level: medium
train_only: true
round: 16
---
# No Crash Parser Not Reached Ecoff BFD Object Negative Memory

## Policy
For `no_crash x parser_not_reached`, avoid replaying the observed dead end. This negative memory is co-equal with positive policies and should redirect generation before another official submission.

## Procedure
- The available object seed was recognized as another object format and printed symbols normally; ECOFF-like stubs and archive stubs did not reach ECOFF symbolic-info slurping. The missing gate is a recognizable ECOFF object with optional/debug headers and a symbolic table whose FDR local-symbol base/count are accepted before the unsafe pointer checks.
- When `no_crash x parser_not_reached` appears for `ecoff-bfd-object`, treat this candidate family as a basin-to-avoid rather than as evidence of proximity to the target.
- Keep any proven parser/harness envelope, but change the missing gate or state relation before submitting again.

## Format Contract
- ECOFF objects include a file header, optional header, section headers, and symbolic/debug header tables. The vulnerable path depends on symbolic information with file-descriptor records referring into local-symbol tables using base/count fields.
- Harness: The built target is AFL-style and reads one raw object/archive file. It invokes binutils symbol-reading behavior after BFD identifies the format; no external selector controls the format path.

## Negative Memory
- Do not treat this verifier signal as a near miss unless a later candidate changes the missing gate or state relation.
- Do not submit candidates that are clean, parser-mismatched, off-target, or crashing both fixed and vulnerable images in this same shape.
- Preserve only descriptive format facts from the failed attempt; do not promote an unverified causal recovery.

## Evidence Shape
- Support: one diagnosed persistent failure from round 16.
- Scope: generator avoidance for the same failure-keyed basin.
