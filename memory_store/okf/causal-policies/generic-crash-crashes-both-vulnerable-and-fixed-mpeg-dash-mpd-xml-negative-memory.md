---
type: causal-policy
title: "Generic Crash Crashes Both Vulnerable And Fixed Mpeg Dash Mpd XML Negative Memory"
description: "Round 10 negative memory for generic_crash with verifier signal crashes_both_vulnerable_and_fixed."
failure_class: "generic_crash"
verifier_signal: "crashes_both_vulnerable_and_fixed"
candidate_family: "construct"
input_format: "MPEG-DASH MPD XML"
harness_convention: "oss-fuzz probe/analyze wrapper"
vuln_class: "memory corruption in DASH string handling"
access_scope: generate
success_count: 0
confidence: medium
tags: ["generic-crash", "crashes-both-vulnerable-and-fixed", "negative-memory", "round-10"]
match_keys: ["generic_crash", "crashes_both_vulnerable_and_fixed", "MPEG-DASH MPD XML", "oss-fuzz probe/analyze wrapper", "negative_memory"]
allowed_scopes: [generate]
forbidden_fields: [raw_poc_bytes, task_id, exact_offset, checksum, submit_metadata]
evidence_level: medium
train_only: true
round: 10
---
# Generic Crash Crashes Both Vulnerable And Fixed Mpeg Dash Mpd XML Negative Memory

## Policy
For `generic_crash x crashes_both_vulnerable_and_fixed`, avoid replaying the observed dead end. This negative memory is co-equal with positive policies and should redirect generation before another official submission.

## Procedure
1. Long BaseURL, SegmentTemplate, SegmentBase, and dynamic/static MPD variants reached GPAC inspection and one candidate crashed both vulnerable and fixed builds.
2. When `generic_crash x crashes_both_vulnerable_and_fixed` appears for `MPEG-DASH MPD XML`, treat this candidate family as a basin-to-avoid rather than as evidence of proximity to the target.
3. Keep any proven parser/harness envelope, but change the missing gate or state relation before submitting again.

## Format Contract
- MPD is XML with MPD, Period, AdaptationSet, Representation, and segment description elements. DASH URL fields can be supplied through BaseURL, SegmentTemplate attributes, SegmentList entries, or SegmentBase initialization data.
- Harness: The harness passes raw XML-like file bytes to GPAC probe/analyze. No custom byte carving is visible; parser reachability depends on forming enough MPD structure for a selectable representation or segment description.

## Negative Memory
- Do not treat this verifier signal as a near miss unless a later candidate changes the missing gate or state relation.
- Do not submit candidates that are clean, parser-mismatched, off-target, or crashing both fixed and vulnerable images in this same shape.
- Preserve only descriptive format facts from the failed attempt; do not promote an unverified causal recovery.

## Evidence Shape
- Support: one diagnosed round-10 persistent failure.
- Scope: generator avoidance for the same failure-keyed basin.
