---
type: causal-policy
title: "VMS Ia64 Library Archive Construct Wrong Sink Parser Reached Target Function Via Generic Scalar Read Stack Buffer Overflow Read Verified Recovery"
description: "Round 36 verified recovery for wrong_sink with verifier signal parser_reached_target_function_via_generic_scalar_read."
failure_class: "wrong_sink"
verifier_signal: "parser_reached_target_function_via_generic_scalar_read"
candidate_family: "construct"
input_format: "vms-ia64-library-archive"
harness_convention: "libfuzzer-bfd-tempfile"
vuln_class: "stack-buffer-overflow-read"
access_scope: generate
success_count: 1
confidence: high
tags: ["wrong-sink", "parser-reached-target-function-via-generic-scalar-read", "vms-ia64-library-archive", "libfuzzer-bfd-tempfile", "construct", "stack-buffer-overflow-read", "verified-recovery", "round-36"]
match_keys: ["wrong_sink", "parser_reached_target_function_via_generic_scalar_read", "vms-ia64-library-archive", "libfuzzer-bfd-tempfile", "stack-buffer-overflow-read", "wrong-sink", "parser-reached-target-function-via-generic-scalar-read", "verified_recovery", "construct"]
allowed_scopes: [generate]
forbidden_fields: [raw_poc_bytes, task_id, exact_offset, checksum, submit_metadata]
evidence_level: high
train_only: true
round: 36
---
# VMS Ia64 Library Archive Construct Wrong Sink Parser Reached Target Function Via Generic Scalar Read Stack Buffer Overflow Read Verified Recovery

- key: `wrong_sink x parser_reached_target_function_via_generic_scalar_read`
- outcome: server-verified target match
- success_count: 1
- related format facts: [[vms-ia64-library-archive]]
- related harness facts: [[libfuzzer-bfd-tempfile]]

## Failure Shape
Build a BFD-recognized IA-64 VMS library with a valid library header, coherent index descriptors, and an index block whose first entry is structurally valid but leaves a trailing fragment smaller than the next index-record header. The traversal loop accepts the used-byte count, advances to the fragment, then reads the next record header past the fixed index block while the fixed build rejects the short remaining span.

## Policy
When `wrong_sink x parser_reached_target_function_via_generic_scalar_read` appears for `vms-ia64-library-archive` under `libfuzzer-bfd-tempfile`, preserve the parser, format, and harness gates that the verifier proved before mutating the sink-specific relation. Treat official vulnerable/fixed divergence as the success gate; local crash labels are supporting signals only.

## Procedure
1. Start from the `[[vms-ia64-library-archive]]` format contract and `[[libfuzzer-bfd-tempfile]]` harness contract; keep recognition, dispatch selectors, lengths, and state setup coherent until parser reachability is stable.
2. Apply the causal relation from the failure shape before broad mutation or seed sweeping.
3. Change one invariant at a time: selector-to-subparser, declared length-to-available data, container count-to-record body, lifetime/ownership state, or allocation-size relation.
4. Submit only candidates where the vulnerable image reaches the target relation and the fixed image exits cleanly, rejects the relation, or otherwise avoids the target crash.

## Verifier Contract
This policy is ranked by one round-36 official target match. Re-rank or quarantine it if later use returns only clean exits, wrong sinks, wrapper-specific crashes, or fixed-image crashes.

## Negative Memory
- Do not corrupt the outer `vms-ia64-library-archive` recognition gate while retargeting this signal.
- Do not count parser reachability, both-image crashes, local wrapper crashes, clean exits, or fixed-image crashes as success.
- Do not store payload bytes, exact positions, task identifiers, checksums, or submit metadata.

## Evidence Shape
- Support: 1 server-verified round 36 solve after 1 attempts.
- Candidate family: construct.
- Scope: generator repair and retargeting only.
