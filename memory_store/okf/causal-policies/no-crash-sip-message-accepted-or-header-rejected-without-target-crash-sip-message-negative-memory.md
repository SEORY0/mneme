---
type: causal-policy
title: "No Crash Sip Message Accepted Or Header Rejected Without Target Crash Sip Message Negative Memory"
description: "Round 8 negative memory for no_crash with verifier signal sip_message_accepted_or_header_rejected_without_target_crash."
failure_class: "no_crash"
verifier_signal: "sip_message_accepted_or_header_rejected_without_target_crash"
candidate_family: "construct"
input_format: "sip message"
harness_convention: "libfuzzer"
vuln_class: "out-of-bounds-read"
access_scope: generate
success_count: 0
confidence: medium
tags: ["no-crash", "sip-message-accepted-or-header-rejected-without-target-crash", "sip-message", "negative_memory", "round-8"]
match_keys: ["no_crash", "sip_message_accepted_or_header_rejected_without_target_crash", "sip message", "libfuzzer", "negative_memory"]
allowed_scopes: [generate]
forbidden_fields: [raw_poc_bytes, task_id, exact_offset, checksum, submit_metadata]
evidence_level: medium
train_only: true
round: 8
---
# No Crash Sip Message Accepted Or Header Rejected Without Target Crash Sip Message Negative Memory

## Policy
Treat `no_crash x sip_message_accepted_or_header_rejected_without_target_crash` as a persistent failure basin for `sip message` under `libfuzzer`. Preserve any reachability it proved, but do not keep mutating the same field basin unless the next verification changes the signal.

## Diagnosed Dead End
- Valid SIP envelopes with To parameters, empty parameter values, truncated header endings, quoted value EOF, and multi-body variants did not reproduce the described boundary error. The unresolved detail is the exact state where the To-parameter parser has a non-null-terminated span but the surrounding message parser still considers the header complete.

## Format and Harness Gates
- Format: A useful input must be a SIP request/status message with a valid start line and CRLF-delimited headers. The target parameter parser is entered from a To header after a URI/body has ended and a semicolon starts parameters; tag and general parameters have distinct parser states.
- Harness: The fuzzer passes raw message bytes to parse_msg and then frees the parsed message. There is no mode byte; the input must satisfy the SIP message/header envelope before To-parameter parsing matters.

## Procedure
1. Before retrying this basin, rebuild the carrier around the exact harness contract and confirm parser reachability.
2. Replace the failed mutation family with a more specific invariant that would change the verifier signal.
3. Avoid broad seed mutation, oversized mutation, or off-target crash chasing when this same signal recurs.

## Negative Memory
- Do not promote this basin into a recovery policy until an official vulnerable/fixed verifier target match is observed.
- Do not preserve raw bytes, offsets, checksums, or task-local identifiers.

## Evidence Shape
- Support: one round-8 persistent failure trace.
- Scope: generator avoidance and retargeting for the same failure key.
