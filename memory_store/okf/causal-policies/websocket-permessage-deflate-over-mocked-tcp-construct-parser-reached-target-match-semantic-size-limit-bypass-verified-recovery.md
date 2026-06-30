---
type: causal-policy
title: "Websocket Permessage Deflate Over Mocked Tcp Construct Parser Reached Target Match Semantic Size Limit Bypass Verified Recovery"
description: "Round 26 verified recovery for generic_crash with verifier signal parser_reached_target_match."
failure_class: "generic_crash"
verifier_signal: "parser_reached_target_match"
candidate_family: "construct"
input_format: "websocket-permessage-deflate-over-mocked-tcp"
harness_convention: "libfuzzer-uwebsockets-mocked-tcp"
vuln_class: "semantic-size-limit-bypass"
access_scope: generate
success_count: 1
confidence: high
tags: ["generic-crash", "parser-reached-target-match", "websocket-permessage-deflate-over-mocked-tcp", "libfuzzer-uwebsockets-mocked-tcp", "construct", "verified-recovery", "round-26"]
match_keys: ["generic_crash", "parser_reached_target_match", "websocket-permessage-deflate-over-mocked-tcp", "libfuzzer-uwebsockets-mocked-tcp", "semantic-size-limit-bypass", "verified_recovery"]
allowed_scopes: [generate]
forbidden_fields: [raw_poc_bytes, task_id, exact_offset, checksum, submit_metadata]
evidence_level: high
train_only: true
round: 26
---
# Websocket Permessage Deflate Over Mocked Tcp Construct Parser Reached Target Match Semantic Size Limit Bypass Verified Recovery

- key: `generic_crash x parser_reached_target_match`
- outcome: verified recovery
- success_count: 1
- failure_count: 0
- formats: [[websocket-permessage-deflate-over-mocked-tcp]]
- harnesses: [[libfuzzer-uwebsockets-mocked-tcp]]

## Failure Shape
Use the mocked TCP chunk framing to deliver a valid WebSocket HTTP upgrade that negotiates permessage-deflate, followed by a masked client data frame marked compressed. Keep the compressed wire payload within the pre-inflate limit while making the inflated message just exceed the configured application payload limit, so the vulnerable build passes the pre-inflate check and reaches the message handler with an oversized message.

## Policy
For `generic_crash x parser_reached_target_match` on `websocket-permessage-deflate-over-mocked-tcp`, preserve the format recognition and harness contract before varying the vulnerable invariant. Prefer `construct` only while that carrier and harness contract remain stable.

## Procedure
1. Preserve the `websocket-permessage-deflate-over-mocked-tcp` carrier and `libfuzzer-uwebsockets-mocked-tcp` harness contract until parser reachability is stable.
2. Apply the causal invariant in the failure shape before broad mutation or seed sweeping.
3. Treat local crash class as supporting signal only; keep the candidate only when vulnerable and fixed images diverge on the official target relation.

## Verifier Contract
The official vulnerable-versus-fixed target match is the confirmation gate for this recovery policy; local crash class is supporting evidence only.

## Negative Memory
- Do not corrupt the outer `websocket-permessage-deflate-over-mocked-tcp` recognition gate while retargeting this signal.
- Do not treat off-target crashes, clean parser exits, fixed-build crashes, or both-image crashes as success for this policy.
- Never store raw payload bytes, exact offsets, checksums, or task-local identifiers in memory.

## Format Contract
The active input is not a standalone deflate buffer. It is a sequence of mocked socket chunks, each with a small length prefix followed by network bytes. WebSocket reachability requires a valid upgrade request and client frames must be masked. RSV1 marks a frame as permessage-deflate-compressed after the extension has been negotiated.

## Harness Contract
libFuzzer feeds raw bytes to a uSockets mock. The mock repeatedly consumes a chunk-length byte and then delivers that many bytes to the server callback. The active binary is the mocked echo server with compression enabled and a small max-payload setting; no FuzzedDataProvider or external file format is involved.

## Evidence Shape
- Support: 1 server-verified round 26 solve after 2 attempts.
- Scope: generator repair and retargeting only.
