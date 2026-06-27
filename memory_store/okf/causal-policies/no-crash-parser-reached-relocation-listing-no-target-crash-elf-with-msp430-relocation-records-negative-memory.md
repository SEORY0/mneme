---
type: causal-policy
title: "No Crash Parser Reached Relocation Listing No Target Crash ELF With Msp430 Relocation Records Negative Memory"
description: "Round 9 negative memory for no_crash with verifier signal parser_reached_relocation_listing_no_target_crash."
failure_class: "no_crash"
verifier_signal: "parser_reached_relocation_listing_no_target_crash"
candidate_family: "seed_mutate"
input_format: "ELF with MSP430 relocation records"
harness_convention: "libfuzzer"
vuln_class: "out-of-bounds-read-or-write"
access_scope: generate
success_count: 0
confidence: medium
tags: ["no-crash", "parser-reached-relocation-listing-no-target-crash", "elf-with-msp430-relocation-records", "negative-memory", "round-9"]
match_keys: ["no_crash", "parser_reached_relocation_listing_no_target_crash", "ELF with MSP430 relocation records", "libfuzzer", "out-of-bounds-read-or-write", "negative_memory"]
allowed_scopes: [generate]
forbidden_fields: [raw_poc_bytes, task_id, exact_offset, checksum, submit_metadata]
evidence_level: medium
train_only: true
round: 9
---
# No Crash Parser Reached Relocation Listing No Target Crash ELF With Msp430 Relocation Records Negative Memory

- key: `no_crash x parser_reached_relocation_listing_no_target_crash`
- outcome: persistent failure / basin to avoid
- success_count: 0
- failure_count: 1
- related format facts: [[elf-with-msp430-relocation-records]]
- related harness facts: [[libfuzzer]]

## Failure Shape
- A valid ELF seed could be mutated so readelf recognized the file as MSP430 and printed relocation
  data, but the tested mutations did not drive the relocation-application path that calls the
  target-specific MSP430 ULEB handler.
- The remaining gap is likely enabling a relocated dump or a debug/unwind section that causes
  relocations to be applied to section bytes, not merely listed.

## Policy
Treat `no_crash x parser_reached_relocation_listing_no_target_crash` on `ELF with MSP430 relocation records` as a basin to avoid unless a new candidate changes the parser gate, state relation, or official target sink. Preserve any proven reachability, but reject variants that return to the same verifier signal without changing the causal gate under test.

## Procedure
1. Keep only the smallest parser or harness envelope that the verifier proved was reached.
2. Identify the missing causal relation from the signal: parser selection, container acceptance, length relation, stateful subobject, allocation state, or official target sink.
3. Change one relation at a time and discard candidates that return to the same clean-exit, off-target-crash, wrong-sink, usage-only, or both-image-crash basin.
4. If a local crash is not an official target match, shrink or discard it before mutating deeper fields.
5. Promote a recovery from this basin only after a later verifier-confirmed target match.

## Format Contract
- The useful seed was an ELF object with section headers, dynamic symbols, and a relocation section.
- For the MSP430-specific path, the ELF machine must identify MSP430, the relocation section must
  link to a symbol table, and paired subtract/set ULEB relocation records must refer to an in-file
  target section.

## Harness Contract
- libFuzzer writes the raw bytes to a temporary file and invokes readelf-style processing with
  headers, sections, symbols, relocations, dynamic data, unwind, notes, and architecture reporting
  enabled.
- The harness does not use a length prefix or mode selector.

## Negative Memory
- Do not resubmit broad mutations that only reproduce `parser_reached_relocation_listing_no_target_crash`.
- Do not count parser reachability, both-image crashes, local wrapper crashes, clean exits, or fixed-image crashes as success.
- Do not store raw payload bytes, exact positions, task identifiers, or submit metadata.

## Evidence Shape
- Support: one diagnosed persistent failure from round 9.
- Scope: generator repair and basin avoidance only.
