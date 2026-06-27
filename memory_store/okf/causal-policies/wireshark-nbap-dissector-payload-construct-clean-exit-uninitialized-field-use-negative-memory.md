---
type: causal-policy
title: Wireshark Nbap Dissector Payload Clean Exit Negative Memory
description: Negative memory for wireshark-nbap-dissector-payload candidates that ended in no_crash with verifier signal `clean_exit`.
failure_class: no_crash
verifier_signal: clean_exit
candidate_family: construct
input_format: wireshark-nbap-dissector-payload
harness_convention: libfuzzer
vuln_class: uninitialized-field-use
access_scope: generate
success_count: 0
confidence: medium
tags: [no-crash, clean-exit, wireshark-nbap-dissector-payload, libfuzzer, construct, uninitialized-field-use, negative-memory]
match_keys: [no-crash, clean-exit, wireshark-nbap-dissector-payload, libfuzzer, construct, uninitialized-field-use, negative-memory]
allowed_scopes: [generate]
forbidden_fields: [raw_poc_bytes, task_id, exact_offset, checksum, submit_metadata]
evidence_level: medium
train_only: true
---
## Policy
Treat `no_crash with verifier signal `clean_exit`` for `wireshark-nbap-dissector-payload` as evidence that the current carrier reached a clean or wrong harness basin, not the vulnerable invariant. Retarget by preserving only the proven parser gate and changing the missing relation named below.

## Procedure
1. Keep any parser-recognition envelope that reached `clean_exit`.
2. Stop repeating the dead-end basin: ASN.1/PER-shaped NBAP payload probes and DCH-heavy byte streams exited cleanly. The missing condition is a valid NBAP message path where DCH ID is referenced before initialization, not just arbitrary DCH-like fields.
3. Rebuild around `[[wireshark-nbap-dissector-payload]]` and `[[libfuzzer]]`, then mutate the narrow missing relation instead of adding unrelated padding or broad corruption.
4. Submit only after local verify produces a vulnerable-build crash or a plausible parser-branch wrong-sink crash; clean exits under this signal are not submit candidates.

## Negative Memory
- This is a persistent Round 11 failure basin, not a recovery recipe.
- Do not spend retries on the same carrier shape unless new evidence changes the verifier signal.
- If the harness itself reports usage or setup failure, fix the invocation/carrier contract before mutating vulnerability fields.

## Evidence Shape
- Support: 1 diagnosed Round 11 failed solve attempt.
- Attempts observed: 5.
