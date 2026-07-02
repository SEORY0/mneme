---
type: causal-policy
title: "Rar5 Seed Mutate Wrong Sink Parser Reached Window Mismatch Dictionary Copy Overflow Heap Buffer Overflow Write Verified Recovery"
description: "Round 34 verified recovery for rar5 when wrong_sink pairs with parser_reached_window_mismatch_dictionary_copy_overflow."
failure_class: "wrong_sink"
verifier_signal: "parser_reached_window_mismatch_dictionary_copy_overflow"
candidate_family: "seed_mutate"
input_format: "rar5"
harness_convention: "libfuzzer-libarchive"
vuln_class: "heap-buffer-overflow-write"
access_scope: generate
success_count: 1
confidence: high
tags: ["wrong-sink", "parser-reached-window-mismatch-dictionary-copy-overflow", "rar5", "libfuzzer-libarchive", "seed-mutate", "verified-recovery", "round-34"]
match_keys: ["wrong-sink", "parser-reached-window-mismatch-dictionary-copy-overflow", "rar5", "libfuzzer-libarchive", "seed-mutate", "heap-buffer-overflow-write", "verified-recovery"]
allowed_scopes: [generate]
forbidden_fields: [raw_poc_bytes, task_id, exact_offset, checksum, submit_metadata]
evidence_level: high
train_only: true
round: 34
---
# Rar5 Seed Mutate Wrong Sink Parser Reached Window Mismatch Dictionary Copy Overflow Heap Buffer Overflow Write Verified Recovery

- key: `wrong_sink x parser_reached_window_mismatch_dictionary_copy_overflow`
- outcome: server-verified vulnerable/fixed split
- success_count: 1
- related format facts: [[rar5]]
- related harness facts: [[libfuzzer-libarchive]]

## Round 34 Verified Support

- key: `wrong_sink x parser_reached_window_mismatch_dictionary_copy_overflow`
- outcome: server-verified vulnerable/fixed split
- candidate family: `seed_mutate`
- vulnerability class: `heap-buffer-overflow-write`
- related format facts: [[rar5]]
- related harness facts: [[libfuzzer-libarchive]]

### Policy
When `wrong_sink x parser_reached_window_mismatch_dictionary_copy_overflow` appears for `rar5`, preserve the accepted parser and harness gates, then target the specific state relation that the verifier proved. Treat the official vulnerable-only target match as the success gate; local crash class alone is not enough.

### Procedure
1. Use the [[libfuzzer-libarchive]] harness contract and the [[rar5]] format contract before changing sink fields.
2. Recreate the verified causal relation: Start from a valid non-solid RAR5 multivolume fixture and concatenate the complete volume sequence so the one-buffer libarchive fuzzer can switch volumes internally. Preserve the RAR5 marker, volume headers, compressed data, and base-block CRC gates. Mutate only the split FILE headers: declare a smaller dictionary/window class on the primary split block, keep a larger dictionary/window class on continuation blocks, and recompute the affected header CRCs. During continuation decompression the vulnerable build applies the larger mask to the smaller allocated window buffer and overflows during a dictionary-copy operation; the fixed build rejects the inconsistent continuation declaration.
3. Keep selectors, lengths, state setup, and container invariants coherent until the target parser state is reached.
4. Submit only when the candidate is expected to preserve the vulnerable/fixed split rather than a generic both-build crash.

### Format Contract
RAR5 archives begin with a fixed marker followed by CRC-protected variable-length base blocks. MAIN blocks carry archive flags such as volume state. FILE blocks can carry extra-data size, data size, split-before and split-after flags, file size metadata, compression information with method, solid bit, and dictionary/window selector, host OS, name, and compressed member data. Multivolume archives are represented by repeated RAR5 signatures and per-volume MAIN/FILE/ENDARC blocks.

### Harness Contract
The libarchive libFuzzer target feeds the entire PoC as one in-memory archive stream, enables all filters and formats, iterates archive headers, and drains entry data through archive_read_data. It has no mode byte, no filename side channel, no checksum wrapper beyond archive headers, and no FuzzedDataProvider split; concatenated RAR5 volumes are consumed from the same raw byte stream.

### Evidence Shape
- Support: one server-verified round 34 solve.
- Candidate family: `seed_mutate`.
- Verifier key: `wrong_sink x parser_reached_window_mismatch_dictionary_copy_overflow`.
- Vulnerability class: `heap-buffer-overflow-write`.

## Negative Memory
- Do not count parser reachability, both-image crashes, fixed-image crashes, local wrapper crashes, clean exits, or off-target sanitizer crashes as success for this key.
- Do not store concrete payload bytes, exact positions, task identifiers, checksums, or submit metadata.
