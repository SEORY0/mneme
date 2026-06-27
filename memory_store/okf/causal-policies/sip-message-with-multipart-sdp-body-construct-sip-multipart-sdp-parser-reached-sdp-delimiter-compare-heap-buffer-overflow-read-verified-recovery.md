---
type: causal-policy
title: "SIP Message With Multipart Sdp Body Construct SIP Multipart Sdp Parser Reached Sdp Delimiter Compare Heap Buffer Overflow Read Verified Recovery"
description: "Round 19 verified recovery for wrong_sink with verifier signal parser_reached_sdp_delimiter_compare."
failure_class: "wrong_sink"
verifier_signal: "parser_reached_sdp_delimiter_compare"
candidate_family: "construct_sip_multipart_sdp"
input_format: "sip-message-with-multipart-sdp-body"
harness_convention: "libfuzzer"
vuln_class: "heap-buffer-overflow-read"
access_scope: generate
success_count: 1
confidence: medium
tags: ["wrong-sink", "parser-reached-sdp-delimiter-compare", "sip-message-with-multipart-sdp-body", "libfuzzer", "construct-sip-multipart-sdp", "verified-recovery", "round-19"]
match_keys: ["wrong-sink", "parser-reached-sdp-delimiter-compare", "sip-message-with-multipart-sdp-body", "libfuzzer", "heap-buffer-overflow-read"]
allowed_scopes: [generate]
forbidden_fields: [raw_poc_bytes, task_id, exact_offset, checksum, submit_metadata]
evidence_level: high
train_only: true
round: 19
---
# SIP Message With Multipart Sdp Body Construct SIP Multipart Sdp Parser Reached Sdp Delimiter Compare Heap Buffer Overflow Read Verified Recovery

- key: `wrong_sink x parser_reached_sdp_delimiter_compare`
- outcome: verified recovery
- success_count: 1
- failure_count: 0
- formats: [[sip-message-with-multipart-sdp-body]]
- harnesses: [[libfuzzer]]

## Failure Shape
Use a syntactically valid SIP message that parses through the normal message parser, declare a multipart content type with a boundary, and include an application/sdp part with ordinary SDP session/media lines. The trigger is a later delimiter candidate near the end of the body that is shorter than the declared boundary, so the SDP multipart delimiter scanner compares past the available line buffer; the fixed build bounds the comparison and rejects it.

## Policy
For `wrong_sink x parser_reached_sdp_delimiter_compare` on `sip-message-with-multipart-sdp-body`, preserve the parser and harness gates first, then mutate only the causal invariant described by the verified trace. Prefer `construct_sip_multipart_sdp` while this format and harness contract are present.

## Procedure
1. Preserve the `sip-message-with-multipart-sdp-body` carrier enough for the `libfuzzer` harness to reach the parser path.
2. Keep unrelated envelope fields minimal and stable so verifier feedback stays tied to the target sink.
3. Apply the verified invariant from the failure shape rather than random broad mutation.
4. Submit only candidates where the vulnerable image reaches the target relation and the fixed image rejects or avoids it.

## Verifier Contract
The local class may remain coarse. Treat the official vulnerable-versus-fixed target match as the confirmation gate for this policy.

## Negative Memory
- Do not corrupt the outer `sip-message-with-multipart-sdp-body` recognition gate while retargeting this signal.
- Do not treat off-target crashes or both-image crashes as success for this policy.
- Never store raw payload bytes, exact offsets, checksums, or task-local identifiers in memory.

## Evidence Shape
- Support: 1 server-verified round 19 solve.
- Scope: generator repair only.
