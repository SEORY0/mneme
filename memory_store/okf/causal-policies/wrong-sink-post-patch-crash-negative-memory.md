---
type: causal-policy
title: Wrong Sink Post Patch Crash Negative Memory
description: Negative memory for wrong_sink with verifier signal post_patch_crash.
failure_class: wrong_sink
verifier_signal: post_patch_crash
candidate_family: seed-sweep
input_format: any
harness_convention: any
access_scope: generate
success_count: 0
confidence: medium
tags: [wrong-sink, post-patch-crash, negative_memory]
match_keys: [wrong-sink, post-patch-crash, negative_memory]
allowed_scopes: [generate]
forbidden_fields: [raw_poc_bytes, task_id, exact_offset, checksum, submit_metadata]
evidence_level: medium
train_only: true
---
# Wrong Sink Post Patch Crash Negative Memory

- key: `wrong_sink x post_patch_crash`
- outcome: persistent failure basin
- support_count: 1
- candidate_families: seed-sweep
- observed_formats: aac-usac-mps

## Policy
Treat this verifier signal as negative memory for the attempted candidate family. Preserve any parser reachability it proved, but do not keep mutating the same field basin unless the next verification changes the signal.

## Procedure
Quarantine the crashing basin. Shrink or discard the off-target crash and retarget the described sink; never submit a candidate that also fails on the fixed image.

## Diagnosed Dead Ends
- Several bundled xAAC/MPS seeds reached deep decoder paths and produced UBSan signals, but the clearest crashing seed reproduced on the fixed image and was in an unrelated transform helper rather than ixheaacd_calc_m1m2_7272. The target path likely needs an MPS configuration that selects the 7272 tree and propagates an earlier parse error into invalid parameter-band or channel state without first hitting the decoder's other undefined-behavior sites.

## Negative Memory
Do not repeat the same carrier plus broad mutation after this signal. Do not promote the diagnosis into a recovery until a later verifier-confirmed candidate flips the official gate.
