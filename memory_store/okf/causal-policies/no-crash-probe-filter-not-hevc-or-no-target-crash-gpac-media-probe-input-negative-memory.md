---
type: causal-policy
title: "No Crash Probe Filter Not Hevc Or No Target Crash Gpac Media Probe Input Negative Memory"
description: "Round 12 negative memory for no_crash with verifier signal probe_filter_not_hevc_or_no_target_crash."
failure_class: "no_crash"
verifier_signal: "probe_filter_not_hevc_or_no_target_crash"
candidate_family: "seed_mutate+construct"
input_format: "gpac media probe input"
harness_convention: "libfuzzer"
vuln_class: "stack-buffer-overflow-or-bounds"
access_scope: generate
success_count: 0
confidence: medium
tags: ["no-crash", "probe-filter-not-hevc-or-no-target-crash", "gpac-media-probe-input", "negative-memory", "round-12"]
match_keys: ["no_crash", "probe_filter_not_hevc_or_no_target_crash", "gpac-media-probe-input", "libfuzzer", "stack-buffer-overflow-or-bounds", "negative_memory"]
allowed_scopes: [generate]
forbidden_fields: [raw_poc_bytes, task_id, exact_offset, checksum, submit_metadata]
evidence_level: medium
train_only: true
round: 12
---
# No Crash Probe Filter Not Hevc Or No Target Crash Gpac Media Probe Input Negative Memory

- key: `no_crash x probe_filter_not_hevc_or_no_target_crash`
- outcome: persistent failure / basin to avoid
- success_count: 0
- failure_count: 1
- related format facts: [[gpac-media-probe-input]]
- related harness facts: [[libfuzzer]]

## Failure Shape
The actual target is GPAC probe/analyze, which expects a media file that can be routed through GPAC filters. Raw Annex-B-like HEVC NAL bytes and a VPS-like elementary stream did not select a compatible filter, while an in-repo MP4 sample and a small SVG were probed as non-HEVC media. No candidate reached HEVC slice reference-list computation.

## Policy
Treat `no_crash x probe_filter_not_hevc_or_no_target_crash` on `gpac-media-probe-input` as a basin to avoid unless a new candidate changes the parser gate, state relation, or official target sink. Preserve any proven reachability, but reject variants that return to the same verifier signal without changing the causal gate under test.

## Procedure
1. Keep only the smallest parser or harness envelope that the verifier proved was reached.
2. Identify the missing causal relation from the signal: parser selection, container acceptance, length relation, stateful subobject, allocation state, or official target sink.
3. Change one relation at a time and discard candidates that return to the same clean-exit, off-target-crash, wrong-sink, usage-only, or both-image-crash basin.
4. If a local crash is not an official target match, shrink or discard it before mutating deeper fields.
5. Promote a recovery from this basin only after a later verifier-confirmed target match.

## Format Contract
The vulnerable function is reached after HEVC VPS/SPS/PPS and an inter slice have been parsed into HEVCState. The risky data are short-term reference-picture-set counts and used flags, which drive fixed-size reference list construction. A plain elementary NAL is insufficient unless the harness recognizes it as HEVC media and parses the required parameter sets and slice header.

## Harness Contract
The target binary is fuzz_probe_analyze. It runs GPAC file probing and inspection on the raw input as a media asset; successful probes emit XML inspection records. Inputs that do not map to a known media filter fail before HEVC parsing.

## Negative Memory
- Do not resubmit broad mutations that only reproduce `probe_filter_not_hevc_or_no_target_crash`.
- Do not count parser reachability, both-image crashes, local wrapper crashes, clean exits, or fixed-image crashes as success.
- Do not store raw payload bytes, exact positions, task identifiers, or submit metadata.

## Evidence Shape
- Support: one diagnosed persistent failure from round 12.
- Scope: generator repair and basin avoidance only.
