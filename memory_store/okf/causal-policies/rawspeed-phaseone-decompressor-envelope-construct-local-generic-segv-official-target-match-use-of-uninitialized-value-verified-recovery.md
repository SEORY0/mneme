---
type: causal-policy
title: "Rawspeed Phaseone Decompressor Envelope Construct Local Generic Segv Official Target Match Use Of Uninitialized Value Verified Recovery"
description: "Round 26 verified recovery for generic_crash with verifier signal local_generic_segv_official_target_match."
failure_class: "generic_crash"
verifier_signal: "local_generic_segv_official_target_match"
candidate_family: "construct"
input_format: "rawspeed-phaseone-decompressor-envelope"
harness_convention: "libfuzzer"
vuln_class: "use-of-uninitialized-value"
access_scope: generate
success_count: 1
confidence: high
tags: ["generic-crash", "local-generic-segv-official-target-match", "rawspeed-phaseone-decompressor-envelope", "libfuzzer", "construct", "verified-recovery", "round-26"]
match_keys: ["generic_crash", "local_generic_segv_official_target_match", "rawspeed-phaseone-decompressor-envelope", "libfuzzer", "use-of-uninitialized-value", "verified_recovery"]
allowed_scopes: [generate]
forbidden_fields: [raw_poc_bytes, task_id, exact_offset, checksum, submit_metadata]
evidence_level: high
train_only: true
round: 26
---
# Rawspeed Phaseone Decompressor Envelope Construct Local Generic Segv Official Target Match Use Of Uninitialized Value Verified Recovery

- key: `generic_crash x local_generic_segv_official_target_match`
- outcome: verified recovery
- success_count: 1
- failure_count: 0
- formats: [[rawspeed-phaseone-decompressor-envelope]]
- harnesses: [[libfuzzer]]

## Failure Shape
Build the raw decompressor envelope, not a camera file: valid small even-width 16-bit single-component image fields, a strip count equal to image height, and per-strip payloads large enough for the decompressor to initialize rows. Keep all strip records structurally valid, but duplicate one in-range row selector so another expected image row is never initialized; the vulnerable build trusts the strip row vector and later checks the image buffer, while the fixed build rejects the row mapping.

## Policy
For `generic_crash x local_generic_segv_official_target_match` on `rawspeed-phaseone-decompressor-envelope`, preserve the format recognition and harness contract before varying the vulnerable invariant. Prefer `construct` only while that carrier and harness contract remain stable.

## Procedure
1. Preserve the `rawspeed-phaseone-decompressor-envelope` carrier and `libfuzzer` harness contract until parser reachability is stable.
2. Apply the causal invariant in the failure shape before broad mutation or seed sweeping.
3. Treat local crash class as supporting signal only; keep the candidate only when vulnerable and fixed images diverge on the official target relation.

## Verifier Contract
The official vulnerable-versus-fixed target match is the confirmation gate for this recovery policy; local crash class is supporting evidence only.

## Negative Memory
- Do not corrupt the outer `rawspeed-phaseone-decompressor-envelope` recognition gate while retargeting this signal.
- Do not treat off-target crashes, clean parser exits, fixed-build crashes, or both-image crashes as success for this policy.
- Never store raw payload bytes, exact offsets, checksums, or task-local identifiers in memory.

## Format Contract
The PhaseOne decompressor fuzzer consumes a little-endian envelope containing image width, height, image type, components-per-pixel, CFA flag, then a strip count and repeated strip records. Each strip record contains a row selector, a payload length, and that many compressed strip bytes. The decompressor requires a positive even width, bounded dimensions, 16-bit single-component pixels, and a strip vector length equal to image height.

## Harness Contract
The harness is libFuzzer over raw bytes. It wraps the input in a ByteStream, constructs a RawImage from leading scalar fields, reads all remaining strip records from the same front-to-back byte stream, allocates image data, runs PhaseOneDecompressor, then checks image memory initialization. There is no file magic, filename layer, mode selector, or FuzzedDataProvider back-consumption.

## Evidence Shape
- Support: 1 server-verified round 26 solve after 1 attempts.
- Scope: generator repair and retargeting only.
