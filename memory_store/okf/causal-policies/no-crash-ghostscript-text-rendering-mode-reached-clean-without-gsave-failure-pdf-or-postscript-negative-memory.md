---
type: causal-policy
title: "No Crash Ghostscript Text Rendering Mode Reached Clean Without Gsave Failure Pdf Or Postscript Negative Memory"
description: "Round 7 negative memory for no_crash with verifier signal ghostscript_text_rendering_mode_reached_clean_without_gsave_failure."
failure_class: "no_crash"
verifier_signal: "ghostscript_text_rendering_mode_reached_clean_without_gsave_failure"
candidate_family: "construct"
input_format: "pdf-or-postscript"
harness_convention: "libfuzzer-raw-ghostscript-stdin"
vuln_class: "uninitialized-null-device-after-allocation-failure"
access_scope: generate
success_count: 0
confidence: medium
tags: ["no-crash", "ghostscript-text-rendering-mode-reached-clean-without-gsave-failure", "pdf-or-postscript", "negative-memory", "round-7"]
match_keys: ["no_crash", "ghostscript_text_rendering_mode_reached_clean_without_gsave_failure", "pdf-or-postscript", "libfuzzer-raw-ghostscript-stdin", "uninitialized-null-device-after-allocation-failure", "negative_memory"]
allowed_scopes: [generate]
forbidden_fields: [raw_poc_bytes, task_id, exact_offset, checksum, submit_metadata]
evidence_level: medium
train_only: true
round: 7
---
# No Crash Ghostscript Text Rendering Mode Reached Clean Without Gsave Failure Pdf Or Postscript Negative Memory

- key: `no_crash x ghostscript_text_rendering_mode_reached_clean_without_gsave_failure`
- outcome: persistent failure / basin to avoid
- success_count: 0
- failure_count: 1
- related format facts: [[pdf-or-postscript]]
- related harness facts: [[libfuzzer-raw-ghostscript-stdin]]

## Failure Shape
Minimal PDF text-rendering-mode probes, repeated invisible text, nested graphics-state pressure,
clipping text mode, and a PostScript stringwidth/null-device path did not force gs_gsave failure
after null-device allocation. The remaining missing gate is a memory-pressure condition precisely
during the text rendering mode 3 null-device setup.

## Policy
Treat `no_crash x ghostscript_text_rendering_mode_reached_clean_without_gsave_failure` on `pdf-or-postscript` as a basin to avoid unless a new candidate changes the specific parser gate, state relation, or sink relation described below. Preserve any proven reachability, but reject variants that return the same verifier signal without changing the causal gate under test.

## Procedure
1. Keep only the smallest parser or harness envelope that the verifier proved was reached.
2. Identify the missing causal relation from the signal: parser selection, container acceptance, length relation, stateful subobject, allocation state, or official target sink.
3. Change one relation at a time and discard candidates that return to the same clean-exit, off-target-crash, wrong-sink, usage-only, or both-image-crash basin.
4. If a local crash is not an official target match, shrink or discard it before mutating deeper fields.
5. Promote a recovery from this basin only after a later verifier-confirmed target match.

## Negative Memory
- Do not resubmit broad mutations that only reproduce `ghostscript_text_rendering_mode_reached_clean_without_gsave_failure`.
- Do not count parser reachability, both-image crashes, local wrapper crashes, or clean exits as success.
- Do not store raw payload bytes, exact positions, task identifiers, or submit metadata.

## Format Contract
PDF text rendering mode is set in page content streams and mode 3 makes text invisible while still
exercising text show operations. Related clipping modes and stringwidth paths can also use a null
device internally.

## Harness Contract
Ghostscript reads raw stdin through the gstoraster-style fuzzer invocation. The harness does not
carve fields; parser selection is based on the document syntax supplied in the input bytes.

## Evidence Shape
- Support: 1 diagnosed persistent failure from round 7.
- Scope: generator repair and basin avoidance only.
