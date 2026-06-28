---
type: causal-policy
title: "No Crash Json Loaded Or Rejected Without Index Fault Gltf Json Negative Memory"
description: "Round 24 negative memory for no_crash with verifier signal json_loaded_or_rejected_without_index_fault."
failure_class: "no_crash"
verifier_signal: "json_loaded_or_rejected_without_index_fault"
candidate_family: "construct"
input_format: "gltf-json"
harness_convention: "libfuzzer"
vuln_class: "out-of-bounds-index"
access_scope: generate
success_count: 0
confidence: medium
tags: ["no-crash", "json-loaded-or-rejected-without-index-fault", "gltf-json", "libfuzzer", "construct", "negative-memory", "round-24"]
match_keys: ["no-crash", "json-loaded-or-rejected-without-index-fault", "gltf-json", "libfuzzer", "out-of-bounds-index"]
allowed_scopes: [generate]
forbidden_fields: [raw_poc_bytes, task_id, exact_offset, checksum, submit_metadata]
evidence_level: medium
train_only: true
round: 24
---
# No Crash Json Loaded Or Rejected Without Index Fault Gltf Json Negative Memory

- key: `no_crash x json_loaded_or_rejected_without_index_fault`
- outcome: negative memory
- success_count: 0
- failure_count: 1
- formats: [[gltf-json]]
- harnesses: [[libfuzzer]]

## Dead-End Shape
Constructed glTF JSON variants with invalid primitive indices, invalid attribute accessor indices, invalid bufferView references, morph target references, and negative sentinel bufferView values did not produce a sanitizer-visible LoadFromString fault.

## Policy
For `no_crash x json_loaded_or_rejected_without_index_fault` on `gltf-json`, avoid replaying the observed dead end. This negative memory is co-equal with positive policies and should redirect generation before another official submission. Prefer `construct` only while this format and harness contract are present.

## Procedure
1. When `no_crash x json_loaded_or_rejected_without_index_fault` appears for `gltf-json`, treat this candidate family as a basin-to-avoid rather than evidence of proximity.
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
