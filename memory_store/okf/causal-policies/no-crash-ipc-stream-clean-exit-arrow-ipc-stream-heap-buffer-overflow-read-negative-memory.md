---
type: causal-policy
title: "No Crash Ipc Stream Clean Exit Arrow Ipc Stream Heap Buffer Overflow Read Negative Memory"
description: "Negative memory for persistent no_crash / ipc_stream_clean_exit basin."
failure_class: "no_crash"
verifier_signal: "ipc_stream_clean_exit"
candidate_family: "seed_replay_and_metadata_mutate"
input_format: "arrow-ipc-stream"
harness_convention: "afl-libfuzzer-ipc-stream-reader"
vuln_class: "heap-buffer-overflow-read"
access_scope: generate
success_count: 0
confidence: medium
tags: ["no-crash", "seed-replay-and-metadata-mutate", "arrow-ipc-stream", "heap-buffer-overflow-read", "negative-memory"]
match_keys: ["no-crash", "ipc-stream-clean-exit", "arrow-ipc-stream", "afl-libfuzzer-ipc-stream-reader", "heap-buffer-overflow-read", "negative-memory"]
allowed_scopes: [generate]
forbidden_fields: [raw_poc_bytes, task_id, exact_offset, checksum, submit_metadata]
evidence_level: medium
train_only: true
provenance: round-35-consolidator
---
# No Crash Ipc Stream Clean Exit Arrow Ipc Stream Heap Buffer Overflow Read Negative Memory

## Policy
For `no_crash` with verifier signal `ipc_stream_clean_exit` on `arrow-ipc-stream` under `afl-libfuzzer-ipc-stream-reader`, treat the recorded family as a basin to avoid until a later verifier-confirmed candidate flips the gate. Preserve the descriptive format/harness facts, but do not promote this into a recovery policy.

## Avoided Basin
- All available Arrow IPC stream corpus seeds replayed through the harness without a crash.
- A nested integration stream was a valid parser carrier, but targeted mutations to field-node lengths and record-batch buffer descriptors either produced clean exits or invalid statuses that the fuzz harness ignored.
- The missing relation is likely a still-deserializable nested or sliced array state that makes ValidateFull call the Slice helpers with an unsafe logical offset or length, not merely malformed stream framing or rejected buffer metadata.

## Recovery Direction
- Keep the parser/harness reachability facts in [[arrow-ipc-stream]] and [[afl-libfuzzer-ipc-stream-reader]].
- Retarget away from the failed relation named by `ipc_stream_clean_exit`; require vulnerable-only official confirmation before promoting any replacement.

## Evidence Shape
- Support: one round 35 persistent failure with concrete diagnosis and no official target match.
