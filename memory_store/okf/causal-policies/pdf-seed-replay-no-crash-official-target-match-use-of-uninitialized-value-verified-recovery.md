---
type: causal-policy
title: "PDF Seed Replay No Crash Official Target Match Use Of Uninitialized Value Verified Recovery"
description: "Round 32 server-verified recovery for pdf keyed by no_crash x official_target_match."
failure_class: "no_crash"
verifier_signal: "official_target_match"
candidate_family: "seed_replay"
input_format: "pdf"
harness_convention: "libfuzzer"
vuln_class: "use-of-uninitialized-value"
access_scope: generate
success_count: 1
confidence: high
tags: ["no-crash", "official-target-match", "pdf", "libfuzzer", "seed-replay", "use-of-uninitialized-value", "verified-recovery", "round-32"]
match_keys: ["no-crash", "official-target-match", "pdf", "libfuzzer", "seed-replay", "use-of-uninitialized-value", "verified-recovery"]
allowed_scopes: [generate]
forbidden_fields: [raw_poc_bytes, task_id, exact_offset, checksum, submit_metadata]
evidence_level: high
train_only: true
round: 32
---
# PDF Seed Replay No Crash Official Target Match Use Of Uninitialized Value Verified Recovery

- key: `no_crash x official_target_match`
- outcome: server-verified target match
- success_count: 1
- related format facts: [[pdf]]
- related harness facts: [[libfuzzer]]

## Policy
When `pdf` under `[[libfuzzer]]` produces `official_target_match` from `no_crash`, keep the parser-reaching envelope and retarget the causal invariant that the official verifier accepted. Local sink labels are advisory once the vulnerable image fails and the fixed image stays clean or the server reports target match.

## Procedure
1. Preserve the harness and format contract that reached the parser: `[[pdf]]` through `[[libfuzzer]]`.
2. Apply the verified recovery: Use a compact real PDF corpus carrier that already preserves the Poppler render harness gates: normal document header, catalog/pages/page graph, content stream object, and trailer/xref material. The successful carrier keeps the malformed xref/stream relation narrow enough to drive Poppler's stream construction and repair path; broad edits to the stream terminator, declared length, startxref, or xref count either lost target reachability or produced local-only crashes. Submit the target-reaching seed itself rather than widening the mutation.
3. Keep mutations narrow around the gate/invariant relation rather than rebuilding unrelated carriers or adding broad random noise.
4. If local labels report a non-target sink while the parser branch is reached, submit one minimized candidate before discarding it.
5. Reject both-image crashes, fixed-image crashes, parser rejection, and clean exits as non-success even when they look close locally.

## Format Contract
- PDF reachability for this harness requires a complete raw document: version header, indirect catalog/pages/page objects, a page content stream, xref/trailer metadata, and EOF marker. Poppler can repair malformed xref material, but small changes to the xref table or stream dictionary can move from target reachability to clean rejection; stream dictionaries use declared lengths and endstream markers, while repaired xref state can override or validate stream boundaries.

## Harness Contract
- The libFuzzer target passes the entire input buffer directly to Poppler's raw-data document loader, skips locked or unloadable documents, iterates all pages, and renders each page with the C++ page renderer. There is no mode byte, length suffix, checksum, argv file contract, or FuzzedDataProvider front/back split.

## Negative Memory
- Do not store concrete payload bytes, task identifiers, exact positions, checksums, or submit metadata.
- Do not treat parser reachability alone as success without the official target-match signal.
- Do not repeat a clean-exit or both-image-crash basin once the verifier has characterized it.

## Evidence Shape
- Support: one server-verified Round 32 solve.
- Candidate family: seed_replay.
