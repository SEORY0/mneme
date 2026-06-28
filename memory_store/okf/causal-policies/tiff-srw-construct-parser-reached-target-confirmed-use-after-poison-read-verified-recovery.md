---
type: causal-policy
title: "Tiff SRW Construct Parser Reached Target Confirmed Use After Poison Read Verified Recovery"
description: "Round 15 server-verified recovery for tiff-srw keyed by wrong_sink x parser_reached_target_confirmed."
failure_class: "wrong_sink"
verifier_signal: "parser_reached_target_confirmed"
candidate_family: "construct"
input_format: "tiff-srw"
harness_convention: "libfuzzer"
vuln_class: "use-after-poison-read"
access_scope: generate
success_count: 1
confidence: high
tags: ["wrong-sink", "parser-reached-target-confirmed", "tiff-srw", "libfuzzer", "construct", "use-after-poison-read", "verified-recovery", "round-15"]
match_keys: ["wrong_sink", "parser_reached_target_confirmed", "tiff-srw", "libfuzzer", "use-after-poison-read", "verified_recovery"]
allowed_scopes: [generate]
forbidden_fields: [raw_poc_bytes, task_id, exact_offset, checksum, submit_metadata]
evidence_level: high
train_only: true
round: 15
---
# Tiff SRW Construct Parser Reached Target Confirmed Use After Poison Read Verified Recovery

- key: `wrong_sink x parser_reached_target_confirmed`
- outcome: server-verified target match
- success_count: 1
- related format facts: [[tiff-srw]]
- related harness facts: [[libfuzzer]]

## Policy
When `tiff-srw` under `libfuzzer` reaches `parser_reached_target_confirmed` from `wrong_sink`, preserve the accepted parser carrier and retarget only the causal invariant proven by the verifier. Treat local coarse labels as advisory once the vulnerable image fails and the fixed image does not reproduce the target behavior.

## Procedure
1. Preserve the harness contract and format family that reached the parser; do not switch envelopes after reachability is proven.
2. Use a minimal Samsung TIFF/SRW envelope that selects the SamsungV2 decompressor and provide a
   bitstream with valid small dimensions. Keep the early row/block motion state safe, then switch a
   later first block into a leftward-reference mode so the reference pointer moves outside the row
   boundary.
3. Keep mutations focused on the relevant invariant: parser selection, declared length versus available content, selector versus subparser, table count versus records, lifetime ownership, or sink-specific state.
4. If local labels report a non-target sink while the parser branch is reached, submit once before discarding the candidate.
5. If the fixed image also fails, shrink to the smallest boundary relation and avoid broad randomization.

## Format Contract
- A TIFF/SRW input needs the standard TIFF header and image file directory fields for make/model,
  dimensions, bit depth, compression, strip location, and byte count. The SamsungV2 stream contains a
  metadata bit header, option flags, initial predictor state, and per-row block motion/difference
  data. This decompressor consumes bits in MSB order from little-endian word chunks.

## Harness Contract
- The TIFF decoder fuzzer parses raw bytes as a TIFF-family image and directly exercises the SRW
  decoder when the metadata selects it. There is no filename gate, mode selector, or
  FuzzedDataProvider layout.

## Negative Memory
- Do not replay unrelated seeds after this parser branch is reached.
- Do not count fixed-image crashes, both-image crashes, clean exits, parser rejection, or off-target local stacks as success.
- Do not store concrete payload bytes, task identifiers, exact positions, checksums, or submit metadata.

## Evidence Shape
- Support: one server-verified Round 15 solve.
- Candidate family: construct.
