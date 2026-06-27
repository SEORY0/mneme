---
type: causal-policy
title: "Generic Crash Local Crash Official Clean Zip Negative Memory"
description: "Round 20 negative memory for generic_crash with verifier signal local_crash_official_clean."
failure_class: "generic_crash"
verifier_signal: "local_crash_official_clean"
candidate_family: "construct"
input_format: "zip"
harness_convention: "libfuzzer-miniz-zip_fuzzer"
vuln_class: "zip-parser-resource-or-buffer-boundary"
access_scope: generate
success_count: 0
confidence: medium
tags: ["generic-crash", "local-crash-official-clean", "zip", "negative-memory", "round-20"]
match_keys: ["generic-crash", "local-crash-official-clean", "zip"]
allowed_scopes: [generate]
forbidden_fields: [raw_poc_bytes, task_id, exact_offset, checksum, submit_metadata]
evidence_level: medium
train_only: true
round: 20
---
# Generic Crash Local Crash Official Clean Zip Negative Memory

- key: `generic_crash x local_crash_official_clean`
- outcome: persistent failure basin to avoid
- success_count: 0
- failure_count: 1
- formats: [[zip]]
- harnesses: [[libfuzzer-miniz-zip-fuzzer]]

## Dead End
The round 20 attempts for `zip` under `libfuzzer-miniz-zip_fuzzer` did not produce a verified target match. Do not promote these attempts into positive recovery without a future server-verified solve.

## Diagnosed Basin
- ZIP structures with many central-directory entries and large deflated expansion either stayed clean or produced a local generic decompression/resource crash that did not reproduce officially. This remained an off-target resource basin rather than the described miniz invariant.

## Negative Policy
When retrieval matches `generic_crash x local_crash_official_clean`, avoid repeating this basin. First re-check the harness contract, format gate, and sink-specific dispatch condition. If the candidate only produces clean execution, wrapper-only crashes, off-target crashes, or an unverified recon state, retarget the carrier or abandon this family rather than scaling the same mutation.

## Retarget Hints
- Preserve factual format and harness gates from [[zip]] and [[libfuzzer-miniz-zip-fuzzer]].
- Prefer a different dispatch route or seed family unless new verifier feedback shows the target path is reached.
- Treat generic local crashes, clean exits, and `not_verified` recon states as non-success until official vulnerable-versus-fixed confirmation.

## Evidence Shape
- Support: 1 round 20 failed trace(s) with concrete diagnosis.
- Scope: generator avoidance only.
