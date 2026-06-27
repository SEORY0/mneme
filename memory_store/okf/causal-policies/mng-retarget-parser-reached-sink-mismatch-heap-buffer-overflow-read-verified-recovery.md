---
type: causal-policy
title: "Mng Retarget Parser Reached Sink Mismatch Heap Buffer Overflow Read Verified Recovery"
description: "Round 12 retarget-verified recovery for wrong_sink with verifier signal parser_reached_sink_mismatch."
failure_class: "wrong_sink"
verifier_signal: "parser_reached_sink_mismatch"
candidate_family: "retarget"
input_format: "mng"
harness_convention: "libfuzzer"
vuln_class: "heap-buffer-overflow-read"
access_scope: generate
success_count: 1
confidence: high
tags: ["wrong-sink", "parser-reached-sink-mismatch", "mng", "verified-recovery", "retarget", "round-12"]
match_keys: ["wrong_sink", "parser_reached_sink_mismatch", "mng", "libfuzzer", "heap-buffer-overflow-read", "verified_recovery"]
allowed_scopes: [generate]
forbidden_fields: [raw_poc_bytes, task_id, exact_offset, checksum, submit_metadata]
evidence_level: high
train_only: true
round: 12
---
# Mng Retarget Parser Reached Sink Mismatch Heap Buffer Overflow Read Verified Recovery

- key: `wrong_sink x parser_reached_sink_mismatch`
- outcome: retarget verified recovery
- confidence: 0.82
- success_count: 1
- failure_count: 0
- formats: [[mng]]
- harnesses: [[libfuzzer]]
- related negative memory: [[wrong-sink-parser-reached-sink-mismatch-mng-negative-memory]]

## Failure Shape
The initial MNG LOOP attempts reached the vulnerable chunk reader but did not keep the fixed image clean. The retargeted candidate kept the MNG envelope and moved to the smallest short-LOOP body shape that still reaches the long-read sink while the fixed build rejects it cleanly.

## Policy
Use this policy when `wrong_sink x parser_reached_sink_mismatch` recurs on MNG. Preserve the valid PNG-like MNG chunk envelope, then narrow the LOOP chunk body instead of broadening unrelated chunks. The server-confirmed split is vulnerable-build crash and fixed-build clean.

## Procedure
Build a minimal MNG stream with valid signature, image header chunk, one LOOP control chunk, and a terminal chunk. Keep chunk framing coherent enough for the GraphicsMagick MNG reader, but make the LOOP data shorter than the long integer consumed after the LOOP level byte. Do not add unrelated malformed chunks after parser reachability is established.

## Verifier Contract
Local verify may classify the crash as `wrong_sink` because the immediate read is in the chunk integer helper. The authoritative gate is official submit: vulnerable build exits nonzero and fixed build exits cleanly.

## Format Contract
MNG uses PNG-style big-endian chunk framing: signature, length, four-character chunk type, chunk data, and CRC per chunk. The LOOP chunk is parsed after the image header and its body is interpreted as a level byte followed by loop-count fields.

## Harness Contract
The GraphicsMagick coder fuzzer feeds raw file bytes to the MNG image reader through a Magick blob; no fuzzer-side prefix, selector, or FuzzedDataProvider carving is used.

## Negative Guards
- Do not preserve variants where the fixed image exits nonzero.
- Do not mutate unrelated chunks once the LOOP reader is reached.
- Do not store raw payload bytes, exact positions, task identifiers, checksums, or submit metadata.
