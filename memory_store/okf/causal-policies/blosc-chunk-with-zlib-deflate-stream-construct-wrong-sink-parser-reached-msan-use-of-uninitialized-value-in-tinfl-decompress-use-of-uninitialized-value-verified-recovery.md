---
type: causal-policy
title: "Blosc Chunk With Zlib Deflate Stream Construct Wrong Sink Parser Reached Msan Use Of Uninitialized Value In Tinfl Decompress Use Of Uninitialized Value Verified Recovery"
description: "Round 37 verified recovery for wrong_sink with verifier signal parser_reached_msan_use_of_uninitialized_value_in_tinfl_decompress."
failure_class: "wrong_sink"
verifier_signal: "parser_reached_msan_use_of_uninitialized_value_in_tinfl_decompress"
candidate_family: "construct"
input_format: "blosc-chunk-with-zlib-deflate-stream"
harness_convention: "libfuzzer"
vuln_class: "use-of-uninitialized-value"
access_scope: generate
success_count: 1
confidence: high
tags: ["wrong-sink", "parser-reached-msan-use-of-uninitialized-value-in-tinfl-decompress", "blosc-chunk-with-zlib-deflate-stream", "libfuzzer", "construct", "use-of-uninitialized-value", "verified-recovery", "round-37"]
match_keys: ["wrong_sink", "parser_reached_msan_use_of_uninitialized_value_in_tinfl_decompress", "blosc-chunk-with-zlib-deflate-stream", "libfuzzer", "use-of-uninitialized-value", "verified-recovery", "construct"]
allowed_scopes: [generate]
forbidden_fields: [raw_poc_bytes, task_id, exact_offset, checksum, submit_metadata]
evidence_level: high
train_only: true
round: 37
---
# Blosc Chunk With Zlib Deflate Stream Construct Wrong Sink Parser Reached Msan Use Of Uninitialized Value In Tinfl Decompress Use Of Uninitialized Value Verified Recovery

- key: `wrong_sink x parser_reached_msan_use_of_uninitialized_value_in_tinfl_decompress`
- outcome: server-verified target match
- success_count: 1
- related format facts: [[blosc-chunk-with-zlib-deflate-stream]]
- related harness facts: [[libfuzzer]]

## Failure Shape
Build a valid regular Blosc chunk that selects the zlib/miniz codec, has internally consistent uncompressed size, block size, total compressed size, and a single block-start entry. The one compressed block should be a zlib-wrapped fixed-Huffman deflate stream that emits an initialized literal and then uses a reserved high distance symbol whose decoded base distance is zero. The copy length should exactly complete the declared block so miniz proceeds into checksum verification, where the bytes copied from the current output cursor are used and the sanitizer reports the uninitialized value.

## Policy
When `wrong_sink x parser_reached_msan_use_of_uninitialized_value_in_tinfl_decompress` appears for `blosc-chunk-with-zlib-deflate-stream` under `libfuzzer`, preserve the parser, format, and harness gates that the verifier proved before mutating the sink-specific relation. Treat official vulnerable/fixed divergence as the success gate; local crash labels are supporting signals only.

## Procedure
1. Start from the `[[blosc-chunk-with-zlib-deflate-stream]]` format contract and `[[libfuzzer]]` harness contract; keep recognition, dispatch selectors, lengths, and state setup coherent until parser reachability is stable.
2. Apply the causal relation from the failure shape before broad mutation or seed sweeping.
3. Change one invariant at a time: selector-to-subparser, declared length-to-available data, container count-to-record body, lifetime/ownership state, allocation-size relation, or sanitizer-specific sink relation.
4. Submit only candidates where the vulnerable image reaches the target relation and the fixed image exits cleanly, rejects the relation, or otherwise avoids the target crash.

## Verifier Contract
This policy is ranked by 1 official target match. Re-rank or quarantine it if later use returns only clean exits, wrong sinks, wrapper-specific crashes, or fixed-image crashes.

## Negative Memory
- Do not corrupt the outer `blosc-chunk-with-zlib-deflate-stream` recognition gate while retargeting this signal.
- Do not count parser reachability, both-image crashes, local wrapper crashes, clean exits, or fixed-image crashes as success.
- Do not store payload bytes, exact positions, task identifiers, checksums, or submit metadata.

## Evidence Shape
- Support: server-verified round 37 solve after 9 attempts.
- Candidate family: construct.
- Official split: vulnerable exit 77, fixed exit 0, target_match True.
- Scope: generator repair and retargeting only.
