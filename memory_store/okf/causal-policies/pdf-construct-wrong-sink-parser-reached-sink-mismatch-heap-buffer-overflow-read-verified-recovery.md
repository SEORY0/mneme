---
type: causal-policy
title: "PDF Construct Wrong Sink Parser Reached Sink Mismatch Heap Buffer Overflow Read Verified Recovery"
description: "Round 32 server-verified recovery for pdf keyed by wrong_sink x parser_reached_sink_mismatch."
failure_class: "wrong_sink"
verifier_signal: "parser_reached_sink_mismatch"
candidate_family: "construct"
input_format: "pdf"
harness_convention: "libfuzzer"
vuln_class: "heap-buffer-overflow-read"
access_scope: generate
success_count: 1
confidence: high
tags: ["wrong-sink", "parser-reached-sink-mismatch", "pdf", "libfuzzer", "construct", "heap-buffer-overflow-read", "verified-recovery", "round-32"]
match_keys: ["wrong-sink", "parser-reached-sink-mismatch", "pdf", "libfuzzer", "construct", "heap-buffer-overflow-read", "verified-recovery"]
allowed_scopes: [generate]
forbidden_fields: [raw_poc_bytes, task_id, exact_offset, checksum, submit_metadata]
evidence_level: high
train_only: true
round: 32
---
# PDF Construct Wrong Sink Parser Reached Sink Mismatch Heap Buffer Overflow Read Verified Recovery

- key: `wrong_sink x parser_reached_sink_mismatch`
- outcome: server-verified target match
- success_count: 1
- related format facts: [[pdf]]
- related harness facts: [[libfuzzer]]

## Policy
When `pdf` under `[[libfuzzer]]` produces `parser_reached_sink_mismatch` from `wrong_sink`, keep the parser-reaching envelope and retarget the causal invariant that the official verifier accepted. Local sink labels are advisory once the vulnerable image fails and the fixed image stays clean or the server reports target match.

## Procedure
1. Preserve the harness and format contract that reached the parser: `[[pdf]]` through `[[libfuzzer]]`.
2. Apply the verified recovery: Use a raw linearized PDF that satisfies Poppler's optimized-document gates: the first object is a linearization dictionary with a matching document length, an xref table appears immediately after that first object, and the catalog/page graph remains renderable. Point the linearization hint range at an indirect stream object whose object number is negative. When page rendering asks Poppler to validate linearization hints, the hint parser builds that stream and passes the negative object number into XRef entry lookup before ordinary indirect-reference validation; the fixed build rejects the negative entry and continues cleanly.
3. Keep mutations narrow around the gate/invariant relation rather than rebuilding unrelated carriers or adding broad random noise.
4. If local labels report a non-target sink while the parser branch is reached, submit one minimized candidate before discarding it.
5. Reject both-image crashes, fixed-image crashes, parser rejection, and clean exits as non-success even when they look close locally.

## Format Contract
- PDF linearization is parsed from the first indirect object. The declared document length must match the raw file length for Poppler to treat the file as optimized. In the linearized path, Poppler expects an xref table directly after the first object rather than only at EOF. The /H array identifies a byte range that is copied and parsed as an indirect hint stream; that stream dictionary uses /S to split page-offset hints from shared-object hints. A normal catalog, pages tree, page dictionary, content stream, trailer, and xref metadata are still useful so the harness reaches page rendering and the fixed build can fall back safely.

## Harness Contract
- The libFuzzer target passes the entire input buffer directly to Poppler's raw-data document loader, skips locked or unloadable documents, iterates all reported pages, creates each page by index, and renders each page with the C++ page renderer. There is no leading selector byte, argv filename contract, checksum wrapper, or FuzzedDataProvider front/back split.

## Negative Memory
- Do not store concrete payload bytes, task identifiers, exact positions, checksums, or submit metadata.
- Do not treat parser reachability alone as success without the official target-match signal.
- Do not repeat a clean-exit or both-image-crash basin once the verifier has characterized it.

## Evidence Shape
- Support: one server-verified Round 32 solve.
- Candidate family: construct.
