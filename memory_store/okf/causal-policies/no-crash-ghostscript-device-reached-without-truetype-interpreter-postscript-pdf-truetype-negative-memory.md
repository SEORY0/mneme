---
type: causal-policy
title: "No Crash Ghostscript Device Reached Without Truetype Interpreter Postscript Pdf Truetype Negative Memory"
description: "Round 17 negative memory for no_crash with verifier signal ghostscript_device_reached_without_truetype_interpreter."
failure_class: "no_crash"
verifier_signal: "ghostscript_device_reached_without_truetype_interpreter"
candidate_family: "construct_and_seed_probe"
input_format: "postscript-pdf-truetype"
harness_convention: "libfuzzer ghostscript pdfwrite device"
vuln_class: "instruction-buffer-out-of-bounds-read"
access_scope: generate
success_count: 0
confidence: medium
tags: ["no-crash", "ghostscript-device-reached-without-truetype-interpreter", "postscript-pdf-truetype", "libfuzzer-ghostscript-pdfwrite-device", "negative-memory", "round-17"]
match_keys: ["no-crash", "ghostscript-device-reached-without-truetype-interpreter", "postscript-pdf-truetype", "libfuzzer-ghostscript-pdfwrite-device", "instruction-buffer-out-of-bounds-read", "negative-memory"]
allowed_scopes: [generate]
forbidden_fields: [raw_poc_bytes, task_id, exact_offset, checksum, submit_metadata]
evidence_level: medium
train_only: true
round: 17
---
# No Crash Ghostscript Device Reached Without Truetype Interpreter Postscript Pdf Truetype Negative Memory

- key: `no_crash x ghostscript_device_reached_without_truetype_interpreter`
- outcome: persistent failure / basin to avoid
- success_count: 0
- failure_count: 1
- related format facts: [[postscript-pdf-truetype]]
- related harness facts: [[libfuzzer-ghostscript-pdfwrite-device]]

## Failure Shape
- A small PostScript document and a tiny PDF reached the Ghostscript device wrapper cleanly, while a raw TrueType font was rejected at interpreter startup.
- The missing gate is embedding and executing a TrueType program through a document font resource so the NPUSHB instruction interpreter is reached.

## Policy
Treat `no_crash x ghostscript_device_reached_without_truetype_interpreter` on `postscript-pdf-truetype` as a basin to avoid unless a new candidate changes the parser gate, state relation, or target-sink relation described above. Preserve any proven reachability, but discard variants that return to the same clean-exit, off-target-crash, wrong-sink, usage-only, or both-image-crash basin.

## Procedure
1. Keep only the smallest parser or harness envelope that the verifier proved was reached.
2. Identify the missing causal relation from the signal: parser selection, container acceptance, length relation, stateful subobject, allocation state, or official target sink.
3. Change one relation at a time and discard candidates that return to this same basin.
4. If a local crash is not an official target match, shrink or discard it before mutating deeper fields.
5. Promote a recovery from this basin only after a later verifier-confirmed target match.

## Negative Memory
- Do not resubmit broad mutations that only reproduce `ghostscript_device_reached_without_truetype_interpreter`.
- Do not count parser reachability, local wrapper crashes, both-image crashes, or clean exits as success.
- Do not store raw payload bytes, exact positions, task identifiers, checksums, or submit metadata.

## Format Contract
Use [[postscript-pdf-truetype]] for descriptive format gates and invariants.

## Harness Contract
Use [[libfuzzer-ghostscript-pdfwrite-device]] for the input-carving contract.

## Evidence Shape
- Support: 1 diagnosed persistent failure from round 17.
- Scope: generator repair and basin avoidance only.
