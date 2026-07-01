---
type: negative-memory
title: "Ipv6 Udp Coap Meshcop Tlv Construct No Crash Clean Exit After Ipv6 Udp Coap Meshcop Tlv Attempts Channel Mask Validation Bypass Negative Memory"
description: "Round 37 negative memory for no_crash with verifier signal clean_exit_after_ipv6_udp_coap_meshcop_tlv_attempts."
failure_class: "no_crash"
verifier_signal: "clean_exit_after_ipv6_udp_coap_meshcop_tlv_attempts"
candidate_family: "construct"
input_format: "ipv6-udp-coap-meshcop-tlv"
harness_convention: "libfuzzer-ip6-send"
vuln_class: "channel-mask-validation-bypass"
access_scope: generate
success_count: 0
failure_count: 1
confidence: medium
tags: ["no-crash", "clean-exit-after-ipv6-udp-coap-meshcop-tlv-attempts", "ipv6-udp-coap-meshcop-tlv", "libfuzzer-ip6-send", "construct", "channel-mask-validation-bypass", "negative-memory", "round-37"]
match_keys: ["no_crash", "clean_exit_after_ipv6_udp_coap_meshcop_tlv_attempts", "ipv6-udp-coap-meshcop-tlv", "libfuzzer-ip6-send", "channel-mask-validation-bypass", "negative-memory", "construct"]
allowed_scopes: [generate]
forbidden_fields: [raw_poc_bytes, task_id, exact_offset, checksum, submit_metadata]
evidence_level: medium
train_only: true
round: 37
---
# Ipv6 Udp Coap Meshcop Tlv Construct No Crash Clean Exit After Ipv6 Udp Coap Meshcop Tlv Attempts Channel Mask Validation Bypass Negative Memory

- key: `no_crash x clean_exit_after_ipv6_udp_coap_meshcop_tlv_attempts`
- outcome: persistent failure / basin to avoid
- success_count: 0
- failure_count: 1
- related format facts: [[ipv6-udp-coap-meshcop-tlv]]
- related harness facts: [[libfuzzer-ip6-send]]

## Failure Shape
Constructed packets reached plausible Thread Management Framework carriers but stayed clean. Attempts covered active-set CoAP messages with timestamp and malformed channel-mask TLVs, confirmable and non-confirmable CoAP forms, token and no-token forms, link-security selector variants, mesh-local source and destination variants including leader-style unicast addresses, and Pan ID query messages with malformed channel-mask tails. The likely missing condition is either a more exact local-delivery route/state requirement in the ip6-send harness or that the described invalid-channel-mask acceptance is not surfaced as a sanitizer-detectable fault by these carriers. The Pan ID query path reads channel masks without using the vulnerable validator, and multicast delivery does not appear to loop back in this harness.

## Observed Basin
- Failure trajectory classes: no_crash, no_crash, no_crash, no_crash, no_crash, no_crash, no_crash, no_crash.
- Official confirmation: no server target match for this basin.

## Policy
Treat `no_crash x clean_exit_after_ipv6_udp_coap_meshcop_tlv_attempts` on `ipv6-udp-coap-meshcop-tlv` under `libfuzzer-ip6-send` as a basin to avoid unless a new candidate changes the parser gate, state relation, or sink relation described above. Preserve any proven reachability, but reject variants that return to the same clean-exit, off-target-crash, wrapper-mismatch, usage-only, timeout, or fixed-image-crash behavior.

## Procedure
1. Keep only the smallest parser or harness envelope that was actually reached.
2. Identify the missing relation from the signal: parser selection, container acceptance, length relation, stateful subobject, allocation state, or official target sink.
3. Change one relation at a time and discard candidates that return to the same `clean_exit_after_ipv6_udp_coap_meshcop_tlv_attempts` basin.
4. Promote a recovery from this basin only after a later official target match.

## Negative Memory
- Do not resubmit broad mutations that only reproduce `clean_exit_after_ipv6_udp_coap_meshcop_tlv_attempts`.
- Do not count parser reachability, both-image crashes, local wrapper crashes, clean exits, timeouts, or fixed-image crashes as success.
- Do not store payload bytes, exact positions, task identifiers, checksums, or submit metadata.

## Evidence Shape
- Support: one diagnosed persistent failure from round 37 after 18 attempts.
- Candidate family: construct.
- Scope: generator repair and basin avoidance only.
