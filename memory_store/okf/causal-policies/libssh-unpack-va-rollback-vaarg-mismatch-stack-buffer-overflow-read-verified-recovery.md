---
type: causal-policy
title: "Libssh Unpack VA Rollback VaArg Mismatch Stack Buffer Overflow Read Verified Recovery"
description: "Verified recovery for no_crash where ssh_buffer_unpack_va's error-rollback walks va_arg inconsistently, reading past the saved arg list."
failure_class: "no_crash"
verifier_signal: "reached_unpack_error_rollback_vaarg_mismatch"
candidate_family: "construct"
input_format: "ssh-wire-stream"
harness_convention: "libssh-server-fuzzer"
vuln_class: "stack-buffer-overflow-read"
access_scope: generate
success_count: 1
confidence: high
tags: ["no-crash", "construct", "ssh-wire-stream", "stack-buffer-overflow-read", "verified-recovery"]
match_keys: ["no_crash", "reached_unpack_error_rollback_vaarg_mismatch", "ssh-wire-stream", "libssh-server-fuzzer", "stack-buffer-overflow-read", "verified_recovery"]
allowed_scopes: [generate]
forbidden_fields: [raw_poc_bytes, task_id, exact_offset, checksum, submit_metadata]
evidence_level: high
train_only: true
provenance: claude-precise-analysis-2026-06-29
---
# Libssh Unpack VA Rollback VaArg Mismatch Stack Buffer Overflow Read Verified Recovery

## Policy
For `no_crash` on the libssh server fuzzer, the bug is in `ssh_buffer_unpack_va`'s error-rollback path:
when an unpack specifier fails partway through a format string, the rollback loop walks the format from the
start to free/zero what was produced, but for scalar specifiers it consumes the wrong number of `va_arg`
entries relative to the success path, walking past the saved `ap` list → stack OOB read. Force the inner
multi-field unpack (e.g. a `"bSS"`-style format) to fail at the 2nd ssh_string so the rollback runs.

## Procedure
1. The server fuzzer dispatches packets by message-type via a global handler table with NO state filter and
   NO crypto required pre-NEWKEYS — so a cleartext packet reaches its handler directly.
2. Frame: an ASCII SSH identification banner line + CRLF, then ONE cleartext SSH binary packet
   (4-byte big-endian packet_length; 1-byte padding_length ≥ 4; payload; zero padding; 8-byte block align).
3. Payload = a userauth-request (publickey) message whose body makes the handler's multi-string unpack fail
   on the second ssh_string (truncate/short-length the 2nd string), triggering the rollback va_arg mismatch.
4. No encryption/MAC needed. Confirm ASan stack-buffer-overflow READ in the unpack rollback; fix exits 0.

## Format Contract
- See [[ssh-wire-stream]]. Banner line then length-prefixed binary packets; type-keyed dispatch means you
  reach a specific handler purely by the message-type byte.

## Negative Memory
- Do not negotiate full crypto — it is unnecessary and adds failure surface; cleartext reaches the handler.
- Do not store raw bytes, offsets, or task identifiers.

## Evidence Shape
- Support: one verified solve (official vul crash, fix clean).
