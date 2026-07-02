---
type: causal-policy
title: "Jpeg Seed Mutate Wrong Sink Parser Reached Uninitialized Read Verified Recovery"
description: "Round 37 verified recovery for wrong_sink with verifier signal parser_reached."
failure_class: "wrong_sink"
verifier_signal: "parser_reached"
candidate_family: "seed_mutate"
input_format: "jpeg"
harness_convention: "libfuzzer"
vuln_class: "uninitialized-read"
access_scope: generate
success_count: 1
confidence: high
tags: ["wrong-sink", "parser-reached", "jpeg", "libfuzzer", "seed-mutate", "uninitialized-read", "verified-recovery", "round-37"]
match_keys: ["wrong_sink", "parser_reached", "jpeg", "libfuzzer", "uninitialized-read", "verified-recovery", "seed_mutate"]
allowed_scopes: [generate]
forbidden_fields: [raw_poc_bytes, task_id, exact_offset, checksum, submit_metadata]
evidence_level: high
train_only: true
round: 37
---
# Jpeg Seed Mutate Wrong Sink Parser Reached Uninitialized Read Verified Recovery

- key: `wrong_sink x parser_reached`
- outcome: server-verified target match
- success_count: 1
- related format facts: [[jpeg]]
- related harness facts: [[libfuzzer]]

## Failure Shape
Start from a valid progressive JPEG so all marker, table, frame, and scan gates are satisfied. Preserve the first progressive scan header and enough entropy to enter decompression, then end the image before later progressive scans are available. The image still advertises enough rows to enter smoothing output, so the first-scan-only incomplete input path reads previous-scan coefficient-bit state before it has been initialized. Tightening the truncation to leave a small amount of first-scan entropy avoids crashing the fixed build.

## Policy
When `wrong_sink x parser_reached` appears for `jpeg` under `libfuzzer`, preserve the parser, format, and harness gates that the verifier proved before mutating the sink-specific relation. Treat official vulnerable/fixed divergence as the success gate; local crash labels are supporting signals only.

## Procedure
1. Start from the `[[jpeg]]` format contract and `[[libfuzzer]]` harness contract; keep recognition, dispatch selectors, lengths, and state setup coherent until parser reachability is stable.
2. Apply the causal relation from the failure shape before broad mutation or seed sweeping.
3. Change one invariant at a time: selector-to-subparser, declared length-to-available data, container count-to-record body, lifetime/ownership state, allocation-size relation, or sanitizer-specific sink relation.
4. Submit only candidates where the vulnerable image reaches the target relation and the fixed image exits cleanly, rejects the relation, or otherwise avoids the target crash.

## Verifier Contract
This policy is ranked by 1 official target match. Re-rank or quarantine it if later use returns only clean exits, wrong sinks, wrapper-specific crashes, or fixed-image crashes.

## Negative Memory
- Do not corrupt the outer `jpeg` recognition gate while retargeting this signal.
- Do not count parser reachability, both-image crashes, local wrapper crashes, clean exits, or fixed-image crashes as success.
- Do not store payload bytes, exact positions, task identifiers, checksums, or submit metadata.

## Evidence Shape
- Support: server-verified round 37 solve after 16 attempts.
- Candidate family: seed_mutate.
- Official split: vulnerable exit 77, fixed exit 0, target_match True.
- Scope: generator repair and retargeting only.
