---
type: causal-policy
title: "Rar5 Seed Mutate Wrong Sink Parser Reached Parse Tables Stack Overflow Stack Buffer Overflow Write Verified Recovery"
description: "Round 32 server-verified recovery for rar5 keyed by wrong_sink x parser_reached_parse_tables_stack_overflow."
failure_class: "wrong_sink"
verifier_signal: "parser_reached_parse_tables_stack_overflow"
candidate_family: "seed_mutate"
input_format: "rar5"
harness_convention: "libfuzzer-libarchive"
vuln_class: "stack-buffer-overflow-write"
access_scope: generate
success_count: 1
confidence: high
tags: ["wrong-sink", "parser-reached-parse-tables-stack-overflow", "rar5", "libfuzzer-libarchive", "seed-mutate", "stack-buffer-overflow-write", "verified-recovery", "round-32"]
match_keys: ["wrong-sink", "parser-reached-parse-tables-stack-overflow", "rar5", "libfuzzer-libarchive", "seed-mutate", "stack-buffer-overflow-write", "verified-recovery"]
allowed_scopes: [generate]
forbidden_fields: [raw_poc_bytes, task_id, exact_offset, checksum, submit_metadata]
evidence_level: high
train_only: true
round: 32
---
# Rar5 Seed Mutate Wrong Sink Parser Reached Parse Tables Stack Overflow Stack Buffer Overflow Write Verified Recovery

- key: `wrong_sink x parser_reached_parse_tables_stack_overflow`
- outcome: server-verified target match
- success_count: 1
- related format facts: [[rar5]]
- related harness facts: [[libfuzzer-libarchive]]

## Policy
When `rar5` under `[[libfuzzer-libarchive]]` produces `parser_reached_parse_tables_stack_overflow` from `wrong_sink`, keep the parser-reaching envelope and retarget the causal invariant that the official verifier accepted. Local sink labels are advisory once the vulnerable image fails and the fixed image stays clean or the server reports target match.

## Procedure
1. Preserve the harness and format contract that reached the parser: `[[rar5]]` through `[[libfuzzer-libarchive]]`.
2. Apply the verified recovery: Start from a valid compressed RAR5 fixture that already reaches libarchive's RAR5 data decompressor. Preserve the RAR5 signature, base-block CRC fields, file header data-size framing, and the compressed-block checksum/header. Mutate only the compressed block's Huffman table byte stream so the first bit-length table decodes ordinary nibbles until just before the fixed bit-length array is full, then decodes an escape run whose zero-fill count exceeds the remaining capacity by the minimum meaningful margin. The vulnerable build expands the run past the stack bit-length array in parse_tables; the fixed build rejects or bounds the run before the write.
3. Keep mutations narrow around the gate/invariant relation rather than rebuilding unrelated carriers or adding broad random noise.
4. If local labels report a non-target sink while the parser branch is reached, submit one minimized candidate before discarding it.
5. Reject both-image crashes, fixed-image crashes, parser rejection, and clean exits as non-success even when they look close locally.

## Format Contract
- RAR5 archives begin with a fixed marker followed by CRC-protected variable-length base blocks. File blocks with data carry optional extra-data size, data-size, file flags, unpacked size, attributes, compression info, host OS, name, and optional extras before the compressed data region. Compressed data is divided into compressed blocks with a compact block header containing flags, a checksum byte, and a variable-width block-size field. If the table-present flag is set, the block payload starts with Huffman table metadata. The first Huffman metadata phase is nibble-coded and uses an escape nibble to either emit a literal escape value or run-length-fill zero bit lengths.

## Harness Contract
- The libarchive fuzzer provides the entire PoC as one in-memory archive stream through archive_read_open with all filters and formats enabled. There is no leading selector and no FuzzedDataProvider layout. The harness repeatedly calls archive_read_next_header and archive_read_data, so a candidate must be a whole archive that passes format detection and reaches member data decompression; mutating only the compressed data after valid RAR5 headers preserves this contract.

## Negative Memory
- Do not store concrete payload bytes, task identifiers, exact positions, checksums, or submit metadata.
- Do not treat parser reachability alone as success without the official target-match signal.
- Do not repeat a clean-exit or both-image-crash basin once the verifier has characterized it.

## Evidence Shape
- Support: one server-verified Round 32 solve.
- Candidate family: seed_mutate.
