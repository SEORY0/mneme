---
type: causal-policy
title: "Mruby Script Official Target Match After Both Crash Variants"
description: "Verified recovery for generic_crash with official_target_match_after_both_crash_variants on mruby-script inputs."
failure_class: generic_crash
verifier_signal: official_target_match_after_both_crash_variants
candidate_family: construct
input_format: mruby-script
harness_convention: "libfuzzer raw mruby source"
vuln_class: signed-length-bigint-load
access_scope: generate
success_count: 1
confidence: medium
tags: [generic-crash, official-target-match-after-both-crash-variants, mruby-script, signed-length-bigint-load, verified_recovery]
match_keys: [generic-crash, official-target-match-after-both-crash-variants, mruby-script, signed-length-bigint-load]
allowed_scopes: [generate]
forbidden_fields: [raw_poc_bytes, task_id, exact_offset, checksum, submit_metadata]
evidence_level: high
train_only: true
---
# Mruby Script Official Target Match After Both Crash Variants

- key: `generic_crash x official_target_match_after_both_crash_variants`
- outcome: verified recovery
- confidence: 0.69
- success_count: 1
- failure_count: 0
- formats: [[mruby-script]]

## Failure Shape
A candidate family ended at `generic_crash` before a verifier-confirmed repair. The successful shape kept the required `mruby-script` parser envelope and moved the mutation into the boundary relation consumed by the target sink instead of relying on broad corruption.

## Procedure
Use a syntactically valid mruby source file containing a single enormous integer literal that is compiled into a bigint pool entry. The successful family uses a base form that makes the serialized bigint length cross the signed-byte boundary in the VM load path while avoiding the broader both-build crash seen with smaller decimal variants. The vulnerable VM interprets the length as negative; the fixed VM treats it as unsigned and exits cleanly.

Retarget from this failure key by preserving the format gate first, then changing exactly the cross-field invariant that separates the vulnerable build from the fixed build. Prefer compact construction for construct traces and seed-preserving mutation for seed traces.

## Verifier Contract
The expected signal is `official_target_match_after_both_crash_variants` with a vulnerable-build crash and clean fixed build. Parser reachability without the differential crash is not sufficient.

## Negative Guards
Do not store raw payload bytes, exact positions, checksums, or submit metadata. Do not widen the mutation after the parser envelope is accepted; if the fixed image also crashes, shrink back to the single boundary relation.
