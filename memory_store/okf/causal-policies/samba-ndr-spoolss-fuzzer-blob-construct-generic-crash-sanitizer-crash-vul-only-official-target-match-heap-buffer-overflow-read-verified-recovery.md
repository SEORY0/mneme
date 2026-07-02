---
type: causal-policy
title: "Samba Ndr Spoolss Fuzzer Blob Construct Generic Crash Sanitizer Crash Vul Only Official Target Match Heap Buffer Overflow Read Verified Recovery"
description: "Round 34 verified recovery for samba-ndr-spoolss-fuzzer-blob when generic_crash pairs with sanitizer_crash_vul_only_official_target_match."
failure_class: "generic_crash"
verifier_signal: "sanitizer_crash_vul_only_official_target_match"
candidate_family: "construct"
input_format: "samba-ndr-spoolss-fuzzer-blob"
harness_convention: "libfuzzer"
vuln_class: "heap-buffer-overflow-read"
access_scope: generate
success_count: 1
confidence: high
tags: ["generic-crash", "sanitizer-crash-vul-only-official-target-match", "samba-ndr-spoolss-fuzzer-blob", "libfuzzer", "construct", "verified-recovery", "round-34"]
match_keys: ["generic-crash", "sanitizer-crash-vul-only-official-target-match", "samba-ndr-spoolss-fuzzer-blob", "libfuzzer", "construct", "heap-buffer-overflow-read", "verified-recovery"]
allowed_scopes: [generate]
forbidden_fields: [raw_poc_bytes, task_id, exact_offset, checksum, submit_metadata]
evidence_level: high
train_only: true
round: 34
---
# Samba Ndr Spoolss Fuzzer Blob Construct Generic Crash Sanitizer Crash Vul Only Official Target Match Heap Buffer Overflow Read Verified Recovery

- key: `generic_crash x sanitizer_crash_vul_only_official_target_match`
- outcome: server-verified vulnerable/fixed split
- success_count: 1
- related format facts: [[samba-ndr-spoolss-fuzzer-blob]]
- related harness facts: [[libfuzzer]]

## Round 34 Verified Support

- key: `generic_crash x sanitizer_crash_vul_only_official_target_match`
- outcome: server-verified vulnerable/fixed split
- candidate family: `construct`
- vulnerability class: `heap-buffer-overflow-read`
- related format facts: [[samba-ndr-spoolss-fuzzer-blob]]
- related harness facts: [[libfuzzer]]

### Policy
When `generic_crash x sanitizer_crash_vul_only_official_target_match` appears for `samba-ndr-spoolss-fuzzer-blob`, preserve the accepted parser and harness gates, then target the specific state relation that the verifier proved. Treat the official vulnerable-only target match as the success gate; local crash class alone is not enough.

### Procedure
1. Use the [[libfuzzer]] harness contract and the [[samba-ndr-spoolss-fuzzer-blob]] format contract before changing sink fields.
2. Recreate the verified causal relation: Use the raw Samba NDR fuzzer header for TYPE_STRUCT and select the public spoolss struct whose first field is a fixed UTF-16 to_null array. Provide that fixed array as nonzero UTF-16 code units and omit a terminator or later struct fields so ndr_pull_charset_to_null performs an unbounded terminator scan before any later field is needed.
3. Keep selectors, lengths, state setup, and container invariants coherent until the target parser state is reached.
4. Submit only when the candidate is expected to preserve the vulnerable/fixed split rather than a generic both-build crash.

### Format Contract
The blob starts with little-endian flags/type and a public-struct selector, then TYPE_STRUCT passes the remaining bytes as a raw NDR stub. Fixed charset(UTF16),to_null arrays are parsed as zero-code-unit-terminated strings, not single-byte strings.

### Harness Contract
libFuzzer passes raw bytes. The harness consumes two little-endian 16-bit header fields from the front and sends the remaining bytes to Samba NDR pull logic. There is no FuzzedDataProvider and no trailing selector.

### Evidence Shape
- Support: one server-verified round 34 solve.
- Candidate family: `construct`.
- Verifier key: `generic_crash x sanitizer_crash_vul_only_official_target_match`.
- Vulnerability class: `heap-buffer-overflow-read`.

## Negative Memory
- Do not count parser reachability, both-image crashes, fixed-image crashes, local wrapper crashes, clean exits, or off-target sanitizer crashes as success for this key.
- Do not store concrete payload bytes, exact positions, task identifiers, checksums, or submit metadata.
