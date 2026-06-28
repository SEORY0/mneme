---
type: negative-memory
title: "Generic Crash Both Images Crash Gpac Filelist Url Construct Stack Buffer Overflow Write Negative Memory"
description: "Round 25 negative memory for generic_crash with verifier signal both_images_crash."
failure_class: "generic_crash"
verifier_signal: "both_images_crash"
candidate_family: "construct"
input_format: "gpac-filelist-url"
harness_convention: "libfuzzer"
vuln_class: "stack-buffer-overflow-write"
access_scope: generate
success_count: 0
confidence: medium
tags: ["generic-crash", "both-images-crash", "gpac-filelist-url", "libfuzzer", "construct", "negative-memory", "round-25"]
match_keys: ["generic_crash", "both_images_crash", "gpac-filelist-url", "libfuzzer", "stack-buffer-overflow-write", "negative_memory"]
allowed_scopes: [generate]
forbidden_fields: [raw_poc_bytes, task_id, exact_offset, checksum, submit_metadata]
evidence_level: medium
train_only: true
round: 25
---
# Generic Crash Both Images Crash Gpac Filelist Url Construct Stack Buffer Overflow Write Negative Memory

- key: `generic_crash x both_images_crash`
- outcome: persistent failure / basin to avoid
- success_count: 0
- failure_count: 1
- related format facts: [[gpac-filelist-url]]
- related harness facts: [[libfuzzer]]

## Failure Shape
An invalid overlong scheme was treated as an unsupported file-list entry and did not reach RTSP. A valid RTSP URL with an oversized authority component reached RTSP_UnpackURL and crashed in the local vulnerable image, but confirmation and submission showed the fixed image also crashed, so this was not the accepted differential trigger.

## Policy
Treat `generic_crash x both_images_crash` on `gpac-filelist-url` as a basin to avoid unless a new candidate changes the parser gate, state relation, or sink relation described below. Preserve any proven reachability, but reject variants that return to the same clean-exit, off-target-crash, wrong-sink, usage-only, wrapper-mismatch, or both-image-crash basin.

## Procedure
1. Keep only the smallest parser or harness envelope that was actually reached.
2. Identify the missing causal relation from the signal: parser selection, container acceptance, length relation, stateful subobject, allocation state, or official target sink.
3. Change one relation at a time and discard candidates that return to the same `both_images_crash` basin.
4. If a local crash is not an official target match, shrink or discard it before mutating deeper fields.
5. Promote a recovery from this basin only after a later verifier-confirmed target match.

## Negative Memory
- Do not resubmit broad mutations that only reproduce `both_images_crash`.
- Do not count parser reachability, both-image crashes, local wrapper crashes, usage banners, or clean exits as success.
- Do not store raw payload bytes, exact positions, task identifiers, checksums, or submit metadata.

## Format Contract
The harness input behaves as a file-list or URL source rather than a serialized media container. A recognized RTSP-family URL scheme is needed before GPAC instantiates the RTSP input filter and calls the URL unpacker.

## Harness Contract
The libFuzzer target passes the raw text into GPAC's probe/analyze filter session. Unsupported schemes are handled as ordinary file names; supported RTSP schemes cause filter graph construction and RTSP session initialization.

## Evidence Shape
- Support: 1 diagnosed persistent failure from round 25 after 2 attempts.
- Scope: generator repair and basin avoidance only.
