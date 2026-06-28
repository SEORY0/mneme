---
type: causal-policy
title: "No Crash Api Fuzzer Ran Constructed Programs Without Crash Libxml2 Api Vm Bytecode Negative Memory"
description: "Round 24 negative memory for no_crash with verifier signal api fuzzer ran constructed programs without crash."
failure_class: "no_crash"
verifier_signal: "api fuzzer ran constructed programs without crash"
candidate_family: "construct"
input_format: "libxml2-api-vm-bytecode"
harness_convention: "libfuzzer libxml2 api fuzzer"
vuln_class: "libxml2-api-dtd-replacement-invariant"
access_scope: generate
success_count: 0
confidence: medium
tags: ["no-crash", "api-fuzzer-ran-constructed-programs-without-crash", "libxml2-api-vm-bytecode", "libfuzzer-libxml2-api-fuzzer", "construct", "negative-memory", "round-24"]
match_keys: ["no-crash", "api-fuzzer-ran-constructed-programs-without-crash", "libxml2-api-vm-bytecode", "libfuzzer-libxml2-api-fuzzer", "libxml2-api-dtd-replacement-invariant"]
allowed_scopes: [generate]
forbidden_fields: [raw_poc_bytes, task_id, exact_offset, checksum, submit_metadata]
evidence_level: medium
train_only: true
round: 24
---
# No Crash Api Fuzzer Ran Constructed Programs Without Crash Libxml2 Api Vm Bytecode Negative Memory

- key: `no_crash x api fuzzer ran constructed programs without crash`
- outcome: negative memory
- success_count: 0
- failure_count: 1
- formats: [[libxml2-api-vm-bytecode]]
- harnesses: [[libfuzzer-libxml2-api-fuzzer]]

## Dead-End Shape
Constructed VM programs created documents, internal or external subsets, normal nodes, and replacement operations in both subset-as-old and subset-as-incoming-node directions, but did not produce a sanitizer-visible invalid reference. The missing step is likely a follow-up API call that dereferences the inconsistent DTD/document relationship after replacement.

## Policy
For `no_crash x api fuzzer ran constructed programs without crash` on `libxml2-api-vm-bytecode`, avoid replaying the observed dead end. This negative memory is co-equal with positive policies and should redirect generation before another official submission. Prefer `construct` only while this format and harness contract are present.

## Procedure
1. When `no_crash x api fuzzer ran constructed programs without crash` appears for `libxml2-api-vm-bytecode`, treat this candidate family as a basin-to-avoid rather than evidence of proximity.
2. Preserve any proven format or harness envelope, but change the missing gate, state relation, or sink path before another official submission.
3. Prefer a different construction family if the same verifier signal repeats without new parser-depth evidence.

## Verifier Contract
The official vulnerable-versus-fixed target match is the confirmation gate for recovery policies; local crash class is supporting evidence only.

## Negative Memory
- Do not resubmit candidates that are clean, off-target, rejected before the target path, or crashing both fixed and vulnerable images in this same shape.
- Do not promote this trace as a recovery unless a later verifier run flips the target relation.
- Preserve only descriptive format and harness facts from this failed attempt.

## Evidence Shape
- Support: one diagnosed round 24 persistent failure.
- Scope: generator repair and retargeting only.
