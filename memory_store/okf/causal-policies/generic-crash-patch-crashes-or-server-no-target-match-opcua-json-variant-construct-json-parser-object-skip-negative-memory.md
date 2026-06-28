---
type: negative-memory
title: "Generic Crash Patch Crashes Or Server No Target Match Opcua Json Variant Construct Json Parser Object Skip Negative Memory"
description: "Round 25 negative memory for generic_crash with verifier signal patch_crashes_or_server_no_target_match."
failure_class: "generic_crash"
verifier_signal: "patch_crashes_or_server_no_target_match"
candidate_family: "construct"
input_format: "opcua-json-variant"
harness_convention: "libfuzzer"
vuln_class: "json-parser-object-skip"
access_scope: generate
success_count: 0
confidence: medium
tags: ["generic-crash", "patch-crashes-or-server-no-target-match", "opcua-json-variant", "libfuzzer", "construct", "negative-memory", "round-25"]
match_keys: ["generic_crash", "patch_crashes_or_server_no_target_match", "opcua-json-variant", "libfuzzer", "json-parser-object-skip", "negative_memory"]
allowed_scopes: [generate]
forbidden_fields: [raw_poc_bytes, task_id, exact_offset, checksum, submit_metadata]
evidence_level: medium
train_only: true
round: 25
---
# Generic Crash Patch Crashes Or Server No Target Match Opcua Json Variant Construct Json Parser Object Skip Negative Memory

- key: `generic_crash x patch_crashes_or_server_no_target_match`
- outcome: persistent failure / basin to avoid
- success_count: 0
- failure_count: 1
- related format facts: [[opcua-json-variant]]
- related harness facts: [[libfuzzer]]

## Failure Shape
Well-formed Variant envelopes with unknown ExtensionObject bodies can reach the recursive object-skip machinery, and some nested body shapes crash locally. The accepted differential trigger was not found: local confirmation showed the patched image still failed for the crashing family, and server submission did not count the vulnerable side as a target crash.

## Policy
Treat `generic_crash x patch_crashes_or_server_no_target_match` on `opcua-json-variant` as a basin to avoid unless a new candidate changes the parser gate, state relation, or sink relation described below. Preserve any proven reachability, but reject variants that return to the same clean-exit, off-target-crash, wrong-sink, usage-only, wrapper-mismatch, or both-image-crash basin.

## Procedure
1. Keep only the smallest parser or harness envelope that was actually reached.
2. Identify the missing causal relation from the signal: parser selection, container acceptance, length relation, stateful subobject, allocation state, or official target sink.
3. Change one relation at a time and discard candidates that return to the same `patch_crashes_or_server_no_target_match` basin.
4. If a local crash is not an official target match, shrink or discard it before mutating deeper fields.
5. Promote a recovery from this basin only after a later verifier-confirmed target match.

## Negative Memory
- Do not resubmit broad mutations that only reproduce `patch_crashes_or_server_no_target_match`.
- Do not count parser reachability, both-image crashes, local wrapper crashes, usage banners, or clean exits as success.
- Do not store raw payload bytes, exact positions, task identifiers, checksums, or submit metadata.

## Format Contract
The fuzzer decodes raw JSON as an OPC UA Variant. To reach ExtensionObject handling, the top-level object needs a Variant type selector and a body containing an ExtensionObject-like object with a type identifier, optional encoding marker, and a nested Body value. Unknown body types are stored as encoded JSON and skipped by a recursive token walker.

## Harness Contract
The libFuzzer target passes the entire input byte string directly to the JSON decoder as a Variant. There is no file wrapper, checksum, or external mode byte; all reachability is controlled by JSON token structure and the Variant/ExtensionObject fields.

## Evidence Shape
- Support: 1 diagnosed persistent failure from round 25 after 6 attempts.
- Scope: generator repair and basin avoidance only.
