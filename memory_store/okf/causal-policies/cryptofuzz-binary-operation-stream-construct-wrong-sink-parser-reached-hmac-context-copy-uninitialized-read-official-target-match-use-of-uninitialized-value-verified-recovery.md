---
type: causal-policy
title: "Cryptofuzz Binary Operation Stream Construct Wrong Sink Parser Reached Hmac Context Copy Uninitialized Read Official Target Match Use Of Uninitialized Value Verified Recovery"
description: "Round 37 verified recovery for wrong_sink with verifier signal parser_reached_hmac_context_copy_uninitialized_read_official_target_match."
failure_class: "wrong_sink"
verifier_signal: "parser_reached_hmac_context_copy_uninitialized_read_official_target_match"
candidate_family: "construct"
input_format: "cryptofuzz-binary-operation-stream"
harness_convention: "libfuzzer"
vuln_class: "use-of-uninitialized-value"
access_scope: generate
success_count: 1
confidence: high
tags: ["wrong-sink", "parser-reached-hmac-context-copy-uninitialized-read-official-target-match", "cryptofuzz-binary-operation-stream", "libfuzzer", "construct", "use-of-uninitialized-value", "verified-recovery", "round-37"]
match_keys: ["wrong_sink", "parser_reached_hmac_context_copy_uninitialized_read_official_target_match", "cryptofuzz-binary-operation-stream", "libfuzzer", "use-of-uninitialized-value", "verified-recovery", "construct"]
allowed_scopes: [generate]
forbidden_fields: [raw_poc_bytes, task_id, exact_offset, checksum, submit_metadata]
evidence_level: high
train_only: true
round: 37
---
# Cryptofuzz Binary Operation Stream Construct Wrong Sink Parser Reached Hmac Context Copy Uninitialized Read Official Target Match Use Of Uninitialized Value Verified Recovery

- key: `wrong_sink x parser_reached_hmac_context_copy_uninitialized_read_official_target_match`
- outcome: server-verified target match
- success_count: 1
- related format facts: [[cryptofuzz-binary-operation-stream]]
- related harness facts: [[libfuzzer]]

## Failure Shape
Build a valid cryptofuzz HMAC operation stream for the forced wolfCrypt-OpenSSL module. Select the direct HMAC API path rather than the EVP wrapper, use a valid digest and otherwise ordinary HMAC fields, keep the cleartext as a single part, and drive the context copier to copy the newly allocated HMAC context before any successful HMAC initialization. Tightening away from the zero-length-key variant avoided a fixed-build crash while preserving the uninitialized-context trigger.

## Policy
When `wrong_sink x parser_reached_hmac_context_copy_uninitialized_read_official_target_match` appears for `cryptofuzz-binary-operation-stream` under `libfuzzer`, preserve the parser, format, and harness gates that the verifier proved before mutating the sink-specific relation. Treat official vulnerable/fixed divergence as the success gate; local crash labels are supporting signals only.

## Procedure
1. Start from the `[[cryptofuzz-binary-operation-stream]]` format contract and `[[libfuzzer]]` harness contract; keep recognition, dispatch selectors, lengths, and state setup coherent until parser reachability is stable.
2. Apply the causal relation from the failure shape before broad mutation or seed sweeping.
3. Change one invariant at a time: selector-to-subparser, declared length-to-available data, container count-to-record body, lifetime/ownership state, allocation-size relation, or sanitizer-specific sink relation.
4. Submit only candidates where the vulnerable image reaches the target relation and the fixed image exits cleanly, rejects the relation, or otherwise avoids the target crash.

## Verifier Contract
This policy is ranked by 1 official target match. Re-rank or quarantine it if later use returns only clean exits, wrong sinks, wrapper-specific crashes, or fixed-image crashes.

## Negative Memory
- Do not corrupt the outer `cryptofuzz-binary-operation-stream` recognition gate while retargeting this signal.
- Do not count parser reachability, both-image crashes, local wrapper crashes, clean exits, or fixed-image crashes as success.
- Do not store payload bytes, exact positions, task identifiers, checksums, or submit metadata.

## Evidence Shape
- Support: server-verified round 37 solve after 3 attempts.
- Candidate family: construct.
- Official split: vulnerable exit 139, fixed exit 0, target_match True.
- Scope: generator repair and retargeting only.
