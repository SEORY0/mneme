---
type: causal-policy
title: "No Crash Cil Compile Rejected Or Clean Exit Selinux Cil Policy Text Construct Cil Policy Text Type Confusion Or Invalid Class Kind Negative Memory"
description: "Round 14 negative memory for no_crash with verifier signal cil_compile_rejected_or_clean_exit."
failure_class: "no_crash"
verifier_signal: "cil_compile_rejected_or_clean_exit"
candidate_family: "construct_cil_policy_text"
input_format: "selinux-cil-policy-text"
harness_convention: "libfuzzer"
vuln_class: "type-confusion-or-invalid-class-kind"
access_scope: generate
success_count: 0
confidence: medium
tags: ["no-crash", "cil-compile-rejected-or-clean-exit", "selinux-cil-policy-text", "negative-memory", "round-14"]
match_keys: ["no_crash", "cil_compile_rejected_or_clean_exit", "selinux-cil-policy-text", "libfuzzer", "type-confusion-or-invalid-class-kind", "negative_memory"]
allowed_scopes: [generate]
forbidden_fields: [raw_poc_bytes, task_id, exact_offset, checksum, submit_metadata]
evidence_level: medium
train_only: true
round: 14
---
# No Crash Cil Compile Rejected Or Clean Exit Selinux Cil Policy Text Construct Cil Policy Text Type Confusion Or Invalid Class Kind Negative Memory

- key: `no_crash x cil_compile_rejected_or_clean_exit`
- outcome: persistent failure / basin to avoid
- success_count: 0
- failure_count: 1
- related format facts: [[selinux-cil-policy-text]]
- related harness facts: [[libfuzzer]]

## Failure Shape
A CIL policy using a map class name in a classcommon declaration did not produce a sanitizer signal. The likely missing gate is a fully compilable policy that reaches classcommon resolution while keeping later class/order/user/sid invariants valid.

## Policy
Treat `no_crash x cil_compile_rejected_or_clean_exit` on `selinux-cil-policy-text` as a basin to avoid unless a new candidate changes the parser gate, state relation, or official target sink. Preserve any proven reachability, but reject variants that return to the same verifier signal without changing the causal gate under test.

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
