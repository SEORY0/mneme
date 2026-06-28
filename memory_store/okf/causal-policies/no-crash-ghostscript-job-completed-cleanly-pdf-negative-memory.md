---
type: causal-policy
title: "No Crash Ghostscript Job Completed Cleanly Pdf Negative Memory"
description: "Round 12 negative memory for no_crash with verifier signal ghostscript_job_completed_cleanly."
failure_class: "no_crash"
verifier_signal: "ghostscript_job_completed_cleanly"
candidate_family: "seed_mutate_and_construct"
input_format: "pdf"
harness_convention: "libfuzzer"
vuln_class: "xref-stream-size-zero-processing"
access_scope: generate
success_count: 0
confidence: medium
tags: ["no-crash", "ghostscript-job-completed-cleanly", "pdf", "negative-memory", "round-12"]
match_keys: ["no_crash", "ghostscript_job_completed_cleanly", "pdf", "libfuzzer", "xref-stream-size-zero-processing", "negative_memory"]
allowed_scopes: [generate]
forbidden_fields: [raw_poc_bytes, task_id, exact_offset, checksum, submit_metadata]
evidence_level: medium
train_only: true
round: 12
---
# No Crash Ghostscript Job Completed Cleanly Pdf Negative Memory

- key: `no_crash x ghostscript_job_completed_cleanly`
- outcome: persistent failure / basin to avoid
- success_count: 0
- failure_count: 1
- related format facts: [[pdf]]
- related harness facts: [[libfuzzer]]

## Failure Shape
Valid PDF seeds, a minimal xref-stream PDF declaring an empty xref size, an old-style empty xref table, and a PostScript smoke input all ran cleanly. The minimal xref stream did not make Ghostscript continue far enough into the vulnerable zero-size xref-stream processing state.

## Policy
Treat `no_crash x ghostscript_job_completed_cleanly` on `pdf` as a basin to avoid unless a new candidate changes the parser gate, state relation, or official target sink. Preserve any proven reachability, but reject variants that return to the same verifier signal without changing the causal gate under test.

## Procedure
1. Keep only the smallest parser or harness envelope that the verifier proved was reached.
2. Identify the missing causal relation from the signal: parser selection, container acceptance, length relation, stateful subobject, allocation state, or official target sink.
3. Change one relation at a time and discard candidates that return to the same clean-exit, off-target-crash, wrong-sink, usage-only, or both-image-crash basin.
4. If a local crash is not an official target match, shrink or discard it before mutating deeper fields.
5. Promote a recovery from this basin only after a later verifier-confirmed target match.

## Format Contract
The target format is a complete PDF or PostScript job for Ghostscript's CUPS raster path. PDF xref streams are indirect stream objects with a trailer dictionary, width array, length, root reference, and startxref pointer. Declaring an empty xref table alone is not sufficient without a coherent document graph.

## Harness Contract
The harness feeds raw input as stdin to Ghostscript configured with a CUPS raster output device. There is no mode selector; the input must be a self-contained Ghostscript-readable job, and parser reachability depends on normal PDF repair and object traversal.

## Negative Memory
- Do not resubmit broad mutations that only reproduce `ghostscript_job_completed_cleanly`.
- Do not count parser reachability, both-image crashes, local wrapper crashes, clean exits, or fixed-image crashes as success.
- Do not store raw payload bytes, exact positions, task identifiers, or submit metadata.

## Evidence Shape
- Support: one diagnosed persistent failure from round 12.
- Scope: generator repair and basin avoidance only.
