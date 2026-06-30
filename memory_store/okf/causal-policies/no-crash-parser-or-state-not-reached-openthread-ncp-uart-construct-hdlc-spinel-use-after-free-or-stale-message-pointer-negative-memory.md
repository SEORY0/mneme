---
type: causal-policy
title: "No Crash Parser Or State Not Reached Openthread Ncp Uart Construct Hdlc Spinel Use After Free Or Stale Message Pointer Negative Memory"
description: "Round 30 negative memory for no_crash with verifier signal parser_or_state_not_reached."
failure_class: "no_crash"
verifier_signal: "parser_or_state_not_reached"
candidate_family: "construct-hdlc-spinel"
input_format: "openthread-ncp-uart"
harness_convention: "libfuzzer-afl-wrapper"
vuln_class: "use-after-free-or-stale-message-pointer"
access_scope: generate
success_count: 0
confidence: medium
tags: ["no-crash", "parser-or-state-not-reached", "openthread-ncp-uart", "libfuzzer-afl-wrapper", "construct-hdlc-spinel", "negative-memory", "round-30"]
match_keys: ["no-crash", "parser-or-state-not-reached", "openthread-ncp-uart", "libfuzzer-afl-wrapper", "use-after-free-or-stale-message-pointer", "negative-memory"]
allowed_scopes: [generate]
forbidden_fields: [raw_poc_bytes, task_id, exact_offset, checksum, submit_metadata]
evidence_level: medium
train_only: true
round: 30
---
# No Crash Parser Or State Not Reached Openthread Ncp Uart Construct Hdlc Spinel Use After Free Or Stale Message Pointer Negative Memory

- key: `no-crash x parser-or-state-not-reached`
- outcome: persistent failure / basin to avoid
- success_count: 0
- formats: [[openthread-ncp-uart]]
- harnesses: [[libfuzzer-afl-wrapper]]

## Failure Shape
The NCP UART envelope was constructed as HDLC-framed Spinel and cleanly exercised basic command handling, but the attempts did not reach the precise Thread state where a data message being prepared for mesh forwarding allocates a higher-priority Address Solicit control message and evicts that same in-flight message. Distinct attempts covered basic parser reachability, local network-data prefix insertion followed by unresolved IPv6 routing, increasing allocator pressure with large unresolved IPv6 messages, direct CoAP Address Solicit requests to the leader locator, and NCP role-transition commands intended to force a child-to-router upgrade.

## Negative Policy
For `no-crash x parser-or-state-not-reached` on `openthread-ncp-uart`, do not continue broad mutation inside the same basin. The recorded trajectory was `no-crash, no-crash, no-crash, no-crash, no-crash` without a verified vulnerable-only target match.

## Avoid
1. Do not submit candidates that only prove parser reachability, clean exit, fixed-image crash, or a coarse local crash.
2. Do not widen mutations across multiple independent metadata families after this signal; first identify the missing gate or state transition.
3. Preserve the useful format and harness facts, but retarget a different causal invariant before spending more attempts.
4. If the verifier signal says the parser or state was not reached, rebuild the carrier/state path before touching sink-specific fields.

## Recovery Direction
Keep the accepted envelope facts from [[openthread-ncp-uart]] and [[libfuzzer-afl-wrapper]], then search for the smallest missing gate named by the diagnosis instead of repeating the failed candidate family.

## Evidence Shape
- Support: diagnosed round 30 failure.
- Scope: generator repair only; no success-rate credit.
