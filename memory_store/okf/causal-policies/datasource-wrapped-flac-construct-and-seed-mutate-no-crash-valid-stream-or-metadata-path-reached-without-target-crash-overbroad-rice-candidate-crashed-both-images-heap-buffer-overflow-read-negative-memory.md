---
type: negative-memory
title: "Datasource Wrapped Flac Construct And Seed Mutate No Crash Valid Stream Or Metadata Path Reached Without Target Crash Overbroad Rice Candidate Crashed Both Images Heap Buffer Overflow Read Negative Memory"
description: "Round 33 negative memory for no_crash with verifier signal valid_stream_or_metadata_path_reached_without_target_crash; overbroad_rice_candidate_crashed_both_images."
failure_class: "no_crash"
verifier_signal: "valid_stream_or_metadata_path_reached_without_target_crash; overbroad_rice_candidate_crashed_both_images"
candidate_family: "construct_and_seed_mutate"
input_format: "datasource-wrapped-flac"
harness_convention: "libfuzzer-flac-decoder-datasource"
vuln_class: "heap-buffer-overflow-read"
access_scope: generate
success_count: 0
failure_count: 1
confidence: medium
tags: ["no-crash", "valid-stream-or-metadata-path-reached-without-target-crash-overbroad-rice-candidate-crashed-both-images", "datasource-wrapped-flac", "libfuzzer-flac-decoder-datasource", "construct-and-seed-mutate", "heap-buffer-overflow-read", "negative-memory", "round-33"]
match_keys: ["no_crash", "valid_stream_or_metadata_path_reached_without_target_crash; overbroad_rice_candidate_crashed_both_images", "datasource-wrapped-flac", "libfuzzer-flac-decoder-datasource", "construct-and-seed-mutate", "heap-buffer-overflow-read", "negative_memory"]
allowed_scopes: [generate]
forbidden_fields: [raw_poc_bytes, task_id, exact_offset, checksum, submit_metadata]
evidence_level: medium
train_only: true
round: 33
---
# Datasource Wrapped Flac Construct And Seed Mutate No Crash Valid Stream Or Metadata Path Reached Without Target Crash Overbroad Rice Candidate Crashed Both Images Heap Buffer Overflow Read Negative Memory

- key: `no_crash x valid_stream_or_metadata_path_reached_without_target_crash; overbroad_rice_candidate_crashed_both_images`
- outcome: persistent failure / basin to avoid
- success_count: 0
- failure_count: 1
- related format facts: [[datasource-wrapped-flac]]
- related harness facts: [[libfuzzer-flac-decoder-datasource]]

## Failure Shape
The datasource envelope was established and valid wrapped FLAC seeds executed cleanly. Metadata underfill, complete picture-header underfill, frame-like trailing chunks, seek sequencing, one-byte and empty read chunks, and a large Rice residual-tail construction did not produce a vulnerable-only target crash. The Rice-tail construction was over-broad under official differential because both images crashed, so it was not a scoring target relation. The remaining gap is a more precise signed-block bitreader tail state that crashes the vulnerable build while the fixed build rejects or drains it cleanly.

## Policy
Treat `no_crash x valid_stream_or_metadata_path_reached_without_target_crash; overbroad_rice_candidate_crashed_both_images` on `datasource-wrapped-flac` as a basin to avoid unless a new candidate changes the parser gate, state relation, sink relation, or official differential behavior described below. Do not repeat variants that only preserve the same clean-exit, off-target, post-patch-crash, both-image-crash, or target-handoff-missing signal.

## Procedure
1. Keep only the smallest parser or harness envelope that was actually reached.
2. Identify the missing relation from the verifier signal: parser selection, container acceptance, length relation, stateful subobject, allocation state, or official target sink.
3. Change one causal relation at a time and discard candidates that return to `valid_stream_or_metadata_path_reached_without_target_crash; overbroad_rice_candidate_crashed_both_images`.
4. If a local crash is not an official target match, shrink or discard it before mutating deeper fields.
5. Promote a recovery from this basin only after a later verifier-confirmed vulnerable-only target match.

## Negative Memory
- Do not resubmit broad mutations that only reproduce `valid_stream_or_metadata_path_reached_without_target_crash; overbroad_rice_candidate_crashed_both_images`.
- Do not count parser reachability, both-image crashes, local wrapper crashes, usage banners, clean exits, timeouts, or fixed-image crashes as success.
- Never store payload bytes, exact positions, task identifiers, checksums, or submit metadata.

## Format Contract
Use [[datasource-wrapped-flac]]. A native FLAC stream starts with the stream marker, STREAMINFO metadata first, optional metadata blocks, and then audio frames. Audio frames carry sync, stream parameters, subframe headers, optional wasted-bit coding, predictor warmup samples, entropy coding method, partition order, Rice parameters, residual bitstream, padding, and frame checksum. Metadata block headers carry last-block, type, and body length; responded metadata types are parsed rather than skipped.

## Harness Contract
Use [[libfuzzer-flac-decoder-datasource]]. The active decoder harness does not feed raw FLAC directly. Every harness value is a front-consumed datasource item encoded as a little-endian length followed by that many bytes. The first boolean selects native FLAC versus Ogg initialization. Several option booleans may consume additional scalar or data items. Operation-loop booleans and byte selectors call decoder operations such as process_single, process_until_end_of_metadata, process_until_end_of_stream, and seek_absolute. Decoder read callbacks pull FLAC stream bytes from subsequent length-prefixed datasource items; oversized items are truncated to the callback request, so long streams must be split into callback-sized chunks.

## Evidence Shape
- Support: 1 diagnosed persistent failure from round 33 after 8 attempts.
- Scope: generator repair and basin avoidance only.
