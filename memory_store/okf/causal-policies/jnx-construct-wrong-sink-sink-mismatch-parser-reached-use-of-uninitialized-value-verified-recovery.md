---
type: causal-policy
title: "JNX Construct Wrong Sink Sink Mismatch Parser Reached Use Of Uninitialized Value Verified Recovery"
description: "Round 32 server-verified recovery for jnx keyed by wrong_sink x sink_mismatch_parser_reached."
failure_class: "wrong_sink"
verifier_signal: "sink_mismatch_parser_reached"
candidate_family: "construct"
input_format: "jnx"
harness_convention: "libfuzzer"
vuln_class: "use-of-uninitialized-value"
access_scope: generate
success_count: 1
confidence: high
tags: ["wrong-sink", "sink-mismatch-parser-reached", "jnx", "libfuzzer", "construct", "use-of-uninitialized-value", "verified-recovery", "round-32"]
match_keys: ["wrong-sink", "sink-mismatch-parser-reached", "jnx", "libfuzzer", "construct", "use-of-uninitialized-value", "verified-recovery"]
allowed_scopes: [generate]
forbidden_fields: [raw_poc_bytes, task_id, exact_offset, checksum, submit_metadata]
evidence_level: high
train_only: true
round: 32
---
# JNX Construct Wrong Sink Sink Mismatch Parser Reached Use Of Uninitialized Value Verified Recovery

- key: `wrong_sink x sink_mismatch_parser_reached`
- outcome: server-verified target match
- success_count: 1
- related format facts: [[jnx]]
- related harness facts: [[libfuzzer]]

## Policy
When `jnx` under `[[libfuzzer]]` produces `sink_mismatch_parser_reached` from `wrong_sink`, keep the parser-reaching envelope and retarget the causal invariant that the official verifier accepted. Local sink labels are advisory once the vulnerable image fails and the fixed image stays clean or the server reports target match.

## Procedure
1. Preserve the harness and format contract that reached the parser: `[[jnx]]` through `[[libfuzzer]]`.
2. Apply the verified recovery: Build a minimal valid one-tile JNX envelope with consistent little-endian level and tile metadata. The tile payload should be arranged so that, after the JNX reader prepends its JPEG prefix, GraphicsMagick's generic blob detector selects a different image coder instead of JPEG. A compact embedded DICOM header with a short character value for the photometric interpretation field reaches a fixed-length string comparison that reads uninitialized stack bytes. The fixed build forces tile decoding through the JPEG coder, closing the secondary-coder route.
3. Keep mutations narrow around the gate/invariant relation rather than rebuilding unrelated carriers or adding broad random noise.
4. If local labels report a non-target sink while the parser branch is reached, submit one minimized candidate before discarding it.
5. Reject both-image crashes, fixed-image crashes, parser rejection, and clean exits as non-success even when they look close locally.

## Format Contract
- JNX uses a little-endian container header, a level table, and per-level tile records containing geographic bounds, dimensions, payload length, and payload pointer. JNX tile payloads omit the leading JPEG marker because the reader injects it before passing the tile blob onward. GraphicsMagick DICOM detection uses a preamble marker, and DICOM elements can use explicit VR headers with short lengths for character fields.

## Harness Contract
- The GraphicsMagick coder harness is libFuzzer over raw file bytes. There is no FuzzedDataProvider carving; the input blob is handed to the JNX reader selected by the harness, and embedded tile bytes are then passed through GraphicsMagick's normal blob-to-image dispatch.

## Negative Memory
- Do not store concrete payload bytes, task identifiers, exact positions, checksums, or submit metadata.
- Do not treat parser reachability alone as success without the official target-match signal.
- Do not repeat a clean-exit or both-image-crash basin once the verifier has characterized it.

## Evidence Shape
- Support: one server-verified Round 32 solve.
- Candidate family: construct.
