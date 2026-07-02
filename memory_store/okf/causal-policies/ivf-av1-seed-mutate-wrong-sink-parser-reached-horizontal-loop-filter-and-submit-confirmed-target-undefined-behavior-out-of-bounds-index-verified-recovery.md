---
type: causal-policy
title: "IVF AV1 Seed Mutate Wrong Sink Parser Reached Horizontal Loop Filter And Submit Confirmed Target Undefined Behavior Out Of Bounds Index Verified Recovery"
description: "Round 32 server-verified recovery for ivf-av1 keyed by wrong_sink x parser_reached_horizontal_loop_filter_and_submit_confirmed_target."
failure_class: "wrong_sink"
verifier_signal: "parser_reached_horizontal_loop_filter_and_submit_confirmed_target"
candidate_family: "seed_mutate"
input_format: "ivf-av1"
harness_convention: "libfuzzer"
vuln_class: "undefined-behavior-out-of-bounds-index"
access_scope: generate
success_count: 1
confidence: high
tags: ["wrong-sink", "parser-reached-horizontal-loop-filter-and-submit-confirmed-target", "ivf-av1", "libfuzzer", "seed-mutate", "undefined-behavior-out-of-bounds-index", "verified-recovery", "round-32"]
match_keys: ["wrong-sink", "parser-reached-horizontal-loop-filter-and-submit-confirmed-target", "ivf-av1", "libfuzzer", "seed-mutate", "undefined-behavior-out-of-bounds-index", "verified-recovery"]
allowed_scopes: [generate]
forbidden_fields: [raw_poc_bytes, task_id, exact_offset, checksum, submit_metadata]
evidence_level: high
train_only: true
round: 32
---
# IVF AV1 Seed Mutate Wrong Sink Parser Reached Horizontal Loop Filter And Submit Confirmed Target Undefined Behavior Out Of Bounds Index Verified Recovery

- key: `wrong_sink x parser_reached_horizontal_loop_filter_and_submit_confirmed_target`
- outcome: server-verified target match
- success_count: 1
- related format facts: [[ivf-av1]]
- related harness facts: [[libfuzzer]]

## Policy
When `ivf-av1` under `[[libfuzzer]]` produces `parser_reached_horizontal_loop_filter_and_submit_confirmed_target` from `wrong_sink`, keep the parser-reaching envelope and retarget the causal invariant that the official verifier accepted. Local sink labels are advisory once the vulnerable image fails and the fixed image stays clean or the server reports target match.

## Procedure
1. Preserve the harness and format contract that reached the parser: `[[ivf-av1]]` through `[[libfuzzer]]`.
2. Apply the verified recovery: Use a structurally valid IVF AV1 decoder corpus member that reaches tile decode and post-frame loop filtering. The important gates are a complete IVF header, at least one decodable AV1 frame, loop filtering enabled, and transform/block metadata that makes the horizontal loop-filter bitmask address a paired edge outside the current superblock boundary. The crash comes from the loop-filter threshold lookup using an out-of-range edge-derived selector; the fixed build rejects or avoids that invalid selector.
3. Keep mutations narrow around the gate/invariant relation rather than rebuilding unrelated carriers or adding broad random noise.
4. If local labels report a non-target sink while the parser branch is reached, submit one minimized candidate before discarding it.
5. Reject both-image crashes, fixed-image crashes, parser rejection, and clean exits as non-success even when they look close locally.

## Format Contract
- The input is an IVF container carrying AV1 frame payloads. The harness reads a fixed-size IVF file header first, then repeatedly reads IVF frame records and passes each frame payload to the AV1 decoder. Tiny non-IVF byte stubs are rejected before decode. Corpus-derived IVF samples are useful because they preserve frame framing, codec setup, tile parsing, and post-decode filter state.

## Harness Contract
- The libFuzzer input bytes are wrapped with fmemopen as a file. The harness reads the IVF header from the front of the raw input, initializes the AV1 decoder, loops through IVF frames with ivf_read_frame, calls aom_codec_decode for each frame, then drains decoded frames. There is no FuzzedDataProvider split and no argv or stdin contract beyond the raw file bytes.

## Negative Memory
- Do not store concrete payload bytes, task identifiers, exact positions, checksums, or submit metadata.
- Do not treat parser reachability alone as success without the official target-match signal.
- Do not repeat a clean-exit or both-image-crash basin once the verifier has characterized it.

## Evidence Shape
- Support: one server-verified Round 32 solve.
- Candidate family: seed_mutate.
