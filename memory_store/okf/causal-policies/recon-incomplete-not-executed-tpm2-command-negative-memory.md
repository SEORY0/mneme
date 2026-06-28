---
type: negative-memory
title: "Recon Incomplete Not Executed Tpm2 Command Negative Memory"
description: "Round 21 negative memory for recon-incomplete with verifier signal not-executed."
failure_class: "recon-incomplete"
verifier_signal: "not-executed"
candidate_family: "recon-only"
input_format: "tpm2-command"
harness_convention: "libfuzzer"
vuln_class: "out-of-bounds-read"
access_scope: generate
success_count: 0
confidence: medium
tags: ["recon-incomplete", "not-executed", "tpm2-command", "libfuzzer", "recon-only", "negative-memory", "round-21"]
match_keys: ["recon-incomplete", "not-executed", "tpm2-command", "libfuzzer", "out-of-bounds-read"]
allowed_scopes: [generate]
forbidden_fields: [raw_poc_bytes, task_id, exact_offset, checksum, submit_metadata]
evidence_level: medium
train_only: true
round: 21
---
# Recon Incomplete Not Executed Tpm2 Command Negative Memory

- key: `recon-incomplete x not-executed`
- outcome: persistent failure / basin to avoid
- success_count: 0
- failure_count: 1
- related format facts: [[tpm2-command]]
- harnesses: [[libfuzzer]]

## Failure Shape
Recon identified the TPM2 fuzzer contract and the RSA prime adjustment sink, but no candidate command was verified within the worker budget. A likely solve needs a valid TPM2 command sequence that reaches RSA key generation with a large enough prime candidate representation to make the bigNum-to-Crypt_Int cast expose more limbs than the fixed-size Crypt_Int array.

## Policy
Treat `recon-incomplete x not-executed` on `tpm2-command` as negative memory for the attempted carrier. Preserve only the reachability that was actually observed, then retarget the missing gate or sink-specific state before spending more verification attempts.

## Procedure
1. Keep any parser or harness envelope that the verifier proved was reached.
2. Identify the missing causal relation from the signal: parser selection, feature gate, length relation, stateful subobject, or official target sink.
3. Change one relation at a time and reject variants that return to this same clean-exit, off-target, usage-only, both-crash, or nonreproducible basin.
4. Promote a recovery from this basin only after a later server-confirmed target match.

## Negative Memory
- Do not resubmit another candidate with this exact failure signal unless it changes the causal gate being tested.
- Do not broaden random mutation after reachability is known; move to the smallest missing format or state contract.
- Do not treat local generic crashes, wrapper usage paths, clean parser exits, fixed-build crashes, or wrong-sink labels as success.
- Never store raw payload bytes, exact offsets, checksums, or task-local identifiers in memory.

## Evidence Shape
- Support: 1 diagnosed persistent failure from round 21.
- Scope: generator repair and basin avoidance only.
