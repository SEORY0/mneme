---
type: causal-policy
title: "Generic Crash Local Wrapper Crash Official Clean Animated Image Negative Memory"
description: "Round 20 negative memory for generic_crash with verifier signal local_wrapper_crash_official_clean."
failure_class: "generic_crash"
verifier_signal: "local_wrapper_crash_official_clean"
candidate_family: "seed_mutate"
input_format: "animated-image"
harness_convention: "libfuzzer"
vuln_class: "uninitialized-memory-read"
access_scope: generate
success_count: 0
confidence: medium
tags: ["generic-crash", "local-wrapper-crash-official-clean", "animated-image", "negative-memory", "round-20"]
match_keys: ["generic-crash", "local-wrapper-crash-official-clean", "animated-image"]
allowed_scopes: [generate]
forbidden_fields: [raw_poc_bytes, task_id, exact_offset, checksum, submit_metadata]
evidence_level: medium
train_only: true
round: 20
---
# Generic Crash Local Wrapper Crash Official Clean Animated Image Negative Memory

- key: `generic_crash x local_wrapper_crash_official_clean`
- outcome: persistent failure basin to avoid
- success_count: 0
- failure_count: 1
- formats: [[animated-image]]
- harnesses: [[libfuzzer]]

## Dead End
The round 20 attempts for `animated-image` under `libfuzzer` did not produce a verified target match. Do not promote these attempts into positive recovery without a future server-verified solve.

## Diagnosed Basin
- Several in-tree animated GIF seeds and invalid-image seeds exercised the animated image decode path. One animated seed produced only a local wrapper crash and did not reproduce on official submit. The missing trigger is likely a specific animated frame metadata state that reaches decodeNextFrame with uninitialized frame data rather than merely being a valid or invalid animated image.

## Negative Policy
When retrieval matches `generic_crash x local_wrapper_crash_official_clean`, avoid repeating this basin. First re-check the harness contract, format gate, and sink-specific dispatch condition. If the candidate only produces clean execution, wrapper-only crashes, off-target crashes, or an unverified recon state, retarget the carrier or abandon this family rather than scaling the same mutation.

## Retarget Hints
- Preserve factual format and harness gates from [[animated-image]] and [[libfuzzer]].
- Prefer a different dispatch route or seed family unless new verifier feedback shows the target path is reached.
- Treat generic local crashes, clean exits, and `not_verified` recon states as non-success until official vulnerable-versus-fixed confirmation.

## Evidence Shape
- Support: 1 round 20 failed trace(s) with concrete diagnosis.
- Scope: generator avoidance only.
