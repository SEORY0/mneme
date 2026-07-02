---
type: causal-policy
title: "Pdf Construct Wrong Sink Parser Reached Uninitialized Alpha Read In Color Key Mask Use Of Uninitialized Value From Image Alpha Padding Verified Recovery"
description: "Server-verified recovery for pdf when wrong_sink pairs with parser_reached_uninitialized_alpha_read_in_color_key_mask."
failure_class: "wrong_sink"
verifier_signal: "parser_reached_uninitialized_alpha_read_in_color_key_mask"
candidate_family: "construct"
input_format: "pdf"
harness_convention: "libfuzzer"
vuln_class: "use-of-uninitialized-value from image alpha padding"
access_scope: generate
success_count: 1
confidence: high
tags: ["wrong-sink", "parser-reached-uninitialized-alpha-read-in-color-key-mask", "pdf", "libfuzzer", "construct", "verified-recovery", "round-33"]
match_keys: ["wrong-sink", "parser-reached-uninitialized-alpha-read-in-color-key-mask", "pdf", "libfuzzer", "construct", "use-of-uninitialized-value-from-image-alpha-padding", "verified-recovery"]
allowed_scopes: [generate]
forbidden_fields: [raw_poc_bytes, task_id, exact_offset, checksum, submit_metadata]
evidence_level: high
train_only: true
round: 33
---
# Pdf Construct Wrong Sink Parser Reached Uninitialized Alpha Read In Color Key Mask Use Of Uninitialized Value From Image Alpha Padding Verified Recovery

- key: `wrong_sink x parser_reached_uninitialized_alpha_read_in_color_key_mask`
- outcome: server-verified vulnerable/fixed split
- success_count: 1
- related format facts: [[pdf]]
- related harness facts: [[libfuzzer]]

## Policy
When `wrong_sink x parser_reached_uninitialized_alpha_read_in_color_key_mask` appears for `pdf`, preserve the parser and harness gates that were proven by the verifier before mutating the sink-specific relation. Treat official vulnerable-only target match as the success gate, not a local coarse crash label.

## Procedure
1. Use the `libfuzzer` harness contract and the `pdf` format contract before changing sink fields.
2. Recreate the causal relation from the verified trace: Build a small renderable PDF with a page image XObject that is drawn by the page contents. The image must use a color-key mask so MuPDF allocates an added alpha component, but the image samples should not match the color-key range. Use an accepted non-fast-path component bit depth so image unpacking takes the generic bit reader; that path writes color components but leaves the padded alpha component uninitialized. Rendering the page then reads that alpha through the color-key path, while the fixed build initializes the padding cleanly.
3. Keep lengths, dispatch selectors, structural checks, and state setup coherent until the target parser state is reached.
4. Submit only after the fixed image exits cleanly or rejects the relation while the vulnerable image reaches the target sink.

## Format Contract
Use [[pdf]]. A PDF image XObject can be reached from page resources and painted with a short content stream. A color-key /Mask array creates an alpha-bearing destination pixmap even when the source colorspace has only color components. MuPDF accepts image component depths beyond the common PDF fast paths as long as they are within its supported range; the image stream length must match the derived stride and height so the image is not merely truncated.

## Harness Contract
Use [[libfuzzer]]. The MuPDF PDF fuzzer consumes the submitted file as raw PDF bytes from memory, opens it as a PDF document, and renders page contents to a pixmap. There is no mode byte, archive wrapper, checksum gate, or FuzzedDataProvider carving.

## Evidence Shape
- Support: 1 server-verified round 33 solve.
- Candidate family: construct.
- Verifier key: `wrong_sink x parser_reached_uninitialized_alpha_read_in_color_key_mask`.
- Vulnerability class: `use-of-uninitialized-value from image alpha padding`.
- Recovery summary: Build a small renderable PDF with a page image XObject that is drawn by the page contents. The image must use a color-key mask so MuPDF allocates an added alpha component, but the image samples should not match the color-key range. Use an accepted non-fast-path component bit depth so image unpacking takes the generic bit reader; that path writes color components but leaves the padded alpha component uninitialized. Rendering the page then reads that alpha through the color-key path, while the fixed build initializes the padding cleanly.

## Negative Memory
- Do not count parser reachability, both-image crashes, local-only wrapper crashes, clean exits, or fixed-image crashes as success for this key.
- Do not store raw payload bytes, exact positions, task identifiers, checksums, or submit metadata.
