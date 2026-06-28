---
type: causal-policy
title: "No Crash Local Wrapper False Positive Official Clean Libxml2 Html Fuzzer Input Negative Memory"
description: "Round 20 negative memory for no_crash with verifier signal local_wrapper_false_positive_official_clean."
failure_class: "no_crash"
verifier_signal: "local_wrapper_false_positive_official_clean"
candidate_family: "construct_html_allocator_limit"
input_format: "libxml2 html fuzzer input"
harness_convention: "libfuzzer-libxml2-html with carved options and allocation limit"
vuln_class: "null-deref-or-invalid-access-after-allocation-failure"
access_scope: generate
success_count: 0
confidence: medium
tags: ["no-crash", "local-wrapper-false-positive-official-clean", "libxml2-html-fuzzer-input", "negative-memory", "round-20"]
match_keys: ["no-crash", "local-wrapper-false-positive-official-clean", "libxml2-html-fuzzer-input"]
allowed_scopes: [generate]
forbidden_fields: [raw_poc_bytes, task_id, exact_offset, checksum, submit_metadata]
evidence_level: medium
train_only: true
round: 20
---
# No Crash Local Wrapper False Positive Official Clean Libxml2 Html Fuzzer Input Negative Memory

- key: `no_crash x local_wrapper_false_positive_official_clean`
- outcome: persistent failure basin to avoid
- success_count: 0
- failure_count: 1
- formats: [[libxml2-html-fuzzer-input]]
- harnesses: [[libfuzzer-libxml2-html-with-carved-options-and-allocation-limit]]

## Dead End
The round 20 attempts for `libxml2 html fuzzer input` under `libfuzzer-libxml2-html with carved options and allocation limit` did not produce a verified target match. Do not promote these attempts into positive recovery without a future server-verified solve.

## Diagnosed Basin
- Allocator-limit HTML candidates produced local wrapper segfaults without a stable confirmed target crash; official submission of the smallest local crash returned vulnerable clean. The unresolved trigger is a more precise malloc-failure point inside attribute parsing rather than broad low allocation limits.

## Negative Policy
When retrieval matches `no_crash x local_wrapper_false_positive_official_clean`, avoid repeating this basin. First re-check the harness contract, format gate, and sink-specific dispatch condition. If the candidate only produces clean execution, wrapper-only crashes, off-target crashes, or an unverified recon state, retarget the carrier or abandon this family rather than scaling the same mutation.

## Retarget Hints
- Preserve factual format and harness gates from [[libxml2-html-fuzzer-input]] and [[libfuzzer-libxml2-html-with-carved-options-and-allocation-limit]].
- Prefer a different dispatch route or seed family unless new verifier feedback shows the target path is reached.
- Treat generic local crashes, clean exits, and `not_verified` recon states as non-success until official vulnerable-versus-fixed confirmation.

## Evidence Shape
- Support: 1 round 20 failed trace(s) with concrete diagnosis.
- Scope: generator avoidance only.
