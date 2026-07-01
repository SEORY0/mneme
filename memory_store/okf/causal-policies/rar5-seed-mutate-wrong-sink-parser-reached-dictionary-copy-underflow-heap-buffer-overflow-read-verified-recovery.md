---
type: causal-policy
title: "Rar5 Seed Mutate Wrong Sink Parser Reached Dictionary Copy Underflow Heap Buffer Overflow Read Verified Recovery"
description: "Server-verified recovery for rar5 when wrong_sink pairs with parser_reached_dictionary_copy_underflow."
failure_class: "wrong_sink"
verifier_signal: "parser_reached_dictionary_copy_underflow"
candidate_family: "seed_mutate"
input_format: "rar5"
harness_convention: "libfuzzer-libarchive"
vuln_class: "heap-buffer-overflow-read"
access_scope: generate
success_count: 1
confidence: high
tags: ["wrong-sink", "parser-reached-dictionary-copy-underflow", "rar5", "libfuzzer-libarchive", "seed-mutate", "verified-recovery", "round-33"]
match_keys: ["wrong-sink", "parser-reached-dictionary-copy-underflow", "rar5", "libfuzzer-libarchive", "seed-mutate", "heap-buffer-overflow-read", "verified-recovery"]
allowed_scopes: [generate]
forbidden_fields: [raw_poc_bytes, task_id, exact_offset, checksum, submit_metadata]
evidence_level: high
train_only: true
round: 33
---
# Rar5 Seed Mutate Wrong Sink Parser Reached Dictionary Copy Underflow Heap Buffer Overflow Read Verified Recovery

- key: `wrong_sink x parser_reached_dictionary_copy_underflow`
- outcome: server-verified vulnerable/fixed split
- success_count: 1
- related format facts: [[rar5]]
- related harness facts: [[libfuzzer-libarchive]]

## Policy
When `wrong_sink x parser_reached_dictionary_copy_underflow` appears for `rar5`, preserve the parser and harness gates that were proven by the verifier before mutating the sink-specific relation. Treat official vulnerable-only target match as the success gate, not a local coarse crash label.

## Procedure
1. Use the `libfuzzer-libarchive` harness contract and the `rar5` format contract before changing sink fields.
2. Recreate the causal relation from the verified trace: Start from a compressed RAR5 fixture that already reaches member-data decompression and preserves the marker, base-header CRCs, file metadata, compressed-block header, and Huffman tables. Mutate the file compression metadata so the dictionary window selector declares the maximum window, then alter one early copy-distance relation in the compressed command stream so the first reachable dictionary copy asks for history before the available output. This keeps the archive structurally valid while making the vulnerable signed mask conversion expose an out-of-window read; the fixed build rejects or safely handles the relation.
3. Keep lengths, dispatch selectors, structural checks, and state setup coherent until the target parser state is reached.
4. Submit only after the fixed image exits cleanly or rejects the relation while the vulnerable image reaches the target sink.

## Format Contract
Use [[rar5]]. RAR5 archives begin with a fixed marker followed by integrity-protected variable-length base blocks. File blocks with data carry optional extra-data size, data size, file flags, unpacked size, attributes, optional content integrity metadata, compression info, host OS, filename, and then compressed member data. The compression info contains method, version, solid flag, and a dictionary/window selector. Compressed data uses a compact block header with an integrity field and table-present flag, followed by Huffman table metadata and command bits that can emit literals, filters, or dictionary-copy operations.

## Harness Contract
Use [[libfuzzer-libarchive]]. The libarchive libFuzzer harness feeds the PoC bytes directly as one in-memory archive stream, enables all filters and archive formats, iterates archive headers, and drains each entry with archive_read_data. There is no selector prefix and no FuzzedDataProvider front/back split; reaching the target requires a whole RAR5 archive whose header CRCs and compressed-data gates remain coherent.

## Evidence Shape
- Support: 1 server-verified round 33 solve.
- Candidate family: seed_mutate.
- Verifier key: `wrong_sink x parser_reached_dictionary_copy_underflow`.
- Vulnerability class: `heap-buffer-overflow-read`.
- Recovery summary: Start from a compressed RAR5 fixture that already reaches member-data decompression and preserves the marker, base-header CRCs, file metadata, compressed-block header, and Huffman tables. Mutate the file compression metadata so the dictionary window selector declares the maximum window, then alter one early copy-distance relation in the compressed command stream so the first reachable dictionary copy asks for history before the available output. This keeps the archive structurally valid while making the vulnerable signed mask conversion expose an out-of-window read; the fixed build rejects or safely handles the relation.

## Negative Memory
- Do not count parser reachability, both-image crashes, local-only wrapper crashes, clean exits, or fixed-image crashes as success for this key.
- Do not store raw payload bytes, exact positions, task identifiers, checksums, or submit metadata.
