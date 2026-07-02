---
type: causal-policy
title: "Sudoers Policy Text Construct Wrong Sink Sink Mismatch Double Free Verified Recovery"
description: "Round 37 verified recovery for wrong_sink with verifier signal sink_mismatch."
failure_class: "wrong_sink"
verifier_signal: "sink_mismatch"
candidate_family: "construct"
input_format: "sudoers-policy-text"
harness_convention: "libfuzzer"
vuln_class: "double-free"
access_scope: generate
success_count: 1
confidence: high
tags: ["wrong-sink", "sink-mismatch", "sudoers-policy-text", "libfuzzer", "construct", "double-free", "verified-recovery", "round-37"]
match_keys: ["wrong_sink", "sink_mismatch", "sudoers-policy-text", "libfuzzer", "double-free", "verified-recovery", "construct"]
allowed_scopes: [generate]
forbidden_fields: [raw_poc_bytes, task_id, exact_offset, checksum, submit_metadata]
evidence_level: high
train_only: true
round: 37
---
# Sudoers Policy Text Construct Wrong Sink Sink Mismatch Double Free Verified Recovery

- key: `wrong_sink x sink_mismatch`
- outcome: server-verified target match
- success_count: 1
- related format facts: [[sudoers-policy-text]]
- related harness facts: [[libfuzzer]]

## Failure Shape
Use a syntactically valid sudoers policy with a single command specification. Before the command token, provide the same path-valued command option twice so the second value replaces the first. The vulnerable parser frees the first option value during replacement but leaves it on the parser leak-tracking list, so parser cleanup frees it again. The fixed build removes or relinks the old option before freeing it.

## Policy
When `wrong_sink x sink_mismatch` appears for `sudoers-policy-text` under `libfuzzer`, preserve the parser, format, and harness gates that the verifier proved before mutating the sink-specific relation. Treat official vulnerable/fixed divergence as the success gate; local crash labels are supporting signals only.

## Procedure
1. Start from the `[[sudoers-policy-text]]` format contract and `[[libfuzzer]]` harness contract; keep recognition, dispatch selectors, lengths, and state setup coherent until parser reachability is stable.
2. Apply the causal relation from the failure shape before broad mutation or seed sweeping.
3. Change one invariant at a time: selector-to-subparser, declared length-to-available data, container count-to-record body, lifetime/ownership state, allocation-size relation, or sanitizer-specific sink relation.
4. Submit only candidates where the vulnerable image reaches the target relation and the fixed image exits cleanly, rejects the relation, or otherwise avoids the target crash.

## Verifier Contract
This policy is ranked by 1 official target match. Re-rank or quarantine it if later use returns only clean exits, wrong sinks, wrapper-specific crashes, or fixed-image crashes.

## Negative Memory
- Do not corrupt the outer `sudoers-policy-text` recognition gate while retargeting this signal.
- Do not count parser reachability, both-image crashes, local wrapper crashes, clean exits, or fixed-image crashes as success.
- Do not store payload bytes, exact positions, task identifiers, checksums, or submit metadata.

## Evidence Shape
- Support: server-verified round 37 solve after 7 attempts.
- Candidate family: construct.
- Official split: vulnerable exit 1, fixed exit 0, target_match True.
- Scope: generator repair and retargeting only.
