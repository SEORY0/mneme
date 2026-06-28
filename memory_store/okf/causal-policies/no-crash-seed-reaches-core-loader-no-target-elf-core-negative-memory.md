---
type: causal-policy
title: "No Crash Seed Reaches Core Loader No Target Elf Core Negative Memory"
description: "Round 24 negative memory for no_crash with verifier signal seed_reaches_core_loader_no_target."
failure_class: "no_crash"
verifier_signal: "seed_reaches_core_loader_no_target"
candidate_family: "seed_mutate"
input_format: "elf-core"
harness_convention: "libfuzzer"
vuln_class: "integer-overflow-bounds-check"
access_scope: generate
success_count: 0
confidence: medium
tags: ["no-crash", "seed-reaches-core-loader-no-target", "elf-core", "libfuzzer", "seed-mutate", "negative-memory", "round-24"]
match_keys: ["no-crash", "seed-reaches-core-loader-no-target", "elf-core", "libfuzzer", "integer-overflow-bounds-check"]
allowed_scopes: [generate]
forbidden_fields: [raw_poc_bytes, task_id, exact_offset, checksum, submit_metadata]
evidence_level: medium
train_only: true
round: 24
---
# No Crash Seed Reaches Core Loader No Target Elf Core Negative Memory

- key: `no_crash x seed_reaches_core_loader_no_target`
- outcome: negative memory
- success_count: 0
- failure_count: 1
- formats: [[elf-core]]
- harnesses: [[libfuzzer]]

## Dead-End Shape
The packaged core-file seed is a valid ELF core and runs through the fuzz target without crashing. I did not construct the dynamic-link-map note/program-header combination needed to make read_addrs see an oversized count that bypasses the incomplete availability check.

## Policy
For `no_crash x seed_reaches_core_loader_no_target` on `elf-core`, avoid replaying the observed dead end. This negative memory is co-equal with positive policies and should redirect generation before another official submission. Prefer `seed_mutate` only while this format and harness contract are present.

## Procedure
1. When `no_crash x seed_reaches_core_loader_no_target` appears for `elf-core`, treat this candidate family as a basin-to-avoid rather than evidence of proximity.
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
