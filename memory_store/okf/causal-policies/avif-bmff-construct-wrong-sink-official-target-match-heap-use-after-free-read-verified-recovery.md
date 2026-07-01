---
type: causal-policy
title: "Avif Bmff Construct Wrong Sink Official Target Match Heap Use After Free Read Verified Recovery"
description: "Round 36 verified recovery for wrong_sink with verifier signal official_target_match."
failure_class: "wrong_sink"
verifier_signal: "official_target_match"
candidate_family: "construct"
input_format: "avif-bmff"
harness_convention: "libfuzzer"
vuln_class: "heap-use-after-free-read"
access_scope: generate
success_count: 1
confidence: high
tags: ["wrong-sink", "official-target-match", "avif-bmff", "libfuzzer", "construct", "heap-use-after-free-read", "verified-recovery", "round-36"]
match_keys: ["wrong_sink", "official_target_match", "avif-bmff", "libfuzzer", "heap-use-after-free-read", "wrong-sink", "official-target-match", "verified_recovery", "construct"]
allowed_scopes: [generate]
forbidden_fields: [raw_poc_bytes, task_id, exact_offset, checksum, submit_metadata]
evidence_level: high
train_only: true
round: 36
---
# Avif Bmff Construct Wrong Sink Official Target Match Heap Use After Free Read Verified Recovery

- key: `wrong_sink x official_target_match`
- outcome: server-verified target match
- success_count: 1
- related format facts: [[avif-bmff]]
- related harness facts: [[libfuzzer]]

## Failure Shape
Construct a compact BMFF-style AVIF container where the first top-level file-type box is compatible only through its compatible-brand array, then follow it with a malformed duplicate file-type box whose payload length forces replacement of the stored file-type backing buffer before parse failure. The vulnerable error path reports success after the duplicate parse fails, so the later compatibility check reads the stale compatible-brand pointer; the fixed build treats the duplicate or failed parse as an error.

## Policy
When `wrong_sink x official_target_match` appears for `avif-bmff` under `libfuzzer`, preserve the parser, format, and harness gates that the verifier proved before mutating the sink-specific relation. Treat official vulnerable/fixed divergence as the success gate; local crash labels are supporting signals only.

## Procedure
1. Start from the `[[avif-bmff]]` format contract and `[[libfuzzer]]` harness contract; keep recognition, dispatch selectors, lengths, and state setup coherent until parser reachability is stable.
2. Apply the causal relation from the failure shape before broad mutation or seed sweeping.
3. Change one invariant at a time: selector-to-subparser, declared length-to-available data, container count-to-record body, lifetime/ownership state, or allocation-size relation.
4. Submit only candidates where the vulnerable image reaches the target relation and the fixed image exits cleanly, rejects the relation, or otherwise avoids the target crash.

## Verifier Contract
This policy is ranked by one round-36 official target match. Re-rank or quarantine it if later use returns only clean exits, wrong sinks, wrapper-specific crashes, or fixed-image crashes.

## Negative Memory
- Do not corrupt the outer `avif-bmff` recognition gate while retargeting this signal.
- Do not count parser reachability, both-image crashes, local wrapper crashes, clean exits, or fixed-image crashes as success.
- Do not store payload bytes, exact positions, task identifiers, checksums, or submit metadata.

## Evidence Shape
- Support: 1 server-verified round 36 solve after 8 attempts.
- Candidate family: construct.
- Scope: generator repair and retargeting only.
