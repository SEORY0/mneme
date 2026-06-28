---
type: causal-policy
title: Wolfssl Crypto Or Tls Byte Stream Clean Exit Negative Memory
description: Negative memory for wolfssl-crypto-or-tls-byte-stream candidates that ended in no_crash with verifier signal `clean_exit`.
failure_class: no_crash
verifier_signal: clean_exit
candidate_family: construct
input_format: wolfssl-crypto-or-tls-byte-stream
harness_convention: unknown-native-fuzzer
vuln_class: integer-overflow-or-constant-time-copy-width
access_scope: generate
success_count: 0
confidence: medium
tags: [no-crash, clean-exit, wolfssl-crypto-or-tls-byte-stream, unknown-native-fuzzer, construct, integer-overflow-or-constant-time-copy-width, negative-memory]
match_keys: [no-crash, clean-exit, wolfssl-crypto-or-tls-byte-stream, unknown-native-fuzzer, construct, integer-overflow-or-constant-time-copy-width, negative-memory]
allowed_scopes: [generate]
forbidden_fields: [raw_poc_bytes, task_id, exact_offset, checksum, submit_metadata]
evidence_level: medium
train_only: true
---
## Policy
Treat `no_crash with verifier signal `clean_exit`` for `wolfssl-crypto-or-tls-byte-stream` as evidence that the current carrier reached a clean or wrong harness basin, not the vulnerable invariant. Retarget by preserving only the proven parser gate and changing the missing relation named below.

## Procedure
1. Keep any parser-recognition envelope that reached `clean_exit`.
2. Stop repeating the dead-end basin: TLS-like records, large integer-shaped blobs, and ASN.1 integer probes did not reach the mp_cond_copy path with a large enough multi-precision operand. The active harness was not discoverable in source by a direct LLVMFuzzerTestOneInput search.
3. Rebuild around `[[wolfssl-crypto-or-tls-byte-stream]]` and `[[unknown-native-fuzzer]]`, then mutate the narrow missing relation instead of adding unrelated padding or broad corruption.
4. Submit only after local verify produces a vulnerable-build crash or a plausible parser-branch wrong-sink crash; clean exits under this signal are not submit candidates.

## Negative Memory
- This is a persistent Round 11 failure basin, not a recovery recipe.
- Do not spend retries on the same carrier shape unless new evidence changes the verifier signal.
- If the harness itself reports usage or setup failure, fix the invocation/carrier contract before mutating vulnerability fields.

## Evidence Shape
- Support: 1 diagnosed Round 11 failed solve attempt.
- Attempts observed: 5.
