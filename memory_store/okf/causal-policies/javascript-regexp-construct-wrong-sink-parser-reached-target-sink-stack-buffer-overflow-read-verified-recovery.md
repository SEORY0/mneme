---
type: causal-policy
title: "Javascript Regexp Construct Wrong Sink Parser Reached Target Sink Stack Buffer Overflow Read Verified Recovery"
description: "Round 36 verified recovery for wrong_sink with verifier signal parser_reached_target_sink."
failure_class: "wrong_sink"
verifier_signal: "parser_reached_target_sink"
candidate_family: "construct"
input_format: "javascript-regexp"
harness_convention: "libfuzzer-raw-js"
vuln_class: "stack-buffer-overflow-read"
access_scope: generate
success_count: 1
confidence: high
tags: ["wrong-sink", "parser-reached-target-sink", "javascript-regexp", "libfuzzer-raw-js", "construct", "stack-buffer-overflow-read", "verified-recovery", "round-36"]
match_keys: ["wrong_sink", "parser_reached_target_sink", "javascript-regexp", "libfuzzer-raw-js", "stack-buffer-overflow-read", "wrong-sink", "parser-reached-target-sink", "verified_recovery", "construct"]
allowed_scopes: [generate]
forbidden_fields: [raw_poc_bytes, task_id, exact_offset, checksum, submit_metadata]
evidence_level: high
train_only: true
round: 36
---
# Javascript Regexp Construct Wrong Sink Parser Reached Target Sink Stack Buffer Overflow Read Verified Recovery

- key: `wrong_sink x parser_reached_target_sink`
- outcome: server-verified target match
- success_count: 1
- related format facts: [[javascript-regexp]]
- related harness facts: [[libfuzzer-raw-js]]

## Failure Shape
Feed raw JavaScript that constructs a RegExp pattern from a normal JS string. A short filler prefix is needed before the final escape so the regex parser reads from an allocation layout where the byte after the pattern is checked by ASAN. The invariant violation is a pattern ending in a lone escape: consuming the escape advances the parser cursor to the end, and the vulnerable word-boundary branch dereferences the cursor before checking for end-of-pattern.

## Policy
When `wrong_sink x parser_reached_target_sink` appears for `javascript-regexp` under `libfuzzer-raw-js`, preserve the parser, format, and harness gates that the verifier proved before mutating the sink-specific relation. Treat official vulnerable/fixed divergence as the success gate; local crash labels are supporting signals only.

## Procedure
1. Start from the `[[javascript-regexp]]` format contract and `[[libfuzzer-raw-js]]` harness contract; keep recognition, dispatch selectors, lengths, and state setup coherent until parser reachability is stable.
2. Apply the causal relation from the failure shape before broad mutation or seed sweeping.
3. Change one invariant at a time: selector-to-subparser, declared length-to-available data, container count-to-record body, lifetime/ownership state, or allocation-size relation.
4. Submit only candidates where the vulnerable image reaches the target relation and the fixed image exits cleanly, rejects the relation, or otherwise avoids the target crash.

## Verifier Contract
This policy is ranked by one round-36 official target match. Re-rank or quarantine it if later use returns only clean exits, wrong sinks, wrapper-specific crashes, or fixed-image crashes.

## Negative Memory
- Do not corrupt the outer `javascript-regexp` recognition gate while retargeting this signal.
- Do not count parser reachability, both-image crashes, local wrapper crashes, clean exits, or fixed-image crashes as success.
- Do not store payload bytes, exact positions, task identifiers, checksums, or submit metadata.

## Evidence Shape
- Support: 1 server-verified round 36 solve after 14 attempts.
- Candidate family: construct.
- Scope: generator repair and retargeting only.
