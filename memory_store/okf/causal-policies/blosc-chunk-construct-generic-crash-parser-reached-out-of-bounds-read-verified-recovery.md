---
type: causal-policy
title: "Blosc Chunk Construct Generic Crash Parser Reached Out Of Bounds Read Verified Recovery"
description: "Round 37 verified recovery for generic_crash with verifier signal parser_reached."
failure_class: "generic_crash"
verifier_signal: "parser_reached"
candidate_family: "construct"
input_format: "blosc-chunk"
harness_convention: "afl-libfuzzer"
vuln_class: "out-of-bounds-read"
access_scope: generate
success_count: 1
confidence: high
tags: ["generic-crash", "parser-reached", "blosc-chunk", "afl-libfuzzer", "construct", "out-of-bounds-read", "verified-recovery", "round-37"]
match_keys: ["generic_crash", "parser_reached", "blosc-chunk", "afl-libfuzzer", "out-of-bounds-read", "verified-recovery", "construct"]
allowed_scopes: [generate]
forbidden_fields: [raw_poc_bytes, task_id, exact_offset, checksum, submit_metadata]
evidence_level: high
train_only: true
round: 37
---
# Blosc Chunk Construct Generic Crash Parser Reached Out Of Bounds Read Verified Recovery

- key: `generic_crash x parser_reached`
- outcome: server-verified target match
- success_count: 1
- related format facts: [[blosc-chunk]]
- related harness facts: [[afl-libfuzzer]]

## Failure Shape
Build a raw Blosc chunk whose outer size fields are self-consistent: the advertised compressed size equals the file size, the uncompressed size is nonzero and fits in the harness output allocation, and the block-start table points to in-bounds stream metadata. Use a non-memcpy chunk with split streams, then make one stream advertise a negative compressed size but follow it with a token that is not the handled run-length encoding. That leaves the decompressor's stream cursor inconsistent and moves it before the accepted stream area, so a later stream-size read occurs from outside the valid chunk. The fixed build rejects the malformed stream state instead of reading through it.

## Policy
When `generic_crash x parser_reached` appears for `blosc-chunk` under `afl-libfuzzer`, preserve the parser, format, and harness gates that the verifier proved before mutating the sink-specific relation. Treat official vulnerable/fixed divergence as the success gate; local crash labels are supporting signals only.

## Procedure
1. Start from the `[[blosc-chunk]]` format contract and `[[afl-libfuzzer]]` harness contract; keep recognition, dispatch selectors, lengths, and state setup coherent until parser reachability is stable.
2. Apply the causal relation from the failure shape before broad mutation or seed sweeping.
3. Change one invariant at a time: selector-to-subparser, declared length-to-available data, container count-to-record body, lifetime/ownership state, allocation-size relation, or sanitizer-specific sink relation.
4. Submit only candidates where the vulnerable image reaches the target relation and the fixed image exits cleanly, rejects the relation, or otherwise avoids the target crash.

## Verifier Contract
This policy is ranked by 1 official target match. Re-rank or quarantine it if later use returns only clean exits, wrong sinks, wrapper-specific crashes, or fixed-image crashes.

## Negative Memory
- Do not corrupt the outer `blosc-chunk` recognition gate while retargeting this signal.
- Do not count parser reachability, both-image crashes, local wrapper crashes, clean exits, or fixed-image crashes as success.
- Do not store payload bytes, exact positions, task identifiers, checksums, or submit metadata.

## Evidence Shape
- Support: server-verified round 37 solve after 42 attempts.
- Candidate family: construct.
- Official split: vulnerable exit 1, fixed exit 0, target_match True.
- Scope: generator repair and retargeting only.
