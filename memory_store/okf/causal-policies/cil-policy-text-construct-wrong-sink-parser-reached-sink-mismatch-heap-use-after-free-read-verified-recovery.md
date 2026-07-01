---
type: "causal-policy"
title: "Cil Policy Text Construct Wrong Sink Parser Reached Sink Mismatch Heap Use After Free Read Verified Recovery"
description: "Round 38 verified recovery for wrong_sink with verifier signal parser_reached_sink_mismatch."
failure_class: "wrong_sink"
verifier_signal: "parser_reached_sink_mismatch"
candidate_family: "construct"
input_format: "cil-policy-text"
harness_convention: "libfuzzer"
vuln_class: "heap-use-after-free-read"
access_scope: "generate"
success_count: 1
confidence: "high"
tags: ["wrong-sink", "parser-reached-sink-mismatch", "cil-policy-text", "libfuzzer", "construct", "heap-use-after-free-read", "verified-recovery", "round-38"]
match_keys: ["wrong_sink", "parser_reached_sink_mismatch", "cil-policy-text", "libfuzzer", "heap-use-after-free-read", "verified-recovery", "construct"]
allowed_scopes: ["generate"]
forbidden_fields: ["raw_poc_bytes", "task_id", "exact_offset", "checksum", "submit_metadata"]
evidence_level: "high"
train_only: true
round: 38
---
# Cil Policy Text Construct Wrong Sink Parser Reached Sink Mismatch Heap Use After Free Read Verified Recovery

- key: `wrong_sink x parser_reached_sink_mismatch`
- outcome: server-verified target match
- success_count: 1
- related format facts: [[cil-policy-text]]
- related harness facts: [[libfuzzer]]

## Failure Shape
Construct a valid minimal CIL policy scaffold, define a map class and a map permission, then arrange for the mapping that populates that map permission to live inside an optional block that is later disabled by a resolution failure. The reset path clears the map permission while the later verification path still follows the stale mapped class-permission relation.

## Policy
When `wrong_sink x parser_reached_sink_mismatch` appears for `[[cil-policy-text]]` under `[[libfuzzer]]`, preserve every recognition, length, selector, allocation-state, lifetime, and checksum-equivalent gate needed to reach the target parser before changing the sink-specific relation. Treat vulnerable/fixed divergence from the official verifier as the success gate; local parser reachability and local crash labels are supporting signals only.

## Procedure
1. Start from the `[[cil-policy-text]]` format contract and `[[libfuzzer]]` harness contract; keep the accepted envelope, dispatch selectors, declared lengths, and state setup coherent until parser reachability is stable.
2. Recreate the causal relation described in the failure shape before broad mutation or seed sweeping.
3. Change one invariant at a time: selector-to-subparser, declared length-to-available data, count-to-record body, lifetime/ownership state, allocation-size relation, or sanitizer-specific sink relation.
4. Submit only candidates where the vulnerable image reaches the target relation and the fixed image exits cleanly, rejects the relation, or otherwise avoids the target crash.

## Verifier Contract
This policy is ranked by one official target match. Re-rank or quarantine it if later use returns only clean exits, wrong sinks, wrapper-specific crashes, or fixed-image crashes.

## Negative Memory
- Do not corrupt the outer `[[cil-policy-text]]` recognition gate while retargeting this signal.
- Do not count parser reachability, both-image crashes, local wrapper crashes, clean exits, or fixed-image crashes as success.
- Do not store payload bytes, exact positions, task identifiers, checksums, or submit metadata.

## Evidence Shape
- Support: server-verified round 38 solve after 2 attempts.
- Candidate family: construct.
- Official split: vulnerable exit 1, fixed exit 0, target_match True.
- Scope: generator repair and retargeting only.
