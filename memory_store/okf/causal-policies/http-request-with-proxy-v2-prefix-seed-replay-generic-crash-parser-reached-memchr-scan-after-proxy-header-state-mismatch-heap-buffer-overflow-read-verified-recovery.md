---
type: causal-policy
title: "Http Request With Proxy V2 Prefix Seed Replay Generic Crash Parser Reached Memchr Scan After Proxy Header State Mismatch Heap Buffer Overflow Read Verified Recovery"
description: "Round 37 verified recovery for generic_crash with verifier signal parser_reached_memchr_scan_after_proxy_header_state_mismatch."
failure_class: "generic_crash"
verifier_signal: "parser_reached_memchr_scan_after_proxy_header_state_mismatch"
candidate_family: "seed_replay"
input_format: "http-request-with-proxy-v2-prefix"
harness_convention: "libfuzzer"
vuln_class: "heap-buffer-overflow-read"
access_scope: generate
success_count: 1
confidence: high
tags: ["generic-crash", "parser-reached-memchr-scan-after-proxy-header-state-mismatch", "http-request-with-proxy-v2-prefix", "libfuzzer", "seed-replay", "heap-buffer-overflow-read", "verified-recovery", "round-37"]
match_keys: ["generic_crash", "parser_reached_memchr_scan_after_proxy_header_state_mismatch", "http-request-with-proxy-v2-prefix", "libfuzzer", "heap-buffer-overflow-read", "verified-recovery", "seed_replay"]
allowed_scopes: [generate]
forbidden_fields: [raw_poc_bytes, task_id, exact_offset, checksum, submit_metadata]
evidence_level: high
train_only: true
round: 37
---
# Http Request With Proxy V2 Prefix Seed Replay Generic Crash Parser Reached Memchr Scan After Proxy Header State Mismatch Heap Buffer Overflow Read Verified Recovery

- key: `generic_crash x parser_reached_memchr_scan_after_proxy_header_state_mismatch`
- outcome: server-verified target match
- success_count: 1
- related format facts: [[http-request-with-proxy-v2-prefix]]
- related harness facts: [[libfuzzer]]

## Failure Shape
Use a real HttpWithProxy fuzz corpus input rather than a hand-built request. The successful family preserves the raw chunked HTTP/proxy stream shape that reaches repeated header parsing with proxy support enabled, then lets the parser revisit proxy-prefixed/header bytes while its remaining-length state is inconsistent. That drives the vulnerable build into an over-wide header terminator scan; the fixed build handles or rejects the repeated proxy/header state cleanly.

## Policy
When `generic_crash x parser_reached_memchr_scan_after_proxy_header_state_mismatch` appears for `http-request-with-proxy-v2-prefix` under `libfuzzer`, preserve the parser, format, and harness gates that the verifier proved before mutating the sink-specific relation. Treat official vulnerable/fixed divergence as the success gate; local crash labels are supporting signals only.

## Procedure
1. Start from the `[[http-request-with-proxy-v2-prefix]]` format contract and `[[libfuzzer]]` harness contract; keep recognition, dispatch selectors, lengths, and state setup coherent until parser reachability is stable.
2. Apply the causal relation from the failure shape before broad mutation or seed sweeping.
3. Change one invariant at a time: selector-to-subparser, declared length-to-available data, container count-to-record body, lifetime/ownership state, allocation-size relation, or sanitizer-specific sink relation.
4. Submit only candidates where the vulnerable image reaches the target relation and the fixed image exits cleanly, rejects the relation, or otherwise avoids the target crash.

## Verifier Contract
This policy is ranked by 1 official target match. Re-rank or quarantine it if later use returns only clean exits, wrong sinks, wrapper-specific crashes, or fixed-image crashes.

## Negative Memory
- Do not corrupt the outer `http-request-with-proxy-v2-prefix` recognition gate while retargeting this signal.
- Do not count parser reachability, both-image crashes, local wrapper crashes, clean exits, or fixed-image crashes as success.
- Do not store payload bytes, exact positions, task identifiers, checksums, or submit metadata.

## Evidence Shape
- Support: server-verified round 37 solve after 16 attempts.
- Candidate family: seed_replay.
- Official split: vulnerable exit 1, fixed exit 0, target_match True.
- Scope: generator repair and retargeting only.
