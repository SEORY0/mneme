---
type: causal-policy
title: Wrong Sink Sink Mismatch Fixed Image Also Crashed Negative Memory
description: Negative memory for wrong_sink with verifier signal sink_mismatch_fixed_image_also_crashed.
failure_class: wrong_sink
verifier_signal: sink_mismatch_fixed_image_also_crashed
candidate_family: construct
input_format: any
harness_convention: any
access_scope: generate
success_count: 0
confidence: medium
tags: [wrong-sink, sink-mismatch-fixed-image-also-crashed, negative_memory]
match_keys: [wrong-sink, sink-mismatch-fixed-image-also-crashed, negative_memory]
allowed_scopes: [generate]
forbidden_fields: [raw_poc_bytes, task_id, exact_offset, checksum, submit_metadata]
evidence_level: medium
train_only: true
---
# Wrong Sink Sink Mismatch Fixed Image Also Crashed Negative Memory

- key: `wrong_sink x sink_mismatch_fixed_image_also_crashed`
- outcome: persistent failure basin
- support_count: 1
- candidate_families: construct
- observed_formats: json-dwg

## Policy
Treat this verifier signal as negative memory for the attempted candidate family. Preserve any parser reachability it proved, but do not keep mutating the same field basin unless the next verification changes the signal.

## Procedure
Quarantine the crashing basin. Shrink or discard the off-target crash and retarget the described sink; never submit a candidate that also fails on the fixed image.

## Diagnosed Dead Ends
- A JSON DWG header with an overlong layer-colors array reliably reached injson and produced a header-array write crash, but official submission showed the fixed image still failed, so this is an adjacent non-solving crash. The target likely requires the parser to confuse a JSON array's parsed element type with the real header field width without simply exceeding the fixed element count.

## Negative Memory
Do not repeat the same carrier plus broad mutation after this signal. Do not promote the diagnosis into a recovery until a later verifier-confirmed candidate flips the official gate.
