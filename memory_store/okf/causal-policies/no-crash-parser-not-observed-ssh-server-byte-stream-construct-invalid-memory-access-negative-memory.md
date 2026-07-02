---
type: negative-memory
title: "No Crash Parser Not Observed SSH Server Byte Stream Construct Invalid Memory Access Negative Memory"
description: "Round 26 negative memory for no_crash with verifier signal parser_not_observed."
failure_class: "no_crash"
verifier_signal: "parser_not_observed"
candidate_family: "construct"
input_format: "ssh-server-byte-stream"
harness_convention: "libfuzzer"
vuln_class: "invalid-memory-access"
access_scope: generate
success_count: 0
confidence: medium
tags: ["no-crash", "parser-not-observed", "ssh-server-byte-stream", "libfuzzer", "construct", "negative-memory", "round-26"]
match_keys: ["no_crash", "parser_not_observed", "ssh-server-byte-stream", "libfuzzer", "invalid-memory-access", "negative_memory"]
allowed_scopes: [generate]
forbidden_fields: [raw_poc_bytes, task_id, exact_offset, checksum, submit_metadata]
evidence_level: medium
train_only: true
round: 26
---
# No Crash Parser Not Observed SSH Server Byte Stream Construct Invalid Memory Access Negative Memory

- key: `no_crash x parser_not_observed`
- outcome: persistent failure / basin to avoid
- success_count: 0
- failure_count: 1
- related format facts: [[ssh-server-byte-stream]]
- related harness facts: [[libfuzzer]]

## Failure Shape
Constructed SSH server byte streams satisfied the visible banner and packet-framing contract, then varied pre-key packet families that can reach unpack-like length handling. The local verifier never reported a sanitizer finding or parser signal, so the attempt likely did not reach the specific secure-buffer/private-key unpack path described by the target.

## Policy
Treat `no_crash x parser_not_observed` on `ssh-server-byte-stream` as a basin to avoid unless a new candidate changes the parser gate, state relation, or sink relation described below. Preserve any proven reachability, but reject variants that return to the same clean-exit, off-target-crash, wrong-sink, usage-only, wrapper-mismatch, or both-image-crash basin.

## Procedure
1. Keep only the smallest parser or harness envelope that was actually reached.
2. Identify the missing causal relation from the signal: parser selection, container acceptance, length relation, stateful subobject, allocation state, or official target sink.
3. Change one relation at a time and discard candidates that return to the same `parser_not_observed` basin.
4. If a local crash is not an official target match, shrink or discard it before mutating deeper fields.
5. Promote a recovery from this basin only after a later verifier-confirmed target match.

## Negative Memory
- Do not resubmit broad mutations that only reproduce `parser_not_observed`.
- Do not count parser reachability, both-image crashes, local wrapper crashes, usage banners, clean exits, or fixed-image crashes as success.
- Never store raw payload bytes, exact positions, task identifiers, checksums, or submit metadata.

## Format Contract
SSH server inputs are raw client-side socket byte streams: a text identification line followed by binary SSH transport packets. Each cleartext packet carries a network-order packet length, a padding-length byte, payload bytes beginning with an SSH message type, and padding chosen so the packet aligns to the pre-key block size. KEXINIT payloads contain a cookie, ten SSH name-list strings, a first-packet-follows flag, and a reserved word; many later fields are SSH strings with network-order lengths.

## Harness Contract
The libFuzzer harness writes the entire PoC to one end of a socketpair, shuts down writes, installs a server RSA key, accepts the other socket as a libssh server session, runs server key exchange, and then drains queued ssh_message objects only if key exchange succeeds. There is no FuzzedDataProvider carving; the whole file is the client byte stream.

## Evidence Shape
- Support: 1 diagnosed persistent failure from round 26 after 5 attempts.
- Scope: generator repair and basin avoidance only.
