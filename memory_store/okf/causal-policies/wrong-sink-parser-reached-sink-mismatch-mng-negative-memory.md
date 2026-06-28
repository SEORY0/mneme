---
type: causal-policy
title: "Wrong Sink Parser Reached Sink Mismatch Mng Negative Memory"
description: "Round 12 negative memory for wrong_sink with verifier signal parser_reached_sink_mismatch."
failure_class: "wrong_sink"
verifier_signal: "parser_reached_sink_mismatch"
candidate_family: "construct"
input_format: "mng"
harness_convention: "libfuzzer"
vuln_class: "heap-buffer-overflow-read"
access_scope: generate
success_count: 0
confidence: medium
tags: ["wrong-sink", "parser-reached-sink-mismatch", "mng", "negative-memory", "round-12"]
match_keys: ["wrong_sink", "parser_reached_sink_mismatch", "mng", "libfuzzer", "heap-buffer-overflow-read", "negative_memory"]
allowed_scopes: [generate]
forbidden_fields: [raw_poc_bytes, task_id, exact_offset, checksum, submit_metadata]
evidence_level: medium
train_only: true
round: 12
---
# Wrong Sink Parser Reached Sink Mismatch Mng Negative Memory

- key: `wrong_sink x parser_reached_sink_mismatch`
- outcome: persistent failure / basin to avoid
- success_count: 0
- failure_count: 1
- related format facts: [[mng]]
- related harness facts: [[libfuzzer]]

## Failure Shape
The constructed MNG reliably reached the described LOOP path and crashed in the vulnerable local verifier, but every short-LOOP variant submitted caused the fixed image to return nonzero, so the attempt did not produce the required vuln-crash/fix-clean split.

## Policy
Treat `wrong_sink x parser_reached_sink_mismatch` on `mng` as a basin to avoid unless a new candidate changes the parser gate, state relation, or official target sink. Preserve any proven reachability, but reject variants that return to the same verifier signal without changing the causal gate under test.

## Procedure
1. Keep only the smallest parser or harness envelope that the verifier proved was reached.
2. Identify the missing causal relation from the signal: parser selection, container acceptance, length relation, stateful subobject, allocation state, or official target sink.
3. Change one relation at a time and discard candidates that return to the same clean-exit, off-target-crash, wrong-sink, usage-only, or both-image-crash basin.
4. If a local crash is not an official target match, shrink or discard it before mutating deeper fields.
5. Promote a recovery from this basin only after a later verifier-confirmed target match.

## Format Contract
MNG uses a PNG-like byte stream: file signature followed by big-endian length, four-character chunk type, chunk data, and CRC for each chunk. The basic image header chunk must appear before control chunks, and a terminal chunk can close the stream. LOOP chunk data is interpreted as a level byte followed by a loop-count integer.

## Harness Contract
The GraphicsMagick coder fuzzer feeds the raw file bytes to the MNG image reader through a Magick blob; there is no fuzzer-side prefix or mode selector.

## Negative Memory
- Do not resubmit broad mutations that only reproduce `parser_reached_sink_mismatch`.
- Do not count parser reachability, both-image crashes, local wrapper crashes, clean exits, or fixed-image crashes as success.
- Do not store raw payload bytes, exact positions, task identifiers, or submit metadata.

## Evidence Shape
- Support: one diagnosed persistent failure from round 12.
- Scope: generator repair and basin avoidance only.

## Retarget Recovery
Round 12 retargeting found a verified recovery for this same failure key: [[mng-retarget-parser-reached-sink-mismatch-heap-buffer-overflow-read-verified-recovery]]. Prefer the verified short-LOOP body relation before repeating fixed-image-nonclean variants from this basin.
