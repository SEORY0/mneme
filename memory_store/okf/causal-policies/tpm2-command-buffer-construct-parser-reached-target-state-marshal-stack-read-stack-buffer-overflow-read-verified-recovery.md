---
type: causal-policy
title: "Tpm2 Command Buffer Construct Parser Reached Target State Marshal Stack Read Stack Buffer Overflow Read Verified Recovery"
description: "Round 29 verified recovery for wrong_sink with verifier signal parser_reached_target_state_marshal_stack_read."
failure_class: "wrong_sink"
verifier_signal: "parser_reached_target_state_marshal_stack_read"
candidate_family: "construct"
input_format: "tpm2-command-buffer"
harness_convention: "libfuzzer"
vuln_class: "stack-buffer-overflow-read"
access_scope: generate
success_count: 1
confidence: high
tags: ["wrong-sink", "parser-reached-target-state-marshal-stack-read", "tpm2-command-buffer", "libfuzzer", "construct", "stack-buffer-overflow-read", "verified-recovery", "round-29"]
match_keys: ["wrong_sink", "parser_reached_target_state_marshal_stack_read", "tpm2-command-buffer", "libfuzzer", "stack-buffer-overflow-read", "wrong-sink", "parser-reached-target-state-marshal-stack-read", "tpm2-command-buffer", "libfuzzer", "stack-buffer-overflow-read", "verified_recovery", "construct", "construct"]
allowed_scopes: [generate]
forbidden_fields: [raw_poc_bytes, task_id, exact_offset, checksum, submit_metadata]
evidence_level: high
train_only: true
round: 29
---
# Tpm2 Command Buffer Construct Parser Reached Target State Marshal Stack Read Stack Buffer Overflow Read Verified Recovery

- key: `wrong_sink x parser_reached_target_state_marshal_stack_read`
- outcome: verified target match / recovery policy
- success_count: 1
- related format facts: [[tpm2-command-buffer]]
- related harness facts: [[libfuzzer]]

## Policy
For `wrong_sink x parser_reached_target_state_marshal_stack_read` on `tpm2-command-buffer`, keep the parser and harness gates that produced the verifier signal, then vary only the causal relation described below. This is a positive recovery policy because the official vulnerable/fixed verifier recorded a target match.

## Procedure
1. Build a valid TPM2 command buffer for defining an owner-authorized orderly NV index. Keep the outer command framing, declared command size, password authorization session, empty auth values, and NV public-area size internally consistent. Set the NV public attributes so the index is RAM-backed and readable/writable through owner authorization, then choose the public data size so the NV RAM header plus data exactly consumes the fixed orderly RAM backing array. That leaves no terminator entry, so the vulnerable persistent-state marshaller scans one header past the local copy of the array during commit; the fixed build rejects or stops this boundary case.
2. Preserve format recognition and the harness input contract while mutating the narrow sink invariant; do not broaden into an off-target crash or a both-image crash.
3. If later verifier output changes the failure key, re-rank against that new key before mutating unrelated fields.

## Format Contract
- Format [[tpm2-command-buffer]]: The input is a single TPM2 command buffer. Multi-byte fields are big-endian. The command envelope contains a tag, a total-size field that must equal the full buffer length, a command selector, command handles, an authorization-session byte count, one password-session record, and command parameters. The define-space parameters contain a sized auth value followed by a sized NV public structure; the NV public structure contains an NV handle, hash algorithm, NV attributes, a sized auth policy, and a data-size field.
- Harness [[libfuzzer]]: The libFuzzer harness initializes a TPM2 instance, sends an internal startup command, then passes the raw fuzzer bytes directly to TPMLIB_Process as one TPM2 command. After processing, it obtains volatile and permanent state, terminates, restores both state blobs, and initializes again. There is no FuzzedDataProvider split and no file envelope outside the TPM command itself.

## Negative Memory
- Do not corrupt the outer `tpm2-command-buffer` recognition gate while retargeting this signal.
- Do not count parser reachability, clean exits, fixed-image crashes, both-image crashes, or local wrong-sink labels as success without official target match.
- Never store payload bytes, exact positions, checksums, submit metadata, or task-local identifiers.

## Evidence Shape
- Support: one round-29 worker trace with official target match.
- Scope: generator repair and retargeting only; pair with [[tpm2-command-buffer]] and [[libfuzzer]].
