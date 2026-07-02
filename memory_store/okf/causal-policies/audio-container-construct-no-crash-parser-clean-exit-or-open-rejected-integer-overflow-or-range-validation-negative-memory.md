---
type: negative-memory
title: "Audio Container Construct No Crash Parser Clean Exit Or Open Rejected Integer Overflow Or Range Validation Negative Memory"
description: "Round 36 negative memory for no_crash with verifier signal parser_clean_exit_or_open_rejected."
failure_class: "no_crash"
verifier_signal: "parser_clean_exit_or_open_rejected"
candidate_family: "construct"
input_format: "audio-container"
harness_convention: "libfuzzer"
vuln_class: "integer-overflow-or-range-validation"
access_scope: generate
success_count: 0
failure_count: 1
confidence: medium
tags: ["no-crash", "parser-clean-exit-or-open-rejected", "audio-container", "libfuzzer", "construct", "integer-overflow-or-range-validation", "negative-memory", "round-36"]
match_keys: ["no_crash", "parser_clean_exit_or_open_rejected", "audio-container", "libfuzzer", "integer-overflow-or-range-validation", "no-crash", "parser-clean-exit-or-open-rejected", "negative_memory", "construct"]
allowed_scopes: [generate]
forbidden_fields: [raw_poc_bytes, task_id, exact_offset, checksum, submit_metadata]
evidence_level: medium
train_only: true
round: 36
---
# Audio Container Construct No Crash Parser Clean Exit Or Open Rejected Integer Overflow Or Range Validation Negative Memory

- key: `no_crash x parser_clean_exit_or_open_rejected`
- outcome: persistent failure / basin to avoid
- success_count: 0
- failure_count: 1
- related format facts: [[audio-container]]
- related harness facts: [[libfuzzer]]

## Failure Shape
Constructed WAV, NIST, PVF, and RIFF extensible carriers reached recognizable container envelopes but did not produce a sanitizer signal. Text-header containers accepted oversized SF_INFO values without causing the fuzzer read loop to overrun its channel-sized buffer. RIFF variants with high samplerate or maximum channel fields also stayed clean, suggesting the missing trigger is a different container or an open-time arithmetic/allocation path before the harness channel guard.

## Observed Basin
- Failure trajectory classes: no_crash.
- Official confirmation: no server target match for this basin.

## Policy
Treat `no_crash x parser_clean_exit_or_open_rejected` on `audio-container` under `libfuzzer` as a basin to avoid unless a new candidate changes the parser gate, state relation, or sink relation described above. Preserve any proven reachability, but reject variants that return to the same clean-exit, off-target-crash, wrapper-mismatch, usage-only, or fixed-image-crash behavior.

## Procedure
1. Keep only the smallest parser or harness envelope that was actually reached.
2. Identify the missing relation from the signal: parser selection, container acceptance, length relation, stateful subobject, allocation state, or official target sink.
3. Change one relation at a time and discard candidates that return to the same `parser_clean_exit_or_open_rejected` basin.
4. Promote a recovery from this basin only after a later official target match.

## Negative Memory
- Do not resubmit broad mutations that only reproduce `parser_clean_exit_or_open_rejected`.
- Do not count parser reachability, both-image crashes, local wrapper crashes, clean exits, or fixed-image crashes as success.
- Do not store payload bytes, exact positions, task identifiers, checksums, or submit metadata.

## Evidence Shape
- Support: 1 diagnosed persistent failure from round 36 after 6 attempts.
- Scope: generator repair and basin avoidance only.
