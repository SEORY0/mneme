---
type: causal-policy
title: "Wrong Sink Pbmplus Image Parser Reached Sink Mismatch Official Fix Crash Negative Memory"
description: "Negative memory for wrong_sink with parser_reached_sink_mismatch_official_fix_crash on pbmplus-image inputs."
failure_class: wrong_sink
verifier_signal: parser_reached_sink_mismatch_official_fix_crash
candidate_family: seed_mutate_then_construct
input_format: pbmplus-image
harness_convention: libfuzzer
vuln_class: use-of-uninitialized-value
access_scope: generate
success_count: 0
confidence: medium
tags: [wrong-sink, parser-reached-sink-mismatch-official-fix-crash, pbmplus-image, use-of-uninitialized-value, negative_memory]
match_keys: [wrong-sink, parser-reached-sink-mismatch-official-fix-crash, pbmplus-image, use-of-uninitialized-value]
allowed_scopes: [generate]
forbidden_fields: [raw_poc_bytes, task_id, exact_offset, checksum, submit_metadata]
evidence_level: medium
train_only: true
---
# Wrong Sink Pbmplus Image Parser Reached Sink Mismatch Official Fix Crash Negative Memory

- key: `wrong_sink x parser_reached_sink_mismatch_official_fix_crash`
- outcome: persistent failure basin
- success_count: 0
- failure_count: 1
- formats: [[pbmplus-image]]

## Dead End
The selected target was the twelve-bit compression fuzzer, not a JPEG decompression or transform target. JPEG and BMP corpus seeds did not reach the target parser. Valid PBMPLUS PPM and PGM images did reach the loader and produced a MemorySanitizer uninitialized-value crash when the fuzzer touched compressed output written into a caller-provided destination buffer. Local vulnerable/fixed confirmation showed the fixed image exiting cleanly for reduced PBMPLUS variants, but official verification stored nonzero fixed exits for submitted variants, so no official solve was recorded.

## Avoid
Do not repeat the same candidate family when the verifier signal matches this key. Treat broad seed mutation, wrapper usage paths, both-image crashes, parser-clean exits, or local-only crashes as evidence that the current surface is not the target differential.

## Recovery Direction
Preserve only independently validated format or harness reachability facts. Re-enter generation by first satisfying the harness contract and the earliest format gate, then use a different target-specific invariant instead of enlarging or randomly mutating the failed family.
