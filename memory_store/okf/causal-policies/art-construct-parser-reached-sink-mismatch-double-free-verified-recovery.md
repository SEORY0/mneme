---
type: causal-policy
title: "ART Construct Parser Reached Sink Mismatch Double Free Verified Recovery"
description: "Round 29 verified recovery for wrong_sink with verifier signal parser_reached_sink_mismatch."
failure_class: "wrong_sink"
verifier_signal: "parser_reached_sink_mismatch"
candidate_family: "construct"
input_format: "art"
harness_convention: "libfuzzer"
vuln_class: "double-free"
access_scope: generate
success_count: 1
confidence: high
tags: ["wrong-sink", "parser-reached-sink-mismatch", "art", "libfuzzer", "construct", "double-free", "verified-recovery", "round-29"]
match_keys: ["wrong_sink", "parser_reached_sink_mismatch", "art", "libfuzzer", "double-free", "wrong-sink", "parser-reached-sink-mismatch", "art", "libfuzzer", "double-free", "verified_recovery", "construct", "construct"]
allowed_scopes: [generate]
forbidden_fields: [raw_poc_bytes, task_id, exact_offset, checksum, submit_metadata]
evidence_level: high
train_only: true
round: 29
---
# ART Construct Parser Reached Sink Mismatch Double Free Verified Recovery

- key: `wrong_sink x parser_reached_sink_mismatch`
- outcome: verified target match / recovery policy
- success_count: 1
- related format facts: [[art]]
- related harness facts: [[libfuzzer]]

## Policy
For `wrong_sink x parser_reached_sink_mismatch` on `art`, keep the parser and harness gates that produced the verifier signal, then vary only the causal relation described below. This is a positive recovery policy because the official vulnerable/fixed verifier recorded a target match.

## Procedure
1. Construct a minimal structurally complete ART binary so the radare2 ART plugin accepts it, allocates plugin metadata, and exposes that metadata through the plugin database callback. No malformed secondary records are needed; the trigger is the normal lifecycle where ownership is transferred to the bin object and then the plugin cleanup path frees the same metadata again.
2. Preserve format recognition and the harness input contract while mutating the narrow sink invariant; do not broaden into an off-target crash or a both-image crash.
3. If later verifier output changes the failure key, re-rank against that new key before mutating unrelated fields.

## Format Contract
- Format [[art]]: ART inputs for this parser begin with an identifying magic and version, followed by fixed-width little-endian image, bitmap, oat, relocation, roots, and flag metadata fields. The parser only needs the fixed header to populate its metadata namespace; section bodies can be minimal when the goal is plugin lifecycle cleanup rather than section decoding.
- Harness [[libfuzzer]]: The harness is a libFuzzer binary-analysis target that feeds the PoC file as raw bytes to radare2's analysis path. There is no FuzzedDataProvider split or mode byte in the input file; selecting the ART parser is done by the file magic.

## Negative Memory
- Do not corrupt the outer `art` recognition gate while retargeting this signal.
- Do not count parser reachability, clean exits, fixed-image crashes, both-image crashes, or local wrong-sink labels as success without official target match.
- Never store payload bytes, exact positions, checksums, submit metadata, or task-local identifiers.

## Evidence Shape
- Support: one round-29 worker trace with official target match.
- Scope: generator repair and retargeting only; pair with [[art]] and [[libfuzzer]].
