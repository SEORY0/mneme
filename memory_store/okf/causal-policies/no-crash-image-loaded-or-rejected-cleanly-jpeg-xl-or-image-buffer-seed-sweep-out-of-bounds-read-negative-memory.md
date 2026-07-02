---
type: causal-policy
title: "No Crash Image Loaded Or Rejected Cleanly Jpeg Xl Or Image Buffer Seed Sweep Out Of Bounds Read Negative Memory"
description: "Round 30 negative memory for no_crash with verifier signal image_loaded_or_rejected_cleanly."
failure_class: "no_crash"
verifier_signal: "image_loaded_or_rejected_cleanly"
candidate_family: "seed_sweep"
input_format: "jpeg-xl-or-image-buffer"
harness_convention: "libfuzzer-smartcrop"
vuln_class: "out-of-bounds-read"
access_scope: generate
success_count: 0
confidence: medium
tags: ["no-crash", "image-loaded-or-rejected-cleanly", "jpeg-xl-or-image-buffer", "libfuzzer-smartcrop", "seed-sweep", "negative-memory", "round-30"]
match_keys: ["no-crash", "image-loaded-or-rejected-cleanly", "jpeg-xl-or-image-buffer", "libfuzzer-smartcrop", "out-of-bounds-read", "negative-memory"]
allowed_scopes: [generate]
forbidden_fields: [raw_poc_bytes, task_id, exact_offset, checksum, submit_metadata]
evidence_level: medium
train_only: true
round: 30
---
# No Crash Image Loaded Or Rejected Cleanly Jpeg Xl Or Image Buffer Seed Sweep Out Of Bounds Read Negative Memory

- key: `no-crash x image-loaded-or-rejected-cleanly`
- outcome: persistent failure / basin to avoid
- success_count: 0
- formats: [[jpeg-xl-or-image-buffer]]
- harnesses: [[libfuzzer-smartcrop]]

## Failure Shape
The active target was a smartcrop image-buffer harness, not the initially suspected transform fuzzer. Valid PNG, JPEG, ordinary JPEG XL, blending/spline JPEG XL, and minimized decoder corpus seeds executed cleanly. The source-level trigger appears to require a JPEG XL frame with noise enabled so the render pipeline has additional noise input channels; the available corpus did not expose that feature gate and no local encoder was present to create a noise-bearing JPEG XL image.

## Negative Policy
For `no-crash x image-loaded-or-rejected-cleanly` on `jpeg-xl-or-image-buffer`, do not continue broad mutation inside the same basin. The recorded trajectory was `no-crash, no-crash, no-crash, no-crash, no-crash, no-crash, no-crash, no-crash, no-crash, no-crash, no-crash, no-crash` without a verified vulnerable-only target match.

## Avoid
1. Do not submit candidates that only prove parser reachability, clean exit, fixed-image crash, or a coarse local crash.
2. Do not widen mutations across multiple independent metadata families after this signal; first identify the missing gate or state transition.
3. Preserve the useful format and harness facts, but retarget a different causal invariant before spending more attempts.
4. If the verifier signal says the parser or state was not reached, rebuild the carrier/state path before touching sink-specific fields.

## Recovery Direction
Keep the accepted envelope facts from [[jpeg-xl-or-image-buffer]] and [[libfuzzer-smartcrop]], then search for the smallest missing gate named by the diagnosis instead of repeating the failed candidate family.

## Evidence Shape
- Support: diagnosed round 30 failure.
- Scope: generator repair only; no success-rate credit.
