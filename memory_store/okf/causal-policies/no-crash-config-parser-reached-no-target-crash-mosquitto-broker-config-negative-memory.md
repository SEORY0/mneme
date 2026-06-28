---
type: causal-policy
title: "No Crash Config Parser Reached No Target Crash Mosquitto Broker Config Negative Memory"
description: "Round 12 negative memory for no_crash with verifier signal config_parser_reached_no_target_crash."
failure_class: "no_crash"
verifier_signal: "config_parser_reached_no_target_crash"
candidate_family: "construct"
input_format: "mosquitto broker config"
harness_convention: "libfuzzer"
vuln_class: "use-after-free-or-exit-cleanup"
access_scope: generate
success_count: 0
confidence: medium
tags: ["no-crash", "config-parser-reached-no-target-crash", "mosquitto-broker-config", "negative-memory", "round-12"]
match_keys: ["no_crash", "config_parser_reached_no_target_crash", "mosquitto-broker-config", "libfuzzer", "use-after-free-or-exit-cleanup", "negative_memory"]
allowed_scopes: [generate]
forbidden_fields: [raw_poc_bytes, task_id, exact_offset, checksum, submit_metadata]
evidence_level: medium
train_only: true
round: 12
---
# No Crash Config Parser Reached No Target Crash Mosquitto Broker Config Negative Memory

- key: `no_crash x config_parser_reached_no_target_crash`
- outcome: persistent failure / basin to avoid
- success_count: 0
- failure_count: 1
- related format facts: [[mosquitto-broker-config]]
- related harness facts: [[libfuzzer]]

## Failure Shape
The harness is the broker configuration test path, not an MQTT packet parser. Websocket listeners, mixed listeners, invalid listener syntax, plugin directives, and bridge directives all either parsed cleanly or produced ordinary configuration errors. The test-config path exits after config parsing and cleanup, so no candidate reproduced the described broker-already-exiting state.

## Policy
Treat `no_crash x config_parser_reached_no_target_crash` on `mosquitto-broker-config` as a basin to avoid unless a new candidate changes the parser gate, state relation, or official target sink. Preserve any proven reachability, but reject variants that return to the same verifier signal without changing the causal gate under test.

## Procedure
1. Keep only the smallest parser or harness envelope that the verifier proved was reached.
2. Identify the missing causal relation from the signal: parser selection, container acceptance, length relation, stateful subobject, allocation state, or official target sink.
3. Change one relation at a time and discard candidates that return to the same clean-exit, off-target-crash, wrong-sink, usage-only, or both-image-crash basin.
4. If a local crash is not an official target match, shrink or discard it before mutating deeper fields.
5. Promote a recovery from this basin only after a later verifier-confirmed target match.

## Format Contract
Mosquitto broker configuration is line-oriented text with global options and listener-scoped options. Listener entries select ports and protocol, websocket support is configured with protocol directives, plugins are configured by path directives, and bridge connections require address/topic-related options.

## Harness Contract
The harness writes the raw fuzzer bytes to a temporary configuration file and runs the broker in test-configuration mode with that file. It does not feed MQTT packets; successful parsing prints that the configuration file is OK and then exits through configuration cleanup.

## Negative Memory
- Do not resubmit broad mutations that only reproduce `config_parser_reached_no_target_crash`.
- Do not count parser reachability, both-image crashes, local wrapper crashes, clean exits, or fixed-image crashes as success.
- Do not store raw payload bytes, exact positions, task identifiers, or submit metadata.

## Evidence Shape
- Support: one diagnosed persistent failure from round 12.
- Scope: generator repair and basin avoidance only.
