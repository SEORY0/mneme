---
type: causal-policy
title: "Xslt Stylesheet Seed Mutate Wrong Sink Parser Reached Double Free Double Free Verified Recovery"
description: "Round 37 verified recovery for wrong_sink with verifier signal parser_reached_double_free."
failure_class: "wrong_sink"
verifier_signal: "parser_reached_double_free"
candidate_family: "seed_mutate"
input_format: "xslt-stylesheet"
harness_convention: "afl-file-xslt"
vuln_class: "double-free"
access_scope: generate
success_count: 1
confidence: high
tags: ["wrong-sink", "parser-reached-double-free", "xslt-stylesheet", "afl-file-xslt", "seed-mutate", "double-free", "verified-recovery", "round-37"]
match_keys: ["wrong_sink", "parser_reached_double_free", "xslt-stylesheet", "afl-file-xslt", "double-free", "verified-recovery", "seed_mutate"]
allowed_scopes: [generate]
forbidden_fields: [raw_poc_bytes, task_id, exact_offset, checksum, submit_metadata]
evidence_level: high
train_only: true
round: 37
---
# Xslt Stylesheet Seed Mutate Wrong Sink Parser Reached Double Free Double Free Verified Recovery

- key: `wrong_sink x parser_reached_double_free`
- outcome: server-verified target match
- success_count: 1
- related format facts: [[xslt-stylesheet]]
- related harness facts: [[afl-file-xslt]]

## Failure Shape
Use a standalone stylesheet parsed without entity substitution. Keep an internal entity reference alive inside a template path that is executed during transformation, and place an attribute-producing instruction inside a message-evaluation context. The message template-string evaluator frees attribute child storage while the entity-containing stylesheet tree still retains ownership, so stylesheet document teardown later frees the same allocation again.

## Policy
When `wrong_sink x parser_reached_double_free` appears for `xslt-stylesheet` under `afl-file-xslt`, preserve the parser, format, and harness gates that the verifier proved before mutating the sink-specific relation. Treat official vulnerable/fixed divergence as the success gate; local crash labels are supporting signals only.

## Procedure
1. Start from the `[[xslt-stylesheet]]` format contract and `[[afl-file-xslt]]` harness contract; keep recognition, dispatch selectors, lengths, and state setup coherent until parser reachability is stable.
2. Apply the causal relation from the failure shape before broad mutation or seed sweeping.
3. Change one invariant at a time: selector-to-subparser, declared length-to-available data, container count-to-record body, lifetime/ownership state, allocation-size relation, or sanitizer-specific sink relation.
4. Submit only candidates where the vulnerable image reaches the target relation and the fixed image exits cleanly, rejects the relation, or otherwise avoids the target crash.

## Verifier Contract
This policy is ranked by 1 official target match. Re-rank or quarantine it if later use returns only clean exits, wrong sinks, wrapper-specific crashes, or fixed-image crashes.

## Negative Memory
- Do not corrupt the outer `xslt-stylesheet` recognition gate while retargeting this signal.
- Do not count parser reachability, both-image crashes, local wrapper crashes, clean exits, or fixed-image crashes as success.
- Do not store payload bytes, exact positions, task identifiers, checksums, or submit metadata.

## Evidence Shape
- Support: server-verified round 37 solve after 9 attempts.
- Candidate family: seed_mutate.
- Official split: vulnerable exit 1, fixed exit 0, target_match True.
- Scope: generator repair and retargeting only.
