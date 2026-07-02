---
type: causal-policy
title: "Wav Ms Adpcm Construct Wrong Sink Official Target Match Heap Buffer Overflow Write Verified Recovery"
description: "Round 36 verified recovery for wrong_sink with verifier signal official_target_match."
failure_class: "wrong_sink"
verifier_signal: "official_target_match"
candidate_family: "construct"
input_format: "wav-ms-adpcm"
harness_convention: "afl-libfuzzer"
vuln_class: "heap-buffer-overflow-write"
access_scope: generate
success_count: 1
confidence: high
tags: ["wrong-sink", "official-target-match", "wav-ms-adpcm", "afl-libfuzzer", "construct", "heap-buffer-overflow-write", "verified-recovery", "round-36"]
match_keys: ["wrong_sink", "official_target_match", "wav-ms-adpcm", "afl-libfuzzer", "heap-buffer-overflow-write", "wrong-sink", "official-target-match", "verified_recovery", "construct"]
allowed_scopes: [generate]
forbidden_fields: [raw_poc_bytes, task_id, exact_offset, checksum, submit_metadata]
evidence_level: high
train_only: true
round: 36
---
# Wav Ms Adpcm Construct Wrong Sink Official Target Match Heap Buffer Overflow Write Verified Recovery

- key: `wrong_sink x official_target_match`
- outcome: server-verified target match
- success_count: 1
- related format facts: [[wav-ms-adpcm]]
- related harness facts: [[afl-libfuzzer]]

## Failure Shape
Use the extensible WAV header route with an MS ADPCM subtype, not the ordinary MS ADPCM format tag. Advertise more than stereo channels while choosing the block alignment and valid-bits field so the MS ADPCM initializer's derived samples-per-block check passes. The vulnerable decoder then treats every non-mono stream as stereo during preamble and packed-nibble expansion, but the sample buffer is sized from the advertised channel count and small samples-per-block value; the packed block expansion overruns that allocation. The fixed build rejects this inconsistent multi-channel ADPCM shape.

## Policy
When `wrong_sink x official_target_match` appears for `wav-ms-adpcm` under `afl-libfuzzer`, preserve the parser, format, and harness gates that the verifier proved before mutating the sink-specific relation. Treat official vulnerable/fixed divergence as the success gate; local crash labels are supporting signals only.

## Procedure
1. Start from the `[[wav-ms-adpcm]]` format contract and `[[afl-libfuzzer]]` harness contract; keep recognition, dispatch selectors, lengths, and state setup coherent until parser reachability is stable.
2. Apply the causal relation from the failure shape before broad mutation or seed sweeping.
3. Change one invariant at a time: selector-to-subparser, declared length-to-available data, container count-to-record body, lifetime/ownership state, or allocation-size relation.
4. Submit only candidates where the vulnerable image reaches the target relation and the fixed image exits cleanly, rejects the relation, or otherwise avoids the target crash.

## Verifier Contract
This policy is ranked by one round-36 official target match. Re-rank or quarantine it if later use returns only clean exits, wrong sinks, wrapper-specific crashes, or fixed-image crashes.

## Negative Memory
- Do not corrupt the outer `wav-ms-adpcm` recognition gate while retargeting this signal.
- Do not count parser reachability, both-image crashes, local wrapper crashes, clean exits, or fixed-image crashes as success.
- Do not store payload bytes, exact positions, task identifiers, checksums, or submit metadata.

## Evidence Shape
- Support: 1 server-verified round 36 solve after 12 attempts.
- Candidate family: construct.
- Scope: generator repair and retargeting only.
