---
type: causal-policy
title: "Mpegts Construct Parser Reached Target Sink Official Target Match Use Of Uninitialized Value Verified Recovery"
description: "Round 28 verified recovery for wrong_sink with verifier signal parser_reached_target_sink_official_target_match."
failure_class: "wrong_sink"
verifier_signal: "parser_reached_target_sink_official_target_match"
candidate_family: "construct"
input_format: "mpegts"
harness_convention: "libfuzzer"
vuln_class: "use-of-uninitialized-value"
access_scope: generate
success_count: 1
confidence: high
tags: ["wrong-sink", "parser-reached-target-sink-official-target-match", "mpegts", "libfuzzer", "construct", "use-of-uninitialized-value", "verified-recovery", "round-28"]
match_keys: ["wrong_sink", "parser_reached_target_sink_official_target_match", "mpegts", "libfuzzer", "use-of-uninitialized-value", "verified_recovery", "construct", "use-of-uninitialized-value"]
allowed_scopes: [generate]
forbidden_fields: [raw_poc_bytes, task_id, exact_offset, checksum, submit_metadata]
evidence_level: high
train_only: true
round: 28
---
# Mpegts Construct Parser Reached Target Sink Official Target Match Use Of Uninitialized Value Verified Recovery

## Policy
For `wrong_sink x parser_reached_target_sink_official_target_match`, preserve the format and harness gates that reached the parser or sink, then apply the verified causal relation below. This is a positive recovery policy because the official vulnerable/fixed verifier recorded a target match.

## Procedure
1. Build a small MPEG transport stream with valid packet framing, a PAT that opens a PMT, and valid PSI section checksums. Put an MPEG-4 IOD program descriptor in the PMT; inside it, include an ES descriptor with a decoder-config descriptor followed by an SL config descriptor that uses a predefined nonzero mode. This reaches the SL parser while an internal context flag is still uninitialized, so the vulnerable build branches on uninitialized state and the fixed build initializes or rejects the state cleanly.
2. Keep the carrier abstract: preserve the gate, invariant, and sink relation rather than task-local bytes, exact offsets, checksums, or identifiers.
3. If the verifier signal changes, re-rank against the new failure key before mutating unrelated fields.

## Format Contract
- Format [[mpegts]]: MPEG-TS reachability required aligned transport packets with sync bytes, payload-start section pointer fields, coherent PAT-to-PMT PID wiring, and valid PSI section lengths and CRCs. The vulnerable MPEG-4 descriptor parser is reached from a PMT program descriptor, not from elementary stream payload. The descriptor body must contain a normal IO descriptor header, an ES descriptor with simple flags, a decoder-config child, and then the SL descriptor child.
- Harness [[libfuzzer]]: The FFmpeg demuxer fuzzer feeds the file bytes to the MPEG-TS demuxer through an AVIO-backed libFuzzer harness. For this demuxer target, the payload can be a raw transport stream with no leading mode byte or FuzzedDataProvider split; once the demuxer opens the PAT and PMT sections, parsing happens during input opening and stream-info discovery.

## Negative Memory
- Do not broaden mutations after parser or harness reachability is proven.
- Do not submit candidates that reproduce on the fixed image, crash both images, or move to an off-target wrapper crash.
- Do not store payload bytes, exact offsets, checksums, or task-local identifiers.

## Evidence Shape
- Support: one round-28 worker trace with official target match.
- Scope: generator repair for the same failure-keyed basin; pair with [[mpegts]] and [[libfuzzer]].
