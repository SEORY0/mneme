---
type: negative-memory
title: "Wrong Sink Sink Mismatch Fix Also Crashes UPX Packed Unix Seed Mutate Heap Buffer Overflow Read Negative Memory"
description: "Round 27 diagnosed persistent failure for wrong_sink with verifier signal sink_mismatch_fix_also_crashes."
failure_class: "wrong_sink"
verifier_signal: "sink_mismatch_fix_also_crashes"
candidate_family: "seed_mutate"
input_format: "upx-packed-unix"
harness_convention: "libfuzzer"
vuln_class: "heap-buffer-overflow-read"
access_scope: generate
success_count: 0
confidence: high
tags: ["wrong-sink", "sink-mismatch-fix-also-crashes", "upx-packed-unix", "libfuzzer", "seed-mutate", "heap-buffer-overflow-read", "negative-memory", "round-27"]
match_keys: ["wrong_sink", "sink_mismatch_fix_also_crashes", "upx-packed-unix", "libfuzzer", "heap-buffer-overflow-read", "negative_memory"]
allowed_scopes: [generate]
forbidden_fields: [raw_poc_bytes, task_id, exact_offset, checksum, submit_metadata]
evidence_level: high
train_only: true
round: 27
---
# Wrong Sink Sink Mismatch Fix Also Crashes UPX Packed Unix Seed Mutate Heap Buffer Overflow Read Negative Memory

- key: `wrong_sink x sink_mismatch_fix_also_crashes`
- outcome: diagnosed persistent failure; avoid repeating this basin without a new gate relation.
- success_count: 0

## Failure Shape
- A genuine packed Unix seed reached the unpacker when the packed-file envelope, pack header, and trailer pointer were preserved.
- Reducing a compressed block size by a small amount produced a vulnerable-build heap read in the decompressor, but the fixed build also crashed, so the input was over-broad rather than isolating the p_unix compressed-size invariant.
- Other classic packed ELF and larger Unix seeds either rejected the mutation as corrupt or did not reach the intended packed-file test path.

## Format / Harness Contract
- UPX packed Unix files preserve an executable envelope and carry a trailer with a pack header and a pointer to compressed data.
- The compressed data begins with packed metadata containing original size and blocksize, followed by b_info records that carry uncompressed size, compressed size, and method/filter bytes.
- Some corpus files expose a plain trailer magic, while newer packed shared-object samples may not be accepted by the test-mode unpacker.
- Harness [[libfuzzer]]:
  - The harness writes the raw input bytes to a temporary file and invokes UPX test mode on that file.
  - The input is not carved, prefixed, checksummed by the harness, or consumed through FuzzedDataProvider; all structure must be valid enough for UPX packed-file recognition.

## Policy
Treat `wrong_sink x sink_mismatch_fix_also_crashes` as a negative-memory key for `upx-packed-unix` under `libfuzzer`. A future candidate needs a different causal relation than the recorded `seed_mutate` attempt family, or explicit evidence that the missing parser/sink gate has changed.

## Procedure
1. First re-establish the exact parser or harness gate named by the verifier signal before changing payload scale.
2. If the prior basin was clean execution, search for the narrow branch that reaches the sink rather than sweeping larger mutations.
3. If the prior basin was fixed-image or both-image failure, narrow the mutation until the fixed build rejects or survives before submitting.

## Negative Memory
- Do not repeat the `seed_mutate` family against this failure key without a new gate hypothesis.
- Do not keep candidates that are clean, parser-not-reached, fixed-image crashes, or off-target wrapper failures.
- Do not store payload bytes, exact offsets, checksums, or task-local identifiers.

## Evidence Shape
- Support: one diagnosed round-27 persistent failure.
- Pair with [[upx-packed-unix]] and [[libfuzzer]].
