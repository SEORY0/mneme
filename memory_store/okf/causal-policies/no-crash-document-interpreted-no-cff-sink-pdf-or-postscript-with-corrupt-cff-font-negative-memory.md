---
type: causal-policy
title: "No Crash Document Interpreted No CFF Sink PDF Or Postscript With Corrupt CFF Font Negative Memory"
description: "Round 18 negative memory for no_crash with verifier signal document_interpreted_no_cff_sink."
failure_class: "no_crash"
verifier_signal: "document_interpreted_no_cff_sink"
candidate_family: "construct"
input_format: "pdf-or-postscript-with-corrupt-cff-font"
harness_convention: "libfuzzer-ghostscript-ps2write-device"
vuln_class: "buffer-overrun"
access_scope: generate
success_count: 0
failure_count: 1
confidence: medium
tags: ["no-crash", "document-interpreted-no-cff-sink", "pdf-or-postscript-with-corrupt-cff-font", "libfuzzer-ghostscript-ps2write-device", "negative-memory", "round-18"]
match_keys: ["no-crash", "document-interpreted-no-cff-sink", "pdf-or-postscript-with-corrupt-cff-font", "libfuzzer-ghostscript-ps2write-device", "buffer-overrun", "negative-memory"]
allowed_scopes: [generate]
forbidden_fields: [raw_poc_bytes, task_id, exact_offset, checksum, submit_metadata]
evidence_level: medium
train_only: true
round: 18
---
# No Crash Document Interpreted No CFF Sink PDF Or Postscript With Corrupt CFF Font Negative Memory

- key: `no_crash x document_interpreted_no_cff_sink`
- outcome: persistent failure / basin to avoid
- success_count: 0
- failure_count: 1
- related format facts: [[pdf-or-postscript-with-corrupt-cff-font]]
- related harness facts: [[libfuzzer-ghostscript-ps2write-device]]

## Failure Shape
- A minimal document reached the Ghostscript writer device but did not carry a corrupted CFF font far enough into GhostPDF/Ghostscript CFF number expansion to exercise the undersized output guard.

## Policy
Treat `no_crash x document_interpreted_no_cff_sink` on `pdf-or-postscript-with-corrupt-cff-font` as a basin to avoid unless a new candidate changes the parser gate, state relation, or target-sink relation described above. Preserve any proven reachability, but discard variants that return to the same clean-exit, off-target-crash, wrong-sink, usage-only, or both-image-crash basin.

## Procedure
1. Keep only the smallest parser or harness envelope that the verifier proved was reached.
2. Identify the missing causal relation from the signal: parser selection, container acceptance, length relation, stateful subobject, allocation state, or official target sink.
3. Change one relation at a time and discard candidates that return to this same basin.
4. If a local crash is not an official target match, shrink or discard it before mutating deeper fields.
5. Promote a recovery from this basin only after a later verifier-confirmed target match.

## Negative Memory
- Do not resubmit broad mutations that only reproduce `document_interpreted_no_cff_sink`.
- Do not count parser reachability, local wrapper crashes, both-image crashes, or clean exits as success.
- Do not store raw payload bytes, exact positions, task identifiers, checksums, or submit metadata.

## Format Contract
Use [[pdf-or-postscript-with-corrupt-cff-font]] for descriptive format gates and invariants.

## Harness Contract
Use [[libfuzzer-ghostscript-ps2write-device]] for the input-carving contract.

## Evidence Shape
- Support: 1 diagnosed persistent failure from round 18.
- Scope: generator repair and basin avoidance only.

## Round 18 Failure Evidence
- Verifier key: `no_crash x document_interpreted_no_cff_sink`.
- Candidate family: `construct`.
- Basin summary: A minimal document reached the Ghostscript writer device but did not carry a corrupted CFF font far enough into GhostPDF/Ghostscript CFF number expansion to exercise the undersized output guard.
