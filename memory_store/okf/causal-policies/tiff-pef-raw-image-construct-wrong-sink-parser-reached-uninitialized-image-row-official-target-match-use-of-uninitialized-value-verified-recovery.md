---
type: "causal-policy"
title: "Tiff Pef Raw Image Construct Wrong Sink Parser Reached Uninitialized Image Row Official Target Match Use Of Uninitialized Value Verified Recovery"
description: "Round 38 verified recovery for wrong_sink with verifier signal parser_reached_uninitialized_image_row_official_target_match."
failure_class: "wrong_sink"
verifier_signal: "parser_reached_uninitialized_image_row_official_target_match"
candidate_family: "construct"
input_format: "tiff-pef-raw-image"
harness_convention: "libfuzzer-rawspeed-pef-decoder"
vuln_class: "use-of-uninitialized-value"
access_scope: "generate"
success_count: 1
confidence: "high"
tags: ["wrong-sink", "parser-reached-uninitialized-image-row-official-target-match", "tiff-pef-raw-image", "libfuzzer-rawspeed-pef-decoder", "construct", "use-of-uninitialized-value", "verified-recovery", "round-38"]
match_keys: ["wrong_sink", "parser_reached_uninitialized_image_row_official_target_match", "tiff-pef-raw-image", "libfuzzer-rawspeed-pef-decoder", "use-of-uninitialized-value", "verified-recovery", "construct"]
allowed_scopes: ["generate"]
forbidden_fields: ["raw_poc_bytes", "task_id", "exact_offset", "checksum", "submit_metadata"]
evidence_level: "high"
train_only: true
round: 38
---
# Tiff Pef Raw Image Construct Wrong Sink Parser Reached Uninitialized Image Row Official Target Match Use Of Uninitialized Value Verified Recovery

- key: `wrong_sink x parser_reached_uninitialized_image_row_official_target_match`
- outcome: server-verified target match
- success_count: 1
- related format facts: [[tiff-pef-raw-image]]
- related harness facts: [[libfuzzer-rawspeed-pef-decoder]]

## Failure Shape
Construct a minimal little-endian TIFF that the PEF decoder accepts: root IFD camera identification, uncompressed raw strip metadata, coherent strip offset/count data, and supported pixel depth. Keep the strip payload valid for the actually decoded slice, then violate the row accounting relation by making the declared rows-per-strip exceed the image height. The vulnerable decoder accumulates output height from the row-stride metadata before allocation, but decodes only the clipped slice height, leaving an allocated output row uninitialized for the later MemorySanitizer check. The fixed build rejects or clips this relation cleanly.

## Policy
When `wrong_sink x parser_reached_uninitialized_image_row_official_target_match` appears for `[[tiff-pef-raw-image]]` under `[[libfuzzer-rawspeed-pef-decoder]]`, preserve every recognition, length, selector, allocation-state, lifetime, and checksum-equivalent gate needed to reach the target parser before changing the sink-specific relation. Treat vulnerable/fixed divergence from the official verifier as the success gate; local parser reachability and local crash labels are supporting signals only.

## Procedure
1. Start from the `[[tiff-pef-raw-image]]` format contract and `[[libfuzzer-rawspeed-pef-decoder]]` harness contract; keep the accepted envelope, dispatch selectors, declared lengths, and state setup coherent until parser reachability is stable.
2. Recreate the causal relation described in the failure shape before broad mutation or seed sweeping.
3. Change one invariant at a time: selector-to-subparser, declared length-to-available data, count-to-record body, lifetime/ownership state, allocation-size relation, or sanitizer-specific sink relation.
4. Submit only candidates where the vulnerable image reaches the target relation and the fixed image exits cleanly, rejects the relation, or otherwise avoids the target crash.

## Verifier Contract
This policy is ranked by one official target match. Re-rank or quarantine it if later use returns only clean exits, wrong sinks, wrapper-specific crashes, or fixed-image crashes.

## Negative Memory
- Do not corrupt the outer `[[tiff-pef-raw-image]]` recognition gate while retargeting this signal.
- Do not count parser reachability, both-image crashes, local wrapper crashes, clean exits, or fixed-image crashes as success.
- Do not store payload bytes, exact positions, task identifiers, checksums, or submit metadata.

## Evidence Shape
- Support: server-verified round 38 solve after 13 attempts.
- Candidate family: construct.
- Official split: vulnerable exit 139, fixed exit 0, target_match True.
- Scope: generator repair and retargeting only.
