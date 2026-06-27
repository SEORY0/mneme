---
type: causal-policy
title: "No Crash BFD Nm Clean Exit Or Unrecognized Object Ecoff BFD Object Negative Memory"
description: "Round 10 negative memory for no_crash with verifier signal bfd_nm_clean_exit_or_unrecognized_object."
failure_class: "no_crash"
verifier_signal: "bfd_nm_clean_exit_or_unrecognized_object"
candidate_family: "construct"
input_format: "ecoff-or-bfd-object"
harness_convention: "file-fuzzer"
vuln_class: "heap-buffer-overflow-read"
access_scope: generate
success_count: 0
confidence: medium
tags: ["no-crash", "bfd-nm-clean-exit-or-unrecognized-object", "negative-memory", "round-10"]
match_keys: ["no_crash", "bfd_nm_clean_exit_or_unrecognized_object", "ecoff-or-bfd-object", "file-fuzzer", "negative_memory"]
allowed_scopes: [generate]
forbidden_fields: [raw_poc_bytes, task_id, exact_offset, checksum, submit_metadata]
evidence_level: medium
train_only: true
round: 10
---
# No Crash BFD Nm Clean Exit Or Unrecognized Object Ecoff BFD Object Negative Memory

## Policy
For `no_crash x bfd_nm_clean_exit_or_unrecognized_object`, avoid replaying the observed dead end. This negative memory is co-equal with positive policies and should redirect generation before another official submission.

## Procedure
1. Archive, ELF/COFF, and ECOFF-like object stubs did not reach the ECOFF symbol-table slurp path with useful file descriptor and string-table metadata.
2. When `no_crash x bfd_nm_clean_exit_or_unrecognized_object` appears for `ecoff-or-bfd-object`, treat this candidate family as a basin-to-avoid rather than as evidence of proximity to the target.
3. Keep any proven parser/harness envelope, but change the missing gate or state relation before submitting again.

## Format Contract
- The target relation involves ECOFF file-descriptor records, symbol records, and string-table bases used by BFD while nm filters symbols. A reachable input must be recognized as an ECOFF object and provide internally consistent enough optional/debug headers for BFD to allocate and walk those tables.
- Harness: The fuzz harness writes the raw bytes to a temporary object file and invokes the nm display path with symbol and line-number options enabled. There is no provider carving; BFD format recognition and object metadata drive all reachability.

## Negative Memory
- Do not treat this verifier signal as a near miss unless a later candidate changes the missing gate or state relation.
- Do not submit candidates that are clean, parser-mismatched, off-target, or crashing both fixed and vulnerable images in this same shape.
- Preserve only descriptive format facts from the failed attempt; do not promote an unverified causal recovery.

## Evidence Shape
- Support: one diagnosed round-10 persistent failure.
- Scope: generator avoidance for the same failure-keyed basin.
