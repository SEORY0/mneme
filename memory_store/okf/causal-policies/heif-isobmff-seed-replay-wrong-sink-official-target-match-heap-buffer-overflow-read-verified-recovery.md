---
type: causal-policy
title: "Heif Isobmff Seed Replay Wrong Sink Official Target Match Heap Buffer Overflow Read Verified Recovery"
description: "Round 36 verified recovery for wrong_sink with verifier signal official_target_match."
failure_class: "wrong_sink"
verifier_signal: "official_target_match"
candidate_family: "seed_replay"
input_format: "heif-isobmff"
harness_convention: "afl-libfuzzer-file-fuzzer"
vuln_class: "heap-buffer-overflow-read"
access_scope: generate
success_count: 1
confidence: high
tags: ["wrong-sink", "official-target-match", "heif-isobmff", "afl-libfuzzer-file-fuzzer", "seed-replay", "heap-buffer-overflow-read", "verified-recovery", "round-36"]
match_keys: ["wrong_sink", "official_target_match", "heif-isobmff", "afl-libfuzzer-file-fuzzer", "heap-buffer-overflow-read", "wrong-sink", "official-target-match", "verified_recovery", "seed_replay", "seed-replay"]
allowed_scopes: [generate]
forbidden_fields: [raw_poc_bytes, task_id, exact_offset, checksum, submit_metadata]
evidence_level: high
train_only: true
round: 36
---
# Heif Isobmff Seed Replay Wrong Sink Official Target Match Heap Buffer Overflow Read Verified Recovery

- key: `wrong_sink x official_target_match`
- outcome: server-verified target match
- success_count: 1
- related format facts: [[heif-isobmff]]
- related harness facts: [[afl-libfuzzer-file-fuzzer]]

## Failure Shape
Use a structurally valid HEIF image with an auxiliary alpha item and keep the item references, properties, extents, and image payload coherent enough for the file fuzzer to decode the primary image. The fixed decode request reaches color conversion into a fixed YCbCr output; the vulnerable non-HDR alpha handling copies from the smaller alpha plane with a byte count appropriate for a wider representation, producing a bounded alpha-plane over-read that the fixed build rejects or avoids.

## Policy
When `wrong_sink x official_target_match` appears for `heif-isobmff` under `afl-libfuzzer-file-fuzzer`, preserve the parser, format, and harness gates that the verifier proved before mutating the sink-specific relation. Treat official vulnerable/fixed divergence as the success gate; local crash labels are supporting signals only.

## Procedure
1. Start from the `[[heif-isobmff]]` format contract and `[[afl-libfuzzer-file-fuzzer]]` harness contract; keep recognition, dispatch selectors, lengths, and state setup coherent until parser reachability is stable.
2. Apply the causal relation from the failure shape before broad mutation or seed sweeping.
3. Change one invariant at a time: selector-to-subparser, declared length-to-available data, container count-to-record body, lifetime/ownership state, or allocation-size relation.
4. Submit only candidates where the vulnerable image reaches the target relation and the fixed image exits cleanly, rejects the relation, or otherwise avoids the target crash.

## Verifier Contract
This policy is ranked by one round-36 official target match. Re-rank or quarantine it if later use returns only clean exits, wrong sinks, wrapper-specific crashes, or fixed-image crashes.

## Negative Memory
- Do not corrupt the outer `heif-isobmff` recognition gate while retargeting this signal.
- Do not count parser reachability, both-image crashes, local wrapper crashes, clean exits, or fixed-image crashes as success.
- Do not store payload bytes, exact positions, task identifiers, checksums, or submit metadata.

## Evidence Shape
- Support: 1 server-verified round 36 solve after 2 attempts.
- Candidate family: seed_replay.
- Scope: generator repair and retargeting only.
