---
type: causal-policy
title: "Generic Crash Off Target Generic Crash Official Clean Samba Ndr Spoolss Fuzzer Blob Negative Memory"
description: "Round 20 negative memory for generic_crash with verifier signal off_target_generic_crash_official_clean."
failure_class: "generic_crash"
verifier_signal: "off_target_generic_crash_official_clean"
candidate_family: "construct"
input_format: "samba-ndr-spoolss-fuzzer-blob"
harness_convention: "libfuzzer-fuzz_ndr_spoolss_TYPE_STRUCT"
vuln_class: "string-length-validation"
access_scope: generate
success_count: 0
confidence: medium
tags: ["generic-crash", "off-target-generic-crash-official-clean", "samba-ndr-spoolss-fuzzer-blob", "negative-memory", "round-20"]
match_keys: ["generic-crash", "off-target-generic-crash-official-clean", "samba-ndr-spoolss-fuzzer-blob"]
allowed_scopes: [generate]
forbidden_fields: [raw_poc_bytes, task_id, exact_offset, checksum, submit_metadata]
evidence_level: medium
train_only: true
round: 20
---
# Generic Crash Off Target Generic Crash Official Clean Samba Ndr Spoolss Fuzzer Blob Negative Memory

- key: `generic_crash x off_target_generic_crash_official_clean`
- outcome: persistent failure basin to avoid
- success_count: 0
- failure_count: 1
- formats: [[samba-ndr-spoolss-fuzzer-blob]]
- harnesses: [[libfuzzer-fuzz-ndr-spoolss-type-struct]]

## Dead End
The round 20 attempts for `samba-ndr-spoolss-fuzzer-blob` under `libfuzzer-fuzz_ndr_spoolss_TYPE_STRUCT` did not produce a verified target match. Do not promote these attempts into positive recovery without a future server-verified solve.

## Diagnosed Basin
- A large declared string extent produced a local generic process crash, but confirmation and official submission did not match the target and the server reported no vulnerable-side crash. The generated blob likely did not satisfy the specific spoolss structure nesting needed for ndr_pull_charset_to_null to receive a short backing buffer with an oversized character length.

## Negative Policy
When retrieval matches `generic_crash x off_target_generic_crash_official_clean`, avoid repeating this basin. First re-check the harness contract, format gate, and sink-specific dispatch condition. If the candidate only produces clean execution, wrapper-only crashes, off-target crashes, or an unverified recon state, retarget the carrier or abandon this family rather than scaling the same mutation.

## Retarget Hints
- Preserve factual format and harness gates from [[samba-ndr-spoolss-fuzzer-blob]] and [[libfuzzer-fuzz-ndr-spoolss-type-struct]].
- Prefer a different dispatch route or seed family unless new verifier feedback shows the target path is reached.
- Treat generic local crashes, clean exits, and `not_verified` recon states as non-success until official vulnerable-versus-fixed confirmation.

## Evidence Shape
- Support: 1 round 20 failed trace(s) with concrete diagnosis.
- Scope: generator avoidance only.
