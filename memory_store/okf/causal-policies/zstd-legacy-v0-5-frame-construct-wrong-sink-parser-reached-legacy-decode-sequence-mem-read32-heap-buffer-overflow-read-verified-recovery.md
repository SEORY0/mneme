---
type: causal-policy
title: "Zstd Legacy V0 5 Frame Construct Wrong Sink Parser Reached Legacy Decode Sequence Mem Read32 Heap Buffer Overflow Read Verified Recovery"
description: "Server-verified recovery for zstd-legacy-v0-5-frame when wrong_sink pairs with parser_reached_legacy_decode_sequence_mem_read32."
failure_class: "wrong_sink"
verifier_signal: "parser_reached_legacy_decode_sequence_mem_read32"
candidate_family: "construct"
input_format: "zstd-legacy-v0.5-frame"
harness_convention: "libfuzzer"
vuln_class: "heap-buffer-overflow-read"
access_scope: generate
success_count: 1
confidence: high
tags: ["wrong-sink", "parser-reached-legacy-decode-sequence-mem-read32", "zstd-legacy-v0-5-frame", "libfuzzer", "construct", "verified-recovery", "round-33"]
match_keys: ["wrong-sink", "parser-reached-legacy-decode-sequence-mem-read32", "zstd-legacy-v0-5-frame", "libfuzzer", "construct", "heap-buffer-overflow-read", "verified-recovery"]
allowed_scopes: [generate]
forbidden_fields: [raw_poc_bytes, task_id, exact_offset, checksum, submit_metadata]
evidence_level: high
train_only: true
round: 33
---
# Zstd Legacy V0 5 Frame Construct Wrong Sink Parser Reached Legacy Decode Sequence Mem Read32 Heap Buffer Overflow Read Verified Recovery

- key: `wrong_sink x parser_reached_legacy_decode_sequence_mem_read32`
- outcome: server-verified vulnerable/fixed split
- success_count: 1
- related format facts: [[zstd-legacy-v0-5-frame]]
- related harness facts: [[libfuzzer]]

## Policy
When `wrong_sink x parser_reached_legacy_decode_sequence_mem_read32` appears for `zstd-legacy-v0-5-frame`, preserve the parser and harness gates that were proven by the verifier before mutating the sink-specific relation. Treat official vulnerable-only target match as the success gate, not a local coarse crash label.

## Procedure
1. Use the `libfuzzer` harness contract and the `zstd-legacy-v0-5-frame` format contract before changing sink fields.
2. Recreate the causal relation from the verified trace: Use the stream-decompression harness with a front seed prefix that makes the first input chunk contain the complete remaining frame. Build a minimal legacy v0.5 compressed frame that satisfies the frame, block, literals, sequence-header, and entropy-table gates, then choose a sequence symbol that requests the long literal-length extension while declaring only a single dumps byte and omitting following frame data. The vulnerable decoder reads a multi-byte extension from the exhausted dumps area and crosses the end of the fuzzer input allocation; the fixed build rejects or handles the truncated extension.
3. Keep lengths, dispatch selectors, structural checks, and state setup coherent until the target parser state is reached.
4. Submit only after the fixed image exits cleanly or rejects the relation while the vulnerable image reaches the target sink.

## Format Contract
Use [[zstd-legacy-v0-5-frame]]. Legacy zstd v0.5 frames have a compact magic/header followed by block headers that encode block type and compressed size, then the block payload. Compressed blocks contain a literals section followed by sequence metadata. The sequence metadata includes a sequence count, table-type controls, a dumps-length field, optional dumps bytes, entropy table descriptions, and the backward bitstream. Long literal or match lengths consume extension bytes from the dumps area.

## Harness Contract
Use [[libfuzzer]]. The libFuzzer stream-decompression harness treats the input as raw bytes but first consumes a front seed before parsing. That seed drives pseudo-random input and output chunk sizes for the streaming API. If the first parser chunk is small, legacy streaming may copy data into an internal staging buffer; selecting a seed that feeds the frame as one direct chunk can make end-of-input overreads visible against the fuzzer allocation.

## Evidence Shape
- Support: 1 server-verified round 33 solve.
- Candidate family: construct.
- Verifier key: `wrong_sink x parser_reached_legacy_decode_sequence_mem_read32`.
- Vulnerability class: `heap-buffer-overflow-read`.
- Recovery summary: Use the stream-decompression harness with a front seed prefix that makes the first input chunk contain the complete remaining frame. Build a minimal legacy v0.5 compressed frame that satisfies the frame, block, literals, sequence-header, and entropy-table gates, then choose a sequence symbol that requests the long literal-length extension while declaring only a single dumps byte and omitting following frame data. The vulnerable decoder reads a multi-byte extension from the exhausted dumps area and crosses the end of the fuzzer input allocation; the fixed build rejects or handles the truncated extension.

## Negative Memory
- Do not count parser reachability, both-image crashes, local-only wrapper crashes, clean exits, or fixed-image crashes as success for this key.
- Do not store raw payload bytes, exact positions, task identifiers, checksums, or submit metadata.
