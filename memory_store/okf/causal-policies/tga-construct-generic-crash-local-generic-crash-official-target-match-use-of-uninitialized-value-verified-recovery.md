---
type: causal-policy
title: "Tga Construct Generic Crash Local Generic Crash Official Target Match Use Of Uninitialized Value Verified Recovery"
description: "Server-verified recovery for tga when generic_crash pairs with local_generic_crash_official_target_match."
failure_class: "generic_crash"
verifier_signal: "local_generic_crash_official_target_match"
candidate_family: "construct"
input_format: "tga"
harness_convention: "libfuzzer-kimageformats-raw-qbuffer"
vuln_class: "use-of-uninitialized-value"
access_scope: generate
success_count: 1
confidence: high
tags: ["generic-crash", "local-generic-crash-official-target-match", "tga", "libfuzzer-kimageformats-raw-qbuffer", "construct", "verified-recovery", "round-33"]
match_keys: ["generic-crash", "local-generic-crash-official-target-match", "tga", "libfuzzer-kimageformats-raw-qbuffer", "construct", "use-of-uninitialized-value", "verified-recovery"]
allowed_scopes: [generate]
forbidden_fields: [raw_poc_bytes, task_id, exact_offset, checksum, submit_metadata]
evidence_level: high
train_only: true
round: 33
---
# Tga Construct Generic Crash Local Generic Crash Official Target Match Use Of Uninitialized Value Verified Recovery

- key: `generic_crash x local_generic_crash_official_target_match`
- outcome: server-verified vulnerable/fixed split
- success_count: 1
- related format facts: [[tga]]
- related harness facts: [[libfuzzer-kimageformats-raw-qbuffer]]

## Policy
When `generic_crash x local_generic_crash_official_target_match` appears for `tga`, preserve the parser and harness gates that were proven by the verifier before mutating the sink-specific relation. Treat official vulnerable-only target match as the success gate, not a local coarse crash label.

## Procedure
1. Use the `libfuzzer-kimageformats-raw-qbuffer` harness contract and the `tga` format contract before changing sink fields.
2. Recreate the causal relation from the verified trace: Construct a compact indexed RLE TGA that passes the TGA support gates, including palette-mode, dimension, pixel-depth, and RLE image-type checks. Use a raw RLE packet whose declared run requires more index bytes than the file supplies, so the vulnerable decoder advances the destination pointer after a failed or short read and later expands uninitialized destination data through the palette conversion path. Keep the outer header otherwise coherent so the fixed build can reject or zero-fill the underfilled packet cleanly.
3. Keep lengths, dispatch selectors, structural checks, and state setup coherent until the target parser state is reached.
4. Submit only after the fixed image exits cleanly or rejects the relation while the vulnerable image reaches the target sink.

## Format Contract
Use [[tga]]. TGA inputs are raw files with a fixed little-endian header containing image type, palette descriptor, dimensions, pixel depth, descriptor flags, optional image ID, optional palette data, and then image data. RLE image data is a sequence of packet headers; each header selects raw-run versus repeated-pixel form and declares a pixel or index count. Indexed images require palette-mode header fields that pass support checks before the image buffer is converted through palette lookup.

## Harness Contract
Use [[libfuzzer-kimageformats-raw-qbuffer]]. The kimageformats libFuzzer harness feeds the PoC bytes directly into a QBuffer, then calls the TGA QImageIOHandler canRead and read methods. There is no filename extension, pcap wrapper, selector byte, checksum, or FuzzedDataProvider front/back carving; all reachability is controlled by the raw TGA bytes.

## Evidence Shape
- Support: 1 server-verified round 33 solve.
- Candidate family: construct.
- Verifier key: `generic_crash x local_generic_crash_official_target_match`.
- Vulnerability class: `use-of-uninitialized-value`.
- Recovery summary: Construct a compact indexed RLE TGA that passes the TGA support gates, including palette-mode, dimension, pixel-depth, and RLE image-type checks. Use a raw RLE packet whose declared run requires more index bytes than the file supplies, so the vulnerable decoder advances the destination pointer after a failed or short read and later expands uninitialized destination data through the palette conversion path. Keep the outer header otherwise coherent so the fixed build can reject or zero-fill the underfilled packet cleanly.

## Negative Memory
- Do not count parser reachability, both-image crashes, local-only wrapper crashes, clean exits, or fixed-image crashes as success for this key.
- Do not store raw payload bytes, exact positions, task identifiers, checksums, or submit metadata.
