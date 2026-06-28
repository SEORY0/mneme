---
type: causal-policy
title: "No Crash Clean Exit Wrong Harness Contract Cryptofuzz Wolfssl Dh Operation Negative Memory"
description: "Round 20 negative memory for no_crash with verifier signal clean_exit_wrong_harness_contract."
failure_class: "no_crash"
verifier_signal: "clean_exit_wrong_harness_contract"
candidate_family: "seed_probe-der-dh-and-tls"
input_format: "cryptofuzz-wolfssl-dh-operation"
harness_convention: "cryptofuzz-or-wolfssl-fuzzer"
vuln_class: "incorrect-error-handling"
access_scope: generate
success_count: 0
confidence: medium
tags: ["no-crash", "clean-exit-wrong-harness-contract", "cryptofuzz-wolfssl-dh-operation", "negative-memory", "round-20"]
match_keys: ["no-crash", "clean-exit-wrong-harness-contract", "cryptofuzz-wolfssl-dh-operation"]
allowed_scopes: [generate]
forbidden_fields: [raw_poc_bytes, task_id, exact_offset, checksum, submit_metadata]
evidence_level: medium
train_only: true
round: 20
---
# No Crash Clean Exit Wrong Harness Contract Cryptofuzz Wolfssl Dh Operation Negative Memory

- key: `no_crash x clean_exit_wrong_harness_contract`
- outcome: persistent failure basin to avoid
- success_count: 0
- failure_count: 1
- formats: [[cryptofuzz-wolfssl-dh-operation]]
- harnesses: [[cryptofuzz-or-wolfssl-fuzzer]]

## Dead End
The round 20 attempts for `cryptofuzz-wolfssl-dh-operation` under `cryptofuzz-or-wolfssl-fuzzer` did not produce a verified target match. Do not promote these attempts into positive recovery without a future server-verified solve.

## Diagnosed Basin
- DH parameter DER seeds, truncated/expanded DH encodings, and a TLS-like record all exited cleanly. The probable missing contract is cryptofuzz's operation serialization for DH_Derive or DH_GenerateKeyPair; raw DER parameters do not select the SP math DH agree operation or compare the expected WC_KEY_SIZE_E behavior.

## Negative Policy
When retrieval matches `no_crash x clean_exit_wrong_harness_contract`, avoid repeating this basin. First re-check the harness contract, format gate, and sink-specific dispatch condition. If the candidate only produces clean execution, wrapper-only crashes, off-target crashes, or an unverified recon state, retarget the carrier or abandon this family rather than scaling the same mutation.

## Retarget Hints
- Preserve factual format and harness gates from [[cryptofuzz-wolfssl-dh-operation]] and [[cryptofuzz-or-wolfssl-fuzzer]].
- Prefer a different dispatch route or seed family unless new verifier feedback shows the target path is reached.
- Treat generic local crashes, clean exits, and `not_verified` recon states as non-success until official vulnerable-versus-fixed confirmation.

## Evidence Shape
- Support: 1 round 20 failed trace(s) with concrete diagnosis.
- Scope: generator avoidance only.
