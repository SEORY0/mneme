---
type: causal-policy
title: "PDF Construct Parser Reached Sink Mismatch But Official Target Match Stack Buffer Underflow Read Verified Recovery"
description: "Round 8 verified recovery for wrong_sink with verifier signal parser_reached_sink_mismatch_but_official_target_match."
failure_class: "wrong_sink"
verifier_signal: "parser_reached_sink_mismatch_but_official_target_match"
candidate_family: "construct"
input_format: "pdf"
harness_convention: "libfuzzer"
vuln_class: "stack-buffer-underflow-read"
access_scope: generate
success_count: 1
confidence: high
tags: ["wrong-sink", "parser-reached-sink-mismatch-but-official-target-match", "pdf", "construct", "verified-recovery", "round-8"]
match_keys: ["wrong_sink", "parser_reached_sink_mismatch_but_official_target_match", "pdf", "libfuzzer", "stack-buffer-underflow-read", "verified_recovery"]
allowed_scopes: [generate]
forbidden_fields: [raw_poc_bytes, task_id, exact_offset, checksum, submit_metadata]
evidence_level: high
train_only: true
round: 8
---
# PDF Construct Parser Reached Sink Mismatch But Official Target Match Stack Buffer Underflow Read Verified Recovery

## Policy
For `wrong_sink x parser_reached_sink_mismatch_but_official_target_match`, preserve the format and harness gates that reached the target path, then apply the verified causal relation below. This is a positive recovery policy because the official vulnerable/fixed verifier recorded a target match.

## Procedure
1. Build a syntactically valid one-page PDF that renders a function-based shading. The shading references a calculator function whose program invokes a stack-manipulation operator with an operand depth larger than the available operand stack, causing the vulnerable interpreter to read below the stack while rendering; the fixed image rejects it.
2. Keep the carrier abstract: preserve the gate/invariant relation, not task-local bytes, offsets, checksums, or submission metadata.
3. If a later candidate changes the verifier signal, re-rank against the new failure key before mutating unrelated fields.

## Format Contract
- The PDF needs a valid object graph with catalog, page tree, page resources, content stream, shading resource, and calculator function stream. Rendering the page, not merely parsing objects, is what executes the function program.
- Harness: The MuPDF fuzzer opens the raw bytes as a PDF stream and renders available pages to pixmaps. There is no leading mode selector or FuzzedDataProvider split; the input must be a self-contained PDF document.

## Negative Memory
- Do not broaden mutations after the parser/harness gate is proven.
- Do not submit candidates that reproduce on the fixed image or move to an off-target wrapper crash.
- Do not store raw payload bytes, exact offsets, checksums, or task-local identifiers.

## Evidence Shape
- Support: one round-8 worker trace with official target match.
- Scope: generator repair for the same failure-keyed basin.
