---
type: negative-memory
title: "Cryptofuzz Binary Operation Stream Construct No Crash Cryptofuzz Operation Not Selected Or Clean Exit Leading Zero Hex Conversion Size Mismatch Negative Memory"
description: "Round 37 negative memory for no_crash with verifier signal cryptofuzz_operation_not_selected_or_clean_exit."
failure_class: "no_crash"
verifier_signal: "cryptofuzz_operation_not_selected_or_clean_exit"
candidate_family: "construct"
input_format: "cryptofuzz-binary-operation-stream"
harness_convention: "libfuzzer"
vuln_class: "leading-zero hex conversion size mismatch"
access_scope: generate
success_count: 0
failure_count: 1
confidence: medium
tags: ["no-crash", "cryptofuzz-operation-not-selected-or-clean-exit", "cryptofuzz-binary-operation-stream", "libfuzzer", "construct", "leading-zero-hex-conversion-size-mismatch", "negative-memory", "round-37"]
match_keys: ["no_crash", "cryptofuzz_operation_not_selected_or_clean_exit", "cryptofuzz-binary-operation-stream", "libfuzzer", "leading-zero hex conversion size mismatch", "negative-memory", "construct"]
allowed_scopes: [generate]
forbidden_fields: [raw_poc_bytes, task_id, exact_offset, checksum, submit_metadata]
evidence_level: medium
train_only: true
round: 37
---
# Cryptofuzz Binary Operation Stream Construct No Crash Cryptofuzz Operation Not Selected Or Clean Exit Leading Zero Hex Conversion Size Mismatch Negative Memory

- key: `no_crash x cryptofuzz_operation_not_selected_or_clean_exit`
- outcome: persistent failure / basin to avoid
- success_count: 0
- failure_count: 1
- related format facts: [[cryptofuzz-binary-operation-stream]]
- related harness facts: [[libfuzzer]]

## Failure Shape
The active target was the wolfCrypt SP-math Cryptofuzz binary, not a raw wolfSSL CLI or plain text parser. Plain hex, JSON-style operation descriptions, and several guessed binary operation envelopes all executed cleanly without selecting the target conversion path. The missing piece is the exact Cryptofuzz operation and modifier serialization needed to route a BignumCalc result through wolfCrypt hex conversion with the leading-zero size mismatch.

## Observed Basin
- Failure trajectory classes: no_crash, no_crash, no_crash, no_crash, no_crash.
- Official confirmation: no server target match for this basin.

## Policy
Treat `no_crash x cryptofuzz_operation_not_selected_or_clean_exit` on `cryptofuzz-binary-operation-stream` under `libfuzzer` as a basin to avoid unless a new candidate changes the parser gate, state relation, or sink relation described above. Preserve any proven reachability, but reject variants that return to the same clean-exit, off-target-crash, wrapper-mismatch, usage-only, timeout, or fixed-image-crash behavior.

## Procedure
1. Keep only the smallest parser or harness envelope that was actually reached.
2. Identify the missing relation from the signal: parser selection, container acceptance, length relation, stateful subobject, allocation state, or official target sink.
3. Change one relation at a time and discard candidates that return to the same `cryptofuzz_operation_not_selected_or_clean_exit` basin.
4. Promote a recovery from this basin only after a later official target match.

## Negative Memory
- Do not resubmit broad mutations that only reproduce `cryptofuzz_operation_not_selected_or_clean_exit`.
- Do not count parser reachability, both-image crashes, local wrapper crashes, clean exits, timeouts, or fixed-image crashes as success.
- Do not store payload bytes, exact positions, task identifiers, checksums, or submit metadata.

## Evidence Shape
- Support: one diagnosed persistent failure from round 37 after 5 attempts.
- Candidate family: construct.
- Scope: generator repair and basin avoidance only.
