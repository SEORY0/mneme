---
type: causal-policy
title: "PHP Script Seed Mutate Then Minimize Generic Crash Parser Reached Reflection Exception Formatting Null Deref Null Dereference Read Verified Recovery"
description: "Round 36 verified recovery for generic_crash with verifier signal parser_reached_reflection_exception_formatting_null_deref."
failure_class: "generic_crash"
verifier_signal: "parser_reached_reflection_exception_formatting_null_deref"
candidate_family: "seed_mutate_then_minimize"
input_format: "php-script"
harness_convention: "libfuzzer-execute"
vuln_class: "null-dereference-read"
access_scope: generate
success_count: 1
confidence: high
tags: ["generic-crash", "parser-reached-reflection-exception-formatting-null-deref", "php-script", "libfuzzer-execute", "seed-mutate-then-minimize", "null-dereference-read", "verified-recovery", "round-36"]
match_keys: ["generic_crash", "parser_reached_reflection_exception_formatting_null_deref", "php-script", "libfuzzer-execute", "null-dereference-read", "generic-crash", "parser-reached-reflection-exception-formatting-null-deref", "verified_recovery", "seed_mutate_then_minimize", "seed-mutate-then-minimize"]
allowed_scopes: [generate]
forbidden_fields: [raw_poc_bytes, task_id, exact_offset, checksum, submit_metadata]
evidence_level: high
train_only: true
round: 36
---
# PHP Script Seed Mutate Then Minimize Generic Crash Parser Reached Reflection Exception Formatting Null Deref Null Dereference Read Verified Recovery

- key: `generic_crash x parser_reached_reflection_exception_formatting_null_deref`
- outcome: server-verified target match
- success_count: 1
- related format facts: [[php-script]]
- related harness facts: [[libfuzzer-execute]]

## Failure Shape
Use a compact executable PHP source file. Define a resolvable class, then invoke ReflectionParameter with the class-method array form where the class component resolves but the method component is not a valid method-name string. This drives the reflection constructor into its error-reporting path; the vulnerable build formats the invalid method component as a string and reads through a null-ish pointer, while the fixed build rejects it cleanly.

## Policy
When `generic_crash x parser_reached_reflection_exception_formatting_null_deref` appears for `php-script` under `libfuzzer-execute`, preserve the parser, format, and harness gates that the verifier proved before mutating the sink-specific relation. Treat official vulnerable/fixed divergence as the success gate; local crash labels are supporting signals only.

## Procedure
1. Start from the `[[php-script]]` format contract and `[[libfuzzer-execute]]` harness contract; keep recognition, dispatch selectors, lengths, and state setup coherent until parser reachability is stable.
2. Apply the causal relation from the failure shape before broad mutation or seed sweeping.
3. Change one invariant at a time: selector-to-subparser, declared length-to-available data, container count-to-record body, lifetime/ownership state, or allocation-size relation.
4. Submit only candidates where the vulnerable image reaches the target relation and the fixed image exits cleanly, rejects the relation, or otherwise avoids the target crash.

## Verifier Contract
This policy is ranked by one round-36 official target match. Re-rank or quarantine it if later use returns only clean exits, wrong sinks, wrapper-specific crashes, or fixed-image crashes.

## Negative Memory
- Do not corrupt the outer `php-script` recognition gate while retargeting this signal.
- Do not count parser reachability, both-image crashes, local wrapper crashes, clean exits, or fixed-image crashes as success.
- Do not store payload bytes, exact positions, task identifiers, checksums, or submit metadata.

## Evidence Shape
- Support: 1 server-verified round 36 solve after 12 attempts.
- Candidate family: seed_mutate_then_minimize.
- Scope: generator repair and retargeting only.
