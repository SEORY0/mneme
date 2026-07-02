---
type: causal-policy
title: "No Crash Clean Exit After Pkcs15 Reader Transcript Opensc Pkcs15 Reader Chunk Stream Out Of Bounds Read Negative Memory"
description: "Negative memory for persistent no_crash / clean_exit_after_pkcs15_reader_transcript basin."
failure_class: "no_crash"
verifier_signal: "clean_exit_after_pkcs15_reader_transcript"
candidate_family: "seed_mutate"
input_format: "opensc-pkcs15-reader-chunk-stream"
harness_convention: "libfuzzer"
vuln_class: "out-of-bounds-read"
access_scope: generate
success_count: 0
confidence: medium
tags: ["no-crash", "seed-mutate", "opensc-pkcs15-reader-chunk-stream", "out-of-bounds-read", "negative-memory"]
match_keys: ["no-crash", "clean-exit-after-pkcs15-reader-transcript", "opensc-pkcs15-reader-chunk-stream", "libfuzzer", "out-of-bounds-read", "negative-memory"]
allowed_scopes: [generate]
forbidden_fields: [raw_poc_bytes, task_id, exact_offset, checksum, submit_metadata]
evidence_level: medium
train_only: true
provenance: round-35-consolidator
---
# No Crash Clean Exit After Pkcs15 Reader Transcript Opensc Pkcs15 Reader Chunk Stream Out Of Bounds Read Negative Memory

## Policy
For `no_crash` with verifier signal `clean_exit_after_pkcs15_reader_transcript` on `opensc-pkcs15-reader-chunk-stream` under `libfuzzer`, treat the recorded family as a basin to avoid until a later verifier-confirmed candidate flips the gate. Preserve the descriptive format/harness facts, but do not promote this into a recovery policy.

## Avoided Basin
- A real PIV reader transcript reached cleanly, but targeted mutations did not produce a sanitizer signal.
- Distinct attempts included replaying corpus seeds, mutating CCC zero-length SimpleTLV fields, varying BER-declared object lengths and APDU chaining, steering dual-card CCC flags, mutating discovery and CHUI objects, mutating certificate-like objects, and appending oversized post-bind operation chunks.
- The likely missing piece is the precise relation between PIV GET DATA length probing, full-read response length, and the zero-length tag state that the fixed build rejects.

## Recovery Direction
- Keep the parser/harness reachability facts in [[opensc-pkcs15-reader-chunk-stream]] and [[libfuzzer]].
- Retarget away from the failed relation named by `clean_exit_after_pkcs15_reader_transcript`; require vulnerable-only official confirmation before promoting any replacement.

## Evidence Shape
- Support: one round 35 persistent failure with concrete diagnosis and no official target match.
