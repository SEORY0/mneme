---
type: causal-policy
title: "No Crash Document Interpreted No Type2 Sink Postscript Or PDF With Type2 Charstring Font Negative Memory"
description: "Round 18 negative memory for no_crash with verifier signal document_interpreted_no_type2_sink."
failure_class: "no_crash"
verifier_signal: "document_interpreted_no_type2_sink"
candidate_family: "construct"
input_format: "postscript-or-pdf-with-type2-charstring-font"
harness_convention: "libfuzzer-ghostscript-pdfwrite-device"
vuln_class: "operand-stack-underflow"
access_scope: generate
success_count: 0
failure_count: 1
confidence: medium
tags: ["no-crash", "document-interpreted-no-type2-sink", "postscript-or-pdf-with-type2-charstring-font", "libfuzzer-ghostscript-pdfwrite-device", "negative-memory", "round-18"]
match_keys: ["no-crash", "document-interpreted-no-type2-sink", "postscript-or-pdf-with-type2-charstring-font", "libfuzzer-ghostscript-pdfwrite-device", "operand-stack-underflow", "negative-memory"]
allowed_scopes: [generate]
forbidden_fields: [raw_poc_bytes, task_id, exact_offset, checksum, submit_metadata]
evidence_level: medium
train_only: true
round: 18
---
# No Crash Document Interpreted No Type2 Sink Postscript Or PDF With Type2 Charstring Font Negative Memory

- key: `no_crash x document_interpreted_no_type2_sink`
- outcome: persistent failure / basin to avoid
- success_count: 0
- failure_count: 1
- related format facts: [[postscript-or-pdf-with-type2-charstring-font]]
- related harness facts: [[libfuzzer-ghostscript-pdfwrite-device]]

## Failure Shape
- A baseline pdfwrite document exercised the device path but did not embed a Type 2 CharString program using the affected rlinecurve or rcurveline operators with insufficient operands.

## Policy
Treat `no_crash x document_interpreted_no_type2_sink` on `postscript-or-pdf-with-type2-charstring-font` as a basin to avoid unless a new candidate changes the parser gate, state relation, or target-sink relation described above. Preserve any proven reachability, but discard variants that return to the same clean-exit, off-target-crash, wrong-sink, usage-only, or both-image-crash basin.

## Procedure
1. Keep only the smallest parser or harness envelope that the verifier proved was reached.
2. Identify the missing causal relation from the signal: parser selection, container acceptance, length relation, stateful subobject, allocation state, or official target sink.
3. Change one relation at a time and discard candidates that return to this same basin.
4. If a local crash is not an official target match, shrink or discard it before mutating deeper fields.
5. Promote a recovery from this basin only after a later verifier-confirmed target match.

## Negative Memory
- Do not resubmit broad mutations that only reproduce `document_interpreted_no_type2_sink`.
- Do not count parser reachability, local wrapper crashes, both-image crashes, or clean exits as success.
- Do not store raw payload bytes, exact positions, task identifiers, checksums, or submit metadata.

## Format Contract
Use [[postscript-or-pdf-with-type2-charstring-font]] for descriptive format gates and invariants.

## Harness Contract
Use [[libfuzzer-ghostscript-pdfwrite-device]] for the input-carving contract.

## Evidence Shape
- Support: 1 diagnosed persistent failure from round 18.
- Scope: generator repair and basin avoidance only.

## Round 18 Failure Evidence
- Verifier key: `no_crash x document_interpreted_no_type2_sink`.
- Candidate family: `construct`.
- Basin summary: A baseline pdfwrite document exercised the device path but did not embed a Type 2 CharString program using the affected rlinecurve or rcurveline operators with insufficient operands.
