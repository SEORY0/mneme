---
type: causal-policy
title: "No Crash Wrapper Usage Path Openthread Ip6 Send Or Meshcop Tlv Negative Memory"
description: "Round 13 negative memory for no_crash with verifier signal wrapper_usage_path."
failure_class: "no_crash"
verifier_signal: "wrapper_usage_path"
candidate_family: "construct"
input_format: "openthread-ip6-send-or-meshcop-tlv"
harness_convention: "honggfuzz-wrapper"
vuln_class: "stack-buffer-overflow"
access_scope: generate
success_count: 0
confidence: medium
tags: ["no-crash", "wrapper-usage-path", "openthread-ip6-send-or-meshcop-tlv", "negative-memory", "round-13"]
match_keys: ["no_crash", "wrapper_usage_path", "openthread-ip6-send-or-meshcop-tlv", "honggfuzz-wrapper", "stack-buffer-overflow", "negative_memory"]
allowed_scopes: [generate]
forbidden_fields: [raw_poc_bytes, task_id, exact_offset, checksum, submit_metadata]
evidence_level: medium
train_only: true
round: 13
---
# No Crash Wrapper Usage Path Openthread Ip6 Send Or Meshcop Tlv Negative Memory

- key: `no_crash x wrapper_usage_path`
- outcome: persistent failure / basin to avoid
- success_count: 0
- failure_count: 1
- related format facts: [[openthread-ip6-send-or-meshcop-tlv]]
- related harness facts: [[honggfuzz-wrapper]]

## Failure Shape
The selected binary reported the ip6-send honggfuzz usage path for every candidate family, so the PoC bytes did not appear to reach the OpenThread packet or MeshCoP handlers under the single-file verifier invocation. Distinct attempts covered CLI commissioner commands, NCP/HDLC-style bytes, IPv6/UDP/CoAP-style bytes, a mutated in-repo radio frame seed, and a raw CoAP/MeshCoP payload.

## Policy
Treat `no_crash x wrapper_usage_path` on `openthread-ip6-send-or-meshcop-tlv` as a basin to avoid unless a new candidate changes the specific parser gate, state relation, or sink relation described below. Preserve any proven reachability, but reject variants that return to the same clean-exit, off-target-crash, wrong-sink, usage-only, or both-image-crash basin.

## Procedure
1. Keep only the smallest parser or harness envelope that the verifier proved was reached.
2. Identify the missing causal relation from the signal: parser selection, container acceptance, length relation, stateful subobject, allocation state, or official target sink.
3. Change one relation at a time and discard candidates that return to the same clean-exit, off-target-crash, wrong-sink, usage-only, or both-image-crash basin.
4. If a local crash is not an official target match, shrink or discard it before mutating deeper fields.
5. Promote a recovery from this basin only after a later verifier-confirmed target match.

## Negative Memory
- Do not resubmit broad mutations that only reproduce `wrapper_usage_path`.
- Do not count parser reachability, both-image crashes, local wrapper crashes, or clean exits as success.
- Do not store raw payload bytes, exact positions, task identifiers, checksums, or submit metadata.

## Format Contract
MeshCoP TLVs use a type-length-value layout. Base TLVs carry a one-byte length, while extended TLVs use the extended-length marker followed by a larger length field. The described invariant is that Commissioner Dataset TLVs in MGMT_COMM_SET handling must reject extended TLV length where the destination buffer expects bounded base TLVs.

## Harness Contract
The source tree builds OpenThread fuzz targets including ip6-send, radio-receive-done, ncp-uart-received, and cli-uart-received. Local verify identified the selected target as the ip6-send honggfuzz wrapper; the wrapper printed fuzzing usage instead of consuming the supplied single PoC file as raw input.

## Evidence Shape
- Support: 1 diagnosed persistent failure from round 13.
- Scope: generator repair and basin avoidance only.
## Round 13 Failure Reinforcement

- key: `no_crash x wrapper_usage_path`
- related format facts: [[openthread-ip6-send-or-meshcop-tlv]]
- related harness facts: [[honggfuzz-wrapper]]

### Failure Shape Delta
The selected binary reported the ip6-send honggfuzz usage path for every candidate family, so the PoC bytes did not appear to reach the OpenThread packet or MeshCoP handlers under the single-file verifier invocation. Distinct attempts covered CLI commissioner commands, NCP/HDLC-style bytes, IPv6/UDP/CoAP-style bytes, a mutated in-repo radio frame seed, and a raw CoAP/MeshCoP payload.

### Format Contract Delta
MeshCoP TLVs use a type-length-value layout. Base TLVs carry a one-byte length, while extended TLVs use the extended-length marker followed by a larger length field. The described invariant is that Commissioner Dataset TLVs in MGMT_COMM_SET handling must reject extended TLV length where the destination buffer expects bounded base TLVs.

### Harness Contract Delta
The source tree builds OpenThread fuzz targets including ip6-send, radio-receive-done, ncp-uart-received, and cli-uart-received. Local verify identified the selected target as the ip6-send honggfuzz wrapper; the wrapper printed fuzzing usage instead of consuming the supplied single PoC file as raw input.

### Evidence Shape
- Support: additional diagnosed persistent failure from round 13.
- Scope: generator repair and basin avoidance only.
