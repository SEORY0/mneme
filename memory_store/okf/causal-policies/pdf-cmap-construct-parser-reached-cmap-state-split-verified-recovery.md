---
type: causal-policy
title: "Pdf Cmap Construct Parser Reached Cmap State Split Verified Recovery"
description: "Round 12 verified recovery for generic_crash with verifier signal parser_reached."
failure_class: "generic_crash"
verifier_signal: "parser_reached"
candidate_family: "construct"
input_format: "pdf-cmap"
harness_convention: "libfuzzer"
vuln_class: "cmap-state-split"
access_scope: generate
success_count: 1
confidence: high
tags: ["generic-crash", "parser-reached", "pdf-cmap", "verified-recovery", "round-12"]
match_keys: ["generic_crash", "parser_reached", "pdf-cmap", "libfuzzer", "cmap-state-split", "verified_recovery"]
allowed_scopes: [generate]
forbidden_fields: [raw_poc_bytes, task_id, exact_offset, checksum, submit_metadata]
evidence_level: high
train_only: true
round: 12
---
# Pdf Cmap Construct Parser Reached Cmap State Split Verified Recovery

- key: `generic_crash x parser_reached`
- outcome: verified recovery
- confidence: 0.82
- success_count: 1
- failure_count: 0
- formats: [[pdf-cmap]]
- harnesses: [[libfuzzer]]

## Failure Shape
The verifier-confirmed candidate preserved the `pdf-cmap` parser envelope under `libfuzzer` and moved the mutation into the relation consumed by the target sink instead of relying on broad corruption.

## Policy
Use this policy when generation reports `generic_crash` with signal `parser_reached` on `pdf-cmap` or the same format family. Preserve parser reachability first, then adjust only the smallest format relation named in the procedure until the vulnerable build crashes and the fixed build stays clean.

## Procedure
Build a minimal valid PDF with a page, a font resource, a ToUnicode CMap stream, and page content that uses that font. In the CMap, combine a broad range mapping with later one-to-many mappings that overlap and split existing cmap tree nodes; rendering text forces lookup through the corrupted one-to-many state.

## Verifier Contract
The official comparison must show target match with a vulnerable-build crash and a clean fixed build. Parser reachability, local-only crashes, off-target crashes, or both-image crashes are not sufficient.

## Format Contract
A PDF ToUnicode CMap is stored as a stream referenced by a font. It declares codespace ranges, then bfchar and bfrange mappings. One-to-many Unicode mappings can appear in bfchar entries or array-based bfrange entries, and overlapping ranges force cmap node splitting.

## Harness Contract
The MuPDF PDF fuzzer consumes raw PDF bytes. The document must be structurally valid enough to load a page, resolve resources, load the font's ToUnicode CMap, and render or interpret text content.

## Negative Guards
- Do not store raw payload bytes, exact positions, task identifiers, or submit metadata.
- Do not widen mutation after the parser envelope is accepted; shrink back to the single boundary relation when the fixed image also crashes.
- Do not promote this policy to another format unless the same failure key and verifier signal recur under official comparison.
