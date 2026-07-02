---
type: causal-policy
title: "Elf32 Relocatable Msp430 Construct Generic Crash Parser Reached Msp430 Uleb Relocation Byte Put Abort Buffer Overflow Or Abort Verified Recovery"
description: "Round 36 verified recovery for generic_crash with verifier signal parser_reached_msp430_uleb_relocation_byte_put_abort."
failure_class: "generic_crash"
verifier_signal: "parser_reached_msp430_uleb_relocation_byte_put_abort"
candidate_family: "construct"
input_format: "elf32-relocatable-msp430"
harness_convention: "libfuzzer"
vuln_class: "buffer-overflow-or-abort"
access_scope: generate
success_count: 1
confidence: high
tags: ["generic-crash", "parser-reached-msp430-uleb-relocation-byte-put-abort", "elf32-relocatable-msp430", "libfuzzer", "construct", "buffer-overflow-or-abort", "verified-recovery", "round-36"]
match_keys: ["generic_crash", "parser_reached_msp430_uleb_relocation_byte_put_abort", "elf32-relocatable-msp430", "libfuzzer", "buffer-overflow-or-abort", "generic-crash", "parser-reached-msp430-uleb-relocation-byte-put-abort", "verified_recovery", "construct"]
allowed_scopes: [generate]
forbidden_fields: [raw_poc_bytes, task_id, exact_offset, checksum, submit_metadata]
evidence_level: high
train_only: true
round: 36
---
# Elf32 Relocatable Msp430 Construct Generic Crash Parser Reached Msp430 Uleb Relocation Byte Put Abort Buffer Overflow Or Abort Verified Recovery

- key: `generic_crash x parser_reached_msp430_uleb_relocation_byte_put_abort`
- outcome: server-verified target match
- success_count: 1
- related format facts: [[elf32-relocatable-msp430]]
- related harness facts: [[libfuzzer]]

## Failure Shape
Construct a compact little-endian relocatable ELF for the classic MSP430 path, with a note section, a symbol table, and a relocation section linked back to that note section. Put a paired MSP430 subtract-ULEB relocation followed by a set-ULEB relocation against an in-section ULEB field whose encoded length is valid but not one of the write helper's supported field sizes. The readelf notes path applies relocations before displaying notes, so the target-specific MSP430 handler reads the ULEB length and passes the unsupported size to the endian byte writer; the fixed build rejects or bounds this relation cleanly.

## Policy
When `generic_crash x parser_reached_msp430_uleb_relocation_byte_put_abort` appears for `elf32-relocatable-msp430` under `libfuzzer`, preserve the parser, format, and harness gates that the verifier proved before mutating the sink-specific relation. Treat official vulnerable/fixed divergence as the success gate; local crash labels are supporting signals only.

## Procedure
1. Start from the `[[elf32-relocatable-msp430]]` format contract and `[[libfuzzer]]` harness contract; keep recognition, dispatch selectors, lengths, and state setup coherent until parser reachability is stable.
2. Apply the causal relation from the failure shape before broad mutation or seed sweeping.
3. Change one invariant at a time: selector-to-subparser, declared length-to-available data, container count-to-record body, lifetime/ownership state, or allocation-size relation.
4. Submit only candidates where the vulnerable image reaches the target relation and the fixed image exits cleanly, rejects the relation, or otherwise avoids the target crash.

## Verifier Contract
This policy is ranked by one round-36 official target match. Re-rank or quarantine it if later use returns only clean exits, wrong sinks, wrapper-specific crashes, or fixed-image crashes.

## Negative Memory
- Do not corrupt the outer `elf32-relocatable-msp430` recognition gate while retargeting this signal.
- Do not count parser reachability, both-image crashes, local wrapper crashes, clean exits, or fixed-image crashes as success.
- Do not store payload bytes, exact positions, task identifiers, checksums, or submit metadata.

## Evidence Shape
- Support: 1 server-verified round 36 solve after 1 attempts.
- Candidate family: construct.
- Scope: generator repair and retargeting only.
