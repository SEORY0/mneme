---
type: causal-policy
title: "Generic Crash Shared String Cleanup Crash But Fixed Image Also Failed Officially Mruby Script Construct Minimal Shared String Script String Sharing Lifetime Negative Memory"
description: "Round 14 negative memory for generic_crash with verifier signal shared_string_cleanup_crash_but_fixed_image_also_failed_officially."
failure_class: "generic_crash"
verifier_signal: "shared_string_cleanup_crash_but_fixed_image_also_failed_officially"
candidate_family: "construct_minimal_shared_string_script"
input_format: "mruby-script"
harness_convention: "libfuzzer"
vuln_class: "string-sharing-lifetime"
access_scope: generate
success_count: 0
confidence: medium
tags: ["generic-crash", "shared-string-cleanup-crash-but-fixed-image-also-failed-officially", "mruby-script", "negative-memory", "round-14"]
match_keys: ["generic_crash", "shared_string_cleanup_crash_but_fixed_image_also_failed_officially", "mruby-script", "libfuzzer", "string-sharing-lifetime", "negative_memory"]
allowed_scopes: [generate]
forbidden_fields: [raw_poc_bytes, task_id, exact_offset, checksum, submit_metadata]
evidence_level: medium
train_only: true
round: 14
---
# Generic Crash Shared String Cleanup Crash But Fixed Image Also Failed Officially Mruby Script Construct Minimal Shared String Script String Sharing Lifetime Negative Memory

- key: `generic_crash x shared_string_cleanup_crash_but_fixed_image_also_failed_officially`
- outcome: persistent failure / basin to avoid
- success_count: 0
- failure_count: 1
- related format facts: [[mruby-script]]
- related harness facts: [[libfuzzer]]

## Failure Shape
Minimal scripts that created a shared heap string, dropped the original, ran garbage collection, and then used keep-ascii bang mutation reached the shared-string cleanup crash shape locally. Official submission still reported the fixed image failing, so the candidate was not accepted as target-differential within the budget.

## Policy
Treat `generic_crash x shared_string_cleanup_crash_but_fixed_image_also_failed_officially` on `mruby-script` as a basin to avoid unless a new candidate changes the parser gate, state relation, or official target sink. Preserve any proven reachability, but reject variants that return to the same verifier signal without changing the causal gate under test.

## Procedure
1. Keep only the smallest carrier that the verifier proved reaches the parser, decoder, or harness path.
2. Identify the missing causal relation from the signal: parser selection, container acceptance, length relation, stateful subobject, allocation state, or official target sink.
3. Change one relation at a time and discard candidates that return to the same clean-exit, off-target-crash, wrong-sink, usage-only, parser-not-reached, or both-image-crash basin.
4. If a local crash is not an official target match, shrink or discard it before mutating deeper fields.
5. Promote a recovery from this basin only after a later verifier-confirmed target match.

## Negative Memory
- Do not count parser reachability, local crashes, clean exits, fixed-image crashes, usage banners, or sink mismatches as success.
- Do not repeat this candidate family unless the new attempt changes the causal gate named above.
- Do not store concrete payload bytes, task identifiers, exact positions, checksums, or submit metadata.

## Evidence Shape
- Support: one diagnosed persistent failure from Round 14.
- Scope: generator repair and basin avoidance only.
