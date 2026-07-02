---
type: causal-policy
title: "Blosc Chunk With Zlib Deflate Stream Construct Wrong Sink Parser Reached Miniz Msan Fixed Clean Confirmed By Submit Use Of Uninitialized Value Verified Recovery"
description: "Round 36 verified recovery for wrong_sink with verifier signal parser_reached_miniz_msan_fixed_clean_confirmed_by_submit."
failure_class: "wrong_sink"
verifier_signal: "parser_reached_miniz_msan_fixed_clean_confirmed_by_submit"
candidate_family: "construct"
input_format: "blosc chunk with zlib deflate stream"
harness_convention: "libfuzzer"
vuln_class: "use-of-uninitialized-value"
access_scope: generate
success_count: 1
confidence: high
tags: ["wrong-sink", "parser-reached-miniz-msan-fixed-clean-confirmed-by-submit", "blosc-chunk-with-zlib-deflate-stream", "libfuzzer", "construct", "use-of-uninitialized-value", "verified-recovery", "round-36"]
match_keys: ["wrong_sink", "parser_reached_miniz_msan_fixed_clean_confirmed_by_submit", "blosc chunk with zlib deflate stream", "libfuzzer", "use-of-uninitialized-value", "wrong-sink", "parser-reached-miniz-msan-fixed-clean-confirmed-by-submit", "blosc-chunk-with-zlib-deflate-stream", "verified_recovery", "construct"]
allowed_scopes: [generate]
forbidden_fields: [raw_poc_bytes, task_id, exact_offset, checksum, submit_metadata]
evidence_level: high
train_only: true
round: 36
---
# Blosc Chunk With Zlib Deflate Stream Construct Wrong Sink Parser Reached Miniz Msan Fixed Clean Confirmed By Submit Use Of Uninitialized Value Verified Recovery

- key: `wrong_sink x parser_reached_miniz_msan_fixed_clean_confirmed_by_submit`
- outcome: server-verified target match
- success_count: 1
- related format facts: [[blosc-chunk-with-zlib-deflate-stream]]
- related harness facts: [[libfuzzer]]

## Failure Shape
Construct a self-consistent regular Blosc chunk: compact header, nonzero uncompressed size, one block, total compressed size matching the complete input, and a block-start table that points to a single compressed stream. Select the zlib/miniz codec with the no-split stream layout. Inside the zlib wrapper, use a fixed-Huffman deflate block whose first meaningful operation is a minimal length/distance copy using the upper invalid distance-code family that reaches miniz's distance-copy path; fixed-Huffman codes must be emitted in their bit-reversed wire form. Avoid the neighboring invalid-distance variant that only creates a broad checksum-time uninitialized read in both builds.

## Policy
When `wrong_sink x parser_reached_miniz_msan_fixed_clean_confirmed_by_submit` appears for `blosc chunk with zlib deflate stream` under `libfuzzer`, preserve the parser, format, and harness gates that the verifier proved before mutating the sink-specific relation. Treat official vulnerable/fixed divergence as the success gate; local crash labels are supporting signals only.

## Procedure
1. Start from the `[[blosc-chunk-with-zlib-deflate-stream]]` format contract and `[[libfuzzer]]` harness contract; keep recognition, dispatch selectors, lengths, and state setup coherent until parser reachability is stable.
2. Apply the causal relation from the failure shape before broad mutation or seed sweeping.
3. Change one invariant at a time: selector-to-subparser, declared length-to-available data, container count-to-record body, lifetime/ownership state, or allocation-size relation.
4. Submit only candidates where the vulnerable image reaches the target relation and the fixed image exits cleanly, rejects the relation, or otherwise avoids the target crash.

## Verifier Contract
This policy is ranked by one round-36 official target match. Re-rank or quarantine it if later use returns only clean exits, wrong sinks, wrapper-specific crashes, or fixed-image crashes.

## Negative Memory
- Do not corrupt the outer `blosc chunk with zlib deflate stream` recognition gate while retargeting this signal.
- Do not count parser reachability, both-image crashes, local wrapper crashes, clean exits, or fixed-image crashes as success.
- Do not store payload bytes, exact positions, task identifiers, checksums, or submit metadata.

## Evidence Shape
- Support: 1 server-verified round 36 solve after 10 attempts.
- Candidate family: construct.
- Scope: generator repair and retargeting only.
