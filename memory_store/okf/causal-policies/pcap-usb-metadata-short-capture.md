---
type: causal-policy
title: Pcap Usb Metadata Short Capture
description: Verified recovery for wrong_sink with target_match on pcap inputs.
failure_class: wrong_sink
verifier_signal: target_match
candidate_family: construct
input_format: pcap
harness_convention: libfuzzer
access_scope: generate
success_count: 1
confidence: medium
tags: [wrong-sink, target-match, construct, pcap, verified_recovery]
match_keys: [wrong-sink, target-match, pcap, heap-buffer-overflow-read]
allowed_scopes: [generate]
forbidden_fields: [raw_poc_bytes, task_id, exact_offset, checksum, submit_metadata]
evidence_level: high
train_only: true
---
# Pcap Usb Metadata Short Capture

- key: `wrong_sink x target_match`
- outcome: verified recovery
- confidence: 0.69
- success_count: 1
- failure_count: 0
- formats: [[pcap]]

## Failure Shape
A prior candidate family produced `wrong_sink` before the verifier-confirmed repair. The winning shape kept the required parser envelope for `pcap` and moved the mutation into the boundary relation consumed by the target sink instead of relying on broad corruption.

## Procedure
Construct a classic PCAP with the USB Linux mmap link type and a packet whose declared capture snapshot is shorter than the USB metadata header. Keep the file header and packet header valid so the savefile reader reaches packet fixup, then let the vulnerable fixup inspect USB metadata fields before checking that the full metadata header is present. The fixed build performs the missing captured-length gate first.

Retarget from this failure key by preserving the format gate first, then changing exactly the cross-field invariant that separates the vulnerable build from the fixed build. Prefer a compact construct when the trace used `construct`; prefer one seed-preserving mutation when the trace used seed mutation.

## Verifier Contract
The local signal should progress from `wrong_sink` toward `target_match`. The official gate must show a vulnerable-build crash and a clean fixed build; parser-only reachability is not enough.

## Negative Guards
Do not store raw payload bytes or task-specific positions. Do not widen the mutation after the parser envelope is accepted; if the fixed image also crashes, shrink back to the single invariant described above.
