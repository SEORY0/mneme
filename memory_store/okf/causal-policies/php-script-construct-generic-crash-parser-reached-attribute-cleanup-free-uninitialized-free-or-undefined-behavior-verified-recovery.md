---
type: causal-policy
title: "Php Script Construct Generic Crash Parser Reached Attribute Cleanup Free Uninitialized Free Or Undefined Behavior Verified Recovery"
description: "Verified recovery distilled from a round trace for generic_crash / parser_reached_attribute_cleanup_free."
failure_class: "generic_crash"
verifier_signal: "parser_reached_attribute_cleanup_free"
candidate_family: "construct"
input_format: "php-script"
harness_convention: "honggfuzz-libfuzzer-php-parser-raw-source"
vuln_class: "uninitialized-free-or-undefined-behavior"
access_scope: generate
success_count: 1
confidence: high
tags: ["generic-crash", "construct", "php-script", "uninitialized-free-or-undefined-behavior", "verified-recovery"]
match_keys: ["generic-crash", "parser-reached-attribute-cleanup-free", "php-script", "honggfuzz-libfuzzer-php-parser-raw-source", "uninitialized-free-or-undefined-behavior", "verified-recovery"]
allowed_scopes: [generate]
forbidden_fields: [raw_poc_bytes, task_id, exact_offset, checksum, submit_metadata]
evidence_level: high
train_only: true
provenance: round-35-consolidator
---
# Php Script Construct Generic Crash Parser Reached Attribute Cleanup Free Uninitialized Free Or Undefined Behavior Verified Recovery

## Policy
For `generic_crash` with verifier signal `parser_reached_attribute_cleanup_free` on `php-script` under `honggfuzz-libfuzzer-php-parser-raw-source`, recover by preserving the format and harness gates that reach the target sink, then mutate only the invariant described by the verified recipe. This policy is keyed to the failure signal and is not a byte-level PoC recipe.

## Procedure
1. Feed raw PHP source to the parser fuzzer using the older double-angle attribute syntax.
2. Attach an attribute to a function declaration with multiple arguments where an earlier argument is a valid compile-time constant and a later argument is rejected during constant-expression compilation.
3. The compiler allocates attribute storage for all arguments and initializes entries in order; the compile error occurs before the later entry is initialized, and shutdown then destroys the partially populated attribute, reaching the vulnerable uninitialized zval destructor path.
4. Runtime-only FFI code and class-target attributes were clean dead ends for this harness.

## Format Contract
- Input format: [[php-script]].
- Harness contract: [[honggfuzz-libfuzzer-php-parser-raw-source]].
- Keep parser reachability and sink selection intact before mutating the vulnerable relation.

## Negative Memory
- Do not broaden this into unrelated `php-script` failures without the same failure class and verifier signal.
- Do not store task identifiers, raw bytes, exact offsets, checksums, or submit metadata.

## Evidence Shape
- Support: one round 35 verified official target match; vulnerable build reached the target signal and the fixed build did not.
