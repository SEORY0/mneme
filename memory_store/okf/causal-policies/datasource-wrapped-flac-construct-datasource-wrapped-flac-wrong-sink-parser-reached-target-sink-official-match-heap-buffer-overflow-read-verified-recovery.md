---
type: causal-policy
title: "Datasource Wrapped Flac Construct Datasource Wrapped Flac Wrong Sink Parser Reached Target Sink Official Match Heap Buffer Overflow Read Verified Recovery"
description: "Server-verified recovery for datasource-wrapped-flac when wrong_sink pairs with parser_reached_target_sink_official_match."
failure_class: "wrong_sink"
verifier_signal: "parser_reached_target_sink_official_match"
candidate_family: "construct_datasource_wrapped_flac"
input_format: "datasource-wrapped-flac"
harness_convention: "libfuzzer-flac-decoder-datasource"
vuln_class: "heap-buffer-overflow-read"
access_scope: generate
success_count: 1
confidence: high
tags: ["wrong-sink", "parser-reached-target-sink-official-match", "datasource-wrapped-flac", "libfuzzer-flac-decoder-datasource", "construct-datasource-wrapped-flac", "verified-recovery", "round-33"]
match_keys: ["wrong-sink", "parser-reached-target-sink-official-match", "datasource-wrapped-flac", "libfuzzer-flac-decoder-datasource", "construct-datasource-wrapped-flac", "heap-buffer-overflow-read", "verified-recovery"]
allowed_scopes: [generate]
forbidden_fields: [raw_poc_bytes, task_id, exact_offset, checksum, submit_metadata]
evidence_level: high
train_only: true
round: 33
---
# Datasource Wrapped Flac Construct Datasource Wrapped Flac Wrong Sink Parser Reached Target Sink Official Match Heap Buffer Overflow Read Verified Recovery

- key: `wrong_sink x parser_reached_target_sink_official_match`
- outcome: server-verified vulnerable/fixed split
- success_count: 1
- related format facts: [[datasource-wrapped-flac]]
- related harness facts: [[libfuzzer-flac-decoder-datasource]]

## Policy
When `wrong_sink x parser_reached_target_sink_official_match` appears for `datasource-wrapped-flac`, preserve the parser and harness gates that were proven by the verifier before mutating the sink-specific relation. Treat official vulnerable-only target match as the success gate, not a local coarse crash label.

## Procedure
1. Use the `libfuzzer-flac-decoder-datasource` harness contract and the `datasource-wrapped-flac` format contract before changing sink fields.
2. Recreate the causal relation from the verified trace: Use the decoder datasource envelope to select native FLAC decoding and run stream processing. Inside the supplied stream, keep the FLAC marker, STREAMINFO metadata, frame header, subframe selector, entropy method, and frame-header integrity gates coherent. Trigger the vulnerable bitreader fast path with a fixed-predictor partitioned-Rice residual whose unary-coded value spans a full internal refill and completes exactly at the refill boundary, so the vulnerable reader tries to prime the next word past the allocated bitreader buffer while the fixed build rejects the boundary state cleanly.
3. Keep lengths, dispatch selectors, structural checks, and state setup coherent until the target parser state is reached.
4. Submit only after the fixed image exits cleanly or rejects the relation while the vulnerable image reaches the target sink.

## Format Contract
Use [[datasource-wrapped-flac]]. A useful FLAC carrier starts with the native marker, has STREAMINFO as the first metadata block, and then reaches an audio frame. Frame headers carry sync, blocking strategy, block size, sample rate, channel assignment, sample width, a UTF-style frame number, optional size/sample-rate extensions, and a header integrity byte. Fixed-predictor subframes can select partitioned Rice residual coding; the residual sample count is implied by frame block size, predictor order, and partition order, while each partition carries a Rice parameter followed by unary-plus-low-bits residual values.

## Harness Contract
Use [[libfuzzer-flac-decoder-datasource]]. The active decoder target is not a raw-file harness. It consumes a front-to-back datasource where each scalar or byte-vector read is encoded as a little-endian length-prefixed item. Initial boolean items select native versus Ogg decoding and optional decoder settings. The operation loop consumes a boolean and an operation byte; decoder read callbacks then consume length-prefixed byte chunks as stream data, and write callbacks can consume a boolean to decide whether to abort.

## Evidence Shape
- Support: 1 server-verified round 33 solve.
- Candidate family: construct_datasource_wrapped_flac.
- Verifier key: `wrong_sink x parser_reached_target_sink_official_match`.
- Vulnerability class: `heap-buffer-overflow-read`.
- Recovery summary: Use the decoder datasource envelope to select native FLAC decoding and run stream processing. Inside the supplied stream, keep the FLAC marker, STREAMINFO metadata, frame header, subframe selector, entropy method, and frame-header integrity gates coherent. Trigger the vulnerable bitreader fast path with a fixed-predictor partitioned-Rice residual whose unary-coded value spans a full internal refill and completes exactly at the refill boundary, so the vulnerable reader tries to prime the next word past the allocated bitreader buffer while the fixed build rejects the boundary state cleanly.

## Negative Memory
- Do not count parser reachability, both-image crashes, local-only wrapper crashes, clean exits, or fixed-image crashes as success for this key.
- Do not store raw payload bytes, exact positions, task identifiers, checksums, or submit metadata.
