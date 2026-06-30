---
type: causal-policy
title: "FIFF Wrapped Mef TIFF RAW Construct Parser Reached Uninitialized Image Data After Truncated Uncompressed RAW Use Of Uninitialized Value Verified Recovery"
description: "Round 26 verified recovery for wrong_sink with verifier signal parser_reached_uninitialized_image_data_after_truncated_uncompressed_raw."
failure_class: "wrong_sink"
verifier_signal: "parser_reached_uninitialized_image_data_after_truncated_uncompressed_raw"
candidate_family: "construct"
input_format: "fiff-wrapped-mef-tiff-raw"
harness_convention: "libfuzzer"
vuln_class: "use-of-uninitialized-value"
access_scope: generate
success_count: 1
confidence: high
tags: ["wrong-sink", "parser-reached-uninitialized-image-data-after-truncated-uncompressed-raw", "fiff-wrapped-mef-tiff-raw", "libfuzzer", "construct", "verified-recovery", "round-26"]
match_keys: ["wrong_sink", "parser_reached_uninitialized_image_data_after_truncated_uncompressed_raw", "fiff-wrapped-mef-tiff-raw", "libfuzzer", "use-of-uninitialized-value", "verified_recovery"]
allowed_scopes: [generate]
forbidden_fields: [raw_poc_bytes, task_id, exact_offset, checksum, submit_metadata]
evidence_level: high
train_only: true
round: 26
---
# FIFF Wrapped Mef TIFF RAW Construct Parser Reached Uninitialized Image Data After Truncated Uncompressed RAW Use Of Uninitialized Value Verified Recovery

- key: `wrong_sink x parser_reached_uninitialized_image_data_after_truncated_uncompressed_raw`
- outcome: verified recovery
- success_count: 1
- failure_count: 0
- formats: [[fiff-wrapped-mef-tiff-raw]]
- harnesses: [[libfuzzer]]

## Failure Shape
Use the FIFF parser envelope to route into a TIFF root whose camera make selects the MEF decoder. Keep the embedded TIFF structurally valid with image dimensions, make/model tags, and one raw strip. Advertise a multi-row uncompressed 12-bit image, but make the strip byte count cover a complete first scanline and stop before the advertised image is complete. The vulnerable decompressor accepts the partial strip, leaves later image rows uninitialized, and the raw decoder's initialized-data check reports the sanitizer fault; the fixed build rejects the truncation before returning a partial image.

## Policy
For `wrong_sink x parser_reached_uninitialized_image_data_after_truncated_uncompressed_raw` on `fiff-wrapped-mef-tiff-raw`, preserve the format recognition and harness contract before varying the vulnerable invariant. Prefer `construct` only while that carrier and harness contract remain stable.

## Procedure
1. Preserve the `fiff-wrapped-mef-tiff-raw` carrier and `libfuzzer` harness contract until parser reachability is stable.
2. Apply the causal invariant in the failure shape before broad mutation or seed sweeping.
3. Treat local crash class as supporting signal only; keep the candidate only when vulnerable and fixed images diverge on the official target relation.

## Verifier Contract
The official vulnerable-versus-fixed target match is the confirmation gate for this recovery policy; local crash class is supporting evidence only.

## Negative Memory
- Do not corrupt the outer `fiff-wrapped-mef-tiff-raw` recognition gate while retargeting this signal.
- Do not treat off-target crashes, clean parser exits, fixed-build crashes, or both-image crashes as success for this policy.
- Never store raw payload bytes, exact offsets, checksums, or task-local identifiers in memory.

## Format Contract
The FIFF parser reads fixed big-endian header pointers and treats the first pointer as an embedded TIFF root after applying its internal base adjustment. TIFF string tags can select the decoder by camera make/model. The MEF path uses the root TIFF image-width, image-length, strip-offset, and strip-byte-count tags, then decodes the strip as big-endian packed 12-bit raw samples. Strip offsets used by the decoder are relative to the whole input file, while TIFF metadata offsets inside the embedded root are relative to that TIFF view.

## Harness Contract
The harness is a libFuzzer raw-byte file harness with no leading mode byte and no FuzzedDataProvider carving. It constructs a FiffParser from the whole input, calls getDecoder, disables crop and unknown-camera hard failures, then calls decodeRaw and decodeMetaData. RawSpeed parser and decoder exceptions are caught, so successful triggering needs a sanitizer-visible failure after parser and decoder reachability.

## Evidence Shape
- Support: 1 server-verified round 26 solve after 5 attempts.
- Scope: generator repair and retargeting only.
