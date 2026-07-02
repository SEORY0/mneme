---
type: causal-policy
title: "Samba NDR Pull Advance Offset Size Integer Wrap Heap Buffer Overflow Verified Recovery"
description: "Verified recovery for no_crash where ndr_pull_advance adds size to offset before the bound check, wrapping uint32."
failure_class: "no_crash"
verifier_signal: "ndr_pull_advance_offset_plus_size_uint32_wrap"
candidate_family: "construct"
input_format: "ndr-stub"
harness_convention: "samba-ndr-fuzzer"
vuln_class: "integer-overflow"
access_scope: generate
success_count: 1
confidence: high
tags: ["no-crash", "construct", "ndr-stub", "integer-overflow", "heap-buffer-overflow", "verified-recovery"]
match_keys: ["no_crash", "ndr_pull_advance_offset_plus_size_uint32_wrap", "ndr-stub", "samba-ndr-fuzzer", "integer-overflow", "verified_recovery"]
allowed_scopes: [generate]
forbidden_fields: [raw_poc_bytes, task_id, exact_offset, checksum, submit_metadata]
evidence_level: high
train_only: true
provenance: claude-precise-analysis-2026-06-29
---
# Samba NDR Pull Advance Offset Size Integer Wrap Heap Buffer Overflow Verified Recovery

## Policy
For `no_crash` on the Samba per-function NDR fuzzer, the bug is an integer wrap in `ndr_pull_advance`: it
does `ndr->offset += size` and only THEN checks `ndr->offset > ndr->data_size`. With uint32 offset/size, a
large `size` wraps `offset+size` around 2^32 to a small value that passes the check, so a later access reads
out of bounds. The fix checks `size > data_size - offset` before advancing.

## Procedure
1. Harness contract: a 4-byte header `[uint16 flags LE][uint16 function LE]`, then NDR stub bytes decoded
   per the selected function. Set flags low-2-bits = 2 (TYPE_OUT, no NDR64 bit) and the function index to
   one whose OUT path calls a subcontext/advance with an attacker-controlled size (e.g. a drsuapi
   GetNCChanges-style compressed/subcontext field).
2. Build the NDR_OUT stub so it reaches the vulnerable `ndr_pull_advance`/subcontext with a `size` large
   enough that `offset + size` wraps past 2^32 to a small value (passing the post-add bound check). Keep the
   earlier level/referent/length fields valid so decode reaches that point.
3. Confirm ASan heap-buffer-overflow at the subsequent read; fix exits 0 (rejects the oversized size).

## Format Contract
- See [[ndr-stub]]. The 4-byte header selects direction (IN/OUT, NDR64 bit) + function opnum; the stub is
  decoded as that function's marshalled data. Reaching the advance needs a valid prefix up to the size field.

## Negative Memory
- Do not corrupt the header/level prefix (decode bails before the advance).
- Do not store raw bytes, offsets, or task identifiers.

## Evidence Shape
- Support: one verified solve (official vul crash, fix clean).
