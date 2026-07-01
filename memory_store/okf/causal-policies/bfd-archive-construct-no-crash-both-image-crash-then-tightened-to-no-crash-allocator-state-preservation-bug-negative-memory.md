---
type: causal-policy
title: "Bfd Archive Construct No Crash Both Image Crash Then Tightened To No Crash Allocator State Preservation Bug Negative Memory"
description: "Round 34 negative memory for bfd-archive when no_crash pairs with both_image_crash_then_tightened_to_no_crash."
failure_class: "no_crash"
verifier_signal: "both_image_crash_then_tightened_to_no_crash"
candidate_family: "construct"
input_format: "bfd-archive"
harness_convention: "libfuzzer"
vuln_class: "allocator-state-preservation-bug"
access_scope: generate
success_count: 0
confidence: medium
tags: ["no-crash", "both-image-crash-then-tightened-to-no-crash", "bfd-archive", "libfuzzer", "construct", "negative-memory", "round-34"]
match_keys: ["no-crash", "both-image-crash-then-tightened-to-no-crash", "bfd-archive", "libfuzzer", "construct", "allocator-state-preservation-bug", "negative-memory"]
allowed_scopes: [generate]
forbidden_fields: [raw_poc_bytes, task_id, exact_offset, checksum, submit_metadata]
evidence_level: medium
train_only: true
round: 34
---
# Bfd Archive Construct No Crash Both Image Crash Then Tightened To No Crash Allocator State Preservation Bug Negative Memory

- key: `no_crash x both_image_crash_then_tightened_to_no_crash`
- outcome: persistent failure / basin to avoid
- success_count: 0
- failure_count: 1
- related format facts: [[bfd-archive]]
- related harness facts: [[libfuzzer]]

## Round 34 Negative Support

- key: `no_crash x both_image_crash_then_tightened_to_no_crash`
- outcome: persistent failure / basin to avoid
- candidate family: `construct`
- vulnerability class: `allocator-state-preservation-bug`
- related format facts: [[bfd-archive]]
- related harness facts: [[libfuzzer]]

### Failure Shape
A malformed ECOFF-style archive map reached the archive target-probing code but crashed both vulnerable and fixed builds in a generic armap reader path. Tightening the armap endian/count relation removed that crash, and SysV ar, XCOFF old/new archive headers, BSD/COFF armaps, and a real ar archive sample stayed clean. The missing relation is a well-formed archive probe that leaves exactly the matched target's BFD allocator state live without falling into an unrelated armap parsing crash.

### Policy
Treat `no_crash x both_image_crash_then_tightened_to_no_crash` on `bfd-archive` as a basin to avoid unless a new candidate changes the parser gate, state relation, harness contract, or target sink relation described below. Preserve any proven reachability, but reject variants that return to the same signal without changing the causal gate under test.

### Procedure
1. Keep only the smallest parser or harness envelope that was actually reached.
2. Identify the missing causal relation from the signal: parser selection, container acceptance, length relation, stateful subobject, allocation state, or official target sink.
3. Change one relation at a time and discard candidates that return to the same clean-exit, off-target-crash, wrong-sink, usage-only, or both-image-crash basin.
4. Promote a recovery from this basin only after a later verifier-confirmed target match.

### Format Contract
BFD archive inputs are raw archive files. SysV ar archives have a global archive marker followed by fixed-format member headers and member bodies. BSD/COFF/ECOFF archive maps are represented as special first members; ECOFF map names encode header and object endianness, and their bodies contain a symbol count, map entries, and a string area. XCOFF archives use old or big archive headers with decimal file-position fields before member records.

### Harness Contract
The libFuzzer input is written verbatim to a temporary file, opened with the default BFD target, checked only as an archive with bfd_check_format, and then closed. There is no FuzzedDataProvider or byte carving; the trigger must arise from BFD target iteration, archive partial matches, and preserve/restore of BFD allocator state during format detection.

### Evidence Shape
- Support: one diagnosed persistent round 34 failure.
- Candidate family: `construct`.
- Verifier key: `no_crash x both_image_crash_then_tightened_to_no_crash`.
- Vulnerability class: `allocator-state-preservation-bug`.

## Negative Memory
- Do not count parser reachability, both-image crashes, fixed-image crashes, local wrapper crashes, clean exits, or off-target sanitizer crashes as success for this key.
- Do not store concrete payload bytes, exact positions, task identifiers, checksums, or submit metadata.
