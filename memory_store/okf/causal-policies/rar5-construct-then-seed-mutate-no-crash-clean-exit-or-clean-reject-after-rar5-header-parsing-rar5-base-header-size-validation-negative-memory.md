---
type: causal-policy
title: "Rar5 Construct Then Seed Mutate No Crash Clean Exit Or Clean Reject After Rar5 Header Parsing Rar5 Base Header Size Validation Negative Memory"
description: "Round 34 negative memory for rar5 when no_crash pairs with clean_exit_or_clean_reject_after_rar5_header_parsing."
failure_class: "no_crash"
verifier_signal: "clean_exit_or_clean_reject_after_rar5_header_parsing"
candidate_family: "construct_then_seed_mutate"
input_format: "rar5"
harness_convention: "libfuzzer-libarchive"
vuln_class: "rar5-base-header-size-validation"
access_scope: generate
success_count: 0
confidence: medium
tags: ["no-crash", "clean-exit-or-clean-reject-after-rar5-header-parsing", "rar5", "libfuzzer-libarchive", "construct-then-seed-mutate", "negative-memory", "round-34"]
match_keys: ["no-crash", "clean-exit-or-clean-reject-after-rar5-header-parsing", "rar5", "libfuzzer-libarchive", "construct-then-seed-mutate", "rar5-base-header-size-validation", "negative-memory"]
allowed_scopes: [generate]
forbidden_fields: [raw_poc_bytes, task_id, exact_offset, checksum, submit_metadata]
evidence_level: medium
train_only: true
round: 34
---
# Rar5 Construct Then Seed Mutate No Crash Clean Exit Or Clean Reject After Rar5 Header Parsing Rar5 Base Header Size Validation Negative Memory

- key: `no_crash x clean_exit_or_clean_reject_after_rar5_header_parsing`
- outcome: persistent failure / basin to avoid
- success_count: 0
- failure_count: 1
- related format facts: [[rar5]]
- related harness facts: [[libfuzzer-libarchive]]

## Round 34 Negative Support

- key: `no_crash x clean_exit_or_clean_reject_after_rar5_header_parsing`
- outcome: persistent failure / basin to avoid
- candidate family: `construct_then_seed_mutate`
- vulnerability class: `rar5-base-header-size-validation`
- related format facts: [[rar5]]
- related harness facts: [[libfuzzer-libarchive]]

### Failure Shape
The invalid zero-sized base-block relation was reachable but did not produce a sanitizer-visible vulnerable failure. A minimal constructed archive, existing malformed RAR5 fixtures, and real stored, compressed, end-marker, and multi-file carriers were mutated to keep the RAR5 marker and recomputed header checksum gates while declaring a zero-sized base block. Moving the invariant across MAIN, FILE, later FILE, and ENDARC contexts stayed in clean exit. A header-stage variant that combined zero declared size with impossible FILE extra-data framing also exited cleanly. The likely missing relation is a deeper compressed-data state that only the vulnerable build can reach after the zero-size header bypass, rather than the zero-size base-block invariant by itself.

### Policy
Treat `no_crash x clean_exit_or_clean_reject_after_rar5_header_parsing` on `rar5` as a basin to avoid unless a new candidate changes the parser gate, state relation, harness contract, or target sink relation described below. Preserve any proven reachability, but reject variants that return to the same signal without changing the causal gate under test.

### Procedure
1. Keep only the smallest parser or harness envelope that was actually reached.
2. Identify the missing causal relation from the signal: parser selection, container acceptance, length relation, stateful subobject, allocation state, or official target sink.
3. Change one relation at a time and discard candidates that return to the same clean-exit, off-target-crash, wrong-sink, usage-only, or both-image-crash basin.
4. Promote a recovery from this basin only after a later verifier-confirmed target match.

### Format Contract
RAR5 archives begin with a fixed marker followed by CRC-protected base blocks. A base block stores a little-endian header CRC, a variable-length declared header size, then variable-length header type and flags. The vulnerable reader computes the CRC only over the declared header-size span, so a declared zero-size block can make later header fields sit outside the checksum-covered area while still being read by the parser. FILE blocks may carry extra-data and packed-data size varints before file flags, unpacked size, attributes, compression info, host OS, filename, optional extra records, and member data. Compressed entries add compressed-block headers and Huffman/table data after the FILE header.

### Harness Contract
The libarchive libFuzzer target feeds the PoC as one raw in-memory archive stream, enables all filters and formats, repeatedly calls archive_read_next_header, and drains entry data with archive_read_data. There is no leading mode byte, chunk framing, filename wrapper, or FuzzedDataProvider split. Parser reachability depends on a complete archive stream whose RAR5 marker, base-header CRCs, and data-size framing are coherent enough for libarchive format detection and header iteration.

### Evidence Shape
- Support: one diagnosed persistent round 34 failure.
- Candidate family: `construct_then_seed_mutate`.
- Verifier key: `no_crash x clean_exit_or_clean_reject_after_rar5_header_parsing`.
- Vulnerability class: `rar5-base-header-size-validation`.

## Negative Memory
- Do not count parser reachability, both-image crashes, fixed-image crashes, local wrapper crashes, clean exits, or off-target sanitizer crashes as success for this key.
- Do not store concrete payload bytes, exact positions, task identifiers, checksums, or submit metadata.
