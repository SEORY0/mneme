---
type: causal-policy
title: "Generic Crash Local Wrapper Crash Official Clean Jbig2 Negative Memory"
description: "Round 20 negative memory for generic_crash with verifier signal local_wrapper_crash_official_clean."
failure_class: "generic_crash"
verifier_signal: "local_wrapper_crash_official_clean"
candidate_family: "seed_mutate"
input_format: "jbig2"
harness_convention: "libfuzzer"
vuln_class: "buffer-overflow-read"
access_scope: generate
success_count: 0
confidence: medium
tags: ["generic-crash", "local-wrapper-crash-official-clean", "jbig2", "negative-memory", "round-20"]
match_keys: ["generic-crash", "local-wrapper-crash-official-clean", "jbig2"]
allowed_scopes: [generate]
forbidden_fields: [raw_poc_bytes, task_id, exact_offset, checksum, submit_metadata]
evidence_level: medium
train_only: true
round: 20
---
# Generic Crash Local Wrapper Crash Official Clean Jbig2 Negative Memory

- key: `generic_crash x local_wrapper_crash_official_clean`
- outcome: persistent failure basin to avoid
- success_count: 0
- failure_count: 1
- formats: [[jbig2]]
- harnesses: [[libfuzzer]]

## Dead End
The round 20 attempts for `jbig2` under `libfuzzer` did not produce a verified target match. Do not promote these attempts into positive recovery without a future server-verified solve.

## Diagnosed Basin
- A valid in-tree JBIG2 stream and several structural mutations exercised the decoder but did not reproduce the target MMR consumed-byte underflow. One tail mutation produced only a local wrapper crash and the official server ran it cleanly, so it was not the target bug. The missing condition appears to be an immediate MMR-coded generic or halftone region whose coded data accounting underflows while still leaving the segment structurally accepted.

## Negative Policy
When retrieval matches `generic_crash x local_wrapper_crash_official_clean`, avoid repeating this basin. First re-check the harness contract, format gate, and sink-specific dispatch condition. If the candidate only produces clean execution, wrapper-only crashes, off-target crashes, or an unverified recon state, retarget the carrier or abandon this family rather than scaling the same mutation.

## Retarget Hints
- Preserve factual format and harness gates from [[jbig2]] and [[libfuzzer]].
- Prefer a different dispatch route or seed family unless new verifier feedback shows the target path is reached.
- Treat generic local crashes, clean exits, and `not_verified` recon states as non-success until official vulnerable-versus-fixed confirmation.

## Evidence Shape
- Support: 1 round 20 failed trace(s) with concrete diagnosis.
- Scope: generator avoidance only.
