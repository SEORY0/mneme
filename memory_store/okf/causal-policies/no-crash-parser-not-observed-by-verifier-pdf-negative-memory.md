---
type: causal-policy
title: "No Crash Parser Not Observed By Verifier PDF Negative Memory"
description: "Round 9 negative memory for no_crash with verifier signal parser_not_observed_by_verifier."
failure_class: "no_crash"
verifier_signal: "parser_not_observed_by_verifier"
candidate_family: "construct"
input_format: "pdf"
harness_convention: "libfuzzer"
vuln_class: "out-of-bounds-read"
access_scope: generate
success_count: 0
confidence: medium
tags: ["no-crash", "parser-not-observed-by-verifier", "pdf", "negative-memory", "round-9"]
match_keys: ["no_crash", "parser_not_observed_by_verifier", "pdf", "libfuzzer", "out-of-bounds-read", "negative_memory"]
allowed_scopes: [generate]
forbidden_fields: [raw_poc_bytes, task_id, exact_offset, checksum, submit_metadata]
evidence_level: medium
train_only: true
round: 9
---
# No Crash Parser Not Observed By Verifier PDF Negative Memory

- key: `no_crash x parser_not_observed_by_verifier`
- outcome: persistent failure / basin to avoid
- success_count: 0
- failure_count: 1
- related format facts: [[pdf]]
- related harness facts: [[libfuzzer]]

## Failure Shape
- Minimal PDFs with oversized content stream length, truncated image streams, empty filtered image
  streams, malformed object streams, and malformed xref streams all rendered or rejected cleanly.
- The missing trigger is a path that seeks the in-memory stream read position past the end and then
  calls BaseMemStream::getChars rather than being caught by higher-level stream bounds checks.

## Policy
Treat `no_crash x parser_not_observed_by_verifier` on `pdf` as a basin to avoid unless a new candidate changes the parser gate, state relation, or official target sink. Preserve any proven reachability, but reject variants that return to the same verifier signal without changing the causal gate under test.

## Procedure
1. Keep only the smallest parser or harness envelope that the verifier proved was reached.
2. Identify the missing causal relation from the signal: parser selection, container acceptance, length relation, stateful subobject, allocation state, or official target sink.
3. Change one relation at a time and discard candidates that return to the same clean-exit, off-target-crash, wrong-sink, usage-only, or both-image-crash basin.
4. If a local crash is not an official target match, shrink or discard it before mutating deeper fields.
5. Promote a recovery from this basin only after a later verifier-confirmed target match.

## Format Contract
- The PDF harness expects a complete PDF byte stream with header, indirect objects, xref/trailer,
  and a catalog.
- Rendering requires a page tree and at least one page object; content streams and image XObjects
  can have independent stream dictionaries, filters, declared lengths, and resource references.

## Harness Contract
- The Poppler C++ fuzzer loads the raw input as an in-memory document and renders pages with the
  page renderer.
- The input is not carved.
- BaseMemStream is used because the document is memory-backed; malformed PDFs must still pass enough
  catalog/page/xref parsing to reach rendering or stream decoding.

## Negative Memory
- Do not resubmit broad mutations that only reproduce `parser_not_observed_by_verifier`.
- Do not count parser reachability, both-image crashes, local wrapper crashes, clean exits, or fixed-image crashes as success.
- Do not store raw payload bytes, exact positions, task identifiers, or submit metadata.

## Evidence Shape
- Support: one diagnosed persistent failure from round 9.
- Scope: generator repair and basin avoidance only.
