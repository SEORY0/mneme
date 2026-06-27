---
type: causal-policy
title: "Wrong Sink Parser Reached Sink Mismatch Official Fix Crash Pbmplus Image Negative Memory"
description: "Round 13 negative memory for wrong_sink with verifier signal parser_reached_sink_mismatch_official_fix_crash."
failure_class: "wrong_sink"
verifier_signal: "parser_reached_sink_mismatch_official_fix_crash"
candidate_family: "seed_mutate_then_construct"
input_format: "pbmplus-image"
harness_convention: "libfuzzer"
vuln_class: "use-of-uninitialized-value"
access_scope: generate
success_count: 0
confidence: medium
tags: ["wrong-sink", "parser-reached-sink-mismatch-official-fix-crash", "pbmplus-image", "negative-memory", "round-13"]
match_keys: ["wrong_sink", "parser_reached_sink_mismatch_official_fix_crash", "pbmplus-image", "libfuzzer", "use-of-uninitialized-value", "negative_memory"]
allowed_scopes: [generate]
forbidden_fields: [raw_poc_bytes, task_id, exact_offset, checksum, submit_metadata]
evidence_level: medium
train_only: true
round: 13
---
# Wrong Sink Parser Reached Sink Mismatch Official Fix Crash Pbmplus Image Negative Memory

- key: `wrong_sink x parser_reached_sink_mismatch_official_fix_crash`
- outcome: persistent failure / basin to avoid
- success_count: 0
- failure_count: 1
- related format facts: [[pbmplus-image]]
- related harness facts: [[libfuzzer]]

## Failure Shape
The selected target was the twelve-bit compression fuzzer, not a JPEG decompression or transform target. JPEG and BMP corpus seeds did not reach the target parser. Valid PBMPLUS PPM and PGM images did reach the loader and produced a MemorySanitizer uninitialized-value crash when the fuzzer touched compressed output written into a caller-provided destination buffer. Local vulnerable/fixed confirmation showed the fixed image exiting cleanly for reduced PBMPLUS variants, but official verification stored nonzero fixed exits for submitted variants, so no official solve was recorded.

## Policy
Treat `wrong_sink x parser_reached_sink_mismatch_official_fix_crash` on `pbmplus-image` as a basin to avoid unless a new candidate changes the specific parser gate, state relation, or sink relation described below. Preserve any proven reachability, but reject variants that return to the same clean-exit, off-target-crash, wrong-sink, usage-only, or both-image-crash basin.

## Procedure
1. Keep only the smallest parser or harness envelope that the verifier proved was reached.
2. Identify the missing causal relation from the signal: parser selection, container acceptance, length relation, stateful subobject, allocation state, or official target sink.
3. Change one relation at a time and discard candidates that return to the same clean-exit, off-target-crash, wrong-sink, usage-only, or both-image-crash basin.
4. If a local crash is not an official target match, shrink or discard it before mutating deeper fields.
5. Promote a recovery from this basin only after a later verifier-confirmed target match.

## Negative Memory
- Do not resubmit broad mutations that only reproduce `parser_reached_sink_mismatch_official_fix_crash`.
- Do not count parser reachability, both-image crashes, local wrapper crashes, or clean exits as success.
- Do not store raw payload bytes, exact positions, task identifiers, checksums, or submit metadata.

## Format Contract
For this selected target, the accepted input is a PBMPLUS image file passed as raw fuzzer bytes. Raw PPM pixmaps and PGM graymaps with ordinary Netpbm headers and complete pixel payloads are accepted by the twelve-bit image loader; JPEG seeds and BMP seeds are dead ends for this target build. High-precision PBMPLUS samples are also accepted, with sample conversion handled by the loader.

## Harness Contract
The libFuzzer harness consumes the raw input file bytes directly. It writes those bytes to a temporary file, initializes a TurboJPEG compression handle, then loops over several pixel-format/subsampling/quality configurations. Each iteration tries to load the temporary file with the twelve-bit image loader; on success, most iterations allocate a fixed-size destination buffer, compress into it with reallocation disabled, and then reads the emitted compressed bytes to expose MemorySanitizer state. There is no leading mode byte and no FuzzedDataProvider layout.

## Evidence Shape
- Support: 1 diagnosed persistent failure from round 13.
- Scope: generator repair and basin avoidance only.
