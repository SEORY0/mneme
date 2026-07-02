---
type: causal-policy
title: "Cdf Ole Compound Document Construct Generic Crash Direct Container Parser Reached And Submit Target Match Integer Overflow To Heap Buffer Overflow Read Verified Recovery"
description: "Server-verified recovery for cdf-ole-compound-document when generic_crash pairs with direct_container_parser_reached_and_submit_target_match."
failure_class: "generic_crash"
verifier_signal: "direct_container_parser_reached_and_submit_target_match"
candidate_family: "construct"
input_format: "cdf-ole-compound-document"
harness_convention: "libfuzzer-libmagic-magic_buffer"
vuln_class: "integer-overflow-to-heap-buffer-overflow-read"
access_scope: generate
success_count: 1
confidence: high
tags: ["generic-crash", "direct-container-parser-reached-and-submit-target-match", "cdf-ole-compound-document", "libfuzzer-libmagic-magic-buffer", "construct", "verified-recovery", "round-33"]
match_keys: ["generic-crash", "direct-container-parser-reached-and-submit-target-match", "cdf-ole-compound-document", "libfuzzer-libmagic-magic-buffer", "construct", "integer-overflow-to-heap-buffer-overflow-read", "verified-recovery"]
allowed_scopes: [generate]
forbidden_fields: [raw_poc_bytes, task_id, exact_offset, checksum, submit_metadata]
evidence_level: high
train_only: true
round: 33
---
# Cdf Ole Compound Document Construct Generic Crash Direct Container Parser Reached And Submit Target Match Integer Overflow To Heap Buffer Overflow Read Verified Recovery

- key: `generic_crash x direct_container_parser_reached_and_submit_target_match`
- outcome: server-verified vulnerable/fixed split
- success_count: 1
- related format facts: [[cdf-ole-compound-document]]
- related harness facts: [[libfuzzer-libmagic-magic-buffer]]

## Policy
When `generic_crash x direct_container_parser_reached_and_submit_target_match` appears for `cdf-ole-compound-document`, preserve the parser and harness gates that were proven by the verifier before mutating the sink-specific relation. Treat official vulnerable-only target match as the success gate, not a local coarse crash label.

## Procedure
1. Use the `libfuzzer-libmagic-magic-buffer` harness contract and the `cdf-ole-compound-document` format contract before changing sink fields.
2. Recreate the causal relation from the verified trace: Build a CDF/OLE document whose header chooses the largest accepted long-sector size and whose SAT, SSAT, directory, and root stream are all reached through a sector id just beyond the multiplication boundary. In the vulnerable image, the overflowing long-sector position wraps to a controlled in-memory sector that supplies valid chain metadata and then reaches a deliberately narrow downstream short-stream read crash. In the fixed image, the overflowing long-sector position is rejected before those controlled sectors are consumed.
3. Keep lengths, dispatch selectors, structural checks, and state setup coherent until the target parser state is reached.
4. Submit only after the fixed image exits cleanly or rejects the relation while the vulnerable image reaches the target sink.

## Format Contract
Use [[cdf-ole-compound-document]]. CDF/OLE parsing starts from a fixed header with magic, byte order, sector-size powers, master SAT entries, directory-chain roots, and optional short-sector allocation metadata. Long-sector reads compute a byte position from the sector size and signed sector id. Directory entries name root storage and user streams; small user streams are read through the short-sector path using the root storage stream and SSAT chain.

## Harness Contract
Use [[libfuzzer-libmagic-magic-buffer]]. The libmagic harness passes the raw file bytes directly to magic_buffer with no mode selector and no FuzzedDataProvider carving. The generated runner can report a wrapper-level clean result for some large files when invoked with an argument path, so direct container execution with the mounted implicit poc path and official submit are the reliable oracles for parser reachability.

## Evidence Shape
- Support: 1 server-verified round 33 solve.
- Candidate family: construct.
- Verifier key: `generic_crash x direct_container_parser_reached_and_submit_target_match`.
- Vulnerability class: `integer-overflow-to-heap-buffer-overflow-read`.
- Recovery summary: Build a CDF/OLE document whose header chooses the largest accepted long-sector size and whose SAT, SSAT, directory, and root stream are all reached through a sector id just beyond the multiplication boundary. In the vulnerable image, the overflowing long-sector position wraps to a controlled in-memory sector that supplies valid chain metadata and then reaches a deliberately narrow downstream short-stream read crash. In the fixed image, the overflowing long-sector position is rejected before those controlled sectors are consumed.

## Negative Memory
- Do not count parser reachability, both-image crashes, local-only wrapper crashes, clean exits, or fixed-image crashes as success for this key.
- Do not store raw payload bytes, exact positions, task identifiers, checksums, or submit metadata.
