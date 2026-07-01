---
type: "causal-policy"
title: "VMS IA64 Library Archive Construct Wrong Sink Parser Reached Target Sink Stack Buffer Overflow Read Verified Recovery"
description: "Round 38 verified recovery for wrong_sink with verifier signal parser_reached_target_sink."
failure_class: "wrong_sink"
verifier_signal: "parser_reached_target_sink"
candidate_family: "construct"
input_format: "vms-ia64-library-archive"
harness_convention: "libfuzzer-bfd-tempfile"
vuln_class: "stack-buffer-overflow-read"
access_scope: "generate"
success_count: 1
confidence: "high"
tags: ["wrong-sink", "parser-reached-target-sink", "vms-ia64-library-archive", "libfuzzer-bfd-tempfile", "construct", "stack-buffer-overflow-read", "verified-recovery", "round-38"]
match_keys: ["wrong_sink", "parser_reached_target_sink", "vms-ia64-library-archive", "libfuzzer-bfd-tempfile", "stack-buffer-overflow-read", "verified-recovery", "construct"]
allowed_scopes: ["generate"]
forbidden_fields: ["raw_poc_bytes", "task_id", "exact_offset", "checksum", "submit_metadata"]
evidence_level: "high"
train_only: true
round: 38
---
# VMS IA64 Library Archive Construct Wrong Sink Parser Reached Target Sink Stack Buffer Overflow Read Verified Recovery

- key: `wrong_sink x parser_reached_target_sink`
- outcome: server-verified target match
- success_count: 1
- related format facts: [[vms-ia64-library-archive]]
- related harness facts: [[libfuzzer-bfd-tempfile]]

## Failure Shape
Construct a BFD-recognized IA-64 VMS library archive with coherent library-header gates, two index descriptors, and a minimal module index so archive bookkeeping succeeds. In the symbol index, use the extended-key path: the inline key metadata points to a key-name block whose chunk header is placed at the last legal header position in the block and whose declared chunk length is the first value that requires bytes beyond the embedded key-block header. This preserves parser reachability and violates only the missing 'chunk length must leave room after vms_kbn' invariant, producing a vulnerable-only stack read in vms_traverse_index.

## Policy
When `wrong_sink x parser_reached_target_sink` appears for `[[vms-ia64-library-archive]]` under `[[libfuzzer-bfd-tempfile]]`, preserve every recognition, length, selector, allocation-state, lifetime, and checksum-equivalent gate needed to reach the target parser before changing the sink-specific relation. Treat vulnerable/fixed divergence from the official verifier as the success gate; local parser reachability and local crash labels are supporting signals only.

## Procedure
1. Start from the `[[vms-ia64-library-archive]]` format contract and `[[libfuzzer-bfd-tempfile]]` harness contract; keep the accepted envelope, dispatch selectors, declared lengths, and state setup coherent until parser reachability is stable.
2. Recreate the causal relation described in the failure shape before broad mutation or seed sweeping.
3. Change one invariant at a time: selector-to-subparser, declared length-to-available data, count-to-record body, lifetime/ownership state, allocation-size relation, or sanitizer-specific sink relation.
4. Submit only candidates where the vulnerable image reaches the target relation and the fixed image exits cleanly, rejects the relation, or otherwise avoids the target crash.

## Verifier Contract
This policy is ranked by one official target match. Re-rank or quarantine it if later use returns only clean exits, wrong sinks, wrapper-specific crashes, or fixed-image crashes.

## Negative Memory
- Do not corrupt the outer `[[vms-ia64-library-archive]]` recognition gate while retargeting this signal.
- Do not count parser reachability, both-image crashes, local wrapper crashes, clean exits, or fixed-image crashes as success.
- Do not store payload bytes, exact positions, task identifiers, checksums, or submit metadata.

## Evidence Shape
- Support: server-verified round 38 solve after 1 attempts.
- Candidate family: construct.
- Official split: vulnerable exit 1, fixed exit 0, target_match True.
- Scope: generator repair and retargeting only.
