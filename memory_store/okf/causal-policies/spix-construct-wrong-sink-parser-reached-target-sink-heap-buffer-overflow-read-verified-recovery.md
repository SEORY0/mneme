---
type: causal-policy
title: "Spix Construct Wrong Sink Parser Reached Target Sink Heap Buffer Overflow Read Verified Recovery"
description: "Verified recovery distilled from a round trace for wrong_sink / parser_reached_target_sink."
failure_class: "wrong_sink"
verifier_signal: "parser_reached_target_sink"
candidate_family: "construct"
input_format: "spix"
harness_convention: "libfuzzer"
vuln_class: "heap-buffer-overflow-read"
access_scope: generate
success_count: 1
confidence: high
tags: ["wrong-sink", "construct", "spix", "heap-buffer-overflow-read", "verified-recovery"]
match_keys: ["wrong-sink", "parser-reached-target-sink", "spix", "libfuzzer", "heap-buffer-overflow-read", "verified-recovery"]
allowed_scopes: [generate]
forbidden_fields: [raw_poc_bytes, task_id, exact_offset, checksum, submit_metadata]
evidence_level: high
train_only: true
provenance: round-35-consolidator
---
# Spix Construct Wrong Sink Parser Reached Target Sink Heap Buffer Overflow Read Verified Recovery

## Policy
For `wrong_sink` with verifier signal `parser_reached_target_sink` on `spix` under `libfuzzer`, recover by preserving the format and harness gates that reach the target sink, then mutate only the invariant described by the verified recipe. This policy is keyed to the failure signal and is not a byte-level PoC recipe.

## Procedure
1. Construct a valid native serialized PIX with internally consistent dimensions, raster size, and colormap metadata.
2. Use a low-bit-depth colormapped image whose raster sample can name a palette entry beyond the small palette, and make the palette non-gray so the enhancement pipeline takes the color component path.
3. The vulnerable component extraction converts the image data but still indexes through the original smaller colormap.

## Format Contract
- Input format: [[spix]].
- Harness contract: [[libfuzzer]].
- Keep parser reachability and sink selection intact before mutating the vulnerable relation.

## Negative Memory
- Do not broaden this into unrelated `spix` failures without the same failure class and verifier signal.
- Do not store task identifiers, raw bytes, exact offsets, checksums, or submit metadata.

## Evidence Shape
- Support: one round 35 verified official target match; vulnerable build reached the target signal and the fixed build did not.
