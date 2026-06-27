---
type: causal-policy
title: "Generic Crash Generic Local Crash Not Reproduced By Submit Jpeg Xl Codestream Negative Memory"
description: "Round 10 negative memory for generic_crash with verifier signal generic_local_crash_not_reproduced_by_submit."
failure_class: "generic_crash"
verifier_signal: "generic_local_crash_not_reproduced_by_submit"
candidate_family: "seed_mutate"
input_format: "jpeg-xl-codestream"
harness_convention: "libfuzzer"
vuln_class: "out-of-bounds-write"
access_scope: generate
success_count: 0
confidence: medium
tags: ["generic-crash", "generic-local-crash-not-reproduced-by-submit", "negative-memory", "round-10"]
match_keys: ["generic_crash", "generic_local_crash_not_reproduced_by_submit", "jpeg-xl-codestream", "libfuzzer", "negative_memory"]
allowed_scopes: [generate]
forbidden_fields: [raw_poc_bytes, task_id, exact_offset, checksum, submit_metadata]
evidence_level: medium
train_only: true
round: 10
---
# Generic Crash Generic Local Crash Not Reproduced By Submit Jpeg Xl Codestream Negative Memory

## Policy
For `generic_crash x generic_local_crash_not_reproduced_by_submit`, avoid replaying the observed dead end. This negative memory is co-equal with positive policies and should redirect generation before another official submission.

## Procedure
1. A real JPEG XL seed plus decoder option suffixes sometimes produced local segmentation faults, but official submission of the crashing family did not reproduce a vulnerable-only exit.
2. When `generic_crash x generic_local_crash_not_reproduced_by_submit` appears for `jpeg-xl-codestream`, treat this candidate family as a basin-to-avoid rather than as evidence of proximity to the target.
3. Keep any proven parser/harness envelope, but change the missing gate or state relation before submitting again.

## Format Contract
- The selected decoder target expects a JPEG XL codestream followed by a compact option suffix. The suffix controls alpha/grayscale output, streaming, JPEG reconstruction, callback output, orientation preservation, output type, endianness, alignment, and CPU target selection.
- Harness: Raw libFuzzer bytes are split by the target: most bytes are passed to the JPEG XL decoder and the final option word is consumed by the harness. A valid seed reaches basic-info, frame, image-output, and full-image decoder events; changing suffix bits alters the output-buffer path.

## Negative Memory
- Do not treat this verifier signal as a near miss unless a later candidate changes the missing gate or state relation.
- Do not submit candidates that are clean, parser-mismatched, off-target, or crashing both fixed and vulnerable images in this same shape.
- Preserve only descriptive format facts from the failed attempt; do not promote an unverified causal recovery.

## Evidence Shape
- Support: one diagnosed round-10 persistent failure.
- Scope: generator avoidance for the same failure-keyed basin.
