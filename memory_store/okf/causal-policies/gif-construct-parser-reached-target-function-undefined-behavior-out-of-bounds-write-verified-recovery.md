---
type: causal-policy
title: "GIF Construct Parser Reached Target Function Undefined Behavior Out Of Bounds Write Verified Recovery"
description: "Round 15 server-verified recovery for gif keyed by wrong_sink x parser_reached_target_function."
failure_class: "wrong_sink"
verifier_signal: "parser_reached_target_function"
candidate_family: "construct"
input_format: "gif"
harness_convention: "libfuzzer"
vuln_class: "undefined-behavior-out-of-bounds-write"
access_scope: generate
success_count: 1
confidence: high
tags: ["wrong-sink", "parser-reached-target-function", "gif", "libfuzzer", "construct", "undefined-behavior-out-of-bounds-write", "verified-recovery", "round-15"]
match_keys: ["wrong_sink", "parser_reached_target_function", "gif", "libfuzzer", "undefined-behavior-out-of-bounds-write", "verified_recovery"]
allowed_scopes: [generate]
forbidden_fields: [raw_poc_bytes, task_id, exact_offset, checksum, submit_metadata]
evidence_level: high
train_only: true
round: 15
---
# GIF Construct Parser Reached Target Function Undefined Behavior Out Of Bounds Write Verified Recovery

- key: `wrong_sink x parser_reached_target_function`
- outcome: server-verified target match
- success_count: 1
- related format facts: [[gif]]
- related harness facts: [[libfuzzer]]

## Policy
When `gif` under `libfuzzer` reaches `parser_reached_target_function` from `wrong_sink`, preserve the accepted parser carrier and retarget only the causal invariant proven by the verifier. Treat local coarse labels as advisory once the vulnerable image fails and the fixed image does not reproduce the target behavior.

## Procedure
1. Preserve the harness contract and format family that reached the parser; do not switch envelopes after reachability is proven.
2. Construct a complete minimal GIF with a logical screen, global palette, graphics-control
   extension that marks a transparent palette index, a tiny image descriptor, valid LZW image data,
   and trailer. The transparent extension must be observed before the image object has a previous
   transparent color, so the palette transparency setter clears the initial sentinel value and then
   marks the requested palette entry.
3. Keep mutations focused on the relevant invariant: parser selection, declared length versus available content, selector versus subparser, table count versus records, lifetime ownership, or sink-specific state.
4. If local labels report a non-target sink while the parser branch is reached, submit once before discarding the candidate.
5. If the fixed image also fails, shrink to the smallest boundary relation and avoid broad randomization.

## Format Contract
- GIF parser reachability requires the signature, logical screen descriptor, palette relationship,
  graphics-control extension, image descriptor, image-data sub-block stream, and trailer to be
  coherent enough for gd's GIF reader to return an image.

## Harness Contract
- The selected libFuzzer target passes the raw file bytes directly to the gd GIF memory loader; there
  is no leading selector, sidecar file, checksum, or FuzzedDataProvider split.

## Negative Memory
- Do not replay unrelated seeds after this parser branch is reached.
- Do not count fixed-image crashes, both-image crashes, clean exits, parser rejection, or off-target local stacks as success.
- Do not store concrete payload bytes, task identifiers, exact positions, checksums, or submit metadata.

## Evidence Shape
- Support: one server-verified Round 15 solve.
- Candidate family: construct.
