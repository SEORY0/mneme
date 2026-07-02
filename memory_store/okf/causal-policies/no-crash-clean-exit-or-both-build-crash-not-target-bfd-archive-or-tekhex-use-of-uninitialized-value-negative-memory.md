---
type: causal-policy
title: "No Crash Clean Exit Or Both Build Crash Not Target Bfd Archive Or Tekhex Use Of Uninitialized Value Negative Memory"
description: "Negative memory for persistent no_crash / clean_exit_or_both_build_crash_not_target basin."
failure_class: "no_crash"
verifier_signal: "clean_exit_or_both_build_crash_not_target"
candidate_family: "construct"
input_format: "bfd-archive-or-tekhex"
harness_convention: "libfuzzer"
vuln_class: "use-of-uninitialized-value"
access_scope: generate
success_count: 0
confidence: medium
tags: ["no-crash", "construct", "bfd-archive-or-tekhex", "use-of-uninitialized-value", "negative-memory"]
match_keys: ["no-crash", "clean-exit-or-both-build-crash-not-target", "bfd-archive-or-tekhex", "libfuzzer", "use-of-uninitialized-value", "negative-memory"]
allowed_scopes: [generate]
forbidden_fields: [raw_poc_bytes, task_id, exact_offset, checksum, submit_metadata]
evidence_level: medium
train_only: true
provenance: round-35-consolidator
---
# No Crash Clean Exit Or Both Build Crash Not Target Bfd Archive Or Tekhex Use Of Uninitialized Value Negative Memory

## Policy
For `no_crash` with verifier signal `clean_exit_or_both_build_crash_not_target` on `bfd-archive-or-tekhex` under `libfuzzer`, treat the recorded family as a basin to avoid until a later verifier-confirmed candidate flips the gate. Preserve the descriptive format/harness facts, but do not promote this into a recovery policy.

## Avoided Basin
- A well-formed archive envelope with a TekHex member was accepted by normal BFD archive/object tooling, but the fuzz harness still exited cleanly for valid minimal and data-record members.
- Adding trailing non-record data produced a coarse crash in both vulnerable and fixed builds, so that path was over-broad rather than the pass_over EOF guard.
- Alternate archive maps and member-record shapes did not produce a target-specific sanitizer finding.

## Recovery Direction
- Keep the parser/harness reachability facts in [[bfd-archive-or-tekhex]] and [[libfuzzer]].
- Retarget away from the failed relation named by `clean_exit_or_both_build_crash_not_target`; require vulnerable-only official confirmation before promoting any replacement.

## Evidence Shape
- Support: one round 35 persistent failure with concrete diagnosis and no official target match.
