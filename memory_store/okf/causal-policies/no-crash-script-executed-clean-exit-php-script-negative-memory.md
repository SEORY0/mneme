---
type: causal-policy
title: "No Crash Script Executed Clean Exit Php Script Negative Memory"
description: "Round 10 negative memory for no_crash with verifier signal script_executed_clean_exit."
failure_class: "no_crash"
verifier_signal: "script_executed_clean_exit"
candidate_family: "construct"
input_format: "php-script"
harness_convention: "libfuzzer"
vuln_class: "heap-use-after-free"
access_scope: generate
success_count: 0
confidence: medium
tags: ["no-crash", "script-executed-clean-exit", "negative-memory", "round-10"]
match_keys: ["no_crash", "script_executed_clean_exit", "php-script", "libfuzzer", "negative_memory"]
allowed_scopes: [generate]
forbidden_fields: [raw_poc_bytes, task_id, exact_offset, checksum, submit_metadata]
evidence_level: medium
train_only: true
round: 10
---
# No Crash Script Executed Clean Exit Php Script Negative Memory

## Policy
For `no_crash x script_executed_clean_exit`, avoid replaying the observed dead end. This negative memory is co-equal with positive policies and should redirect generation before another official submission.

## Procedure
1. Raw PHP scripts with user-defined attributes, named arguments, repeated attributes, variadic constructors, reflection argument reads, and newInstance calls executed cleanly.
2. When `no_crash x script_executed_clean_exit` appears for `php-script`, treat this candidate family as a basin-to-avoid rather than as evidence of proximity to the target.
3. Keep any proven parser/harness envelope, but change the missing gate or state relation before submitting again.

## Format Contract
- The execute fuzzer consumes a normal PHP source file. Attribute syntax is parsed at compile time, and reflection can materialize attribute objects by invoking their constructors with positional and named attribute arguments.
- Harness: The target compiles and executes raw PHP source bytes directly. There is no file-format wrapper; reaching the sink requires valid PHP code that creates attributes and forces reflection-based instantiation during execution.

## Negative Memory
- Do not treat this verifier signal as a near miss unless a later candidate changes the missing gate or state relation.
- Do not submit candidates that are clean, parser-mismatched, off-target, or crashing both fixed and vulnerable images in this same shape.
- Preserve only descriptive format facts from the failed attempt; do not promote an unverified causal recovery.

## Evidence Shape
- Support: one diagnosed round-10 persistent failure.
- Scope: generator avoidance for the same failure-keyed basin.
