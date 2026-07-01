---
type: causal-policy
title: "Ascii Armored Openpgp Construct Wrong Sink Parser Reached Armor Trailer Negative Size Memcpy Negative Size Param Verified Recovery"
description: "Round 36 verified recovery for wrong_sink with verifier signal parser_reached_armor_trailer_negative_size_memcpy."
failure_class: "wrong_sink"
verifier_signal: "parser_reached_armor_trailer_negative_size_memcpy"
candidate_family: "construct"
input_format: "ascii-armored-openpgp"
harness_convention: "libfuzzer"
vuln_class: "negative-size-param"
access_scope: generate
success_count: 1
confidence: high
tags: ["wrong-sink", "parser-reached-armor-trailer-negative-size-memcpy", "ascii-armored-openpgp", "libfuzzer", "construct", "negative-size-param", "verified-recovery", "round-36"]
match_keys: ["wrong_sink", "parser_reached_armor_trailer_negative_size_memcpy", "ascii-armored-openpgp", "libfuzzer", "negative-size-param", "wrong-sink", "parser-reached-armor-trailer-negative-size-memcpy", "verified_recovery", "construct"]
allowed_scopes: [generate]
forbidden_fields: [raw_poc_bytes, task_id, exact_offset, checksum, submit_metadata]
evidence_level: high
train_only: true
round: 36
---
# Ascii Armored Openpgp Construct Wrong Sink Parser Reached Armor Trailer Negative Size Memcpy Negative Size Param Verified Recovery

- key: `wrong_sink x parser_reached_armor_trailer_negative_size_memcpy`
- outcome: server-verified target match
- success_count: 1
- related format facts: [[ascii-armored-openpgp]]
- related harness facts: [[libfuzzer]]

## Failure Shape
Use an ASCII armor carrier where the broad armored-source detector sees a normal OpenPGP armor sentinel later in the leading window, but the actual first dashed header pair has an inner type shorter than the fixed trailer prefix. Include a syntactically valid armor body and matching CRC so reading reaches trailer construction. The vulnerable parser classifies the short prefix as a message, stores the undersized armor header, then computes a wrapped copy length while constructing the expected END line; the fixed build rejects the short type before that trailer path.

## Policy
When `wrong_sink x parser_reached_armor_trailer_negative_size_memcpy` appears for `ascii-armored-openpgp` under `libfuzzer`, preserve the parser, format, and harness gates that the verifier proved before mutating the sink-specific relation. Treat official vulnerable/fixed divergence as the success gate; local crash labels are supporting signals only.

## Procedure
1. Start from the `[[ascii-armored-openpgp]]` format contract and `[[libfuzzer]]` harness contract; keep recognition, dispatch selectors, lengths, and state setup coherent until parser reachability is stable.
2. Apply the causal relation from the failure shape before broad mutation or seed sweeping.
3. Change one invariant at a time: selector-to-subparser, declared length-to-available data, container count-to-record body, lifetime/ownership state, or allocation-size relation.
4. Submit only candidates where the vulnerable image reaches the target relation and the fixed image exits cleanly, rejects the relation, or otherwise avoids the target crash.

## Verifier Contract
This policy is ranked by one round-36 official target match. Re-rank or quarantine it if later use returns only clean exits, wrong sinks, wrapper-specific crashes, or fixed-image crashes.

## Negative Memory
- Do not corrupt the outer `ascii-armored-openpgp` recognition gate while retargeting this signal.
- Do not count parser reachability, both-image crashes, local wrapper crashes, clean exits, or fixed-image crashes as success.
- Do not store payload bytes, exact positions, task identifiers, checksums, or submit metadata.

## Evidence Shape
- Support: 1 server-verified round 36 solve after 6 attempts.
- Candidate family: construct.
- Scope: generator repair and retargeting only.
