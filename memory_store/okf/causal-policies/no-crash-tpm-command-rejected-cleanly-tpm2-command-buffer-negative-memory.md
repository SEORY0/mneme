---
type: causal-policy
title: "No Crash Tpm Command Rejected Cleanly Tpm2 Command Buffer Negative Memory"
description: "Round 17 negative memory for no_crash with verifier signal tpm_command_rejected_cleanly."
failure_class: "no_crash"
verifier_signal: "tpm_command_rejected_cleanly"
candidate_family: "construct"
input_format: "tpm2 command buffer"
harness_convention: "libfuzzer libtpms process command"
vuln_class: "out-of-bounds-read"
access_scope: generate
success_count: 0
confidence: medium
tags: ["no-crash", "tpm-command-rejected-cleanly", "tpm2-command-buffer", "libfuzzer-libtpms-process-command", "negative-memory", "round-17"]
match_keys: ["no-crash", "tpm-command-rejected-cleanly", "tpm2-command-buffer", "libfuzzer-libtpms-process-command", "out-of-bounds-read", "negative-memory"]
allowed_scopes: [generate]
forbidden_fields: [raw_poc_bytes, task_id, exact_offset, checksum, submit_metadata]
evidence_level: medium
train_only: true
round: 17
---
# No Crash Tpm Command Rejected Cleanly Tpm2 Command Buffer Negative Memory

- key: `no_crash x tpm_command_rejected_cleanly`
- outcome: persistent failure / basin to avoid
- success_count: 0
- failure_count: 1
- related format facts: [[tpm2-command-buffer]]
- related harness facts: [[libfuzzer-libtpms-process-command]]

## Failure Shape
- Raw TPM2 command buffers with below-range, near-gap, vendor-space, very large, and malformed valid command codes were rejected cleanly after TPM startup.
- The missing gate is likely a debug or runtime-command path that indexes command attributes before the normal unimplemented-command bounds check.

## Policy
Treat `no_crash x tpm_command_rejected_cleanly` on `tpm2 command buffer` as a basin to avoid unless a new candidate changes the parser gate, state relation, or target-sink relation described above. Preserve any proven reachability, but discard variants that return to the same clean-exit, off-target-crash, wrong-sink, usage-only, or both-image-crash basin.

## Procedure
1. Keep only the smallest parser or harness envelope that the verifier proved was reached.
2. Identify the missing causal relation from the signal: parser selection, container acceptance, length relation, stateful subobject, allocation state, or official target sink.
3. Change one relation at a time and discard candidates that return to this same basin.
4. If a local crash is not an official target match, shrink or discard it before mutating deeper fields.
5. Promote a recovery from this basin only after a later verifier-confirmed target match.

## Negative Memory
- Do not resubmit broad mutations that only reproduce `tpm_command_rejected_cleanly`.
- Do not count parser reachability, local wrapper crashes, both-image crashes, or clean exits as success.
- Do not store raw payload bytes, exact positions, task identifiers, checksums, or submit metadata.

## Format Contract
Use [[tpm2-command-buffer]] for descriptive format gates and invariants.

## Harness Contract
Use [[libfuzzer-libtpms-process-command]] for the input-carving contract.

## Evidence Shape
- Support: 1 diagnosed persistent failure from round 17.
- Scope: generator repair and basin avoidance only.
