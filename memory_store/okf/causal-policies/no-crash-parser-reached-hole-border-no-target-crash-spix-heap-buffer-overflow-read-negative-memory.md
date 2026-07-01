---
type: causal-policy
title: "No Crash Parser Reached Hole Border No Target Crash Spix Heap Buffer Overflow Read Negative Memory"
description: "Negative memory for persistent no_crash / parser_reached_hole_border_no_target_crash basin."
failure_class: "no_crash"
verifier_signal: "parser_reached_hole_border_no_target_crash"
candidate_family: "construct_and_bounded_valid_spix_search"
input_format: "spix"
harness_convention: "libfuzzer"
vuln_class: "heap-buffer-overflow-read"
access_scope: generate
success_count: 0
confidence: medium
tags: ["no-crash", "construct-and-bounded-valid-spix-search", "spix", "heap-buffer-overflow-read", "negative-memory"]
match_keys: ["no-crash", "parser-reached-hole-border-no-target-crash", "spix", "libfuzzer", "heap-buffer-overflow-read", "negative-memory"]
allowed_scopes: [generate]
forbidden_fields: [raw_poc_bytes, task_id, exact_offset, checksum, submit_metadata]
evidence_level: medium
train_only: true
provenance: round-35-consolidator
---
# No Crash Parser Reached Hole Border No Target Crash Spix Heap Buffer Overflow Read Negative Memory

## Policy
For `no_crash` with verifier signal `parser_reached_hole_border_no_target_crash` on `spix` under `libfuzzer`, treat the recorded family as a basin to avoid until a later verifier-confirmed candidate flips the gate. Preserve the descriptive format/harness facts, but do not promote this into a recovery policy.

## Avoided Basin
- Valid serialized PIX inputs reached the SPIX parser and connected-component border code, including the hole-border path, but did not trigger the target boundary over-read.
- Distinct failed hypotheses included ordinary enclosed holes, wide-stride enclosed holes, diagonal foreground carriers that create four-connected holes inside eight-connected components, edge-adjacent sparse topologies, and a bounded batch of larger valid one-bit bitmap carriers.
- These remained clean under official submission or leak-disabled direct harness execution, so the missing condition is likely a narrower border-walk orientation state than these carriers produced.

## Recovery Direction
- Keep the parser/harness reachability facts in [[spix]] and [[libfuzzer]].
- Retarget away from the failed relation named by `parser_reached_hole_border_no_target_crash`; require vulnerable-only official confirmation before promoting any replacement.

## Evidence Shape
- Support: one round 35 persistent failure with concrete diagnosis and no official target match.
