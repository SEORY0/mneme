---
type: causal-policy
title: "No Crash Xpswrite Device Reached Clean Or Interpreter Error Postscript Or Xps For Ghostscript Xpswrite Negative Memory"
description: "Round 13 negative memory for no_crash with verifier signal xpswrite_device_reached_clean_or_interpreter_error."
failure_class: "no_crash"
verifier_signal: "xpswrite_device_reached_clean_or_interpreter_error"
candidate_family: "seed_mutate-and-construct-postscript"
input_format: "postscript-or-xps-for-ghostscript-xpswrite"
harness_convention: "libfuzzer"
vuln_class: "use-after-free"
access_scope: generate
success_count: 0
confidence: medium
tags: ["no-crash", "xpswrite-device-reached-clean-or-interpreter-error", "postscript-or-xps-for-ghostscript-xpswrite", "negative-memory", "round-13"]
match_keys: ["no_crash", "xpswrite_device_reached_clean_or_interpreter_error", "postscript-or-xps-for-ghostscript-xpswrite", "libfuzzer", "use-after-free", "negative_memory"]
allowed_scopes: [generate]
forbidden_fields: [raw_poc_bytes, task_id, exact_offset, checksum, submit_metadata]
evidence_level: medium
train_only: true
round: 13
---
# No Crash Xpswrite Device Reached Clean Or Interpreter Error Postscript Or Xps For Ghostscript Xpswrite Negative Memory

- key: `no_crash x xpswrite_device_reached_clean_or_interpreter_error`
- outcome: persistent failure / basin to avoid
- success_count: 0
- failure_count: 1
- related format facts: [[postscript-or-xps-for-ghostscript-xpswrite]]
- related harness facts: [[libfuzzer]]

## Failure Shape
Repository XPS/PDF/PostScript seeds and small constructed bitmap programs executed the xpswrite wrapper cleanly or stopped at interpreter errors. The missing condition is likely a document that reaches the TIFF-backed xpswrite finalization path where client data is freed in the vulnerable order.

## Policy
Treat `no_crash x xpswrite_device_reached_clean_or_interpreter_error` on `postscript-or-xps-for-ghostscript-xpswrite` as a basin to avoid unless a new candidate changes the specific parser gate, state relation, or sink relation described below. Preserve any proven reachability, but reject variants that return to the same clean-exit, off-target-crash, wrong-sink, usage-only, or both-image-crash basin.

## Procedure
1. Keep only the smallest parser or harness envelope that the verifier proved was reached.
2. Identify the missing causal relation from the signal: parser selection, container acceptance, length relation, stateful subobject, allocation state, or official target sink.
3. Change one relation at a time and discard candidates that return to the same clean-exit, off-target-crash, wrong-sink, usage-only, or both-image-crash basin.
4. If a local crash is not an official target match, shrink or discard it before mutating deeper fields.
5. Promote a recovery from this basin only after a later verifier-confirmed target match.

## Negative Memory
- Do not resubmit broad mutations that only reproduce `xpswrite_device_reached_clean_or_interpreter_error`.
- Do not count parser reachability, both-image crashes, local wrapper crashes, or clean exits as success.
- Do not store raw payload bytes, exact positions, task identifiers, checksums, or submit metadata.

## Format Contract
The xpswrite target accepts Ghostscript-readable document languages such as PostScript, PDF, and XPS. Simple image operators can render pages through the device, but the described bug depends on xpswrite output finalization and libtiff client-data lifetime, not merely on rendering any bitmap.

## Harness Contract
The wrapper is fixed to the Ghostscript xpswrite device. It consumes raw document bytes from the PoC as stdin-style input with no selector, invokes Ghostscript with xpswrite output to a null destination, then exits the Ghostscript instance.

## Evidence Shape
- Support: 1 diagnosed persistent failure from round 13.
- Scope: generator repair and basin avoidance only.
## Round 13 Failure Reinforcement

- key: `no_crash x xpswrite_device_reached_clean_or_interpreter_error`
- related format facts: [[postscript-or-xps-for-ghostscript-xpswrite]]
- related harness facts: [[libfuzzer]]

### Failure Shape Delta
Repository XPS/PDF/PostScript seeds and small constructed bitmap programs executed the xpswrite wrapper cleanly or stopped at interpreter errors. The missing condition is likely a document that reaches the TIFF-backed xpswrite finalization path where client data is freed in the vulnerable order.

### Format Contract Delta
The xpswrite target accepts Ghostscript-readable document languages such as PostScript, PDF, and XPS. Simple image operators can render pages through the device, but the described bug depends on xpswrite output finalization and libtiff client-data lifetime, not merely on rendering any bitmap.

### Harness Contract Delta
The wrapper is fixed to the Ghostscript xpswrite device. It consumes raw document bytes from the PoC as stdin-style input with no selector, invokes Ghostscript with xpswrite output to a null destination, then exits the Ghostscript instance.

### Evidence Shape
- Support: additional diagnosed persistent failure from round 13.
- Scope: generator repair and basin avoidance only.
