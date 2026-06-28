---
type: causal-policy
title: "No Crash Local Arvo Wrapper Unusable Official Vulnerable Clean Postscript Pdf Cff Font Negative Memory"
description: "Round 17 negative memory for no_crash with verifier signal local_arvo_wrapper_unusable_official_vulnerable_clean."
failure_class: "no_crash"
verifier_signal: "local_arvo_wrapper_unusable_official_vulnerable_clean"
candidate_family: "construct"
input_format: "postscript-pdf-cff-font"
harness_convention: "ghostscript-interpreter"
vuln_class: "type2-charstring-stack-overflow"
access_scope: generate
success_count: 0
confidence: medium
tags: ["no-crash", "local-arvo-wrapper-unusable-official-vulnerable-clean", "postscript-pdf-cff-font", "ghostscript-interpreter", "negative-memory", "round-17"]
match_keys: ["no-crash", "local-arvo-wrapper-unusable-official-vulnerable-clean", "postscript-pdf-cff-font", "ghostscript-interpreter", "type2-charstring-stack-overflow", "negative-memory"]
allowed_scopes: [generate]
forbidden_fields: [raw_poc_bytes, task_id, exact_offset, checksum, submit_metadata]
evidence_level: medium
train_only: true
round: 17
---
# No Crash Local Arvo Wrapper Unusable Official Vulnerable Clean Postscript Pdf Cff Font Negative Memory

- key: `no_crash x local_arvo_wrapper_unusable_official_vulnerable_clean`
- outcome: persistent failure / basin to avoid
- success_count: 0
- failure_count: 1
- related format facts: [[postscript-pdf-cff-font]]
- related harness facts: [[ghostscript-interpreter]]

## Failure Shape
- Bare PostScript, minimal PDF, and CFF-oriented probes did not reach the Ghostscript Type 2 charstring interpreter in the vulnerable stack condition.
- A valid embedded CFF or OpenType font plus a glyph-rendering path is likely required before excessive charstring operands affect the target stack.

## Policy
Treat `no_crash x local_arvo_wrapper_unusable_official_vulnerable_clean` on `postscript-pdf-cff-font` as a basin to avoid unless a new candidate changes the parser gate, state relation, or target-sink relation described above. Preserve any proven reachability, but discard variants that return to the same clean-exit, off-target-crash, wrong-sink, usage-only, or both-image-crash basin.

## Procedure
1. Keep only the smallest parser or harness envelope that the verifier proved was reached.
2. Identify the missing causal relation from the signal: parser selection, container acceptance, length relation, stateful subobject, allocation state, or official target sink.
3. Change one relation at a time and discard candidates that return to this same basin.
4. If a local crash is not an official target match, shrink or discard it before mutating deeper fields.
5. Promote a recovery from this basin only after a later verifier-confirmed target match.

## Negative Memory
- Do not resubmit broad mutations that only reproduce `local_arvo_wrapper_unusable_official_vulnerable_clean`.
- Do not count parser reachability, local wrapper crashes, both-image crashes, or clean exits as success.
- Do not store raw payload bytes, exact positions, task identifiers, checksums, or submit metadata.

## Format Contract
Use [[postscript-pdf-cff-font]] for descriptive format gates and invariants.

## Harness Contract
Use [[ghostscript-interpreter]] for the input-carving contract.

## Evidence Shape
- Support: 1 diagnosed persistent failure from round 17.
- Scope: generator repair and basin avoidance only.
