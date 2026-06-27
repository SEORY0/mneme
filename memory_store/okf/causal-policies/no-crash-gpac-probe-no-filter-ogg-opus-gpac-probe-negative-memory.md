---
type: causal-policy
title: "No Crash Gpac Probe No Filter Ogg Opus Gpac Probe Negative Memory"
description: "Round 10 negative memory for no_crash with verifier signal gpac_probe_no_filter."
failure_class: "no_crash"
verifier_signal: "gpac_probe_no_filter"
candidate_family: "construct"
input_format: "ogg-opus-or-gpac-probe-input"
harness_convention: "libfuzzer"
vuln_class: "out-of-bounds-read"
access_scope: generate
success_count: 0
confidence: medium
tags: ["no-crash", "gpac-probe-no-filter", "negative-memory", "round-10"]
match_keys: ["no_crash", "gpac_probe_no_filter", "ogg-opus-or-gpac-probe-input", "libfuzzer", "negative_memory"]
allowed_scopes: [generate]
forbidden_fields: [raw_poc_bytes, task_id, exact_offset, checksum, submit_metadata]
evidence_level: medium
train_only: true
round: 10
---
# No Crash Gpac Probe No Filter Ogg Opus Gpac Probe Negative Memory

## Policy
For `no_crash x gpac_probe_no_filter`, avoid replaying the observed dead end. This negative memory is co-equal with positive policies and should redirect generation before another official submission.

## Procedure
1. Bare Opus header bytes and minimal Ogg pages reached the GPAC probe/analyze wrapper but did not route into the Opus header parser.
2. When `no_crash x gpac_probe_no_filter` appears for `ogg-opus-or-gpac-probe-input`, treat this candidate family as a basin-to-avoid rather than as evidence of proximity to the target.
3. Keep any proven parser/harness envelope, but change the missing gate or state relation before submitting again.

## Format Contract
- The vulnerable parser expects an Opus identification header beginning with an OpusHead tag and then fixed fields such as version, channel count, preskip, sample rate, gain, mapping family, and optional mapping data. Through GPAC probe/analyze, those bytes likely need an accepted Ogg or media-container envelope.
- Harness: The active binary was GPAC fuzz_probe_analyze. It writes or treats the raw bytes as a probed media input; there is no mode byte. Failed candidates produced an empty inspection document or a filter setup failure rather than a direct parser call.

## Negative Memory
- Do not treat this verifier signal as a near miss unless a later candidate changes the missing gate or state relation.
- Do not submit candidates that are clean, parser-mismatched, off-target, or crashing both fixed and vulnerable images in this same shape.
- Preserve only descriptive format facts from the failed attempt; do not promote an unverified causal recovery.

## Evidence Shape
- Support: one diagnosed round-10 persistent failure.
- Scope: generator avoidance for the same failure-keyed basin.
