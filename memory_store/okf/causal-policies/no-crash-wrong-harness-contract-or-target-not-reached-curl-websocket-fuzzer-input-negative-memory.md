---
type: causal-policy
title: "No Crash Wrong Harness Contract Or Target Not Reached Curl Websocket Fuzzer Input Negative Memory"
description: "Round 12 negative memory for no_crash with verifier signal wrong_harness_contract_or_target_not_reached."
failure_class: "no_crash"
verifier_signal: "wrong_harness_contract_or_target_not_reached"
candidate_family: "construct"
input_format: "curl websocket fuzzer input"
harness_convention: "libfuzzer"
vuln_class: "invalid-free"
access_scope: generate
success_count: 0
confidence: medium
tags: ["no-crash", "wrong-harness-contract-or-target-not-reached", "curl-websocket-fuzzer-input", "negative-memory", "round-12"]
match_keys: ["no_crash", "wrong_harness_contract_or_target_not_reached", "curl-websocket-fuzzer-input", "libfuzzer", "invalid-free", "negative_memory"]
allowed_scopes: [generate]
forbidden_fields: [raw_poc_bytes, task_id, exact_offset, checksum, submit_metadata]
evidence_level: medium
train_only: true
round: 12
---
# No Crash Wrong Harness Contract Or Target Not Reached Curl Websocket Fuzzer Input Negative Memory

- key: `no_crash x wrong_harness_contract_or_target_not_reached`
- outcome: persistent failure / basin to avoid
- success_count: 0
- failure_count: 1
- related format facts: [[curl-websocket-fuzzer-input]]
- related harness facts: [[libfuzzer]]

## Failure Shape
The described aws-sigv4 bug is in curl option parsing, but the actual target binary is the websocket fuzzer. Argv-style option payloads and websocket frame/request/response shaped bytes did not reach the awssigv4 code path; several websocket-shaped files tripped a harness directory precondition instead of the target parser.

## Policy
Treat `no_crash x wrong_harness_contract_or_target_not_reached` on `curl-websocket-fuzzer-input` as a basin to avoid unless a new candidate changes the parser gate, state relation, or official target sink. Preserve any proven reachability, but reject variants that return to the same verifier signal without changing the causal gate under test.

## Procedure
1. Keep only the smallest parser or harness envelope that the verifier proved was reached.
2. Identify the missing causal relation from the signal: parser selection, container acceptance, length relation, stateful subobject, allocation state, or official target sink.
3. Change one relation at a time and discard candidates that return to the same clean-exit, off-target-crash, wrong-sink, usage-only, or both-image-crash basin.
4. If a local crash is not an official target match, shrink or discard it before mutating deeper fields.
5. Promote a recovery from this basin only after a later verifier-confirmed target match.

## Format Contract
The vulnerable curl option expects an AWS SigV4 provider string and related request headers, while websocket traffic uses HTTP upgrade messages and WebSocket frames. Those are distinct input families, and the observed fuzzer did not expose the CLI option surface directly.

## Harness Contract
The verifier runs curl_fuzzer_ws. The input is not a null-separated command-line argv contract. Some raw byte patterns are treated as paths or corpus-directory inputs by the harness wrapper, while plain header-like blobs execute the websocket fuzzer and exit normally.

## Negative Memory
- Do not resubmit broad mutations that only reproduce `wrong_harness_contract_or_target_not_reached`.
- Do not count parser reachability, both-image crashes, local wrapper crashes, clean exits, or fixed-image crashes as success.
- Do not store raw payload bytes, exact positions, task identifiers, or submit metadata.

## Evidence Shape
- Support: one diagnosed persistent failure from round 12.
- Scope: generator repair and basin avoidance only.
