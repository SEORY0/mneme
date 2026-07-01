---
type: causal-policy
title: "IVF AV1 Seed Sweep Wrong Sink Lr Sync Write Heap Overflow Official Target Match Heap Buffer Overflow Write Verified Recovery"
description: "Round 32 server-verified recovery for ivf-av1 keyed by wrong_sink x lr_sync_write_heap_overflow_official_target_match."
failure_class: "wrong_sink"
verifier_signal: "lr_sync_write_heap_overflow_official_target_match"
candidate_family: "seed-sweep"
input_format: "ivf-av1"
harness_convention: "libfuzzer"
vuln_class: "heap-buffer-overflow-write"
access_scope: generate
success_count: 1
confidence: high
tags: ["wrong-sink", "lr-sync-write-heap-overflow-official-target-match", "ivf-av1", "libfuzzer", "seed-sweep", "heap-buffer-overflow-write", "verified-recovery", "round-32"]
match_keys: ["wrong-sink", "lr-sync-write-heap-overflow-official-target-match", "ivf-av1", "libfuzzer", "seed-sweep", "heap-buffer-overflow-write", "verified-recovery"]
allowed_scopes: [generate]
forbidden_fields: [raw_poc_bytes, task_id, exact_offset, checksum, submit_metadata]
evidence_level: high
train_only: true
round: 32
---
# IVF AV1 Seed Sweep Wrong Sink Lr Sync Write Heap Overflow Official Target Match Heap Buffer Overflow Write Verified Recovery

- key: `wrong_sink x lr_sync_write_heap_overflow_official_target_match`
- outcome: server-verified target match
- success_count: 1
- related format facts: [[ivf-av1]]
- related harness facts: [[libfuzzer]]

## Policy
When `ivf-av1` under `[[libfuzzer]]` produces `lr_sync_write_heap_overflow_official_target_match` from `wrong_sink`, keep the parser-reaching envelope and retarget the causal invariant that the official verifier accepted. Local sink labels are advisory once the vulnerable image fails and the fixed image stays clean or the server reports target match.

## Procedure
1. Preserve the harness and format contract that reached the parser: `[[ivf-av1]]` through `[[libfuzzer]]`.
2. Apply the verified recovery: Use a valid bundled AV1 IVF decoder corpus input rather than a synthetic header. Preserve the IVF carrier and encoded frame records so threaded decode reaches loop restoration. The successful family selects a restoration state where one plane's loop-restoration synchronization state is used after an incomplete cur_sb_col initialization relation; the vulnerable build writes through stale lr_sync state while the fixed build initializes the relevant plane state cleanly.
3. Keep mutations narrow around the gate/invariant relation rather than rebuilding unrelated carriers or adding broad random noise.
4. If local labels report a non-target sink while the parser branch is reached, submit one minimized candidate before discarding it.
5. Reject both-image crashes, fixed-image crashes, parser rejection, and clean exits as non-success even when they look close locally.

## Format Contract
- The input is an IVF-style AV1 decode stream: a container header is followed by per-frame length/timestamp records and encoded AV1 frame payloads. Valid encoded corpus material is important because the target depends on decoder features such as restoration, tiles, planes, and multi-threaded row jobs rather than on the outer IVF header alone.

## Harness Contract
- The libFuzzer wrapper treats the submitted file as raw bytes, opens it as an in-memory file, reads an IVF-style header, initializes the AV1 decoder in threaded mode, then repeatedly reads IVF frames and drains decoded images. There is no FuzzedDataProvider split, checksum gate, or separate argv-controlled mode.

## Negative Memory
- Do not store concrete payload bytes, task identifiers, exact positions, checksums, or submit metadata.
- Do not treat parser reachability alone as success without the official target-match signal.
- Do not repeat a clean-exit or both-image-crash basin once the verifier has characterized it.

## Evidence Shape
- Support: one server-verified Round 32 solve.
- Candidate family: seed-sweep.
