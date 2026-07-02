---
type: causal-policy
title: "H264 Annexb SVC Construct Target Match Heap Buffer Overflow Read Verified Recovery"
description: "Round 26 verified recovery for generic_crash with verifier signal target_match."
failure_class: "generic_crash"
verifier_signal: "target_match"
candidate_family: "construct"
input_format: "h264-annexb-svc"
harness_convention: "honggfuzz-wrapper"
vuln_class: "heap-buffer-overflow-read"
access_scope: generate
success_count: 1
confidence: high
tags: ["generic-crash", "target-match", "h264-annexb-svc", "honggfuzz-wrapper", "construct", "verified-recovery", "round-26"]
match_keys: ["generic_crash", "target_match", "h264-annexb-svc", "honggfuzz-wrapper", "heap-buffer-overflow-read", "verified_recovery"]
allowed_scopes: [generate]
forbidden_fields: [raw_poc_bytes, task_id, exact_offset, checksum, submit_metadata]
evidence_level: high
train_only: true
round: 26
---
# H264 Annexb SVC Construct Target Match Heap Buffer Overflow Read Verified Recovery

- key: `generic_crash x target_match`
- outcome: verified recovery
- success_count: 1
- failure_count: 0
- formats: [[h264-annexb-svc]]
- harnesses: [[honggfuzz-wrapper]]

## Failure Shape
Use a raw Annex-B stream of non-VCL NAL units. Fill the SVC decoder's non-VCL arena with ignored non-VCL records whose RBSP is still long enough for the non-VCL decoder to keep walking the linked list. End with a single SEI content-color-volume message positioned at the arena tail: the SEI declares a very small payload, but its stored RBSP keeps the CCV parser active long enough for the bitreader to fetch past the non-VCL allocation. The fixed build caps the usable non-VCL budget before this tail placement is reachable.

## Policy
For `generic_crash x target_match` on `h264-annexb-svc`, preserve the format recognition and harness contract before varying the vulnerable invariant. Prefer `construct` only while that carrier and harness contract remain stable.

## Procedure
1. Preserve the `h264-annexb-svc` carrier and `honggfuzz-wrapper` harness contract until parser reachability is stable.
2. Apply the causal invariant in the failure shape before broad mutation or seed sweeping.
3. Treat local crash class as supporting signal only; keep the candidate only when vulnerable and fixed images diverge on the official target relation.

## Verifier Contract
The official vulnerable-versus-fixed target match is the confirmation gate for this recovery policy; local crash class is supporting evidence only.

## Negative Memory
- Do not corrupt the outer `h264-annexb-svc` recognition gate while retargeting this signal.
- Do not treat off-target crashes, clean parser exits, fixed-build crashes, or both-image crashes as success for this policy.
- Never store raw payload bytes, exact offsets, checksums, or task-local identifiers in memory.

## Format Contract
The input is a raw H.264/SVC Annex-B byte stream. NAL units are delimited by start codes; the NAL header selects non-VCL types such as filler/AUD/SEI and VCL slice types. The SVC parser removes the NAL header, byte-swaps/removes emulation bytes into an internal non-VCL arena, and stores a small aligned header before each saved RBSP. SEI RBSP begins with payload type and payload size fields; content-color-volume SEI can make the decoder's bitreader consume fields beyond the declared payload size when the surrounding RBSP remains long enough.

## Harness Contract
The target is a honggfuzz-style standalone wrapper that reads one raw file and calls the SVC decoder fuzzer. The same raw bytes are also used for early harness selectors for color format, core count, architecture, and target layer; there is no FuzzedDataProvider carving. The fuzzer first decodes headers, allocates output buffers, then repeatedly calls decode on the same byte stream shape. A clean run still prints the honggfuzz usage banner, so sanitizer output and submit results are the reliable signal.

## Evidence Shape
- Support: 1 server-verified round 26 solve after 14 attempts.
- Scope: generator repair and retargeting only.
