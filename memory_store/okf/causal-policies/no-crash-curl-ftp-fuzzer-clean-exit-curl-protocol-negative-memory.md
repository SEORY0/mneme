---
type: causal-policy
title: "No Crash Curl Ftp Fuzzer Clean Exit Curl Protocol Negative Memory"
description: "Round 10 negative memory for no_crash with verifier signal curl_ftp_fuzzer_clean_exit."
failure_class: "no_crash"
verifier_signal: "curl_ftp_fuzzer_clean_exit"
candidate_family: "construct"
input_format: "curl-protocol-fuzzer-input"
harness_convention: "libfuzzer"
vuln_class: "null-or-stale-pointer-dereference"
access_scope: generate
success_count: 0
confidence: medium
tags: ["no-crash", "curl-ftp-fuzzer-clean-exit", "negative-memory", "round-10"]
match_keys: ["no_crash", "curl_ftp_fuzzer_clean_exit", "curl-protocol-fuzzer-input", "libfuzzer", "negative_memory"]
allowed_scopes: [generate]
forbidden_fields: [raw_poc_bytes, task_id, exact_offset, checksum, submit_metadata]
evidence_level: medium
train_only: true
round: 10
---
# No Crash Curl Ftp Fuzzer Clean Exit Curl Protocol Negative Memory

## Policy
For `no_crash x curl_ftp_fuzzer_clean_exit`, avoid replaying the observed dead end. This negative memory is co-equal with positive policies and should redirect generation before another official submission.

## Procedure
1. Several distinct protocol selector and URL-shaped families executed the active curl FTP fuzzer cleanly.
2. When `no_crash x curl_ftp_fuzzer_clean_exit` appears for `curl-protocol-fuzzer-input`, treat this candidate family as a basin-to-avoid rather than as evidence of proximity to the target.
3. Keep any proven parser/harness envelope, but change the missing gate or state relation before submitting again.

## Format Contract
- The input is not a full network transcript by itself; the fuzzer interprets raw bytes as protocol-specific curl stimulus and then drives an FTP-oriented transfer/disconnect path internally. URL-like protocol selection alone is accepted but is not sufficient to force the target teardown edge.
- Harness: The local verifier runs a curl FTP libFuzzer target on the raw file bytes. No front/back FuzzedDataProvider carving was visible from the candidate behavior; the whole file is consumed by the target wrapper as its stimulus.

## Negative Memory
- Do not treat this verifier signal as a near miss unless a later candidate changes the missing gate or state relation.
- Do not submit candidates that are clean, parser-mismatched, off-target, or crashing both fixed and vulnerable images in this same shape.
- Preserve only descriptive format facts from the failed attempt; do not promote an unverified causal recovery.

## Evidence Shape
- Support: one diagnosed round-10 persistent failure.
- Scope: generator avoidance for the same failure-keyed basin.
