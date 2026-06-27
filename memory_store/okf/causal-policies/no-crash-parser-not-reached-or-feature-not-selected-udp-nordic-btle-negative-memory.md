---
type: causal-policy
title: "No Crash Parser Not Reached Or Feature Not Selected Udp Nordic Btle Negative Memory"
description: "Round 13 negative memory for no_crash with verifier signal parser_not_reached_or_feature_not_selected."
failure_class: "no_crash"
verifier_signal: "parser_not_reached_or_feature_not_selected"
candidate_family: "construct"
input_format: "udp-nordic-btle"
harness_convention: "afl-fuzzshark"
vuln_class: "wild-pointer-dereference"
access_scope: generate
success_count: 0
confidence: medium
tags: ["no-crash", "parser-not-reached-or-feature-not-selected", "udp-nordic-btle", "negative-memory", "round-13"]
match_keys: ["no_crash", "parser_not_reached_or_feature_not_selected", "udp-nordic-btle", "afl-fuzzshark", "wild-pointer-dereference", "negative_memory"]
allowed_scopes: [generate]
forbidden_fields: [raw_poc_bytes, task_id, exact_offset, checksum, submit_metadata]
evidence_level: medium
train_only: true
round: 13
---
# No Crash Parser Not Reached Or Feature Not Selected Udp Nordic Btle Negative Memory

- key: `no_crash x parser_not_reached_or_feature_not_selected`
- outcome: persistent failure / basin to avoid
- success_count: 0
- failure_count: 1
- related format facts: [[udp-nordic-btle]]
- related harness facts: [[afl-fuzzshark]]

## Failure Shape
The active fuzzer target was the UDP dissector under the IP protocol table, not a direct BTLE target. Raw BTLE, raw Nordic BLE, and UDP-wrapped Nordic BLE shapes across plausible decode paths did not reach the uninitialized acl_data crash.

## Policy
Treat `no_crash x parser_not_reached_or_feature_not_selected` on `udp-nordic-btle` as a basin to avoid unless a new candidate changes the specific parser gate, state relation, or sink relation described below. Preserve any proven reachability, but reject variants that return to the same clean-exit, off-target-crash, wrong-sink, usage-only, or both-image-crash basin.

## Procedure
1. Keep only the smallest parser or harness envelope that the verifier proved was reached.
2. Identify the missing causal relation from the signal: parser selection, container acceptance, length relation, stateful subobject, allocation state, or official target sink.
3. Change one relation at a time and discard candidates that return to the same clean-exit, off-target-crash, wrong-sink, usage-only, or both-image-crash basin.
4. If a local crash is not an official target match, shrink or discard it before mutating deeper fields.
5. Promote a recovery from this basin only after a later verifier-confirmed target match.

## Negative Memory
- Do not resubmit broad mutations that only reproduce `parser_not_reached_or_feature_not_selected`.
- Do not count parser reachability, both-image crashes, local wrapper crashes, or clean exits as success.
- Do not store raw payload bytes, exact positions, task identifiers, checksums, or submit metadata.

## Format Contract
The relevant protocol stack is UDP carrying a Nordic BLE sniffer record, which can then pass a context object into the BTLE dissector. Nordic BLE records contain a sniffer header with version, lengths, packet id, flags, channel, signal metadata, timing metadata, and then the BTLE link-layer payload.

## Harness Contract
The fuzzshark binary reads a raw input file as an IP-protocol UDP payload and invokes the UDP dissector. Port fields inside the UDP header can influence downstream payload dispatch, but decode-as-only dissectors may not be selected by raw payload bytes alone.

## Evidence Shape
- Support: 1 diagnosed persistent failure from round 13.
- Scope: generator repair and basin avoidance only.
## Round 13 Failure Reinforcement

- key: `no_crash x parser_not_reached_or_feature_not_selected`
- related format facts: [[udp-nordic-btle]]
- related harness facts: [[afl-fuzzshark]]

### Failure Shape Delta
The active fuzzer target was the UDP dissector under the IP protocol table, not a direct BTLE target. Raw BTLE, raw Nordic BLE, and UDP-wrapped Nordic BLE shapes across plausible decode paths did not reach the uninitialized acl_data crash.

### Format Contract Delta
The relevant protocol stack is UDP carrying a Nordic BLE sniffer record, which can then pass a context object into the BTLE dissector. Nordic BLE records contain a sniffer header with version, lengths, packet id, flags, channel, signal metadata, timing metadata, and then the BTLE link-layer payload.

### Harness Contract Delta
The fuzzshark binary reads a raw input file as an IP-protocol UDP payload and invokes the UDP dissector. Port fields inside the UDP header can influence downstream payload dispatch, but decode-as-only dissectors may not be selected by raw payload bytes alone.

### Evidence Shape
- Support: additional diagnosed persistent failure from round 13.
- Scope: generator repair and basin avoidance only.
