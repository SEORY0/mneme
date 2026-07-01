---
type: causal-policy
title: "Jbig2 Construct Generic Crash Vul Crash Fix Clean Out Of Bounds Read Verified Recovery"
description: "Server-verified recovery for jbig2 when generic_crash pairs with vul_crash_fix_clean."
failure_class: "generic_crash"
verifier_signal: "vul_crash_fix_clean"
candidate_family: "construct"
input_format: "jbig2"
harness_convention: "libfuzzer"
vuln_class: "out-of-bounds-read"
access_scope: generate
success_count: 1
confidence: high
tags: ["generic-crash", "vul-crash-fix-clean", "jbig2", "libfuzzer", "construct", "verified-recovery", "round-33"]
match_keys: ["generic-crash", "vul-crash-fix-clean", "jbig2", "libfuzzer", "construct", "out-of-bounds-read", "verified-recovery"]
allowed_scopes: [generate]
forbidden_fields: [raw_poc_bytes, task_id, exact_offset, checksum, submit_metadata]
evidence_level: high
train_only: true
round: 33
---
# Jbig2 Construct Generic Crash Vul Crash Fix Clean Out Of Bounds Read Verified Recovery

- key: `generic_crash x vul_crash_fix_clean`
- outcome: server-verified vulnerable/fixed split
- success_count: 1
- related format facts: [[jbig2]]
- related harness facts: [[libfuzzer]]

## Policy
When `generic_crash x vul_crash_fix_clean` appears for `jbig2`, preserve the parser and harness gates that were proven by the verifier before mutating the sink-specific relation. Treat official vulnerable-only target match as the success gate, not a local coarse crash label.

## Procedure
1. Use the `libfuzzer` harness contract and the `jbig2` format contract before changing sink fields.
2. Recreate the causal relation from the verified trace: Build a sequential JBIG2 stream that reaches an immediate halftone region. The stream needs a page info segment, an MMR pattern dictionary segment, and a halftone segment that refers to that dictionary. Keep the halftone MMR payload at end-of-file and choose enough dictionary patterns that the halftone gray-scale decode uses multiple MMR bitplanes. The first short MMR bitplane can report more bytes consumed than were present; a later bitplane then uses the wrapped remaining-size calculation and reads past the available buffer. The fixed build rejects this accounting path cleanly.
3. Keep lengths, dispatch selectors, structural checks, and state setup coherent until the target parser state is reached.
4. Submit only after the fixed image exits cleanly or rejects the relation while the vulnerable image reaches the target sink.

## Format Contract
Use [[jbig2]]. JBIG2 files have a file signature, file flags, and optional page count, then sequential segment records. Segment records carry a segment number, type flags, referred-segment metadata, page association, declared data length, and segment body. Page information establishes the page before page-associated regions. Pattern dictionary bodies include MMR/template flags, pattern cell dimensions, a maximum gray value, and coded collective-bitmap data. Halftone region bodies include region placement, halftone flags, grid dimensions, grid origin and vectors, followed by coded gray-scale bitplane data.

## Harness Contract
Use [[libfuzzer]]. The fuzzer passes raw input bytes directly to jbig2_data_in and then completes and extracts the current page; there is no mode selector, wrapper format, checksum, or FuzzedDataProvider carving. Parser reachability depends entirely on presenting a structurally valid JBIG2 stream in those raw bytes.

## Evidence Shape
- Support: 1 server-verified round 33 solve.
- Candidate family: construct.
- Verifier key: `generic_crash x vul_crash_fix_clean`.
- Vulnerability class: `out-of-bounds-read`.
- Recovery summary: Build a sequential JBIG2 stream that reaches an immediate halftone region. The stream needs a page info segment, an MMR pattern dictionary segment, and a halftone segment that refers to that dictionary. Keep the halftone MMR payload at end-of-file and choose enough dictionary patterns that the halftone gray-scale decode uses multiple MMR bitplanes. The first short MMR bitplane can report more bytes consumed than were present; a later bitplane then uses the wrapped remaining-size calculation and reads past the available buffer. The fixed build rejects this accounting path cleanly.

## Negative Memory
- Do not count parser reachability, both-image crashes, local-only wrapper crashes, clean exits, or fixed-image crashes as success for this key.
- Do not store raw payload bytes, exact positions, task identifiers, checksums, or submit metadata.
