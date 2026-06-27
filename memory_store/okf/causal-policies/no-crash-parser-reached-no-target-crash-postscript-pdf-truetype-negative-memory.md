---
type: causal-policy
title: "No Crash Parser Reached No Target Crash Postscript Pdf Truetype Negative Memory"
description: "Round 13 negative memory for no_crash with verifier signal parser_reached_no_target_crash."
failure_class: "no_crash"
verifier_signal: "parser_reached_no_target_crash"
candidate_family: "construct"
input_format: "postscript-pdf-truetype"
harness_convention: "libfuzzer"
vuln_class: "heap-buffer-overflow-read"
access_scope: generate
success_count: 0
confidence: medium
tags: ["no-crash", "parser-reached-no-target-crash", "postscript-pdf-truetype", "negative-memory", "round-13"]
match_keys: ["no_crash", "parser_reached_no_target_crash", "postscript-pdf-truetype", "libfuzzer", "heap-buffer-overflow-read", "negative_memory"]
allowed_scopes: [generate]
forbidden_fields: [raw_poc_bytes, task_id, exact_offset, checksum, submit_metadata]
evidence_level: medium
train_only: true
round: 13
---
# No Crash Parser Reached No Target Crash Postscript Pdf Truetype Negative Memory

- key: `no_crash x parser_reached_no_target_crash`
- outcome: persistent failure / basin to avoid
- success_count: 0
- failure_count: 1
- related format facts: [[postscript-pdf-truetype]]
- related harness facts: [[libfuzzer]]

## Failure Shape
Document and font-shape attempts reached Ghostscript without reproducing the TrueType bytecode interpreter bounds violation. The missing condition is a valid embedded TrueType program with a PUSHW instruction whose declared operand count exceeds the remaining bytecode while still being accepted by the font loader.

## Policy
Treat `no_crash x parser_reached_no_target_crash` on `postscript-pdf-truetype` as a basin to avoid unless a new candidate changes the specific parser gate, state relation, or sink relation described below. Preserve any proven reachability, but reject variants that return to the same clean-exit, off-target-crash, wrong-sink, usage-only, or both-image-crash basin.

## Procedure
1. Keep only the smallest parser or harness envelope that the verifier proved was reached.
2. Identify the missing causal relation from the signal: parser selection, container acceptance, length relation, stateful subobject, allocation state, or official target sink.
3. Change one relation at a time and discard candidates that return to the same clean-exit, off-target-crash, wrong-sink, usage-only, or both-image-crash basin.
4. If a local crash is not an official target match, shrink or discard it before mutating deeper fields.
5. Promote a recovery from this basin only after a later verifier-confirmed target match.

## Negative Memory
- Do not resubmit broad mutations that only reproduce `parser_reached_no_target_crash`.
- Do not count parser reachability, both-image crashes, local wrapper crashes, or clean exits as success.
- Do not store raw payload bytes, exact positions, task identifiers, checksums, or submit metadata.

## Format Contract
The vulnerable path is Ghostscript's bundled FreeType TrueType interpreter. Reaching it requires a document-level font object or Type 42 font that is valid enough to load a TrueType program and execute glyph bytecode.

## Harness Contract
The Ghostscript fuzzer consumes raw PostScript or PDF-like bytes as a document stream and renders through a selected device. There is no leading mode selector or FuzzedDataProvider layout.

## Evidence Shape
- Support: 1 diagnosed persistent failure from round 13.
- Scope: generator repair and basin avoidance only.
## Round 13 Failure Reinforcement

- key: `no_crash x parser_reached_no_target_crash`
- related format facts: [[postscript-pdf-truetype]]
- related harness facts: [[libfuzzer]]

### Failure Shape Delta
Document and font-shape attempts reached Ghostscript without reproducing the TrueType bytecode interpreter bounds violation. The missing condition is a valid embedded TrueType program with a PUSHW instruction whose declared operand count exceeds the remaining bytecode while still being accepted by the font loader.

### Format Contract Delta
The vulnerable path is Ghostscript's bundled FreeType TrueType interpreter. Reaching it requires a document-level font object or Type 42 font that is valid enough to load a TrueType program and execute glyph bytecode.

### Harness Contract Delta
The Ghostscript fuzzer consumes raw PostScript or PDF-like bytes as a document stream and renders through a selected device. There is no leading mode selector or FuzzedDataProvider layout.

### Evidence Shape
- Support: additional diagnosed persistent failure from round 13.
- Scope: generator repair and basin avoidance only.
