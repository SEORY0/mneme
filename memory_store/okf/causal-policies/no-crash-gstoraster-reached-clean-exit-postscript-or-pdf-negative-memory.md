---
type: causal-policy
title: "No Crash Gstoraster Reached Clean Exit Postscript Or Pdf Negative Memory"
description: "Round 13 negative memory for no_crash with verifier signal gstoraster_reached_clean_exit."
failure_class: "no_crash"
verifier_signal: "gstoraster_reached_clean_exit"
candidate_family: "construct"
input_format: "postscript-or-pdf"
harness_convention: "libfuzzer-gstoraster"
vuln_class: "buffer-overflow-write"
access_scope: generate
success_count: 0
confidence: medium
tags: ["no-crash", "gstoraster-reached-clean-exit", "postscript-or-pdf", "negative-memory", "round-13"]
match_keys: ["no_crash", "gstoraster_reached_clean_exit", "postscript-or-pdf", "libfuzzer-gstoraster", "buffer-overflow-write", "negative_memory"]
allowed_scopes: [generate]
forbidden_fields: [raw_poc_bytes, task_id, exact_offset, checksum, submit_metadata]
evidence_level: medium
train_only: true
round: 13
---
# No Crash Gstoraster Reached Clean Exit Postscript Or Pdf Negative Memory

- key: `no_crash x gstoraster_reached_clean_exit`
- outcome: persistent failure / basin to avoid
- success_count: 0
- failure_count: 1
- related format facts: [[postscript-or-pdf]]
- related harness facts: [[libfuzzer-gstoraster]]

## Failure Shape
A valid PostScript probe reached the gstoraster interpreter but did not enable or hit the debug-message buffer copy path. The missing condition is likely a specific debug channel or interpreter feature that emits the vulnerable diagnostic message.

## Policy
Treat `no_crash x gstoraster_reached_clean_exit` on `postscript-or-pdf` as a basin to avoid unless a new candidate changes the specific parser gate, state relation, or sink relation described below. Preserve any proven reachability, but reject variants that return to the same clean-exit, off-target-crash, wrong-sink, usage-only, or both-image-crash basin.

## Procedure
1. Keep only the smallest parser or harness envelope that the verifier proved was reached.
2. Identify the missing causal relation from the signal: parser selection, container acceptance, length relation, stateful subobject, allocation state, or official target sink.
3. Change one relation at a time and discard candidates that return to the same clean-exit, off-target-crash, wrong-sink, usage-only, or both-image-crash basin.
4. If a local crash is not an official target match, shrink or discard it before mutating deeper fields.
5. Promote a recovery from this basin only after a later verifier-confirmed target match.

## Negative Memory
- Do not resubmit broad mutations that only reproduce `gstoraster_reached_clean_exit`.
- Do not count parser reachability, both-image crashes, local wrapper crashes, or clean exits as success.
- Do not store raw payload bytes, exact positions, task identifiers, checksums, or submit metadata.

## Format Contract
The input can be PostScript or PDF content consumed directly from stdin by Ghostscript. Valid PostScript syntax is enough to reach initialization and page rendering, but debug-output paths depend on internal flags or feature-specific diagnostics.

## Harness Contract
The gstoraster harness passes the raw input bytes through Ghostscript stdin with cups output-device arguments, quiet/batch/no-pause flags, and no leading mode selector or FuzzedDataProvider carving.

## Evidence Shape
- Support: 1 diagnosed persistent failure from round 13.
- Scope: generator repair and basin avoidance only.
## Round 13 Failure Reinforcement

- key: `no_crash x gstoraster_reached_clean_exit`
- related format facts: [[postscript-or-pdf]]
- related harness facts: [[libfuzzer-gstoraster]]

### Failure Shape Delta
A valid PostScript probe reached the gstoraster interpreter but did not enable or hit the debug-message buffer copy path. The missing condition is likely a specific debug channel or interpreter feature that emits the vulnerable diagnostic message.

### Format Contract Delta
The input can be PostScript or PDF content consumed directly from stdin by Ghostscript. Valid PostScript syntax is enough to reach initialization and page rendering, but debug-output paths depend on internal flags or feature-specific diagnostics.

### Harness Contract Delta
The gstoraster harness passes the raw input bytes through Ghostscript stdin with cups output-device arguments, quiet/batch/no-pause flags, and no leading mode selector or FuzzedDataProvider carving.

### Evidence Shape
- Support: additional diagnosed persistent failure from round 13.
- Scope: generator repair and basin avoidance only.
