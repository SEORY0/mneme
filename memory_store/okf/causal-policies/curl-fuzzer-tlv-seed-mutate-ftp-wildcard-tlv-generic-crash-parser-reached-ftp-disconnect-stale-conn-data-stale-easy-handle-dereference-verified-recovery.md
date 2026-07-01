---
type: causal-policy
title: "Curl Fuzzer Tlv Seed Mutate Ftp Wildcard Tlv Generic Crash Parser Reached Ftp Disconnect Stale Conn Data Stale Easy Handle Dereference Verified Recovery"
description: "Round 32 server-verified recovery for curl-fuzzer-tlv keyed by generic_crash x parser_reached_ftp_disconnect_stale_conn_data."
failure_class: "generic_crash"
verifier_signal: "parser_reached_ftp_disconnect_stale_conn_data"
candidate_family: "seed_mutate_ftp_wildcard_tlv"
input_format: "curl-fuzzer-tlv"
harness_convention: "libfuzzer"
vuln_class: "stale-easy-handle-dereference"
access_scope: generate
success_count: 1
confidence: high
tags: ["generic-crash", "parser-reached-ftp-disconnect-stale-conn-data", "curl-fuzzer-tlv", "libfuzzer", "seed-mutate-ftp-wildcard-tlv", "stale-easy-handle-dereference", "verified-recovery", "round-32"]
match_keys: ["generic-crash", "parser-reached-ftp-disconnect-stale-conn-data", "curl-fuzzer-tlv", "libfuzzer", "seed-mutate-ftp-wildcard-tlv", "stale-easy-handle-dereference", "verified-recovery"]
allowed_scopes: [generate]
forbidden_fields: [raw_poc_bytes, task_id, exact_offset, checksum, submit_metadata]
evidence_level: high
train_only: true
round: 32
---
# Curl Fuzzer Tlv Seed Mutate Ftp Wildcard Tlv Generic Crash Parser Reached Ftp Disconnect Stale Conn Data Stale Easy Handle Dereference Verified Recovery

- key: `generic_crash x parser_reached_ftp_disconnect_stale_conn_data`
- outcome: server-verified target match
- success_count: 1
- related format facts: [[curl-fuzzer-tlv]]
- related harness facts: [[libfuzzer]]

## Policy
When `curl-fuzzer-tlv` under `[[libfuzzer]]` produces `parser_reached_ftp_disconnect_stale_conn_data` from `generic_crash`, keep the parser-reaching envelope and retarget the causal invariant that the official verifier accepted. Local sink labels are advisory once the vulnerable image fails and the fixed image stays clean or the server reports target match.

## Procedure
1. Preserve the harness and format contract that reached the parser: `[[curl-fuzzer-tlv]]` through `[[libfuzzer]]`.
2. Apply the verified recovery: Start from a valid FTP TLV seed rather than a URL-only stream. Drive a normal FTP login and passive directory transfer, answer PWD with a syntactically valid current-directory response so the FTP connection records an entry path, and enable wildcard matching on a URL whose path contains a wildcard. The directory data must include a matching entry so curl starts a follow-up wildcard transfer. During connection lookup for that follow-up transfer, curl disconnects a stale cached FTP connection; the vulnerable build calls the protocol disconnect while conn data still names the wrong transfer state, producing the target dereference, while the fixed build exits cleanly.
3. Keep mutations narrow around the gate/invariant relation rather than rebuilding unrelated carriers or adding broad random noise.
4. If local labels report a non-target sink while the parser branch is reached, submit one minimized candidate before discarding it.
5. Reject both-image crashes, fixed-image crashes, parser rejection, and clean exits as non-success even when they look close locally.

## Format Contract
- The curl fuzzer stream is a sequence of big-endian tag-length-value records. One record supplies the URL, ordered response records emulate server replies, an FTP secondary-socket response supplies passive data-channel bytes, and option records can toggle behaviors such as wildcard matching. FTP response slots are consumed by protocol phase, not merely by record order in the file.

## Harness Contract
- The active target is curl_fuzzer_ftp. The libFuzzer wrapper passes the whole file to the TLV parser from the front with no back-loaded fields. The harness installs mocked socket callbacks, sends response zero immediately on connection, sends later responses after client requests, and can open a second socket manager for the FTP passive data channel.

## Negative Memory
- Do not store concrete payload bytes, task identifiers, exact positions, checksums, or submit metadata.
- Do not treat parser reachability alone as success without the official target-match signal.
- Do not repeat a clean-exit or both-image-crash basin once the verifier has characterized it.

## Evidence Shape
- Support: one server-verified Round 32 solve.
- Candidate family: seed_mutate_ftp_wildcard_tlv.
