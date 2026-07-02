---
type: causal-policy
title: "PDF Construct Then Seed Mutate Then Xref Stream Retarget No Crash Clean Exit Or Parser Not Observed Stream Parser Crash Negative Memory"
description: "Negative memory for pdf candidates that ended in no_crash with verifier signal clean_exit_or_parser_not_observed."
failure_class: "no_crash"
verifier_signal: "clean_exit_or_parser_not_observed"
candidate_family: "construct_then_seed_mutate_then_xref_stream_retarget"
input_format: "pdf"
harness_convention: "libfuzzer"
vuln_class: "stream-parser-crash"
access_scope: generate
success_count: 0
confidence: medium
tags: ["no-crash", "clean-exit-or-parser-not-observed", "pdf", "libfuzzer", "construct-then-seed-mutate-then-xref-stream-retarget", "stream-parser-crash", "negative-memory", "round-32"]
match_keys: ["no-crash", "clean-exit-or-parser-not-observed", "pdf", "libfuzzer", "construct-then-seed-mutate-then-xref-stream-retarget", "stream-parser-crash", "negative-memory"]
allowed_scopes: [generate]
forbidden_fields: [raw_poc_bytes, task_id, exact_offset, checksum, submit_metadata]
evidence_level: medium
train_only: true
round: 32
---
# PDF Construct Then Seed Mutate Then Xref Stream Retarget No Crash Clean Exit Or Parser Not Observed Stream Parser Crash Negative Memory

- key: `no_crash x clean_exit_or_parser_not_observed`
- outcome: persistent diagnosed failure
- success_count: 0
- related format facts: [[pdf]]
- related harness facts: [[libfuzzer]]

## Policy
Treat `no_crash x clean_exit_or_parser_not_observed` for `[[pdf]]` under `[[libfuzzer]]` as a dead-end basin until new evidence changes the verifier signal. Preserve only parser-recognition facts, then change the missing relation named by the diagnosis.

## Procedure
1. Keep any envelope property that reached the parser or clean execution, but stop repeating the same carrier shape.
2. Avoid the observed dead end: Malformed stream-length, physical EOF after stream marker, self-referential stream length, seed-preserved content-stream mutations, and xref/object-stream retargets all exited cleanly. The missing relation appears to be a narrower makeStream parser state not reached by ordinary content stream length corruption or the tested object-stream and xref-stream carriers.
3. Rebuild around `[[pdf]]` and `[[libfuzzer]]`, targeting the missing gate or state relation rather than padding, broad corruption, or unrelated seed churn.
4. Submit only after local verification produces a vulnerable-build crash or a plausible parser-branch wrong-sink crash; clean exits under this signal are not submit candidates.

## Format Contract
- PDF reachability for this harness requires a complete raw document with header, catalog, pages tree, page object, resources when rendering text, stream dictionaries, xref or xref-stream metadata, trailer/root linkage, startxref, and EOF marker. Ordinary content streams use a /Length field followed by stream data and endstream; object streams declare an object count, a First value for the object table area, and embedded object bodies. Xref streams declare Type XRef, Size, W field widths, optional compressed-object entries, and trailer keys in the stream dictionary.

## Harness Contract
- The harness is libFuzzer with no FuzzedDataProvider split or mode selector. It passes the entire input buffer to Poppler's raw PDF loader, discards unloadable or locked documents, then renders each page through page_renderer. Parser reachability depends on the raw bytes forming a loadable or repairable PDF document.

## Negative Memory
- Do not store concrete payload bytes, task identifiers, exact positions, checksums, or submit metadata.
- Do not treat parser reachability alone as success without the official target-match signal.
- Do not repeat a clean-exit or both-image-crash basin once the verifier has characterized it.

## Evidence Shape
- Support: one diagnosed Round 32 failed solve attempt.
- Attempts observed: 10.
