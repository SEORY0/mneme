---
type: causal-policy
title: "Rar5 Seed Mutate Wrong Sink Parser Reached Target Parse Tables Read Bits Heap Buffer Overflow Read Verified Recovery"
description: "Round 32 server-verified recovery for rar5 keyed by wrong_sink x parser_reached_target_parse_tables_read_bits."
failure_class: "wrong_sink"
verifier_signal: "parser_reached_target_parse_tables_read_bits"
candidate_family: "seed_mutate"
input_format: "rar5"
harness_convention: "libfuzzer"
vuln_class: "heap-buffer-overflow-read"
access_scope: generate
success_count: 1
confidence: high
tags: ["wrong-sink", "parser-reached-target-parse-tables-read-bits", "rar5", "libfuzzer", "seed-mutate", "heap-buffer-overflow-read", "verified-recovery", "round-32"]
match_keys: ["wrong-sink", "parser-reached-target-parse-tables-read-bits", "rar5", "libfuzzer", "seed-mutate", "heap-buffer-overflow-read", "verified-recovery"]
allowed_scopes: [generate]
forbidden_fields: [raw_poc_bytes, task_id, exact_offset, checksum, submit_metadata]
evidence_level: high
train_only: true
round: 32
---
# Rar5 Seed Mutate Wrong Sink Parser Reached Target Parse Tables Read Bits Heap Buffer Overflow Read Verified Recovery

- key: `wrong_sink x parser_reached_target_parse_tables_read_bits`
- outcome: server-verified target match
- success_count: 1
- related format facts: [[rar5]]
- related harness facts: [[libfuzzer]]

## Policy
When `rar5` under `[[libfuzzer]]` produces `parser_reached_target_parse_tables_read_bits` from `wrong_sink`, keep the parser-reaching envelope and retarget the causal invariant that the official verifier accepted. Local sink labels are advisory once the vulnerable image fails and the fixed image stays clean or the server reports target match.

## Procedure
1. Preserve the harness and format contract that reached the parser: `[[rar5]]` through `[[libfuzzer]]`.
2. Apply the verified recovery: Start from a real compressed RAR5 archive so the marker, CRC-protected base headers, file metadata, and compressed-block header gates are already valid. Keep the table-present compressed block path, declare a short block with a valid block-header checksum, and shape the beginning Huffman code-length stream so it remains syntactically usable but causes the later table decoder to consume far more bits than the declared block can contain. Leave only the reader's required lookahead padding beyond the short block. The vulnerable reader reads past the available block while building Huffman tables; the fixed build avoids that read.
3. Keep mutations narrow around the gate/invariant relation rather than rebuilding unrelated carriers or adding broad random noise.
4. If local labels report a non-target sink while the parser branch is reached, submit one minimized candidate before discarding it.
5. Reject both-image crashes, fixed-image crashes, parser rejection, and clean exits as non-success even when they look close locally.

## Format Contract
- RAR5 starts with a fixed marker followed by CRC-protected base headers using variable-length integers. File blocks carry optional data size, file metadata, compression information, host OS, and a name before compressed data. Compressed data begins with a compact block header containing bit-size, byte-count, last-block, and table-present flags plus a small checksum over the block header fields. Huffman table data follows the block header and starts with nibble-coded code lengths before a bitstream-encoded combined table.

## Harness Contract
- The libarchive fuzzer feeds raw bytes as one archive stream from memory, enables all formats and filters, iterates archive headers, and drains entry data through archive_read_data. There is no prefix byte or FuzzedDataProvider layout; parser reachability depends on preserving the RAR5 marker, base-header CRCs, and compressed member-data gates.

## Negative Memory
- Do not store concrete payload bytes, task identifiers, exact positions, checksums, or submit metadata.
- Do not treat parser reachability alone as success without the official target-match signal.
- Do not repeat a clean-exit or both-image-crash basin once the verifier has characterized it.

## Evidence Shape
- Support: one server-verified Round 32 solve.
- Candidate family: seed_mutate.
