---
type: negative-memory
title: "Fmt Named Argument Fuzzer Buffer Construct No Crash Named Arg Fuzzer Reached Without Sanitizer Finding Numeric Format Carry Error Negative Memory"
description: "Round 36 negative memory for no_crash with verifier signal named_arg_fuzzer_reached_without_sanitizer_finding."
failure_class: "no_crash"
verifier_signal: "named_arg_fuzzer_reached_without_sanitizer_finding"
candidate_family: "construct"
input_format: "fmt-named-argument-fuzzer-buffer"
harness_convention: "honggfuzz-raw-bytes"
vuln_class: "numeric-format-carry-error"
access_scope: generate
success_count: 0
failure_count: 1
confidence: medium
tags: ["no-crash", "named-arg-fuzzer-reached-without-sanitizer-finding", "fmt-named-argument-fuzzer-buffer", "honggfuzz-raw-bytes", "construct", "numeric-format-carry-error", "negative-memory", "round-36"]
match_keys: ["no_crash", "named_arg_fuzzer_reached_without_sanitizer_finding", "fmt-named-argument-fuzzer-buffer", "honggfuzz-raw-bytes", "numeric-format-carry-error", "no-crash", "named-arg-fuzzer-reached-without-sanitizer-finding", "negative_memory", "construct"]
allowed_scopes: [generate]
forbidden_fields: [raw_poc_bytes, task_id, exact_offset, checksum, submit_metadata]
evidence_level: medium
train_only: true
round: 36
---
# Fmt Named Argument Fuzzer Buffer Construct No Crash Named Arg Fuzzer Reached Without Sanitizer Finding Numeric Format Carry Error Negative Memory

- key: `no_crash x named_arg_fuzzer_reached_without_sanitizer_finding`
- outcome: persistent failure / basin to avoid
- success_count: 0
- failure_count: 1
- related format facts: [[fmt-named-argument-fuzzer-buffer]]
- related harness facts: [[honggfuzz-raw-bytes]]

## Failure Shape
The harness envelope was satisfied and the named-argument formatter ran, but verifier candidates stayed clean. Distinct hypotheses covered binary32 and double arguments, fixed/general/exponential presentation, zero and nonzero precisions, all-carry rounding boundaries, project-local fallback regression values, and subnormal or extreme-exponent values. A temporary local instrumented header showed fallback formatting is reachable for some generated states, but those states did not produce a sanitizer-visible crash under the official named-argument harness. The missing relation is likely a narrower fallback state where carry propagation empties or corrupts the generated digit buffer before exponential/general prettification.

## Observed Basin
- Failure trajectory classes: no_crash.
- Official confirmation: no server target match for this basin.

## Policy
Treat `no_crash x named_arg_fuzzer_reached_without_sanitizer_finding` on `fmt-named-argument-fuzzer-buffer` under `honggfuzz-raw-bytes` as a basin to avoid unless a new candidate changes the parser gate, state relation, or sink relation described above. Preserve any proven reachability, but reject variants that return to the same clean-exit, off-target-crash, wrapper-mismatch, usage-only, or fixed-image-crash behavior.

## Procedure
1. Keep only the smallest parser or harness envelope that was actually reached.
2. Identify the missing relation from the signal: parser selection, container acceptance, length relation, stateful subobject, allocation state, or official target sink.
3. Change one relation at a time and discard candidates that return to the same `named_arg_fuzzer_reached_without_sanitizer_finding` basin.
4. Promote a recovery from this basin only after a later official target match.

## Negative Memory
- Do not resubmit broad mutations that only reproduce `named_arg_fuzzer_reached_without_sanitizer_finding`.
- Do not count parser reachability, both-image crashes, local wrapper crashes, clean exits, or fixed-image crashes as success.
- Do not store payload bytes, exact positions, task identifiers, checksums, or submit metadata.

## Evidence Shape
- Support: 1 diagnosed persistent failure from round 36 after 34 attempts.
- Scope: generator repair and basin avoidance only.
