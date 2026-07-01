---
type: causal-policy
title: "Mruby Source Construct Minimal Source Location Literal Generic Crash Parser Reached Symbol Name Conversion Fixed Clean Segmentation Fault Read Verified Recovery"
description: "Round 36 verified recovery for generic_crash with verifier signal parser_reached_symbol_name_conversion_fixed_clean."
failure_class: "generic_crash"
verifier_signal: "parser_reached_symbol_name_conversion_fixed_clean"
candidate_family: "construct_minimal_source_location_literal"
input_format: "mruby-source"
harness_convention: "libfuzzer-mruby-load-string"
vuln_class: "segmentation-fault-read"
access_scope: generate
success_count: 1
confidence: high
tags: ["generic-crash", "parser-reached-symbol-name-conversion-fixed-clean", "mruby-source", "libfuzzer-mruby-load-string", "construct-minimal-source-location-literal", "segmentation-fault-read", "verified-recovery", "round-36"]
match_keys: ["generic_crash", "parser_reached_symbol_name_conversion_fixed_clean", "mruby-source", "libfuzzer-mruby-load-string", "segmentation-fault-read", "generic-crash", "parser-reached-symbol-name-conversion-fixed-clean", "verified_recovery", "construct_minimal_source_location_literal", "construct-minimal-source-location-literal"]
allowed_scopes: [generate]
forbidden_fields: [raw_poc_bytes, task_id, exact_offset, checksum, submit_metadata]
evidence_level: high
train_only: true
round: 36
---
# Mruby Source Construct Minimal Source Location Literal Generic Crash Parser Reached Symbol Name Conversion Fixed Clean Segmentation Fault Read Verified Recovery

- key: `generic_crash x parser_reached_symbol_name_conversion_fixed_clean`
- outcome: server-verified target match
- success_count: 1
- related format facts: [[mruby-source]]
- related harness facts: [[libfuzzer-mruby-load-string]]

## Failure Shape
Use a minimal syntactically valid mruby source expression that asks the compiler for the current source-location filename value while running under the raw load-string harness. In this harness there is no normal CLI filename context, so code generation reaches the symbol-name conversion path with an invalid filename symbol and the vulnerable build dereferences it; the fixed build rejects or handles that symbol cleanly.

## Policy
When `generic_crash x parser_reached_symbol_name_conversion_fixed_clean` appears for `mruby-source` under `libfuzzer-mruby-load-string`, preserve the parser, format, and harness gates that the verifier proved before mutating the sink-specific relation. Treat official vulnerable/fixed divergence as the success gate; local crash labels are supporting signals only.

## Procedure
1. Start from the `[[mruby-source]]` format contract and `[[libfuzzer-mruby-load-string]]` harness contract; keep recognition, dispatch selectors, lengths, and state setup coherent until parser reachability is stable.
2. Apply the causal relation from the failure shape before broad mutation or seed sweeping.
3. Change one invariant at a time: selector-to-subparser, declared length-to-available data, container count-to-record body, lifetime/ownership state, or allocation-size relation.
4. Submit only candidates where the vulnerable image reaches the target relation and the fixed image exits cleanly, rejects the relation, or otherwise avoids the target crash.

## Verifier Contract
This policy is ranked by one round-36 official target match. Re-rank or quarantine it if later use returns only clean exits, wrong sinks, wrapper-specific crashes, or fixed-image crashes.

## Negative Memory
- Do not corrupt the outer `mruby-source` recognition gate while retargeting this signal.
- Do not count parser reachability, both-image crashes, local wrapper crashes, clean exits, or fixed-image crashes as success.
- Do not store payload bytes, exact positions, task identifiers, checksums, or submit metadata.

## Evidence Shape
- Support: 1 server-verified round 36 solve after 8 attempts.
- Candidate family: construct_minimal_source_location_literal.
- Scope: generator repair and retargeting only.
