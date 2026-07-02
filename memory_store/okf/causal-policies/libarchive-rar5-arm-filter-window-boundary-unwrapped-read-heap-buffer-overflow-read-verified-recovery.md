---
type: causal-policy
title: "Libarchive RAR5 ARM Filter Window Boundary Unwrapped Read Heap Buffer Overflow Read Verified Recovery"
description: "Verified recovery for no_crash where the RAR5 ARM de-filter reads a 4-byte word at the circular-window boundary without re-wrapping."
failure_class: "no_crash"
verifier_signal: "rar5_arm_filter_window_boundary_unwrapped_4byte_read"
candidate_family: "seed_mutate"
input_format: "rar5"
harness_convention: "libarchive-fuzzer"
vuln_class: "heap-buffer-overflow-read"
access_scope: generate
success_count: 1
confidence: high
tags: ["no-crash", "seed-mutate", "rar5", "heap-buffer-overflow-read", "verified-recovery"]
match_keys: ["no_crash", "rar5_arm_filter_window_boundary_unwrapped_4byte_read", "rar5", "libarchive-fuzzer", "heap-buffer-overflow-read", "verified_recovery"]
allowed_scopes: [generate]
forbidden_fields: [raw_poc_bytes, task_id, exact_offset, checksum, submit_metadata]
evidence_level: high
train_only: true
provenance: claude-precise-analysis-2026-06-29
---
# Libarchive RAR5 ARM Filter Window Boundary Unwrapped Read Heap Buffer Overflow Read Verified Recovery

## Policy
For `no_crash` on the libarchive fuzzer where the RAR5 ARM filter reads past the window, the bug is in
`run_arm_filter`: it walks the circular unpack window in 4-byte words, masks only the BASE index
(`(...+i) & window_mask`), but the `+1..+3` bytes of the word (the `b[3]==0xEB` test and the 4-byte
`archive_le32dec`) are NOT re-wrapped. When a masked base index lands in the top 3 bytes of the fixed
128 KiB window, the 4-byte read runs 1-3 bytes past the calloc'd buffer → ASan heap OOB read. The fix reads
via a circular copy and masks `(base+3) & window_mask`.

## Procedure
1. Constructing a bit-packed RAR5 compressed+filter block by hand is impractical, so **seed-mutate a real,
   valid ARM-filtered RAR5 sample** from the repo's test corpus (one that decodes cleanly). Do NOT use any
   shipped crashing reproducer — build from a functional sample.
2. The sample must: be a valid RAR5 archive (signature `Rar!\x1a\x07\x01\x00`), select a COMPRESSED (not
   stored) block, and emit a `FILTER_ARM` symbol whose block placement drives a filter iteration index to
   the window boundary (last 3 bytes of the 0x20000 window).
3. Mutate window-fill / filter placement (e.g. via corpus-seeded libFuzzer co-mutation) until an ARM-filter
   iteration's masked base index reaches `window_size-3 .. window_size-1`. Confirm ASan heap-buffer-overflow
   READ in run_arm_filter (3/3); fix exits 0.

## Format Contract
- See [[rar5]]. Filters are parsed only inside a compressed block's bitstream, so a working compressed
  ARM-filtered archive is the prerequisite; the OOB is a boundary-alignment condition, not a header edit.

## Negative Memory
- Do not hand-edit filter params in a stored/uncompressed archive — filters live in the compressed stream.
- Do not use a shipped reproducer; seed-mutate a valid sample.
- Do not store raw bytes, offsets, or task identifiers.

## Evidence Shape
- Support: one verified solve (official vul crash, fix clean).
