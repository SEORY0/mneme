---
type: causal-policy
title: "Miff Seed Mutate Target Sink Match Use Of Uninitialized Value Verified Recovery"
description: "Round 15 server-verified recovery for miff keyed by generic_crash x target_sink_match."
failure_class: "generic_crash"
verifier_signal: "target_sink_match"
candidate_family: "seed_mutate"
input_format: "miff"
harness_convention: "libfuzzer"
vuln_class: "use-of-uninitialized-value"
access_scope: generate
success_count: 1
confidence: high
tags: ["generic-crash", "target-sink-match", "miff", "libfuzzer", "seed-mutate", "use-of-uninitialized-value", "verified-recovery", "round-15"]
match_keys: ["generic_crash", "target_sink_match", "miff", "libfuzzer", "use-of-uninitialized-value", "verified_recovery"]
allowed_scopes: [generate]
forbidden_fields: [raw_poc_bytes, task_id, exact_offset, checksum, submit_metadata]
evidence_level: high
train_only: true
round: 15
---
# Miff Seed Mutate Target Sink Match Use Of Uninitialized Value Verified Recovery

- key: `generic_crash x target_sink_match`
- outcome: server-verified target match
- success_count: 1
- related format facts: [[miff]]
- related harness facts: [[libfuzzer]]

## Policy
When `miff` under `libfuzzer` reaches `target_sink_match` from `generic_crash`, preserve the accepted parser carrier and retarget only the causal invariant proven by the verifier. Treat local coarse labels as advisory once the vulnerable image fails and the fixed image does not reproduce the target behavior.

## Procedure
1. Preserve the harness contract and format family that reached the parser; do not switch envelopes after reachability is proven.
2. Use a real MIFF image seed so the encoder fuzzer reaches MIFF decoding, then mutate a geometry-
   valued header attribute into ratio-style geometry that leaves one GeometryInfo component
   uninitialized. The MIFF reader calls the geometry parser on that header value, and the
   vulnerable parser later branches on the uninitialized component.
3. Keep mutations focused on the relevant invariant: parser selection, declared length versus available content, selector versus subparser, table count versus records, lifetime ownership, or sink-specific state.
4. If local labels report a non-target sink while the parser branch is reached, submit once before discarding the candidate.
5. If the fixed image also fails, shrink to the smallest boundary relation and avoid broad randomization.

## Format Contract
- MIFF files start with an ASCII key-value header identifying ImageMagick, class, dimensions, depth,
  colorspace, resolution, page, and related attributes, followed by the image payload. Several header
  attributes are interpreted as geometry strings by the MIFF reader before pixel data is consumed.

## Harness Contract
- The generated target is the MIFF encoder fuzzer. It treats the entire raw input as a MIFF image
  blob, reads it through Magick++ with the MIFF encoder selected, and then writes it back if reading
  succeeds. There is no harness prefix or separate option carving.

## Negative Memory
- Do not replay unrelated seeds after this parser branch is reached.
- Do not count fixed-image crashes, both-image crashes, clean exits, parser rejection, or off-target local stacks as success.
- Do not store concrete payload bytes, task identifiers, exact positions, checksums, or submit metadata.

## Evidence Shape
- Support: one server-verified Round 15 solve.
- Candidate family: seed_mutate.
