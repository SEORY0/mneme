---
type: causal-policy
title: "Ffmpeg Mlp Access Unit Construct Wrong Sink Parser Reached Target Stack Undefined Behavior Out Of Bounds Index Verified Recovery"
description: "Server-verified recovery for ffmpeg-mlp-access-unit when wrong_sink pairs with parser_reached_target_stack."
failure_class: "wrong_sink"
verifier_signal: "parser_reached_target_stack"
candidate_family: "construct"
input_format: "ffmpeg-mlp-access-unit"
harness_convention: "libfuzzer-ffmpeg-target-dec-fuzzer"
vuln_class: "undefined-behavior-out-of-bounds-index"
access_scope: generate
success_count: 1
confidence: high
tags: ["wrong-sink", "parser-reached-target-stack", "ffmpeg-mlp-access-unit", "libfuzzer-ffmpeg-target-dec-fuzzer", "construct", "verified-recovery", "round-33"]
match_keys: ["wrong-sink", "parser-reached-target-stack", "ffmpeg-mlp-access-unit", "libfuzzer-ffmpeg-target-dec-fuzzer", "construct", "undefined-behavior-out-of-bounds-index", "verified-recovery"]
allowed_scopes: [generate]
forbidden_fields: [raw_poc_bytes, task_id, exact_offset, checksum, submit_metadata]
evidence_level: high
train_only: true
round: 33
---
# Ffmpeg Mlp Access Unit Construct Wrong Sink Parser Reached Target Stack Undefined Behavior Out Of Bounds Index Verified Recovery

- key: `wrong_sink x parser_reached_target_stack`
- outcome: server-verified vulnerable/fixed split
- success_count: 1
- related format facts: [[ffmpeg-mlp-access-unit]]
- related harness facts: [[libfuzzer-ffmpeg-target-dec-fuzzer]]

## Policy
When `wrong_sink x parser_reached_target_stack` appears for `ffmpeg-mlp-access-unit`, preserve the parser and harness gates that were proven by the verifier before mutating the sink-specific relation. Treat official vulnerable-only target match as the success gate, not a local coarse crash label.

## Procedure
1. Use the `libfuzzer-ffmpeg-target-dec-fuzzer` harness contract and the `ffmpeg-mlp-access-unit` format contract before changing sink fields.
2. Recreate the causal relation from the verified trace: Construct a decoder-ready MLP access unit, not a media container. Satisfy the access-unit length, major-sync, restart-header, substream-header, parity, and checksum gates. In the first subblock, decode a minimal valid block so output has accumulated samples. In a following decoding-parameter update, keep the restart state but set the primitive-matrix count just beyond the fixed matrix arrays; the decoder records the invalid count, returns from parameter parsing, and then output rematrixing indexes the stale count. Add an inert separator-sized tail so the target decoder fuzzer delivers the whole packet instead of trimming the last bytes.
3. Keep lengths, dispatch selectors, structural checks, and state setup coherent until the target parser state is reached.
4. Submit only after the fixed image exits cleanly or rejects the relation while the vulnerable image reaches the target sink.

## Format Contract
Use [[ffmpeg-mlp-access-unit]]. MLP decoder input is a raw access-unit packet with a length-bearing access-unit header, optional major-sync header, substream header, restart header, decoding-parameter blocks, residual sample bits, and optional parity/check bytes. Restart headers establish channel bounds and default decoding parameters; later decoding-parameter blocks can update matrix metadata independently. Valid reachability depends on consistent access-unit length, major-sync checksum, restart framing, substream length, and packet parity.

## Harness Contract
Use [[libfuzzer-ffmpeg-target-dec-fuzzer]]. The FFmpeg target decoder libFuzzer harness feeds raw bytes directly to the compiled MLP decoder, with no demux container and no FuzzedDataProvider layout. It scans the input for a fixed packet separator; without an actual separator, a separator-sized trailing region is withheld from the packet, so a single full packet needs an inert tail of that size. The optional large-input codec-context trailer is not needed for this small audio packet.

## Evidence Shape
- Support: 1 server-verified round 33 solve.
- Candidate family: construct.
- Verifier key: `wrong_sink x parser_reached_target_stack`.
- Vulnerability class: `undefined-behavior-out-of-bounds-index`.
- Recovery summary: Construct a decoder-ready MLP access unit, not a media container. Satisfy the access-unit length, major-sync, restart-header, substream-header, parity, and checksum gates. In the first subblock, decode a minimal valid block so output has accumulated samples. In a following decoding-parameter update, keep the restart state but set the primitive-matrix count just beyond the fixed matrix arrays; the decoder records the invalid count, returns from parameter parsing, and then output rematrixing indexes the stale count. Add an inert separator-sized tail so the target decoder fuzzer delivers the whole packet instead of trimming the last bytes.

## Negative Memory
- Do not count parser reachability, both-image crashes, local-only wrapper crashes, clean exits, or fixed-image crashes as success for this key.
- Do not store raw payload bytes, exact positions, task identifiers, checksums, or submit metadata.
