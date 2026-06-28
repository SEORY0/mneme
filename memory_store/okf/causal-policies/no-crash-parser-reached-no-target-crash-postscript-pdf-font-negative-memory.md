---
type: causal-policy
title: "No Crash Parser Reached No Target Crash Postscript Pdf Font Negative Memory"
description: "Round 13 negative memory for no_crash with verifier signal parser_reached_no_target_crash."
failure_class: "no_crash"
verifier_signal: "parser_reached_no_target_crash"
candidate_family: "construct"
input_format: "postscript-pdf-font"
harness_convention: "libfuzzer"
vuln_class: "heap-buffer-overflow-read"
access_scope: generate
success_count: 0
confidence: medium
tags: ["no-crash", "parser-reached-no-target-crash", "postscript-pdf-font", "negative-memory", "round-13"]
match_keys: ["no_crash", "parser_reached_no_target_crash", "postscript-pdf-font", "libfuzzer", "heap-buffer-overflow-read", "negative_memory"]
allowed_scopes: [generate]
forbidden_fields: [raw_poc_bytes, task_id, exact_offset, checksum, submit_metadata]
evidence_level: medium
train_only: true
round: 13
---
# No Crash Parser Reached No Target Crash Postscript Pdf Font Negative Memory

- key: `no_crash x parser_reached_no_target_crash`
- outcome: persistent failure / basin to avoid
- success_count: 0
- failure_count: 1
- related format facts: [[postscript-pdf-font]]
- related harness facts: [[libfuzzer]]

## Failure Shape
Minimal PostScript, Type 3 font, malformed Type 42 font, simple PDF font, and malformed TrueType-stream hypotheses did not trigger the FreeType fallback path. The missing condition is likely a valid enough TrueType glyph program that enters the extremis fallback while leaving a partial glyph bitmap state.

## Policy
Treat `no_crash x parser_reached_no_target_crash` on `postscript-pdf-font` as a basin to avoid unless a new candidate changes the specific parser gate, state relation, or sink relation described below. Preserve any proven reachability, but reject variants that return to the same clean-exit, off-target-crash, wrong-sink, usage-only, or both-image-crash basin.

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
Ghostscript accepts PostScript and PDF inputs and can route embedded or declared fonts through FreeType. The described bug depends on a glyph rendering path where a fallback return code is ignored and partially initialized glyph bitmap data is later consumed.

## Harness Contract
The harness feeds raw document bytes to the Ghostscript raster conversion target. There is no fuzzer-side byte carving; document syntax and font embedding are responsible for reaching the FreeType glyph path.

## Evidence Shape
- Support: 1 diagnosed persistent failure from round 13.
- Scope: generator repair and basin avoidance only.
## Round 13 Failure Reinforcement

- key: `no_crash x parser_reached_no_target_crash`
- related format facts: [[postscript-pdf-font]]
- related harness facts: [[libfuzzer]]

### Failure Shape Delta
Minimal PostScript, Type 3 font, malformed Type 42 font, simple PDF font, and malformed TrueType-stream hypotheses did not trigger the FreeType fallback path. The missing condition is likely a valid enough TrueType glyph program that enters the extremis fallback while leaving a partial glyph bitmap state.

### Format Contract Delta
Ghostscript accepts PostScript and PDF inputs and can route embedded or declared fonts through FreeType. The described bug depends on a glyph rendering path where a fallback return code is ignored and partially initialized glyph bitmap data is later consumed.

### Harness Contract Delta
The harness feeds raw document bytes to the Ghostscript raster conversion target. There is no fuzzer-side byte carving; document syntax and font embedding are responsible for reaching the FreeType glyph path.

### Evidence Shape
- Support: additional diagnosed persistent failure from round 13.
- Scope: generator repair and basin avoidance only.
