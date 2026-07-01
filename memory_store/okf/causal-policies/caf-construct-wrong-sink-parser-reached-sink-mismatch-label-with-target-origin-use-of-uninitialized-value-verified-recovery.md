---
type: causal-policy
title: "CAF Construct Wrong Sink Parser Reached Sink Mismatch Label With Target Origin Use Of Uninitialized Value Verified Recovery"
description: "Round 36 verified recovery for wrong_sink with verifier signal parser_reached_sink_mismatch_label_with_target_origin."
failure_class: "wrong_sink"
verifier_signal: "parser_reached_sink_mismatch_label_with_target_origin"
candidate_family: "construct"
input_format: "caf"
harness_convention: "libfuzzer"
vuln_class: "use-of-uninitialized-value"
access_scope: generate
success_count: 1
confidence: high
tags: ["wrong-sink", "parser-reached-sink-mismatch-label-with-target-origin", "caf", "libfuzzer", "construct", "use-of-uninitialized-value", "verified-recovery", "round-36"]
match_keys: ["wrong_sink", "parser_reached_sink_mismatch_label_with_target_origin", "caf", "libfuzzer", "use-of-uninitialized-value", "wrong-sink", "parser-reached-sink-mismatch-label-with-target-origin", "verified_recovery", "construct"]
allowed_scopes: [generate]
forbidden_fields: [raw_poc_bytes, task_id, exact_offset, checksum, submit_metadata]
evidence_level: high
train_only: true
round: 36
---
# CAF Construct Wrong Sink Parser Reached Sink Mismatch Label With Target Origin Use Of Uninitialized Value Verified Recovery

- key: `wrong_sink x parser_reached_sink_mismatch_label_with_target_origin`
- outcome: server-verified target match
- success_count: 1
- related format facts: [[caf]]
- related harness facts: [[libfuzzer]]

## Failure Shape
Use the raw libsndfile virtual-file harness with a syntactically recognized CAF carrier. Preserve the top-level CAF magic and first descriptor-chunk marker, then truncate immediately after that marker so the descriptor chunk-size conversion performs a short read. The vulnerable build consumes the uninitialized remainder of the fixed-width temporary buffer during header logging; the fixed build rejects or zeroes the short-read path cleanly.

## Policy
When `wrong_sink x parser_reached_sink_mismatch_label_with_target_origin` appears for `caf` under `libfuzzer`, preserve the parser, format, and harness gates that the verifier proved before mutating the sink-specific relation. Treat official vulnerable/fixed divergence as the success gate; local crash labels are supporting signals only.

## Procedure
1. Start from the `[[caf]]` format contract and `[[libfuzzer]]` harness contract; keep recognition, dispatch selectors, lengths, and state setup coherent until parser reachability is stable.
2. Apply the causal relation from the failure shape before broad mutation or seed sweeping.
3. Change one invariant at a time: selector-to-subparser, declared length-to-available data, container count-to-record body, lifetime/ownership state, or allocation-size relation.
4. Submit only candidates where the vulnerable image reaches the target relation and the fixed image exits cleanly, rejects the relation, or otherwise avoids the target crash.

## Verifier Contract
This policy is ranked by one round-36 official target match. Re-rank or quarantine it if later use returns only clean exits, wrong sinks, wrapper-specific crashes, or fixed-image crashes.

## Negative Memory
- Do not corrupt the outer `caf` recognition gate while retargeting this signal.
- Do not count parser reachability, both-image crashes, local wrapper crashes, clean exits, or fixed-image crashes as success.
- Do not store payload bytes, exact positions, task identifiers, checksums, or submit metadata.

## Evidence Shape
- Support: 1 server-verified round 36 solve after 1 attempts.
- Candidate family: construct.
- Scope: generator repair and retargeting only.
