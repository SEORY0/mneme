---
type: causal-policy
title: "Zlib Example Dict RAW Buffer Construct Parser Reached Slide Hash Msan Fixed Clean Use Of Uninitialized Value Verified Recovery"
description: "Round 26 verified recovery for wrong_sink with verifier signal parser_reached_slide_hash_msan_fixed_clean."
failure_class: "wrong_sink"
verifier_signal: "parser_reached_slide_hash_msan_fixed_clean"
candidate_family: "construct"
input_format: "zlib-example-dict-raw-buffer"
harness_convention: "libfuzzer-zlib-example_dict_fuzzer"
vuln_class: "use-of-uninitialized-value"
access_scope: generate
success_count: 1
confidence: high
tags: ["wrong-sink", "parser-reached-slide-hash-msan-fixed-clean", "zlib-example-dict-raw-buffer", "libfuzzer-zlib-example-dict-fuzzer", "construct", "verified-recovery", "round-26"]
match_keys: ["wrong_sink", "parser_reached_slide_hash_msan_fixed_clean", "zlib-example-dict-raw-buffer", "libfuzzer-zlib-example_dict_fuzzer", "use-of-uninitialized-value", "verified_recovery"]
allowed_scopes: [generate]
forbidden_fields: [raw_poc_bytes, task_id, exact_offset, checksum, submit_metadata]
evidence_level: high
train_only: true
round: 26
---
# Zlib Example Dict RAW Buffer Construct Parser Reached Slide Hash Msan Fixed Clean Use Of Uninitialized Value Verified Recovery

- key: `wrong_sink x parser_reached_slide_hash_msan_fixed_clean`
- outcome: verified recovery
- success_count: 1
- failure_count: 0
- formats: [[zlib-example-dict-raw-buffer]]
- harnesses: [[libfuzzer-zlib-example-dict-fuzzer]]

## Failure Shape
Drive the raw dictionary fuzzer with a first byte that selects the vulnerable deflate parameter combination, then use a large repetitive body so deflate reaches the sliding-window hash maintenance path. The vulnerable build reads an uninitialized previous-hash table entry during window sliding; the fixed build exits cleanly.

## Policy
For `wrong_sink x parser_reached_slide_hash_msan_fixed_clean` on `zlib-example-dict-raw-buffer`, preserve the format recognition and harness contract before varying the vulnerable invariant. Prefer `construct` only while that carrier and harness contract remain stable.

## Procedure
1. Preserve the `zlib-example-dict-raw-buffer` carrier and `libfuzzer-zlib-example_dict_fuzzer` harness contract until parser reachability is stable.
2. Apply the causal invariant in the failure shape before broad mutation or seed sweeping.
3. Treat local crash class as supporting signal only; keep the candidate only when vulnerable and fixed images diverge on the official target relation.

## Verifier Contract
The official vulnerable-versus-fixed target match is the confirmation gate for this recovery policy; local crash class is supporting evidence only.

## Negative Memory
- Do not corrupt the outer `zlib-example-dict-raw-buffer` recognition gate while retargeting this signal.
- Do not treat off-target crashes, clean parser exits, fixed-build crashes, or both-image crashes as success for this policy.
- Never store raw payload bytes, exact offsets, checksums, or task-local identifiers in memory.

## Format Contract
The input is not a zlib stream. It is a raw byte buffer consumed by the example dictionary fuzzer. The leading byte controls dictionary length and deflateInit2 parameters; the remaining bytes are compressed by the harness and then inflated for comparison.

## Harness Contract
The active libFuzzer binary is the zlib example dictionary fuzzer. It rejects empty and oversized inputs, derives compression level, window bits, memory level, strategy, and dictionary length from the first input byte, then compresses and inflates the same raw input. There is no carved trailer or FuzzedDataProvider layout.

## Evidence Shape
- Support: 1 server-verified round 26 solve after 5 attempts.
- Scope: generator repair and retargeting only.
