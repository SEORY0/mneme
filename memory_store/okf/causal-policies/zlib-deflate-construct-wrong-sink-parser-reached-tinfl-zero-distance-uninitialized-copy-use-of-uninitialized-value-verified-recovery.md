---
type: causal-policy
title: "Zlib Deflate Construct Wrong Sink Parser Reached Tinfl Zero Distance Uninitialized Copy Use Of Uninitialized Value Verified Recovery"
description: "Round 36 verified recovery for wrong_sink with verifier signal parser_reached_tinfl_zero_distance_uninitialized_copy."
failure_class: "wrong_sink"
verifier_signal: "parser_reached_tinfl_zero_distance_uninitialized_copy"
candidate_family: "construct"
input_format: "zlib-deflate"
harness_convention: "libfuzzer"
vuln_class: "use-of-uninitialized-value"
access_scope: generate
success_count: 1
confidence: high
tags: ["wrong-sink", "parser-reached-tinfl-zero-distance-uninitialized-copy", "zlib-deflate", "libfuzzer", "construct", "use-of-uninitialized-value", "verified-recovery", "round-36"]
match_keys: ["wrong_sink", "parser_reached_tinfl_zero_distance_uninitialized_copy", "zlib-deflate", "libfuzzer", "use-of-uninitialized-value", "wrong-sink", "parser-reached-tinfl-zero-distance-uninitialized-copy", "verified_recovery", "construct"]
allowed_scopes: [generate]
forbidden_fields: [raw_poc_bytes, task_id, exact_offset, checksum, submit_metadata]
evidence_level: high
train_only: true
round: 36
---
# Zlib Deflate Construct Wrong Sink Parser Reached Tinfl Zero Distance Uninitialized Copy Use Of Uninitialized Value Verified Recovery

- key: `wrong_sink x parser_reached_tinfl_zero_distance_uninitialized_copy`
- outcome: server-verified target match
- success_count: 1
- related format facts: [[zlib-deflate]]
- related harness facts: [[libfuzzer]]

## Failure Shape
Build a valid zlib-wrapped deflate stream whose header also gives the harness a nonzero output buffer. Use a final fixed-Huffman block where the first decoded item is a length/distance pair using the reserved high distance symbol that maps to a zero distance in the vulnerable implementation. Because no literal has been emitted yet, the copy reads from the current output cursor before initialized output exists, producing an MSan use-of-uninitialized-value; the fixed build rejects that distance relation.

## Policy
When `wrong_sink x parser_reached_tinfl_zero_distance_uninitialized_copy` appears for `zlib-deflate` under `libfuzzer`, preserve the parser, format, and harness gates that the verifier proved before mutating the sink-specific relation. Treat official vulnerable/fixed divergence as the success gate; local crash labels are supporting signals only.

## Procedure
1. Start from the `[[zlib-deflate]]` format contract and `[[libfuzzer]]` harness contract; keep recognition, dispatch selectors, lengths, and state setup coherent until parser reachability is stable.
2. Apply the causal relation from the failure shape before broad mutation or seed sweeping.
3. Change one invariant at a time: selector-to-subparser, declared length-to-available data, container count-to-record body, lifetime/ownership state, or allocation-size relation.
4. Submit only candidates where the vulnerable image reaches the target relation and the fixed image exits cleanly, rejects the relation, or otherwise avoids the target crash.

## Verifier Contract
This policy is ranked by one round-36 official target match. Re-rank or quarantine it if later use returns only clean exits, wrong sinks, wrapper-specific crashes, or fixed-image crashes.

## Negative Memory
- Do not corrupt the outer `zlib-deflate` recognition gate while retargeting this signal.
- Do not count parser reachability, both-image crashes, local wrapper crashes, clean exits, or fixed-image crashes as success.
- Do not store payload bytes, exact positions, task identifiers, checksums, or submit metadata.

## Evidence Shape
- Support: 1 server-verified round 36 solve after 1 attempts.
- Candidate family: construct.
- Scope: generator repair and retargeting only.
