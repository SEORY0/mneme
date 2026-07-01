---
type: causal-policy
title: "Blosc Compressed Chunk Construct Wrong Sink Parser Reached Target Msan Submit Confirmed Use Of Uninitialized Value Verified Recovery"
description: "Round 36 verified recovery for wrong_sink with verifier signal parser_reached_target_msan_submit_confirmed."
failure_class: "wrong_sink"
verifier_signal: "parser_reached_target_msan_submit_confirmed"
candidate_family: "construct"
input_format: "blosc-compressed-chunk"
harness_convention: "libfuzzer"
vuln_class: "use-of-uninitialized-value"
access_scope: generate
success_count: 1
confidence: high
tags: ["wrong-sink", "parser-reached-target-msan-submit-confirmed", "blosc-compressed-chunk", "libfuzzer", "construct", "use-of-uninitialized-value", "verified-recovery", "round-36"]
match_keys: ["wrong_sink", "parser_reached_target_msan_submit_confirmed", "blosc-compressed-chunk", "libfuzzer", "use-of-uninitialized-value", "wrong-sink", "parser-reached-target-msan-submit-confirmed", "verified_recovery", "construct"]
allowed_scopes: [generate]
forbidden_fields: [raw_poc_bytes, task_id, exact_offset, checksum, submit_metadata]
evidence_level: high
train_only: true
round: 36
---
# Blosc Compressed Chunk Construct Wrong Sink Parser Reached Target Msan Submit Confirmed Use Of Uninitialized Value Verified Recovery

- key: `wrong_sink x parser_reached_target_msan_submit_confirmed`
- outcome: server-verified target match
- success_count: 1
- related format facts: [[blosc-compressed-chunk]]
- related harness facts: [[libfuzzer]]

## Failure Shape
Build a regular Blosc compressed chunk whose header sizes validate and whose compressor-format bits select Lizard with a single unsplit block. Inside the block, provide a LIZv1 stream that passes the length, flag, literal, and block-start gates, then make the short-offset stream HUF/RLE-decode to fewer initialized bytes than the decoder's fixed-width short-offset read requires. The literal stream must still contain enough trailing material for the fast literal-copy availability guard, and the initialized part of the malformed short offset should make a patched decoder reject cleanly instead of reaching a later generic crash.

## Policy
When `wrong_sink x parser_reached_target_msan_submit_confirmed` appears for `blosc-compressed-chunk` under `libfuzzer`, preserve the parser, format, and harness gates that the verifier proved before mutating the sink-specific relation. Treat official vulnerable/fixed divergence as the success gate; local crash labels are supporting signals only.

## Procedure
1. Start from the `[[blosc-compressed-chunk]]` format contract and `[[libfuzzer]]` harness contract; keep recognition, dispatch selectors, lengths, and state setup coherent until parser reachability is stable.
2. Apply the causal relation from the failure shape before broad mutation or seed sweeping.
3. Change one invariant at a time: selector-to-subparser, declared length-to-available data, container count-to-record body, lifetime/ownership state, or allocation-size relation.
4. Submit only candidates where the vulnerable image reaches the target relation and the fixed image exits cleanly, rejects the relation, or otherwise avoids the target crash.

## Verifier Contract
This policy is ranked by one round-36 official target match. Re-rank or quarantine it if later use returns only clean exits, wrong sinks, wrapper-specific crashes, or fixed-image crashes.

## Negative Memory
- Do not corrupt the outer `blosc-compressed-chunk` recognition gate while retargeting this signal.
- Do not count parser reachability, both-image crashes, local wrapper crashes, clean exits, or fixed-image crashes as success.
- Do not store payload bytes, exact positions, task identifiers, checksums, or submit metadata.

## Evidence Shape
- Support: 1 server-verified round 36 solve after 13 attempts.
- Candidate family: construct.
- Scope: generator repair and retargeting only.
