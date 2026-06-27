---
type: causal-policy
title: "No Crash Parser Not Reached Lua Source Negative Memory"
description: "Round 16 negative memory for no_crash with verifier signal parser_not_reached."
failure_class: "no_crash"
verifier_signal: "parser_not_reached"
candidate_family: "construct"
input_format: "lua-source"
harness_convention: "libfuzzer"
vuln_class: "logic-codegen-crash"
access_scope: generate
success_count: 0
confidence: medium
tags: ["no-crash", "parser-not-reached", "lua-source", "negative-memory", "round-16"]
match_keys: ["no_crash", "parser_not_reached", "lua-source", "libfuzzer", "negative_memory"]
allowed_scopes: [generate]
forbidden_fields: [raw_poc_bytes, task_id, exact_offset, checksum, submit_metadata]
evidence_level: medium
train_only: true
round: 16
---
# No Crash Parser Not Reached Lua Source Negative Memory

## Policy
For `no_crash x parser_not_reached`, avoid replaying the observed dead end. This negative memory is co-equal with positive policies and should redirect generation before another official submission.

## Procedure
- Several text chunks using `_ENV <const>` in local, closure, assignment, loop and goto contexts compiled or were rejected without crashing. The attempted source patterns did not trigger the incorrect code-generation edge case.
- When `no_crash x parser_not_reached` appears for `lua-source`, treat this candidate family as a basin-to-avoid rather than as evidence of proximity to the target.
- Keep any proven parser/harness envelope, but change the missing gate or state relation before submitting again.

## Format Contract
- The input format is plain Lua source text. The target accepts text chunks only; source-level constructs such as local declarations, attributes, closures, loops and gotos are parsed by Lua before bytecode execution.
- Harness: The harness creates a fresh Lua state, loads the raw bytes with text-only mode and executes the chunk only if loading succeeds. Standard libraries are not opened, so candidates must avoid depending on library globals for reachability.

## Negative Memory
- Do not treat this verifier signal as a near miss unless a later candidate changes the missing gate or state relation.
- Do not submit candidates that are clean, parser-mismatched, off-target, or crashing both fixed and vulnerable images in this same shape.
- Preserve only descriptive format facts from the failed attempt; do not promote an unverified causal recovery.

## Evidence Shape
- Support: one diagnosed persistent failure from round 16.
- Scope: generator avoidance for the same failure-keyed basin.
