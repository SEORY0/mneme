---
type: causal-policy
title: "TIFF Seed Mutate No Crash Local Parser Reached Clean But Official Target Match Class State Mismatch After Rgba Read Verified Recovery"
description: "Round 32 server-verified recovery for tiff keyed by no_crash x local_parser_reached_clean_but_official_target_match."
failure_class: "no_crash"
verifier_signal: "local_parser_reached_clean_but_official_target_match"
candidate_family: "seed_mutate"
input_format: "tiff"
harness_convention: "libfuzzer-graphicsmagick-ptif-coder"
vuln_class: "class-state-mismatch-after-rgba-read"
access_scope: generate
success_count: 1
confidence: high
tags: ["no-crash", "local-parser-reached-clean-but-official-target-match", "tiff", "libfuzzer-graphicsmagick-ptif-coder", "seed-mutate", "class-state-mismatch-after-rgba-read", "verified-recovery", "round-32"]
match_keys: ["no-crash", "local-parser-reached-clean-but-official-target-match", "tiff", "libfuzzer-graphicsmagick-ptif-coder", "seed-mutate", "class-state-mismatch-after-rgba-read", "verified-recovery"]
allowed_scopes: [generate]
forbidden_fields: [raw_poc_bytes, task_id, exact_offset, checksum, submit_metadata]
evidence_level: high
train_only: true
round: 32
---
# TIFF Seed Mutate No Crash Local Parser Reached Clean But Official Target Match Class State Mismatch After Rgba Read Verified Recovery

- key: `no_crash x local_parser_reached_clean_but_official_target_match`
- outcome: server-verified target match
- success_count: 1
- related format facts: [[tiff]]
- related harness facts: [[libfuzzer-graphicsmagick-ptif-coder]]

## Policy
When `tiff` under `[[libfuzzer-graphicsmagick-ptif-coder]]` produces `local_parser_reached_clean_but_official_target_match` from `no_crash`, keep the parser-reaching envelope and retarget the causal invariant that the official verifier accepted. Local sink labels are advisory once the vulnerable image fails and the fixed image stays clean or the server reports target match.

## Procedure
1. Preserve the harness and format contract that reached the parser: `[[tiff]]` through `[[libfuzzer-graphicsmagick-ptif-coder]]`.
2. Apply the verified recovery: Start from a valid palette TIFF seed with alpha metadata and preserve the image directory, strip data, colormap, sample count, and extra-sample relation. Add a coherent sample-format tag that makes GraphicsMagick's palette quantum importer decline the direct import path while libtiff can still decode through the RGBA strip reader. This leaves the vulnerable reader with a PseudoClass image after an RGBA transfer; the fixed build promotes the image to DirectClass for that path.
3. Keep mutations narrow around the gate/invariant relation rather than rebuilding unrelated carriers or adding broad random noise.
4. If local labels report a non-target sink while the parser branch is reached, submit one minimized candidate before discarding it.
5. Reject both-image crashes, fixed-image crashes, parser rejection, and clean exits as non-success even when they look close locally.

## Format Contract
- Classic TIFF uses an endian header pointing to an image-file-directory. The directory records geometry, photometric interpretation, bits per sample, samples per pixel, planar configuration, strip offsets and byte counts, optional sample format, colormap, and extra-sample alpha metadata. For palette images, preserving the colormap and alpha tags keeps GraphicsMagick in PseudoClass/matte state before method selection; changing sample format can steer from direct palette import to libtiff RGBA fallback without corrupting the carrier.

## Harness Contract
- The generated target is the GraphicsMagick PTIF coder fuzzer. It passes the entire submitted file as a Magick blob, sets the coder name to PTIF, reads through the TIFF-family decoder, and then writes the decoded image back when the coder supports writing. There is no argv file path contract, fuzzer-side selector byte, integrity-field gate, or FuzzedDataProvider layout.

## Negative Memory
- Do not store concrete payload bytes, task identifiers, exact positions, checksums, or submit metadata.
- Do not treat parser reachability alone as success without the official target-match signal.
- Do not repeat a clean-exit or both-image-crash basin once the verifier has characterized it.

## Evidence Shape
- Support: one server-verified Round 32 solve.
- Candidate family: seed_mutate.
