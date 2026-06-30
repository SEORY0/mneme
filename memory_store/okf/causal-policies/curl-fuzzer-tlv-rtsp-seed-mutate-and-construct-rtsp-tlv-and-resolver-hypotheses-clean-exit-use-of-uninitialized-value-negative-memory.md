---
type: negative-memory
title: "Curl Fuzzer Tlv RTSP Seed Mutate And Construct RTSP Tlv And Resolver Hypotheses Clean Exit Use Of Uninitialized Value Negative Memory"
description: "Round 29 negative memory for no_crash with verifier signal rtsp_tlv_and_resolver_hypotheses_clean_exit."
failure_class: "no_crash"
verifier_signal: "rtsp_tlv_and_resolver_hypotheses_clean_exit"
candidate_family: "seed_mutate_and_construct"
input_format: "curl-fuzzer-tlv-rtsp"
harness_convention: "afl-libfuzzer-wrapper"
vuln_class: "use-of-uninitialized-value"
access_scope: generate
success_count: 0
failure_count: 1
confidence: medium
tags: ["no-crash", "rtsp-tlv-and-resolver-hypotheses-clean-exit", "curl-fuzzer-tlv-rtsp", "afl-libfuzzer-wrapper", "seed-mutate-and-construct", "use-of-uninitialized-value", "negative-memory", "round-29"]
match_keys: ["no_crash", "rtsp_tlv_and_resolver_hypotheses_clean_exit", "curl-fuzzer-tlv-rtsp", "afl-libfuzzer-wrapper", "use-of-uninitialized-value", "no-crash", "rtsp-tlv-and-resolver-hypotheses-clean-exit", "curl-fuzzer-tlv-rtsp", "afl-libfuzzer-wrapper", "use-of-uninitialized-value", "negative_memory", "seed_mutate_and_construct", "seed-mutate-and-construct"]
allowed_scopes: [generate]
forbidden_fields: [raw_poc_bytes, task_id, exact_offset, checksum, submit_metadata]
evidence_level: medium
train_only: true
round: 29
---
# Curl Fuzzer Tlv RTSP Seed Mutate And Construct RTSP Tlv And Resolver Hypotheses Clean Exit Use Of Uninitialized Value Negative Memory

- key: `no_crash x rtsp_tlv_and_resolver_hypotheses_clean_exit`
- outcome: persistent failure / basin to avoid
- success_count: 0
- failure_count: 1
- related format facts: [[curl-fuzzer-tlv-rtsp]]
- related harness facts: [[afl-libfuzzer-wrapper]]

## Failure Shape
Valid RTSP TLV carriers, checked-in RTSP corpus seeds, staged RTSP responses, proxy variants with failing and resolvable proxy names, DoH URL variants, local-interface host binding, Unix-domain socket options, IP-version forcing, timeout forcing, and RTSP request-phase mutations all exited cleanly. The likely missing condition is a curl connection state that reaches the vulnerable resolve-server DNS-entry assignment without the normal resolver helper initializing the output pointer, but the exposed RTSP fuzzer defaults force ordinary target connections through a local connect-to redirect and the tested proxy/local-bind alternatives did not produce the uninitialized-value report.

## Policy
Treat `no_crash x rtsp_tlv_and_resolver_hypotheses_clean_exit` on `curl-fuzzer-tlv-rtsp` for `use-of-uninitialized-value` as a basin to avoid unless a new candidate changes the parser gate, state relation, or sink relation described below. Preserve any proven reachability, but reject variants that return to the same clean-exit, off-target-crash, wrong-sink, usage-only, wrapper-mismatch, or both-image-crash basin.

## Procedure
1. Keep only the smallest parser or harness envelope that was actually reached.
2. Identify the missing causal relation from the signal: parser selection, container acceptance, length relation, stateful subobject, allocation state, or official target sink.
3. Change one relation at a time and discard candidates that return to the same `rtsp_tlv_and_resolver_hypotheses_clean_exit` basin.
4. If a local crash is not an official target match, shrink or discard it before mutating deeper fields.
5. Promote a recovery from this basin only after a later verifier-confirmed target match.

## Negative Memory
- Do not resubmit broad mutations that only reproduce `rtsp_tlv_and_resolver_hypotheses_clean_exit`.
- Do not count parser reachability, both-image crashes, local wrapper crashes, usage banners, clean exits, or fixed-image crashes as success.
- Never store payload bytes, exact positions, task identifiers, checksums, or submit metadata.

## Format Contract
curl-fuzzer RTSP inputs are a big-endian TLV stream. A URL TLV configures the transfer URL; numbered response TLVs stage server bytes, with the first useful RTSP response normally in the first post-connect response slot rather than as raw leading text. RTSP option TLVs can select request method, stream URI, session id, transport header, and CSeq values. String TLVs are copied into libcurl options with NUL termination by the harness; integer option TLVs use fixed-width big-endian values. Response slot ordering is part of the protocol state: RTSP replies must match the client request phase well enough for transfer progress, while HTTP or SOCKS-like proxy response slots are separate carrier hypotheses.

## Harness Contract
The active binary is curl_fuzzer_rtsp under an AFL-compatible single-file wrapper. The whole file is parsed as TLVs from the front; there is no FuzzedDataProvider back-loading and no raw URL or raw RTSP transcript mode. The harness parses all TLVs, then applies standard curl callbacks and a local connect-to redirect before running a curl multi transfer against socketpair-backed synthetic sockets. Because of that redirect, ordinary RTSP URL hostnames do not necessarily exercise normal hostname resolution; proxy, DoH, interface, and Unix-socket options are the plausible alternate routes into hostip resolver code.

## Evidence Shape
- Support: 1 diagnosed persistent failure from round 29 after 46 attempts.
- Scope: generator repair and basin avoidance only.
