---
type: causal-policy
title: "Pdf Construct Wrong Sink Parser Reached Use Of Uninitialized Value Use Of Uninitialized Value Verified Recovery"
description: "Server-verified recovery for pdf when wrong_sink pairs with parser_reached_use_of_uninitialized_value."
failure_class: "wrong_sink"
verifier_signal: "parser_reached_use_of_uninitialized_value"
candidate_family: "construct"
input_format: "pdf"
harness_convention: "libfuzzer-poppler-pdf-render"
vuln_class: "use-of-uninitialized-value"
access_scope: generate
success_count: 1
confidence: high
tags: ["wrong-sink", "parser-reached-use-of-uninitialized-value", "pdf", "libfuzzer-poppler-pdf-render", "construct", "verified-recovery", "round-33"]
match_keys: ["wrong-sink", "parser-reached-use-of-uninitialized-value", "pdf", "libfuzzer-poppler-pdf-render", "construct", "use-of-uninitialized-value", "verified-recovery"]
allowed_scopes: [generate]
forbidden_fields: [raw_poc_bytes, task_id, exact_offset, checksum, submit_metadata]
evidence_level: high
train_only: true
round: 33
---
# Pdf Construct Wrong Sink Parser Reached Use Of Uninitialized Value Use Of Uninitialized Value Verified Recovery

- key: `wrong_sink x parser_reached_use_of_uninitialized_value`
- outcome: server-verified vulnerable/fixed split
- success_count: 1
- related format facts: [[pdf]]
- related harness facts: [[libfuzzer-poppler-pdf-render]]

## Policy
When `wrong_sink x parser_reached_use_of_uninitialized_value` appears for `pdf`, preserve the parser and harness gates that were proven by the verifier before mutating the sink-specific relation. Treat official vulnerable-only target match as the success gate, not a local coarse crash label.

## Procedure
1. Use the `libfuzzer-poppler-pdf-render` harness contract and the `pdf` format contract before changing sink fields.
2. Recreate the causal relation from the verified trace: Build a complete PDF with a page annotation that forces Poppler to generate a choice-widget appearance during rendering. Provide AcroForm default resources and a non-auto font size so the listbox layout path uses measured text width. Put an invalid non-string option in the choice list and use centered or right quadding, causing the layout helper to return early without initializing the width output that the appearance builder later consumes.
3. Keep lengths, dispatch selectors, structural checks, and state setup coherent until the target parser state is reached.
4. Submit only after the fixed image exits cleanly or rejects the relation while the vulnerable image reaches the target sink.

## Format Contract
Use [[pdf]]. PDF AcroForm widget annotations can be drawn during page rendering when no appearance stream is supplied. Choice fields read options from the Opt array; invalid option entries may yield null display text. Default appearance and default resources must name a usable font before the appearance builder reaches text layout. Quadding controls whether measured text width affects emitted drawing commands.

## Harness Contract
Use [[libfuzzer-poppler-pdf-render]]. The libFuzzer input is used directly as PDF bytes through Poppler's raw-data document loader. If the document loads and is not locked, the harness renders pages, including annotations. There is no mode selector, FuzzedDataProvider consumption, or external file wrapper.

## Evidence Shape
- Support: 1 server-verified round 33 solve.
- Candidate family: construct.
- Verifier key: `wrong_sink x parser_reached_use_of_uninitialized_value`.
- Vulnerability class: `use-of-uninitialized-value`.
- Recovery summary: Build a complete PDF with a page annotation that forces Poppler to generate a choice-widget appearance during rendering. Provide AcroForm default resources and a non-auto font size so the listbox layout path uses measured text width. Put an invalid non-string option in the choice list and use centered or right quadding, causing the layout helper to return early without initializing the width output that the appearance builder later consumes.

## Negative Memory
- Do not count parser reachability, both-image crashes, local-only wrapper crashes, clean exits, or fixed-image crashes as success for this key.
- Do not store raw payload bytes, exact positions, task identifiers, checksums, or submit metadata.
