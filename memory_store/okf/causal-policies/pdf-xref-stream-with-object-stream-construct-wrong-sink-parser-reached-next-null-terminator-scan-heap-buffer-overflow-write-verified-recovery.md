---
type: causal-policy
title: "Pdf Xref Stream With Object Stream Construct Wrong Sink Parser Reached Next Null Terminator Scan Heap Buffer Overflow Write Verified Recovery"
description: "Round 30 verified recovery for wrong_sink with verifier signal parser_reached_next_null_terminator_scan."
failure_class: "wrong_sink"
verifier_signal: "parser_reached_next_null_terminator_scan"
candidate_family: "construct"
input_format: "pdf-xref-stream-with-object-stream"
harness_convention: "libfuzzer-mupdf-pdf-renderer"
vuln_class: "heap-buffer-overflow-write"
access_scope: generate
success_count: 1
confidence: medium
tags: ["wrong-sink", "parser-reached-next-null-terminator-scan", "pdf-xref-stream-with-object-stream", "libfuzzer-mupdf-pdf-renderer", "construct", "verified-recovery", "round-30"]
match_keys: ["wrong-sink", "parser-reached-next-null-terminator-scan", "pdf-xref-stream-with-object-stream", "libfuzzer-mupdf-pdf-renderer", "heap-buffer-overflow-write"]
allowed_scopes: [generate]
forbidden_fields: [raw_poc_bytes, task_id, exact_offset, checksum, submit_metadata]
evidence_level: high
train_only: true
round: 30
---
# Pdf Xref Stream With Object Stream Construct Wrong Sink Parser Reached Next Null Terminator Scan Heap Buffer Overflow Write Verified Recovery

- key: `wrong-sink x parser-reached-next-null-terminator-scan`
- outcome: verified recovery
- success_count: 1
- failure_count: 0
- formats: [[pdf-xref-stream-with-object-stream]]
- harnesses: [[libfuzzer-mupdf-pdf-renderer]]

## Failure Shape
Build a valid PDF with a normal catalog and page tree, but place the page object inside an object stream referenced from an xref stream. Keep the xref stream structurally consistent so page lookup resolves the compressed page object. Give the object stream an intentionally underdeclared length, then make its object-number table long and free of stream terminator tokens so resolving the page forces the null filter's endstream-search path to fill its fixed scan buffer before it finds the real terminator. The vulnerable build writes the helper terminator byte past that buffer; the fixed build rejects or bounds the scan cleanly.

## Policy
For `wrong-sink x parser-reached-next-null-terminator-scan` on `pdf-xref-stream-with-object-stream`, preserve the parser and harness gates first, then mutate only the causal invariant described by the verified trace. Prefer `construct` while this format and harness contract are present.

## Procedure
1. Preserve the `pdf-xref-stream-with-object-stream` carrier enough for the `libfuzzer-mupdf-pdf-renderer` harness to reach the parser path.
2. Keep unrelated envelope fields minimal and stable so verifier feedback stays tied to the target sink.
3. Apply the verified invariant from the failure shape rather than random broad mutation.
4. Submit only candidates where the vulnerable image reaches the target relation and the fixed image rejects or avoids it.

## Verifier Contract
The local class may remain coarse. Treat the official vulnerable-versus-fixed target match as the confirmation gate for this policy.

## Negative Memory
- Do not corrupt the outer `pdf-xref-stream-with-object-stream` recognition gate while retargeting this signal.
- Do not treat off-target crashes, clean parser reachability, or both-image crashes as success for this policy.
- Never store raw payload bytes, exact offsets, checksums, or task-local identifiers in memory.

## Evidence Shape
- Support: 1 server-verified solve(s), including round 30.
- Scope: generator repair only.
