---
type: causal-policy
title: Gquic Quic Crypto Data Quic Crypto Processed No Target Crash Negative Memory
description: Negative memory for gquic/quic crypto data candidates that ended in no_crash with verifier signal `quic_crypto_processed_no_target_crash`.
failure_class: no_crash
verifier_signal: quic_crypto_processed_no_target_crash
candidate_family: seed_mutate
input_format: gquic/quic crypto data
harness_convention: libfuzzer
vuln_class: stale-plaintext-user-agent-extraction
access_scope: generate
success_count: 0
confidence: medium
tags: [no-crash, quic-crypto-processed-no-target-crash, gquic-quic-crypto-data, libfuzzer, seed-mutate, stale-plaintext-user-agent-extraction, negative-memory]
match_keys: [no-crash, quic-crypto-processed-no-target-crash, gquic-quic-crypto-data, libfuzzer, seed-mutate, stale-plaintext-user-agent-extraction, negative-memory]
allowed_scopes: [generate]
forbidden_fields: [raw_poc_bytes, task_id, exact_offset, checksum, submit_metadata]
evidence_level: medium
train_only: true
---
## Policy
Treat `no_crash with verifier signal `quic_crypto_processed_no_target_crash`` for `gquic/quic crypto data` as evidence that the current carrier reached a clean or wrong harness basin, not the vulnerable invariant. Retarget by preserving only the proven parser gate and changing the missing relation named below.

## Procedure
1. Keep any parser-recognition envelope that reached `quic_crypto_processed_no_target_crash`.
2. Stop repeating the dead-end basin: Valid QUIC crypto-data seeds and appended UAID-like tag material were processed without a crash. The missing condition is likely a coherent legacy GQUIC CHLO tag table where the UAID tag length and offset are internally valid enough to be extracted but semantically invalid for the affected versions.
3. Rebuild around `[[gquic-quic-crypto-data]]` and `[[libfuzzer]]`, then mutate the narrow missing relation instead of adding unrelated padding or broad corruption.
4. Submit only after local verify produces a vulnerable-build crash or a plausible parser-branch wrong-sink crash; clean exits under this signal are not submit candidates.

## Negative Memory
- This is a persistent Round 11 failure basin, not a recovery recipe.
- Do not spend retries on the same carrier shape unless new evidence changes the verifier signal.
- If the harness itself reports usage or setup failure, fix the invocation/carrier contract before mutating vulnerability fields.

## Evidence Shape
- Support: 1 diagnosed Round 11 failed solve attempt.
- Attempts observed: 6.
