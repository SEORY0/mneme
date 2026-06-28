---
type: causal-policy
title: "No Crash Jp2 Container Accepted Without Sanitizer Signal Jp2 Construct Out Of Bounds Read Negative Memory"
description: "Round 14 negative memory for no_crash with verifier signal jp2_container_accepted_without_sanitizer_signal."
failure_class: "no_crash"
verifier_signal: "jp2_container_accepted_without_sanitizer_signal"
candidate_family: "construct"
input_format: "jp2"
harness_convention: "libfuzzer"
vuln_class: "out-of-bounds-read"
access_scope: generate
success_count: 0
confidence: medium
tags: ["no-crash", "jp2-container-accepted-without-sanitizer-signal", "jp2", "negative-memory", "round-14"]
match_keys: ["no_crash", "jp2_container_accepted_without_sanitizer_signal", "jp2", "libfuzzer", "out-of-bounds-read", "negative_memory"]
allowed_scopes: [generate]
forbidden_fields: [raw_poc_bytes, task_id, exact_offset, checksum, submit_metadata]
evidence_level: medium
train_only: true
round: 14
---
# No Crash Jp2 Container Accepted Without Sanitizer Signal Jp2 Construct Out Of Bounds Read Negative Memory

- key: `no_crash x jp2_container_accepted_without_sanitizer_signal`
- outcome: persistent failure / basin to avoid
- success_count: 0
- failure_count: 1
- related format facts: [[jp2]]
- related harness facts: [[libfuzzer]]

## Failure Shape
JP2 signature and file-type boxes with undersized, empty, minimal-valid, and valid-length bodies all exited cleanly. The vulnerable helper's unsigned size relation was reached by construction, but the surrounding allocation/read behavior did not produce a sanitizer-visible out-of-bounds read in these attempts.

## Policy
Treat `no_crash x jp2_container_accepted_without_sanitizer_signal` on `jp2` as a basin to avoid unless a new candidate changes the parser gate, state relation, or official target sink. Preserve any proven reachability, but reject variants that return to the same verifier signal without changing the causal gate under test.

## Procedure
1. Keep only the smallest carrier that the verifier proved reaches the parser, decoder, or harness path.
2. Identify the missing causal relation from the signal: parser selection, container acceptance, length relation, stateful subobject, allocation state, or official target sink.
3. Change one relation at a time and discard candidates that return to the same clean-exit, off-target-crash, wrong-sink, usage-only, parser-not-reached, or both-image-crash basin.
4. If a local crash is not an official target match, shrink or discard it before mutating deeper fields.
5. Promote a recovery from this basin only after a later verifier-confirmed target match.

## Negative Memory
- Do not count parser reachability, local crashes, clean exits, fixed-image crashes, usage banners, or sink mismatches as success.
- Do not repeat this candidate family unless the new attempt changes the causal gate named above.
- Do not store concrete payload bytes, task identifiers, exact positions, checksums, or submit metadata.

## Evidence Shape
- Support: one diagnosed persistent failure from Round 14.
- Scope: generator repair and basin avoidance only.
