---
type: negative-memory
title: "Opensc Pkcs15 Reader Chunk Stream Construct Wrong Sink Parser Reached But Fixed Image Also Crashes Out Of Bounds Read Negative Memory"
description: "Round 36 negative memory for wrong_sink with verifier signal parser_reached_but_fixed_image_also_crashes."
failure_class: "wrong_sink"
verifier_signal: "parser_reached_but_fixed_image_also_crashes"
candidate_family: "construct"
input_format: "opensc-pkcs15-reader-chunk-stream"
harness_convention: "libfuzzer-via-honggfuzz-wrapper"
vuln_class: "out-of-bounds-read"
access_scope: generate
success_count: 0
failure_count: 1
confidence: medium
tags: ["wrong-sink", "parser-reached-but-fixed-image-also-crashes", "opensc-pkcs15-reader-chunk-stream", "libfuzzer-via-honggfuzz-wrapper", "construct", "out-of-bounds-read", "negative-memory", "round-36"]
match_keys: ["wrong_sink", "parser_reached_but_fixed_image_also_crashes", "opensc-pkcs15-reader-chunk-stream", "libfuzzer-via-honggfuzz-wrapper", "out-of-bounds-read", "wrong-sink", "parser-reached-but-fixed-image-also-crashes", "negative_memory", "construct"]
allowed_scopes: [generate]
forbidden_fields: [raw_poc_bytes, task_id, exact_offset, checksum, submit_metadata]
evidence_level: medium
train_only: true
round: 36
---
# Opensc Pkcs15 Reader Chunk Stream Construct Wrong Sink Parser Reached But Fixed Image Also Crashes Out Of Bounds Read Negative Memory

- key: `wrong_sink x parser_reached_but_fixed_image_also_crashes`
- outcome: persistent failure / basin to avoid
- success_count: 0
- failure_count: 1
- related format facts: [[opensc-pkcs15-reader-chunk-stream]]
- related harness facts: [[libfuzzer-via-honggfuzz-wrapper]]

## Failure Shape
The transcript can steer past earlier OpenSC probing drivers into the Italian CNS synthetic PKCS#15 path by using an accepted Italian CNS ATR and harmless failure APDU statuses before the target responses. Personal-data boundary inputs reached itacns parsing and produced heap-buffer-overflow reads, but the fixed image crashed on the same parser family, so that path is over-broad rather than the scored repair. A select-file FCP/security-attribute probe reached the itacns selector edge but did not produce a vulnerable-only target split.

## Observed Basin
- Failure trajectory classes: no_crash, wrong_sink.
- Official confirmation: no server target match for this basin.

## Policy
Treat `wrong_sink x parser_reached_but_fixed_image_also_crashes` on `opensc-pkcs15-reader-chunk-stream` under `libfuzzer-via-honggfuzz-wrapper` as a basin to avoid unless a new candidate changes the parser gate, state relation, or sink relation described above. Preserve any proven reachability, but reject variants that return to the same clean-exit, off-target-crash, wrapper-mismatch, usage-only, or fixed-image-crash behavior.

## Procedure
1. Keep only the smallest parser or harness envelope that was actually reached.
2. Identify the missing relation from the signal: parser selection, container acceptance, length relation, stateful subobject, allocation state, or official target sink.
3. Change one relation at a time and discard candidates that return to the same `parser_reached_but_fixed_image_also_crashes` basin.
4. Promote a recovery from this basin only after a later official target match.

## Negative Memory
- Do not resubmit broad mutations that only reproduce `parser_reached_but_fixed_image_also_crashes`.
- Do not count parser reachability, both-image crashes, local wrapper crashes, clean exits, or fixed-image crashes as success.
- Do not store payload bytes, exact positions, task identifiers, checksums, or submit metadata.

## Evidence Shape
- Support: 1 diagnosed persistent failure from round 36 after 12 attempts.
- Scope: generator repair and basin avoidance only.
