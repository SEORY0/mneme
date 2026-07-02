---
type: causal-policy
title: "Png Seed Mutate Generic Crash Parser Reached Validate Past Idat Exif Copy Crash Wild Address Read Verified Recovery"
description: "Server-verified recovery for png when generic_crash pairs with parser_reached_validate_past_idat_exif_copy_crash."
failure_class: "generic_crash"
verifier_signal: "parser_reached_validate_past_idat_exif_copy_crash"
candidate_family: "seed_mutate"
input_format: "png"
harness_convention: "libfuzzer-spng-read"
vuln_class: "wild-address-read"
access_scope: generate
success_count: 1
confidence: high
tags: ["generic-crash", "parser-reached-validate-past-idat-exif-copy-crash", "png", "libfuzzer-spng-read", "seed-mutate", "verified-recovery", "round-33"]
match_keys: ["generic-crash", "parser-reached-validate-past-idat-exif-copy-crash", "png", "libfuzzer-spng-read", "seed-mutate", "wild-address-read", "verified-recovery"]
allowed_scopes: [generate]
forbidden_fields: [raw_poc_bytes, task_id, exact_offset, checksum, submit_metadata]
evidence_level: high
train_only: true
round: 33
---
# Png Seed Mutate Generic Crash Parser Reached Validate Past Idat Exif Copy Crash Wild Address Read Verified Recovery

- key: `generic_crash x parser_reached_validate_past_idat_exif_copy_crash`
- outcome: server-verified vulnerable/fixed split
- success_count: 1
- related format facts: [[png]]
- related harness facts: [[libfuzzer-spng-read]]

## Policy
When `generic_crash x parser_reached_validate_past_idat_exif_copy_crash` appears for `png`, preserve the parser and harness gates that were proven by the verifier before mutating the sink-specific relation. Treat official vulnerable-only target match as the success gate, not a local coarse crash label.

## Procedure
1. Use the `libfuzzer-spng-read` harness contract and the `png` format contract before changing sink fields.
2. Recreate the causal relation from the verified trace: Start from a valid PNG seed that already decodes through libspng. Preserve the image header, IDAT data, IEND, and all required chunk CRCs. Remove the normal pre-IDAT eXIf chunk, then insert a single undersized eXIf ancillary chunk after IDAT but before IEND. Keep the eXIf chunk non-empty but shorter than a valid EXIF byte-order header so the vulnerable post-IDAT validation path copies from its stale/uninitialized chunk-data pointer before the EXIF size check rejects it. The fixed build rejects the undersized eXIf chunk without the invalid read.
3. Keep lengths, dispatch selectors, structural checks, and state setup coherent until the target parser state is reached.
4. Submit only after the fixed image exits cleanly or rejects the relation while the vulnerable image reaches the target sink.

## Format Contract
Use [[png]]. PNG files start with a fixed signature and are a sequence of length, type, data, and CRC chunks. IHDR must appear first, IDAT carries compressed image data, and IEND terminates the file. eXIf is an ancillary chunk whose payload should contain at least an EXIF/TIFF byte-order header. CRCs are checked by this harness, so any mutation that changes chunk type or data must recompute the chunk CRC. Placing an ancillary chunk after IDAT exercises a different validation path than placing the same chunk before IDAT.

## Harness Contract
Use [[libfuzzer-spng-read]]. The libspng read fuzzer passes the entire PoC as a PNG buffer with no leading selector and no FuzzedDataProvider carving. It sets CRC checking on both critical and ancillary chunks, computes the decoded RGBA size, allocates an output buffer, then calls image decode with tRNS, gAMA, and sBIT decode flags enabled.

## Evidence Shape
- Support: 1 server-verified round 33 solve.
- Candidate family: seed_mutate.
- Verifier key: `generic_crash x parser_reached_validate_past_idat_exif_copy_crash`.
- Vulnerability class: `wild-address-read`.
- Recovery summary: Start from a valid PNG seed that already decodes through libspng. Preserve the image header, IDAT data, IEND, and all required chunk CRCs. Remove the normal pre-IDAT eXIf chunk, then insert a single undersized eXIf ancillary chunk after IDAT but before IEND. Keep the eXIf chunk non-empty but shorter than a valid EXIF byte-order header so the vulnerable post-IDAT validation path copies from its stale/uninitialized chunk-data pointer before the EXIF size check rejects it. The fixed build rejects the undersized eXIf chunk without the invalid read.

## Negative Memory
- Do not count parser reachability, both-image crashes, local-only wrapper crashes, clean exits, or fixed-image crashes as success for this key.
- Do not store raw payload bytes, exact positions, task identifiers, checksums, or submit metadata.
