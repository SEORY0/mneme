---
type: causal-policy
title: "No Crash Parser Not Reached Or No Target Crash Bfd Vms Alpha Archive Or Object Double Free Negative Memory"
description: "Negative memory for persistent no_crash / parser_not_reached_or_no_target_crash basin."
failure_class: "no_crash"
verifier_signal: "parser_not_reached_or_no_target_crash"
candidate_family: "construct"
input_format: "bfd-vms-alpha-archive-or-object"
harness_convention: "libfuzzer-bfd-archive-only"
vuln_class: "double-free"
access_scope: generate
success_count: 0
confidence: medium
tags: ["no-crash", "construct", "bfd-vms-alpha-archive-or-object", "double-free", "negative-memory"]
match_keys: ["no-crash", "parser-not-reached-or-no-target-crash", "bfd-vms-alpha-archive-or-object", "libfuzzer-bfd-archive-only", "double-free", "negative-memory"]
allowed_scopes: [generate]
forbidden_fields: [raw_poc_bytes, task_id, exact_offset, checksum, submit_metadata]
evidence_level: medium
train_only: true
provenance: round-35-consolidator
---
# No Crash Parser Not Reached Or No Target Crash Bfd Vms Alpha Archive Or Object Double Free Negative Memory

## Policy
For `no_crash` with verifier signal `parser_not_reached_or_no_target_crash` on `bfd-vms-alpha-archive-or-object` under `libfuzzer-bfd-archive-only`, treat the recorded family as a basin to avoid until a later verifier-confirmed candidate flips the gate. Preserve the descriptive format/harness facts, but do not promote this into a recovery policy.

## Avoided Basin
- Constructed Alpha VMS library skeletons, standalone Alpha VMS object records, a generic archive wrapper, and a mapped generic archive wrapper all exited cleanly.
- The archive-only harness writes raw bytes to a temporary BFD input and calls archive-format detection only; direct Alpha VMS library recognition uses the VMS library archive path, while direct object cleanup is not reached by the raw-object candidates under this harness.

## Recovery Direction
- Keep the parser/harness reachability facts in [[bfd-vms-alpha-archive-or-object]] and [[libfuzzer-bfd-archive-only]].
- Retarget away from the failed relation named by `parser_not_reached_or_no_target_crash`; require vulnerable-only official confirmation before promoting any replacement.

## Evidence Shape
- Support: one round 35 persistent failure with concrete diagnosis and no official target match.
