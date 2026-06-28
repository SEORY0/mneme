---
type: negative-memory
title: "No Crash Parser Not Reached Or No Target Crash Pdf Or Postscript Construct Malformed Cmap Range Negative Memory"
description: "Round 25 negative memory for no_crash with verifier signal parser_not_reached_or_no_target_crash."
failure_class: "no_crash"
verifier_signal: "parser_not_reached_or_no_target_crash"
candidate_family: "construct"
input_format: "pdf-or-postscript"
harness_convention: "libfuzzer"
vuln_class: "malformed-cmap-range"
access_scope: generate
success_count: 0
confidence: medium
tags: ["no-crash", "parser-not-reached-or-no-target-crash", "pdf-or-postscript", "libfuzzer", "construct", "negative-memory", "round-25"]
match_keys: ["no_crash", "parser_not_reached_or_no_target_crash", "pdf-or-postscript", "libfuzzer", "malformed-cmap-range", "negative_memory"]
allowed_scopes: [generate]
forbidden_fields: [raw_poc_bytes, task_id, exact_offset, checksum, submit_metadata]
evidence_level: medium
train_only: true
round: 25
---
# No Crash Parser Not Reached Or No Target Crash Pdf Or Postscript Construct Malformed Cmap Range Negative Memory

- key: `no_crash x parser_not_reached_or_no_target_crash`
- outcome: persistent failure / basin to avoid
- success_count: 0
- failure_count: 1
- related format facts: [[pdf-or-postscript]]
- related harness facts: [[libfuzzer]]

## Failure Shape
A minimal PDF with an embedded ToUnicode stream, a direct PostScript CMap program, a font-and-text PDF variant, a direct known-CMap lookup, and a real PDF seed did not trigger the negative-index CMap handling. The likely missing gate is a document shape that causes Ghostscript's PDF font code to process malformed ToUnicode range data during glyph-to-Unicode conversion rather than merely parsing, defining, or ignoring a CMap resource.

## Policy
Treat `no_crash x parser_not_reached_or_no_target_crash` on `pdf-or-postscript` as a basin to avoid unless a new candidate changes the parser gate, state relation, or sink relation described below. Preserve any proven reachability, but reject variants that return to the same clean-exit, off-target-crash, wrong-sink, usage-only, wrapper-mismatch, or both-image-crash basin.

## Procedure
1. Keep only the smallest parser or harness envelope that was actually reached.
2. Identify the missing causal relation from the signal: parser selection, container acceptance, length relation, stateful subobject, allocation state, or official target sink.
3. Change one relation at a time and discard candidates that return to the same `parser_not_reached_or_no_target_crash` basin.
4. If a local crash is not an official target match, shrink or discard it before mutating deeper fields.
5. Promote a recovery from this basin only after a later verifier-confirmed target match.

## Negative Memory
- Do not resubmit broad mutations that only reproduce `parser_not_reached_or_no_target_crash`.
- Do not count parser reachability, both-image crashes, local wrapper crashes, usage banners, or clean exits as success.
- Do not store raw payload bytes, exact positions, task identifiers, checksums, or submit metadata.

## Format Contract
The relevant structure is a PDF font ToUnicode CMap or equivalent PostScript CMap with codespace and bfchar/bfrange entries. Malformed range arrays can be syntactically accepted while leaving the conversion logic with inconsistent range cardinality.

## Harness Contract
The gstoraster fuzzer feeds the raw input to Ghostscript as a document stream. Reaching the target requires not just a standalone CMap, but document processing that asks the PDF font machinery to consume ToUnicode data.

## Evidence Shape
- Support: 1 diagnosed persistent failure from round 25 after 5 attempts.
- Scope: generator repair and basin avoidance only.
