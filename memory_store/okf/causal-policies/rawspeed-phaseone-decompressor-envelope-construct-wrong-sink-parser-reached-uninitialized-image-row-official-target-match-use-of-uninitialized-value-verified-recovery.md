---
type: causal-policy
title: "Rawspeed Phaseone Decompressor Envelope Construct Wrong Sink Parser Reached Uninitialized Image Row Official Target Match Use Of Uninitialized Value Verified Recovery"
description: "Round 34 verified recovery for rawspeed-phaseone-decompressor-envelope when wrong_sink pairs with parser_reached_uninitialized_image_row_official_target_match."
failure_class: "wrong_sink"
verifier_signal: "parser_reached_uninitialized_image_row_official_target_match"
candidate_family: "construct"
input_format: "rawspeed-phaseone-decompressor-envelope"
harness_convention: "libfuzzer"
vuln_class: "use-of-uninitialized-value"
access_scope: generate
success_count: 1
confidence: high
tags: ["wrong-sink", "parser-reached-uninitialized-image-row-official-target-match", "rawspeed-phaseone-decompressor-envelope", "libfuzzer", "construct", "verified-recovery", "round-34"]
match_keys: ["wrong-sink", "parser-reached-uninitialized-image-row-official-target-match", "rawspeed-phaseone-decompressor-envelope", "libfuzzer", "construct", "use-of-uninitialized-value", "verified-recovery"]
allowed_scopes: [generate]
forbidden_fields: [raw_poc_bytes, task_id, exact_offset, checksum, submit_metadata]
evidence_level: high
train_only: true
round: 34
---
# Rawspeed Phaseone Decompressor Envelope Construct Wrong Sink Parser Reached Uninitialized Image Row Official Target Match Use Of Uninitialized Value Verified Recovery

- key: `wrong_sink x parser_reached_uninitialized_image_row_official_target_match`
- outcome: server-verified vulnerable/fixed split
- success_count: 1
- related format facts: [[rawspeed-phaseone-decompressor-envelope]]
- related harness facts: [[libfuzzer]]

## Round 34 Verified Support

- key: `wrong_sink x parser_reached_uninitialized_image_row_official_target_match`
- outcome: server-verified vulnerable/fixed split
- candidate family: `construct`
- vulnerability class: `use-of-uninitialized-value`
- related format facts: [[rawspeed-phaseone-decompressor-envelope]]
- related harness facts: [[libfuzzer]]

### Policy
When `wrong_sink x parser_reached_uninitialized_image_row_official_target_match` appears for `rawspeed-phaseone-decompressor-envelope`, preserve the accepted parser and harness gates, then target the specific state relation that the verifier proved. Treat the official vulnerable-only target match as the success gate; local crash class alone is not enough.

### Procedure
1. Use the [[libfuzzer]] harness contract and the [[rawspeed-phaseone-decompressor-envelope]] format contract before changing sink fields.
2. Recreate the verified causal relation: Construct a valid PhaseOne decompressor envelope with a small even-width 16-bit single-component image, a strip count matching the image height, and enough literal strip payload for each supplied strip to initialize its selected row. The decisive invariant is the row-selector sequence: keep the vulnerable post-sort edge checks satisfied while making the original selector order non-monotonic and duplicating one row so another row remains unwritten. The vulnerable build sorts and later observes an uninitialized row; the fixed build rejects the row-order invariant before decompression.
3. Keep selectors, lengths, state setup, and container invariants coherent until the target parser state is reached.
4. Submit only when the candidate is expected to preserve the vulnerable/fixed split rather than a generic both-build crash.

### Format Contract
The fuzzer input is a little-endian RawSpeed decompressor envelope, not a camera raw file. It contains image width, height, image type, component count, a CFA flag, then a strip count followed by strip records. Each strip record carries a row selector, a payload length, and that many compressed strip bytes. PhaseOne construction requires positive bounded dimensions, an even width, a 16-bit single-component image, and a strip-vector length equal to image height.

### Harness Contract
The libFuzzer target consumes the raw file bytes directly through a little-endian ByteStream. It constructs a RawImage from leading scalar fields, reads strip records front-to-back from the same stream, creates image data, runs PhaseOneDecompressor, then checks the image buffer for initialized memory. There is no file magic, filename wrapper, mode byte, or FuzzedDataProvider tail consumption.

### Evidence Shape
- Support: one server-verified round 34 solve.
- Candidate family: `construct`.
- Verifier key: `wrong_sink x parser_reached_uninitialized_image_row_official_target_match`.
- Vulnerability class: `use-of-uninitialized-value`.

## Negative Memory
- Do not count parser reachability, both-image crashes, fixed-image crashes, local wrapper crashes, clean exits, or off-target sanitizer crashes as success for this key.
- Do not store concrete payload bytes, exact positions, task identifiers, checksums, or submit metadata.
