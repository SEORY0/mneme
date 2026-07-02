---
type: causal-policy
title: "Wolfmqtt Datasource Stream Construct Parser Reached MQTT Connect Null Username Length Path Heap Buffer Overflow Write Verified Recovery"
description: "Round 26 verified recovery for generic_crash with verifier signal parser_reached_mqtt_connect_null_username_length_path."
failure_class: "generic_crash"
verifier_signal: "parser_reached_mqtt_connect_null_username_length_path"
candidate_family: "construct"
input_format: "wolfmqtt datasource stream"
harness_convention: "libfuzzer"
vuln_class: "heap-buffer-overflow-write"
access_scope: generate
success_count: 1
confidence: high
tags: ["generic-crash", "parser-reached-mqtt-connect-null-username-length-path", "wolfmqtt-datasource-stream", "libfuzzer", "construct", "verified-recovery", "round-26"]
match_keys: ["generic_crash", "parser_reached_mqtt_connect_null_username_length_path", "wolfmqtt datasource stream", "libfuzzer", "heap-buffer-overflow-write", "verified_recovery"]
allowed_scopes: [generate]
forbidden_fields: [raw_poc_bytes, task_id, exact_offset, checksum, submit_metadata]
evidence_level: high
train_only: true
round: 26
---
# Wolfmqtt Datasource Stream Construct Parser Reached MQTT Connect Null Username Length Path Heap Buffer Overflow Write Verified Recovery

- key: `generic_crash x parser_reached_mqtt_connect_null_username_length_path`
- outcome: verified recovery
- success_count: 1
- failure_count: 0
- formats: [[wolfmqtt-datasource-stream]]
- harnesses: [[libfuzzer]]

## Failure Shape
Build the fuzzer's datasource stream, not an MQTT wire packet. Satisfy the fixed-size setup fields, supply a valid client identifier, leave LWT disabled, and rely on the harness leaving username unset. Size the client identifier so the encoded MQTT CONNECT packet's declared length fits the fixed transmit buffer exactly at the boundary; the vulnerable NULL-username path still emits an empty username length field without including those bytes in the declared remaining length, so the final length write crosses the heap buffer. No network response fields are needed because the crash occurs during CONNECT encoding before the mocked write/read path matters.

## Policy
For `generic_crash x parser_reached_mqtt_connect_null_username_length_path` on `wolfmqtt datasource stream`, preserve the format recognition and harness contract before varying the vulnerable invariant. Prefer `construct` only while that carrier and harness contract remain stable.

## Procedure
1. Preserve the `wolfmqtt datasource stream` carrier and `libfuzzer` harness contract until parser reachability is stable.
2. Apply the causal invariant in the failure shape before broad mutation or seed sweeping.
3. Treat local crash class as supporting signal only; keep the candidate only when vulnerable and fixed images diverge on the official target relation.

## Verifier Contract
The official vulnerable-versus-fixed target match is the confirmation gate for this recovery policy; local crash class is supporting evidence only.

## Negative Memory
- Do not corrupt the outer `wolfmqtt datasource stream` recognition gate while retargeting this signal.
- Do not treat off-target crashes, clean parser exits, fixed-build crashes, or both-image crashes as success for this policy.
- Never store raw payload bytes, exact offsets, checksums, or task-local identifiers in memory.

## Format Contract
The target format is the fuzzing-headers datasource layout: every consumed value is preceded by a little-endian size field. Fixed-size integers and booleans consume their exact byte width after the size prefix; strings consume a size prefix followed by that many bytes and become NUL-terminated C strings through std::string. The MQTT CONNECT encoder builds a fixed header, protocol header, client-id field, optional LWT fields, optional username, and optional password into a fixed transmit buffer.

## Harness Contract
The libFuzzer input is consumed front-to-back by fuzzing::datasource, not as raw MQTT. The harness constructs MqttClient and MqttConnect objects, allocates fixed transmit and receive buffers, reads datasource fields for buffer setup, clean-session, client-id, LWT selection, and optional LWT values, but it does not populate username or password. It then calls MqttClient_NetConnect and MqttClient_Connect; mocked write and read callbacks consume later datasource fields only if encoding completes.

## Evidence Shape
- Support: 1 server-verified round 26 solve after 3 attempts.
- Scope: generator repair and retargeting only.
