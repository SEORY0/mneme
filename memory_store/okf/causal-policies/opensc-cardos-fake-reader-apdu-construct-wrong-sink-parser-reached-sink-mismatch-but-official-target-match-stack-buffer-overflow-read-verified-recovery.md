---
type: causal-policy
title: "Opensc Cardos Fake Reader Apdu Construct Wrong Sink Parser Reached Sink Mismatch But Official Target Match Stack Buffer Overflow Read Verified Recovery"
description: "Round 37 verified recovery for wrong_sink with verifier signal parser_reached_sink_mismatch_but_official_target_match."
failure_class: "wrong_sink"
verifier_signal: "parser_reached_sink_mismatch_but_official_target_match"
candidate_family: "construct"
input_format: "opensc-cardos-fake-reader-apdu"
harness_convention: "libfuzzer-pkcs15-reader"
vuln_class: "stack-buffer-overflow-read"
access_scope: generate
success_count: 1
confidence: high
tags: ["wrong-sink", "parser-reached-sink-mismatch-but-official-target-match", "opensc-cardos-fake-reader-apdu", "libfuzzer-pkcs15-reader", "construct", "stack-buffer-overflow-read", "verified-recovery", "round-37"]
match_keys: ["wrong_sink", "parser_reached_sink_mismatch_but_official_target_match", "opensc-cardos-fake-reader-apdu", "libfuzzer-pkcs15-reader", "stack-buffer-overflow-read", "verified-recovery", "construct"]
allowed_scopes: [generate]
forbidden_fields: [raw_poc_bytes, task_id, exact_offset, checksum, submit_metadata]
evidence_level: high
train_only: true
round: 37
---
# Opensc Cardos Fake Reader Apdu Construct Wrong Sink Parser Reached Sink Mismatch But Official Target Match Stack Buffer Overflow Read Verified Recovery

- key: `wrong_sink x parser_reached_sink_mismatch_but_official_target_match`
- outcome: server-verified target match
- success_count: 1
- related format facts: [[opensc-cardos-fake-reader-apdu]]
- related harness facts: [[libfuzzer-pkcs15-reader]]

## Failure Shape
Drive the fake reader as a CardOS card by supplying a recognized ATR family and successful APDU responses for the initialization probes. The version probe must agree with the ATR-derived CardOS generation so initialization reaches the package-list query. For that query, return a successful ASN.1 package-list response whose outer object uses long-form length encoding and fills the APDU response workspace. Include the expected child object so the parser follows the package-inspection path, but keep its value away from the early success case. The vulnerable loop advances by the decoded object length while subtracting only a short-header accounting amount, leaving a nonzero remaining count after the pointer reaches the end of the stack response buffer. The next tag read crosses the buffer boundary; the fixed build accounts for the actual header length and exits cleanly.

## Policy
When `wrong_sink x parser_reached_sink_mismatch_but_official_target_match` appears for `opensc-cardos-fake-reader-apdu` under `libfuzzer-pkcs15-reader`, preserve the parser, format, and harness gates that the verifier proved before mutating the sink-specific relation. Treat official vulnerable/fixed divergence as the success gate; local crash labels are supporting signals only.

## Procedure
1. Start from the `[[opensc-cardos-fake-reader-apdu]]` format contract and `[[libfuzzer-pkcs15-reader]]` harness contract; keep recognition, dispatch selectors, lengths, and state setup coherent until parser reachability is stable.
2. Apply the causal relation from the failure shape before broad mutation or seed sweeping.
3. Change one invariant at a time: selector-to-subparser, declared length-to-available data, container count-to-record body, lifetime/ownership state, allocation-size relation, or sanitizer-specific sink relation.
4. Submit only candidates where the vulnerable image reaches the target relation and the fixed image exits cleanly, rejects the relation, or otherwise avoids the target crash.

## Verifier Contract
This policy is ranked by 1 official target match. Re-rank or quarantine it if later use returns only clean exits, wrong sinks, wrapper-specific crashes, or fixed-image crashes.

## Negative Memory
- Do not corrupt the outer `opensc-cardos-fake-reader-apdu` recognition gate while retargeting this signal.
- Do not count parser reachability, both-image crashes, local wrapper crashes, clean exits, or fixed-image crashes as success.
- Do not store payload bytes, exact positions, task identifiers, checksums, or submit metadata.

## Evidence Shape
- Support: server-verified round 37 solve after 4 attempts.
- Candidate family: construct.
- Official split: vulnerable exit 1, fixed exit 0, target_match True.
- Scope: generator repair and retargeting only.
