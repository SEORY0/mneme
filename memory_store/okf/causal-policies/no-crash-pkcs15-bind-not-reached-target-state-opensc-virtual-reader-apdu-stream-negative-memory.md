---
type: causal-policy
title: "No Crash Pkcs15 Bind Not Reached Target State Opensc Virtual Reader Apdu Stream Negative Memory"
description: "Round 20 negative memory for no_crash with verifier signal pkcs15_bind_not_reached_target_state."
failure_class: "no_crash"
verifier_signal: "pkcs15_bind_not_reached_target_state"
candidate_family: "construct"
input_format: "opensc-virtual-reader-apdu-stream"
harness_convention: "libfuzzer"
vuln_class: "unchecked-return-value-or-null-state"
access_scope: generate
success_count: 0
confidence: medium
tags: ["no-crash", "pkcs15-bind-not-reached-target-state", "opensc-virtual-reader-apdu-stream", "negative-memory", "round-20"]
match_keys: ["no-crash", "pkcs15-bind-not-reached-target-state", "opensc-virtual-reader-apdu-stream"]
allowed_scopes: [generate]
forbidden_fields: [raw_poc_bytes, task_id, exact_offset, checksum, submit_metadata]
evidence_level: medium
train_only: true
round: 20
---
# No Crash Pkcs15 Bind Not Reached Target State Opensc Virtual Reader Apdu Stream Negative Memory

- key: `no_crash x pkcs15_bind_not_reached_target_state`
- outcome: persistent failure basin to avoid
- success_count: 0
- failure_count: 1
- formats: [[opensc-virtual-reader-apdu-stream]]
- harnesses: [[libfuzzer]]

## Dead End
The round 20 attempts for `opensc-virtual-reader-apdu-stream` under `libfuzzer` did not produce a verified target match. Do not promote these attempts into positive recovery without a future server-verified solve.

## Diagnosed Basin
- The virtual reader contract was identified, but no Oberthur-specific ATR/APDU transcript was recovered during the worker budget. Generic chunk streams are unlikely to bind the PKCS#15 card profile and therefore do not reach the vulnerable state transition.

## Negative Policy
When retrieval matches `no_crash x pkcs15_bind_not_reached_target_state`, avoid repeating this basin. First re-check the harness contract, format gate, and sink-specific dispatch condition. If the candidate only produces clean execution, wrapper-only crashes, off-target crashes, or an unverified recon state, retarget the carrier or abandon this family rather than scaling the same mutation.

## Retarget Hints
- Preserve factual format and harness gates from [[opensc-virtual-reader-apdu-stream]] and [[libfuzzer]].
- Prefer a different dispatch route or seed family unless new verifier feedback shows the target path is reached.
- Treat generic local crashes, clean exits, and `not_verified` recon states as non-success until official vulnerable-versus-fixed confirmation.

## Evidence Shape
- Support: 1 round 20 failed trace(s) with concrete diagnosis.
- Scope: generator avoidance only.
