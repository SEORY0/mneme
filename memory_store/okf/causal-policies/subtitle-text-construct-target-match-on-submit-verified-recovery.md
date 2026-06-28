---
type: causal-policy
title: "Subtitle Text Construct Target Match On Submit Verified Recovery"
description: "Round 10 verified recovery for wrong_sink with verifier signal target_match_on_submit."
failure_class: "wrong_sink"
verifier_signal: "target_match_on_submit"
candidate_family: "construct"
input_format: "subtitle-text"
harness_convention: "libfuzzer"
vuln_class: "heap-buffer-overflow-read"
access_scope: generate
success_count: 1
confidence: high
tags: ["wrong-sink", "target-match-on-submit", "subtitle-text", "verified-recovery", "round-10"]
match_keys: ["wrong_sink", "target_match_on_submit", "subtitle-text", "libfuzzer", "heap-buffer-overflow-read", "verified_recovery"]
allowed_scopes: [generate]
forbidden_fields: [raw_poc_bytes, task_id, exact_offset, checksum, submit_metadata]
evidence_level: high
train_only: true
round: 10
---
# Subtitle Text Construct Target Match On Submit Verified Recovery

## Policy
For `wrong_sink x target_match_on_submit`, preserve the format and harness gates that reached the official target path, then apply the verified causal relation below. This is a positive recovery policy because the official vulnerable/fixed verifier recorded a target match.

## Procedure
1. A subtitle text envelope that typefind/discoverer recognized was combined with mismatched and malformed markup tags.
2. The tag cleanup path scanned for closing delimiters after a non-closed tag and read past the intended tag boundary, producing a vulnerable-only heap read.

## Format Contract
- Subtitle formats such as WebVTT and SubRip are line-oriented text with timestamp cues followed by cue text. Markup tags inside cue text are escaped/unescaped and then passed to cleanup that tracks allowed open and close tags.
- Harness: The selected GStreamer discoverer harness wraps the raw file bytes in an appsrc URI. Typefinding and parser selection happen inside the pipeline; there is no separate filename or container wrapper required for text subtitle inputs.

## Negative Memory
- Do not broaden mutations after the parser/harness gate is proven.
- Do not submit candidates that reproduce on the fixed image or move to an off-target wrapper crash.
- Do not store raw payload bytes, exact offsets, checksums, or task-local identifiers.

## Evidence Shape
- Support: one round-10 worker trace with official target match.
- Scope: generator repair for the same failure-keyed basin.
