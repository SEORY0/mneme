---
type: negative-memory
title: "Cryptofuzz Binary Operation Stream Construct No Crash Clean Exit After Cryptofuzz Bignumcalc Integer Overflow Or Constant Time Copy Width Negative Memory"
description: "Round 37 negative memory for no_crash with verifier signal clean_exit_after_cryptofuzz_bignumcalc."
failure_class: "no_crash"
verifier_signal: "clean_exit_after_cryptofuzz_bignumcalc"
candidate_family: "construct"
input_format: "cryptofuzz-binary-operation-stream"
harness_convention: "libfuzzer-cryptofuzz-binary-operation-stream"
vuln_class: "integer-overflow-or-constant-time-copy-width"
access_scope: generate
success_count: 0
failure_count: 1
confidence: medium
tags: ["no-crash", "clean-exit-after-cryptofuzz-bignumcalc", "cryptofuzz-binary-operation-stream", "libfuzzer-cryptofuzz-binary-operation-stream", "construct", "integer-overflow-or-constant-time-copy-width", "negative-memory", "round-37"]
match_keys: ["no_crash", "clean_exit_after_cryptofuzz_bignumcalc", "cryptofuzz-binary-operation-stream", "libfuzzer-cryptofuzz-binary-operation-stream", "integer-overflow-or-constant-time-copy-width", "negative-memory", "construct"]
allowed_scopes: [generate]
forbidden_fields: [raw_poc_bytes, task_id, exact_offset, checksum, submit_metadata]
evidence_level: medium
train_only: true
round: 37
---
# Cryptofuzz Binary Operation Stream Construct No Crash Clean Exit After Cryptofuzz Bignumcalc Integer Overflow Or Constant Time Copy Width Negative Memory

- key: `no_crash x clean_exit_after_cryptofuzz_bignumcalc`
- outcome: persistent failure / basin to avoid
- success_count: 0
- failure_count: 1
- related format facts: [[cryptofuzz-binary-operation-stream]]
- related harness facts: [[libfuzzer-cryptofuzz-binary-operation-stream]]

## Failure Shape
The Cryptofuzz BignumCalc envelope was confirmed to select wolfCrypt and compare against the reference module. Conditional-copy, multiplication, squaring, modular multiplication, modular squaring, multiply-add, dense operands, power-shaped operands, maximum accepted operands, digit multiplication, and modifier-controlled conversion all executed cleanly without a wolfCrypt/reference divergence or sanitizer crash.

## Observed Basin
- Failure trajectory classes: no_crash, no_crash, no_crash, no_crash, no_crash, no_crash, no_crash, no_crash, no_crash, no_crash, no_crash, no_crash, no_crash, no_crash, no_crash.
- Official confirmation: no server target match for this basin.

## Policy
Treat `no_crash x clean_exit_after_cryptofuzz_bignumcalc` on `cryptofuzz-binary-operation-stream` under `libfuzzer-cryptofuzz-binary-operation-stream` as a basin to avoid unless a new candidate changes the parser gate, state relation, or sink relation described above. Preserve any proven reachability, but reject variants that return to the same clean-exit, off-target-crash, wrapper-mismatch, usage-only, timeout, or fixed-image-crash behavior.

## Procedure
1. Keep only the smallest parser or harness envelope that was actually reached.
2. Identify the missing relation from the signal: parser selection, container acceptance, length relation, stateful subobject, allocation state, or official target sink.
3. Change one relation at a time and discard candidates that return to the same `clean_exit_after_cryptofuzz_bignumcalc` basin.
4. Promote a recovery from this basin only after a later official target match.

## Negative Memory
- Do not resubmit broad mutations that only reproduce `clean_exit_after_cryptofuzz_bignumcalc`.
- Do not count parser reachability, both-image crashes, local wrapper crashes, clean exits, timeouts, or fixed-image crashes as success.
- Do not store payload bytes, exact positions, task identifiers, checksums, or submit metadata.

## Evidence Shape
- Support: one diagnosed persistent failure from round 37 after 15 attempts.
- Candidate family: construct.
- Scope: generator repair and basin avoidance only.
